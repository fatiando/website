"""
Create an animation of spherical rolling windows with Bordado.
"""

import shutil
from pathlib import Path

import imageio
import pygmt

import bordado as bd

outdir = Path("_frames")
shutil.rmtree(outdir, ignore_errors=True)
outdir.mkdir(exist_ok=True)

dpi = 100

region = [-180, 180, -90, 90]
coordinates = bd.random_coordinates_spherical(region, size=5_000, random_seed=42)
fig = pygmt.Figure()
fig.coast(land="gray", region=region, projection="W20c", frame="af")
fig.plot(
    x=coordinates[0].ravel(), y=coordinates[1].ravel(), style="c0.07c", fill="black"
)
fig.savefig(outdir / "global-windows-0000.png", dpi=dpi)

(longitude, latitude), indices = bd.rolling_window_spherical(
    coordinates, region=region, window_size=60, overlap=0.5
)

for i, w in enumerate(indices):
    fig = pygmt.Figure()
    fig.coast(land="gray", region=region, projection="W20c")
    fig.plot(
        x=coordinates[0][w].ravel(),
        y=coordinates[1][w].ravel(),
        style="c0.07c",
        fill="black",
    )
    fig.plot(x=longitude, y=latitude, style="c0.2c", fill="orange")
    fig.plot(x=longitude[i], y=latitude[i], style="c0.3c", fill="red")
    fig.basemap(frame="af")
    fig.savefig(outdir / f"global-windows-{i + 1:04d}.png", dpi=dpi)

images = [imageio.v3.imread(fname) for fname in sorted(outdir.glob("*.png"))]
imageio.mimsave("bordado-spherical-rolling-windows.gif", images, duration=500, loop=0)

shutil.rmtree(outdir, ignore_errors=True)
