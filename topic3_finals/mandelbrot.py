import numpy as np
#Define mandelbrot function here
def plot_matrix(data: np.ndarray):
    import matplotlib.pyplot as plt
    assert data.ndim == 2, "Data must be a 2D array"
    assert data.min() >= 0 and data.max() <= 1, "Data must lie between 0 and 1"
    plt.imshow(data, origin='lower', cmap='gray')
    plt.tight_layout()
    plt.axis('off')
    plt.show()
