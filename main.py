import os, numpy as np
import matplotlib.pyplot as plt

os.makedirs("outputs", exist_ok=True)

x = np.linspace(-3, 3, 800)
y = np.linspace(-3, 3, 800)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(6*R) / (1 + R)

plt.figure(figsize=(6,6))
plt.axis('off')
plt.imshow(Z, origin='lower')
plt.tight_layout()
plt.savefig("outputs/frame_000.png", dpi=200, bbox_inches='tight', pad_inches=0)
print("Wrote outputs/frame_000.png")
