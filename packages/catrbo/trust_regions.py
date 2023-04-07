class TrustRegion:
    """
    Individual trust region code

    Parameters
    -----------
    lb: Lower variable bounds, numpy.array, shape (d,).
    ub: Upper variable bounds, numpy.array, shape (d,).
    cost_model: model for cost estimation, function.
    n_init: number of points in the initial run, int.
    success_tolerance: number of succcessful optimization before trust region resize, int.
    failure_tolerance: number of unsucccessful optimization before trust region resize, int.
    """
    def __init__(
        self,
        lb,
        ub,
        cost_model,
        n_init,
        success_tolerance, 
        failure_tolerance)

        # Very basic input checks
        assert lb.ndim == 1 and ub.ndim == 1
        assert len(lb) == len(ub)
        assert callable(cost_model)
        assert n_init > 0 and isinstance(n_init, int)
