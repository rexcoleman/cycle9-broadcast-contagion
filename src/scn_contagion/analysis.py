"""Analysis tools for phase transition measurement.

- Containment probability curves with Wilson score CIs
- Phase transition location (p_c) via logistic fit + bootstrap
- Hub-targeting efficiency ratio with paired bootstrap CI
- Ablation comparisons
"""

import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import norm


def wilson_ci(successes, n, alpha=0.05):
    """Wilson score confidence interval for binomial proportion."""
    if n == 0:
        return 0.0, 0.0, 1.0
    z = norm.ppf(1 - alpha / 2)
    p_hat = successes / n
    denom = 1 + z ** 2 / n
    center = (p_hat + z ** 2 / (2 * n)) / denom
    half_width = z * np.sqrt(p_hat * (1 - p_hat) / n + z ** 2 / (4 * n ** 2)) / denom
    return float(center), float(max(0, center - half_width)), float(min(1, center + half_width))


def logistic_fn(p, k, p_c):
    """Logistic function for fitting containment probability curve."""
    return 1.0 / (1.0 + np.exp(-k * (p - p_c)))


def estimate_pc(coverage_points, containment_probs, n_reps_per_point=None):
    """Estimate phase transition location p_c via logistic fit.

    Parameters
    ----------
    coverage_points : array-like
        Coverage fractions.
    containment_probs : array-like
        Containment probabilities at each coverage point.

    Returns
    -------
    dict with p_c, sharpness (normalized k), fit_params
    """
    p = np.array(coverage_points)
    y = np.array(containment_probs)

    # Filter out NaN
    mask = ~np.isnan(y)
    p = p[mask]
    y = y[mask]

    if len(p) < 4:
        return {'p_c': float('nan'), 'sharpness': float('nan'), 'k': float('nan')}

    try:
        popt, _ = curve_fit(logistic_fn, p, y, p0=[20.0, 0.3],
                            bounds=([0.1, 0.0], [200.0, 1.0]),
                            maxfev=5000)
        k_fit, pc_fit = popt

        # Normalize sharpness: max slope of logistic is k/4
        # Theoretical max for a step function is infinity, so normalize
        # by the maximum k we'd consider "sharp" (k=50 -> step-like)
        sharpness = min(k_fit / 50.0, 1.0)

        return {
            'p_c': float(pc_fit),
            'sharpness': float(sharpness),
            'k': float(k_fit),
        }
    except (RuntimeError, ValueError):
        # Fit failed - try to find 0.5 crossing manually
        crossings = np.where(np.diff(np.sign(y - 0.5)))[0]
        if len(crossings) > 0:
            idx = crossings[0]
            # Linear interpolation
            p_c = p[idx] + (0.5 - y[idx]) * (p[idx + 1] - p[idx]) / (y[idx + 1] - y[idx] + 1e-10)
            return {'p_c': float(p_c), 'sharpness': 0.0, 'k': 0.0}
        return {'p_c': float('nan'), 'sharpness': float('nan'), 'k': float('nan')}


def bootstrap_pc(coverage_points, run_data, n_bootstrap=1000, n_reps=50, seed=42):
    """Bootstrap confidence interval on p_c.

    Parameters
    ----------
    coverage_points : array-like
        Unique coverage fractions.
    run_data : dict
        {p_coverage: [list of contained 0/1 values]}
    n_bootstrap : int
        Number of bootstrap resamples.
    n_reps : int
        Number of reps per coverage point.

    Returns
    -------
    dict with p_c, ci_lower, ci_upper, sharpness, sharpness_ci
    """
    rng = np.random.default_rng(seed)
    coverage_points = np.array(sorted(coverage_points))

    pc_samples = []
    sharpness_samples = []

    for _ in range(n_bootstrap):
        # Resample within each coverage point
        boot_probs = []
        for p in coverage_points:
            runs = run_data.get(p, run_data.get(round(p, 4), []))
            if len(runs) == 0:
                boot_probs.append(0.0)
                continue
            boot_sample = rng.choice(runs, size=len(runs), replace=True)
            boot_probs.append(boot_sample.mean())

        result = estimate_pc(coverage_points, boot_probs)
        if not np.isnan(result['p_c']):
            pc_samples.append(result['p_c'])
            sharpness_samples.append(result['sharpness'])

    if len(pc_samples) < 10:
        return {
            'p_c': float('nan'),
            'ci_lower': float('nan'),
            'ci_upper': float('nan'),
            'sharpness': float('nan'),
            'sharpness_ci_lower': float('nan'),
            'sharpness_ci_upper': float('nan'),
            'n_valid_bootstraps': len(pc_samples),
        }

    pc_arr = np.array(pc_samples)
    sh_arr = np.array(sharpness_samples)

    return {
        'p_c': float(np.median(pc_arr)),
        'ci_lower': float(np.percentile(pc_arr, 2.5)),
        'ci_upper': float(np.percentile(pc_arr, 97.5)),
        'sharpness': float(np.median(sh_arr)),
        'sharpness_ci_lower': float(np.percentile(sh_arr, 2.5)),
        'sharpness_ci_upper': float(np.percentile(sh_arr, 97.5)),
        'n_valid_bootstraps': len(pc_samples),
    }


def hub_targeting_ratio(pc_uniform, pc_targeted, run_data_uniform, run_data_targeted,
                        coverage_points, n_bootstrap=1000, seed=42):
    """Compute hub-targeting efficiency ratio with paired bootstrap CI.

    ratio = p_c_uniform / p_c_targeted
    """
    rng = np.random.default_rng(seed)
    coverage_points = np.array(sorted(coverage_points))

    ratio_samples = []

    for _ in range(n_bootstrap):
        # Same resample indices for paired bootstrap
        boot_probs_u = []
        boot_probs_t = []
        for p in coverage_points:
            runs_u = run_data_uniform.get(p, run_data_uniform.get(round(p, 4), []))
            runs_t = run_data_targeted.get(p, run_data_targeted.get(round(p, 4), []))

            n_u = len(runs_u)
            n_t = len(runs_t)

            if n_u == 0 or n_t == 0:
                boot_probs_u.append(0.0)
                boot_probs_t.append(0.0)
                continue

            # Use same indices where possible
            n_common = min(n_u, n_t)
            indices = rng.integers(0, n_common, size=n_common)
            boot_probs_u.append(np.array(runs_u[:n_common])[indices].mean())
            boot_probs_t.append(np.array(runs_t[:n_common])[indices].mean())

        res_u = estimate_pc(coverage_points, boot_probs_u)
        res_t = estimate_pc(coverage_points, boot_probs_t)

        if not np.isnan(res_u['p_c']) and not np.isnan(res_t['p_c']) and res_t['p_c'] > 0.001:
            ratio_samples.append(res_u['p_c'] / res_t['p_c'])

    if len(ratio_samples) < 10:
        return {
            'ratio': float('nan'),
            'ci_lower': float('nan'),
            'ci_upper': float('nan'),
        }

    arr = np.array(ratio_samples)
    return {
        'ratio': float(np.median(arr)),
        'ci_lower': float(np.percentile(arr, 2.5)),
        'ci_upper': float(np.percentile(arr, 97.5)),
    }
