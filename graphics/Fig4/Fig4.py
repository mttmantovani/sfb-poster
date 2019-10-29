# Fig 3

import sys
from collections import OrderedDict

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import numpy as np
"""
Global settings:
-----------------
"""
ExportName = 'Fig4.eps'

optionProcessing = False
for opt in sys.argv[1:]:
    if opt.strip() == '--processing':
        optionProcessing = True
"""
Plot functions:
----
"""

matplotlib.rc('axes', linewidth=1.5)

def default_kwargs():
    kwargs = {
        'interpolation': 'nearest',
        'figsize': (15./2.54, 16./2.54),
        'fontsize': 7,
        'titlefontsize': 11,
        'lw': 3.,
        'lss': ['-', '--', ':', '-.'],
        'cls': ['k', 'm', 'cornflowerblue', 'orangered', 'grey'],
        'labelpad': 20
    }

    return kwargs


def load_data():
    dataDict = OrderedDict()
    parDict = OrderedDict()
    varDict = OrderedDict()
    #    datapathDict = {idx: dataset for idx, dataset in enumerate(sys.argv[1:])}
    datapathDict = {
        0: 'data/20190410-172050.txt',
        1: 'data/20190410-191818.txt',
        2: 'data/20190411-000627.txt',
        3: 'data/20190415-090824.txt',
        4: 'data/20190613-105143.txt',
        5: 'data/20190613-121032.txt'
    }

    for k, v in datapathDict.iteritems():
        labelLst = list()
        dataset = np.loadtxt(v)
        for nidx, line in enumerate(open(v, 'r')):
            if nidx == 2:
                parDict[k] = eval(line[1:].strip())
            if nidx == 4:
                varDict[k] = eval(line[1:].strip())
            if nidx == 8:
                labelLst = eval(line[1:].strip())
        dataDict[k] = OrderedDict((k, v) for k, v in zip(labelLst, dataset.T))
        dataDict[k]['filename'] = v

    return parDict, varDict, dataDict


def plot_data(**kwargs):
    # Load data
    parDict, varDict, dataDict = load_data()

    # Set keyword arguments for options
    plt_args = default_kwargs()
    for k in kwargs.keys():
        if k in plt_args.keys():
            plt_args[k] = kwargs[k]
        else:
            raise Exception("Invalid keyword argument '" + k + "'.")

    # Define figure layout
    fig, axes = plt.subplots(2, 1, figsize=plt_args['figsize'])

    ax1 = axes[0]
    ax2 = axes[1]
 #   gs = gridspec.GridSpec(2, 2, width_ratios=[0.25, 1])
 #   ax1 = fig.add_subplot(gs[0, :])  # Current
 #   ax2 = fig.add_subplot(gs[1, 0])  # Local efficiency
 #   ax3 = fig.add_subplot(gs[1, 1])  # Nonlocal efficiency
  #  ax3 = fig.add_subplot()  # Nonlocal efficiency
 #   axins = inset_axes(
 #       ax3,
 #       loc=1,
 #       width=0.7,
 #       height=0.6,
 #       # bbox_to_anchor=(0.24, 0.19),
 #       borderpad=0.2,
 #       bbox_transform=ax3.transAxes)

    # Plot data
 #   ax1.plot(
 #       dataDict[0]['x'],
 #       dataDict[0]['IL'] / float(parDict[0]['GNL']),
 #       lw=plt_args['lw'],
 #       ls=plt_args['lss'][0],
 #       c=plt_args['cls'][0],
 #       label='g=0.05GS')
 #   ax1.plot(
 #       dataDict[1]['x'],
 #       dataDict[1]['IL'] / float(parDict[1]['GNL']),
 #       lw=plt_args['lw'],
 #       ls=plt_args['lss'][1],
 #       c=plt_args['cls'][1],
 #       label='g=0.2GS')
#
 #   ax2.plot(
  #      dataDict[4]['x'],
   ##     abs(dataDict[4]['eta_L']),
   #     lw=plt_args['lw'] + 0.5,
   #     c='orange')

    ax1.plot(
        dataDict[5]['x'],
        abs(dataDict[5]['IL']),
        lw=plt_args['lw'],
        c='gray')


    nB = lambda x: 1. / (np.exp(x) - 1.)
    argnbL = float(parDict[5]['wL']) / float(parDict[5]['TOscL'])
    argnbR = float(parDict[5]['wR']) / float(parDict[5]['TOscR'])
    ax2.plot(
        dataDict[5]['x'],
        dataDict[5]['nOscR'] / nB(argnbR),
        ls='-.',
        c='r',
        lw=plt_args['lw'],
        label='nR')
    ax2.plot(
        dataDict[5]['x'],
        dataDict[5]['nOscL'] / nB(argnbL),
        c='b',
        lw=plt_args['lw'],
        label='nL')
#
#    # Adjustments
#    ax1.set_xlim(-4, 4)
#    ax1.set_ylim(0, 0.6)
#    ax1.set_xticks([-4, -3, -2, -1, 0, 1, 2, 3, 4])
#    ax1.set_yticks([0, 0.25, 0.5])
#    ax1.set_xticklabels([-4, '', -2, '', 0, '', 2, '', 4])
#    ax1.set_yticklabels([0, '', 0.5])
#    ax1.set_xlabel(
#        'eps', fontsize=plt_args['fontsize'], labelpad=plt_args['labelpad'])
#    ax1.set_ylabel(
#        'IR', fontsize=plt_args['fontsize'], labelpad=plt_args['labelpad'])
#    ax1.axvline(0.708, ls=':', lw=1., c='g', zorder=-1)
#    ax1.axvline(2.39792, ls=':', lw=1., c='orange', zorder=-1)
#    ax1.plot(
#        0.708,
#        0.5,
#        marker='^',
#        markeredgecolor='k',
#        markerfacecolor='g',
#        markersize=7,
#        markeredgewidth=0.4)
#    ax1.plot(
#        2.39792,
#        0.5,
#        marker='*',
#        markeredgecolor='k',
#        markerfacecolor='orange',
#        markersize=7,
#        markeredgewidth=0.4)
#    ax.plot(
#        0.7068,
#        0.93,
#        marker='^',
#        markeredgecolor='k',
#        markerfacecolor='g',
#        markersize=7,
#        markeredgewidth=0.4)
#    ax2.plot(
#        2.55,
#        0.93,
#        marker='*',
#        markeredgecolor='k',
#        markerfacecolor='orange',
#        markersize=7,
#        markeredgewidth=0.4)
#
#    # This moves the yaxis label closer to the axis
#    ticklab = ax1.yaxis.get_ticklabels()[0]
#    trans = ticklab.get_transform()
#    ax1.yaxis.set_label_coords(0.0, 0.24, transform=trans)
#
#    # Legend
#    ax1.legend(
#        frameon=False,
#        loc=2,
#        bbox_to_anchor=(-3.4, 0.586),
#        bbox_transform=ax1.transData,
#        borderaxespad=0.,
#        borderpad=0.,
#        handletextpad=-0.2,
#        ncol=2,
#        labelspacing=0.01,
#        handlelength=1.3,
#        columnspacing=0.5)
#
#    ax2.set_xlim(2.2, 2.6)
#    ax2.set_ylim(0, 1.)
#    ax2.set_xticks([2.2, 2.4, 2.6])
#    ax2.set_yticks([0, 0.25, 0.5, 0.75, 1])
#    ax2.set_yticklabels([0, '', '', '', 1])
#
#    ax2.set_xlabel(
#        'eps', fontsize=plt_args['fontsize'], labelpad=plt_args['labelpad'])
#    ax2.set_ylabel('etaL', fontsize=plt_args['fontsize'], labelpad=0)
#
#    #    ticklab = ax2.yaxis.get_ticklabels()[0]
#    #    trans=ticklab.get_transform()
#    #    ax2.yaxis.set_label_coords(0.0, 5., transform=trans)

    ax1.set_xlim(0.706, 0.712)
    ax2.set_xlim(0.706, 0.712)
  #  ax1.set_ylim(0, 1.)
    ax1.set_xticks([0.706, 0.709, 0.712])
    ax1.set_yticks(np.linspace(2.5e-5,3.e-5,3))
    ax1.set_yticklabels(['0.25', '', '0.3']) 
    ax2.set_xticks([0.706, 0.709, 0.712])
  #  ax1.set_yticks([0, 0.25, 0.5, 0.75, 1])
  #  ax1.set_yticklabels([0, '', '', '', 1])
    ax1.set_xticklabels(['', '', ''])
    ax2.set_yticks([0.8, 0.9, 1., 1.1, 1.2])
    ax2.set_yticklabels([0.8, '', 1, '', 1.2])
    ax2.set_xlabel(
        'eps', fontsize=plt_args['fontsize'], labelpad=plt_args['labelpad'])
    ax1.set_ylabel('IL', fontsize=plt_args['fontsize'], labelpad=0)

#    axins.set_xlim(0.706, 0.712)
#    axins.set_ylim(0.7, 1.3)
#    axins.set_xticks([0.706, 0.709, 0.712])
#    axins.set_xticklabels(['', '', ''])
#    #   axins.set_xticklabels(['0.706ins', '', '0.712ins'])
#    axins.set_yticks([0.8, 1, 1.2])
#    axins.set_xlabel(
#        'eps2',
#        fontsize=plt_args['fontsize'],
#        labelpad=plt_args['labelpad'] + 0.2)
#    #   axins.set_ylabel('nav/nB', fontsize=plt_args['fontsize'], labelpad=plt_args['labelpad'])
#
#    # This moves the xaxis label closer to the axis
#    axins.xaxis.set_label_coords(0.5, -0.1)
#    # Legend
#
    ax2.legend(
        frameon=False,
        loc=1,
        bbox_to_anchor=(0.7114, 1.15),
        bbox_transform=ax2.transData,
        borderpad=0,
        borderaxespad=0,
        handletextpad=4,
        ncol=1,
        labelspacing=10,
        columnspacing=0.7,
        handlelength=6)

    for ax in axes:
        ax.tick_params(
            labelsize=plt_args['fontsize'], pad=plt_args['labelpad'])


#    axins.annotate(
#        'nav/nB',
#        xy=(0.706, 1.16),
#        xycoords='data',
#        fontsize=plt_args['fontsize'])

    #ticklab = ax2.xaxis.get_ticklabels()[0]
    #trans=ticklab.get_transform()
    #ax2.xaxis.set_label_coords(0.0, 0.24, transform=trans)

    plt.subplots_adjust(
        left=0.15, right=0.95, top=0.955, bottom=0.15, wspace=0.2, hspace=0.1)
    plt.savefig(ExportName, facecolor='none', edgecolor='none', dpi=400)

    if not optionProcessing:
        plt.show()


if __name__ == '__main__':
    plot_data()
