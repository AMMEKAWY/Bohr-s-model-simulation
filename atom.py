import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants in atomic units
k = 1
e = 1
h_bar = 1
m_e = 1

# Initial conditions
n = 1
r = n * h_bar / (m_e * np.pi)
v = k * e / (m_e * r)

# Time parameters (decreased time step)
dt = 1e-3
num_steps = 500
time = np.linspace(0, num_steps * dt, num_steps)

# Arrays to store position coordinates
x = np.zeros(num_steps)
y = np.zeros(num_steps)

# Create the initial plot with black background
fig, ax = plt.subplots(figsize=(8, 8))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
line, = ax.plot([], [], 'lime', lw=2)
proton, = ax.plot([0], [0], 'ro', label='Proton')  # Proton at the center
ax.set_title('Electron Trajectory in Bohr\'s Model (Atomic Units)')
ax.set_xlabel('X Position (a.u.)')
ax.set_ylabel('Y Position (a.u.)')
ax.legend()
ax.grid(False)

# Function to update the plot at each frame
def update(frame):
    x[frame] = r * np.cos(2 * np.pi * frame * dt / (n * h_bar / (m_e * v)))
    y[frame] = r * np.sin(2 * np.pi * frame * dt / (n * h_bar / (m_e * v)))
    line.set_data(x[:frame], y[:frame])
    
    # Update proton position
    proton.set_data([0], [0])
    
    # Update plot limits dynamically
    ax.set_xlim(np.min(x) - r, np.max(x) + r)
    ax.set_ylim(np.min(y) - r, np.max(y) + r)
    
    return line, proton

# Create the animation
ani = FuncAnimation(fig, update, frames=num_steps, interval=20, blit=True)

# Save the animation as a GIF
ani.save('bohr_model_animation.gif', writer='imagemagick', fps=60)

# Display the saved GIF
plt.show()

