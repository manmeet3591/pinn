import numpy as np
import scipy.io

# Set grid size and time steps
N = 100  # Grid points in x and y
T = 50   # Time steps

# Generate grid coordinates and time points
X_star = np.random.rand(N, 2)       # X_star shape (100, 2): random coordinates for X and Y
U_star = np.random.rand(N, 2, T)    # U_star shape (100, 2, 50): random velocity fields (u, v)
P_star = np.random.rand(N, T)       # P_star shape (100, 50): random pressure field
t_star = np.linspace(0, 2, T).reshape(1, T)  # t_star shape (1, 50): Time vector reshaped

# Save the data in a .mat file
scipy.io.savemat('initial_conditions_vortex_shedding.mat', {
    'X_star': X_star,  # Shape (100, 2)
    'U_star': U_star,  # Shape (100, 2, 50) for u and v components
    'P_star': P_star,  # Shape (100, 50) for pressure field
    't_star': t_star   # Shape (1, 50) for time steps
})

print("Initial conditions saved to 'initial_conditions_vortex_shedding.mat' with correct shapes.")
