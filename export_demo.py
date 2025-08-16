import argparse, os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

p = argparse.ArgumentParser()
p.add_argument("--seconds", type=int, default=10)
p.add_argument("--fps", type=int, default=12)
p.add_argument("--mp4", action="store_true")
p.add_argument("--outfile", default="outputs/demo.mp4")
args = p.parse_args()

os.makedirs("outputs", exist_ok=True)

fig = plt.figure(figsize=(6,6))
ax = plt.gca()
ax.axis('off')

x = np.linspace(-3, 3, 600)
y = np.linspace(-3, 3, 600)
X, Y = np.meshgrid(x, y)
im = ax.imshow(np.zeros_like(X), origin='lower', animated=True)

def update(i):
    t = i / (args.seconds * args.fps)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(6*R + 2*np.pi*t) / (1 + R)
    im.set_data(Z)
    return [im]

ani = animation.FuncAnimation(fig, update, frames=args.seconds*args.fps, blit=True)

if args.mp4:
    print(f"Saving MP4 to: {args.outfile}")
    Writer = animation.writers['ffmpeg']
    ani.save(args.outfile, writer=Writer(fps=args.fps))
    print(f"Done: {args.outfile}")
else:
    ani.save("outputs/demo.gif", writer=animation.PillowWriter(fps=args.fps))
    print("Done: outputs/demo.gif")
