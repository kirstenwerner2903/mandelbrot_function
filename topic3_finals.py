import numpy as np

def mandelbrot_set( xrange:tuple, yrange:tuple, resolution:tuple, max_iter:int ):
    """
    Parameters:
        xrange (tuple): the range of the real part 
        yrange (tuple): the range of the imaginary part
        resolution (tuple): the number of points to sample in the real and imaginary parts
        max_iter (int): the maximum number of iterations to determine boundedness

    Outputs: 
        A 2D numpy array of shape resolution, with values normalized between 0 and 1.
        Each value represents the "escape time" for a point in the complex plane.
    """
    rows=resolution[0]
    columns=resolution[1]
    array = np.ones((rows,columns))
    return array

def plot_matrix(data: np.ndarray):
    import matplotlib.pyplot as plt
    assert data.ndim == 2, "Data must be a 2D array"
    assert data.min() >= 0 and data.max() <= 1, "Data must lie between 0 and 1"
    plt.imshow(data, origin='lower', cmap='gray', vmin=0, vmax=1)
    plt.tight_layout()
    plt.axis('off')
    plt.show()

data = mandelbrot_set(xrange=(-2, 1), yrange=(-1.5, 1.5),
resolution=(1000, 1000), max_iter=100)
plot_matrix(data)