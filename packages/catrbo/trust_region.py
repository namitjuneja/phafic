from torch.quasirandom import SobolEngine

class TrustRegion:
    """
    Individual trust region code

    Parameters
    -----------
    f : black box function to be optimized
    lb: Lower variable bounds, numpy.array, shape (d,).
    ub: Upper variable bounds, numpy.array, shape (d,).
    cost_model: model for cost estimation, function.
    n_init: number of points in the initial run, int.
    succ_tol: number of succcessful optimization before trust region resize, int.
    fail_tol: number of unsucccessful optimization before trust region resize, int.
    """
    def __init__(
        self,
        f,
        lb,
        ub,
        cost_model,
        n_init,
        succ_tol, 
        fail_tol):

        # Very basic input checks
        assert lb.ndim == 1 and ub.ndim == 1
        assert len(lb) == len(ub)
        assert callable(cost_model)
        assert n_init > 0 and isinstance(n_init, int)
        assert succ_tol > 0 and isinstance(succ_tol, int)
        assert fail_tol > 0 and isinstance(fail_tol, int)

        # Save trust region parameters
        self.dim = len(lb)
        self.lb = lb
        self.ub = ub
        self.cost_model = cost_model
        self.n_init = n_init
        self.succ_tol = succ_tol
        self.fail_tol = fail_tol

        # variables containing candidates and their results
        self.Q = [] # queue of points pending evaluation
        self.x = np.empty((0,self.dim)) # points evaluated
        self.fx = [] # evaluation of points evaluated
    
    def get_initial_points():
        self.x_init = self.get_random_points();
        self.Q.extend(self.x_init) # queue the points to be evaluated
    
    def get_random_points():
        seed = np.random.randint(int(1e6)) # remove this for same random points
        sobol = SobolEngine(self.dim, scramble=True, seed=seed)
        x_init = sobol.draw(n_init)
        x_init = self.lb + (self.ub - self.lb)*x_init
        return x_init
    
    def evaluate():
        while self.Q:
            self.x_next = self.Q.pop()
            self.x = np.vstack([self.x, x_next])
            self.f();
