def heatmap(data, row_labels, col_labels, ax=None,
            cbar_kw=None, cbarlabel="", **kwargs):
    """
    Create a heatmap from a numpy array and two lists of labels.

    Parameters
    ----------
    data
        A 2D numpy array of shape (M, N).
    row_labels
        A list or array of length M with the labels for the rows.
    col_labels
        A list or array of length N with the labels for the columns.
    ax
        A `matplotlib.axes.Axes` instance to which the heatmap is plotted.  If
        not provided, use current axes or create a new one.  Optional.
    cbar_kw
        A dictionary with arguments to `matplotlib.Figure.colorbar`.  Optional.
    cbarlabel
        The label for the colorbar.  Optional.
    **kwargs
        All other arguments are forwarded to `imshow`.
    """

    if ax is None:
        ax = plt.gca()

    if cbar_kw is None:
        cbar_kw = {}

    # Plot the heatmap
    im = ax.imshow(data, **kwargs)

    # Create colorbar
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

    # Show all ticks and label them with the respective list entries.
    ax.set_xticks(np.arange(data.shape[1]), labels=col_labels)
    ax.set_yticks(np.arange(data.shape[0]), labels=row_labels)

    # Let the horizontal axes labeling appear on top.
    ax.tick_params(top=True, bottom=False,
                   labeltop=True, labelbottom=False)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=-30, ha="right",
             rotation_mode="anchor")

    # Turn spines off and create white grid.
    ax.spines[:].set_visible(False)

    ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
    ax.tick_params(which="minor", bottom=False, left=False)

    return im, cbar


def annotate_heatmap(im, data=None, valfmt="{x:.2f}",
                     textcolors=("black", "black"),
                     threshold=None, **textkw):
    """
    A function to annotate a heatmap.

    Parameters
    ----------
    im
        The AxesImage to be labeled.
    data
        Data used to annotate.  If None, the image's data is used.  Optional.
    valfmt
        The format of the annotations inside the heatmap.  This should either
        use the string format method, e.g. "$ {x:.2f}", or be a
        `matplotlib.ticker.Formatter`.  Optional.
    textcolors
        A pair of colors.  The first is used for values below a threshold,
        the second for those above.  Optional.
    threshold
        Value in data units according to which the colors from textcolors are
        applied.  If None (the default) uses the middle of the colormap as
        separation.  Optional.
    **kwargs
        All other arguments are forwarded to each call to `text` used to create
        the text labels.
    """

    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()

    # Normalize the threshold to the images color range.
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max())/2.

    # Set default alignment to center, but allow it to be
    # overwritten by textkw.
    kw = dict(horizontalalignment="center",
              verticalalignment="center")
    kw.update(textkw)

    # Get the formatter in case a string is supplied
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

    # Loop over the data and create a `Text` for each "pixel".
    # Change the text's color depending on the data.
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if np.abs(data[i,j]) 70:
                textcolors=("white", "white")
            else:
                textcolors=("white", "white")
            kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
            print(kw)
            text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
            texts.append(text)

    return texts


import numpy as np
import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
from cmcrameri import cm

fluxes = ["a","b","c","d"]
scenarios = ["1","delta 2-1","delta 3-1"]

scenarios2 = ["delta 2-1","delta 3-1"]


flux_array_tree = np.array([[404, 384, 336 ],
                    [376, 411, 499],
                    [21,  16,  10],
                    [-35, -46, -81]])

flux_array_tree_shift= np.array([[404, 386, 343 ],
                    [376, 403, 437],
                    [21,  22,  35],
                    [-35, -45, -50]])

flux_array_downspout= np.array([[271, 184, 104 ],
                    [463, 480, 490],
                    [67,  123,  187],
                    [-36, -21, -16]])

flux_array_pavement= np.array([[766, 142, 13],
                    [0, -3, -2],
                    [0,  638,  772],
                    [0, -12, -17]])


flux_array_tree_p = np.array([[-3, -9],
            [5,16],
            [-1,-1],
            [-2,-6]])

flux_array_shift_p = np.array([[-2, -8],
            [3,8],
            [0,2],
            [-1,-2]])

flux_array_dis_p = np.array([[-11, -22],
            [2,4],
            [7,16],
            [2,3]])

flux_array_pav_p = np.array([[-82, -98],
            [0,0],
            [83,101],
            [-1,-3]])


fig, ax = plt.subplots(figsize=(5,5))

im, cbar = heatmap(flux_array_pav_p, fluxes, scenarios2, ax=ax,
                   cmap=cm.vik_r, cbarlabel="-",vmin=-101,vmax=101)
texts = annotate_heatmap(im, valfmt="{x:d} %",size=15)

fig.tight_layout()
plt.savefig('./flux_array_percent_diff_pav.png',dpi=500)