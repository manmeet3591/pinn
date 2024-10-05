import numpy as np
import scipy.io

# Set grid size and time steps
N = 100  # Grid points in x and y
T = 50   # Time steps

# Generate grid coordinates and time points
X_star = np.random.rand(N, 2)  # Random initial conditions for X and Y
U_star = np.random.rand(N, 2, T)  # Random initial velocity fields for u (x) and v (y)
P_star = np.random.rand(N, T)     # Random initial pressure field
t_star = np.linspace(0, 2, T)     # Time vector

# `U_star[:, 0, :]` is the `u` velocity component (x-direction)
# `U_star[:, 1, :]` is the `v` velocity component (y-direction)

# Save the data in a .mat file
scipy.io.savemat('initial_conditions_vortex_shedding.mat', {
    'X_star': X_star,
    'U_star': U_star,  # Contains both u and v components
    'P_star': P_star,
    't': t_star
})

print("Initial conditions (u, v, p) saved to initial_conditions_vortex_shedding.mat")
