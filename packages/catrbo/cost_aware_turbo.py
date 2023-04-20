from .trust_region import TrustRegion

class CostAwareTurbo:
    """
    The Cost Aware Turbo Algorithm.

    Parameters
    ----------
    f : black box function to be optimized
    lb : Lower variable bounds, numpy.array, shape (d,).
    ub : Upper variable bounds, numpy.array, shape (d,).
    """
    def __init__(
        f,
        lb,
        ub
    ):

        # Very basic input checks
        assert callable(f)
        assert lb.ndim == 1 and ub.ndim == 1
        assert lb.ndims == ub.ndims

        # Save function information
        self.f = f
        self.lb = lb
        self.ub = ub
        self.dim = lb.ndim # number of dimensions of the sample space

    def optimize():
        tr = TrustRegion(f = self.f,
                         lb = self.lb,
                         ub = self.ub)
        tr.get_random_points();
        tr.evaluate();

        while tr.restart_trggered:
            tr.acquire_points();
            tr.evaluate();
        