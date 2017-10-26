import numpy as np
import matplotlib.pyplot as plt

from .tools import polygon_path
from .dggs import DGGS

dg = DGGS()


def _get_ax(ax):
    return ax if ax else plt.gca()


def plot_bbox(extents, style='-', ax=None, **kwargs):
    """
    extents : (left, right, bottom, top)
    """

    ax = _get_ax(ax)
    extents = [float(v) for v in extents]
    return ax.plot(*polygon_path(extents[:2], extents[2:]), style, **kwargs)


def add_cell_plot(cell_addr, style='-', ax=None,  w=None, h=None, crs=None):
    tr, (maxW, maxH) = dg.pixel_coord_transform(cell_addr, w, h, dst_proj=crs)

    w = maxW if w is None else w
    h = maxH if h is None else h

    bb = 0.5 - 1e-8
    x = np.linspace(-bb, w - 1 + bb, w)
    y = np.linspace(-bb, h - 1 + bb, h)
    x, y = polygon_path(x, y)

    u, v = tr(x, y)

    ax = _get_ax(ax)
    ax.plot(u, v, style)