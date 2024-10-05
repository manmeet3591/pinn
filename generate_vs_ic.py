import scipy.io
import numpy as np

# Define domain parameters
L = 10.0  # Length of the domain
H = 4.0   # Height of the domain
D = 1.0   # Diameter of the cylinder
U_inf = 1.0  # Freestream velocity

# Create a meshgrid for the flow domain
nx, ny = 200, 80  # Number of grid points in x and y directions
x = np.linspace(0, L, nx)
y = np.linspace(-H/2, H/2, ny)
X, Y = np.meshgrid(x, y)

# Initialize velocity field
u = U_inf * np.ones_like(X)  # Uniform flow in the x-direction
v = np.zeros_like(X)         # No initial velocity in the y-direction

# Cylinder position
xc, yc = L / 4, 0  # Cylinder center at (L/4, 0)
r = np.sqrt((X - xc)**2 + (Y - yc)**2)  # Distance from cylinder center

# Set velocity inside the cylinder to zero (no-slip condition)
u[r < D/2] = 0
v[r < D/2] = 0

# Initialize pressure field
p = np.zeros_like(X)  # Uniform initial pressure

# Create dictionary to save in .mat format
data = {
    'X': X,
    'Y': Y,
    'u': u,
    'v': v,
    'p': p
}

# Save the data to a .mat file
scipy.io.savemat('vortex_shedding_initial_conditions.mat', data)
