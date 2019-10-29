from pylab import *
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
"""
Global settings:
-----------------
"""
ExportName = 'Fig2.eps'

optionProcessing = False
for opt in sys.argv[1:]:
    if opt.strip() == 'processing=True':
        optionProcessing = True
        print '[processing mode]'
"""
Plot functions:
----
"""

rc('axes', linewidth=1.5)

#Load numerical data
dataDict = dict()
paramDict = dict()
varDict = dict()
datapathDict = {
    0: 'data/equal_resonators_at_finite_kBT_setA.dat',
    1: 'data/equal_resonators_at_zero_kBT_setA.dat',
    2: 'data/GammaS_dependence_at_finite_kBT_setA.dat',
    3: 'data/GammaS_dependence_at_finite_kBT_setB.dat',
}
for k, v in datapathDict.iteritems():
    labelLst = list()
    dataset = loadtxt(v)
    for nidx, line in enumerate(open(v, 'r')):
        if nidx == 2:
            paramDict[k] = eval(line[1:])
        if nidx == 6:
            varDict[k] = str(line[1:]).strip()[1:-1]
        if nidx == 10:
            labelLst = str(line[1:]).strip()[1:-1].replace('\t', '').replace(
                ' ', '').split(',')
    dataDict[k] = {k: v for k, v in zip(labelLst, dataset.T)}
xKey = lambda setIdx: varDict[setIdx]


#Define figure
def plotMultiData(prefix):
    titlefsize = 24
    lgdsize = 9
    fsize = 9
    lblsize = 9
    yfsize = fsize
    xfsize = fsize
    zfsize = fsize
    cfsize = fsize
    tfsize = fsize
    lw = 2

    fig = figure(1, figsize=(8.66, 5.91))
    clf()
    sub = dict()

    sub[0] = subplot2grid((3, 1), (0, 0))
    setIdx = 0
    p = paramDict[setIdx]
    GS = p['GS']
    GN = p['GNL']
    plot(
        dataDict[setIdx][xKey(setIdx)],
        dataDict[setIdx]['IL'],
        'k-',
        lw=lw,
        label='rT={0}'.format('%.1f' % (p['TL'] / p['wL'])))

    setIdx = 1
    p = paramDict[setIdx]
 #   plot(
 #       dataDict[setIdx][xKey(setIdx)],
 #       dataDict[setIdx]['IL'],
 #       'r--',
 #       lw=lw,
 #       label='rT={0}'.format('%.1f' % (p['TL'] / p['wL'])))
    ylabel('IL', fontsize=yfsize, labelpad=30)
    xlim(-3 * GS, 3 * GS)
    ylim(0, 0.5 * GN)

#    lgd = legend(
#        loc=3,
#        bbox_to_anchor=(0.6, 0.56),
#        labelspacing=0.1,
#        columnspacing=0.85,  #0.21, 0.74
#        borderpad=0.35,
#        handletextpad=0.1,
#        ncol=1,
#        handlelength=1.75,
#        borderaxespad=0.,
#        frameon=False)
#    [setp(ltxt, fontsize=lgdsize) for ltxt in lgd.get_texts()]

    #------
    sub[1] = subplot2grid((3, 1), (1, 0), rowspan=2)
    setIdx = 0
    p = paramDict[setIdx]
    plot(
        dataDict[setIdx][xKey(setIdx)], dataDict[setIdx]['nOscL'], 'k-', lw=lw)
    ylabel('nOscL', fontsize=yfsize, labelpad=30)

    xlabel(xKey(setIdx), fontsize=xfsize, labelpad=15)
    xlim(-3 * GS, 3 * GS)
    ylim(0, 14)

    nB = lambda x: 1. / (exp(x) - 1)
    axhline(y=nB(p['wL'] / p['TL']), color='0.6', ls=':', lw=lw)

    ABS = lambda sgn, n, m: 0.5 * sgn * sqrt((n * p['wL'] + m * p['wR'])**2 - 2 * p['GS']**2)
    epsCooling = ABS(1, 1, 0)
    axvline(x=epsCooling, ymin=0.08, ymax=0.4, color='b', ls='-', lw=1.5)

    #------
    axins = inset_axes(
        sub[1],
        loc=3,
        width=3,
        height=1.5,
        bbox_to_anchor=(0.45, 0.39),
        bbox_transform=sub[1].figure.transFigure)
    psList = ['k-', 'g-.']
    for nidx, setIdx in enumerate([2, 3]):
        p = paramDict[setIdx]
        nTH = nB(p['wL'] / p['TL'])
        wL = p['wL']
        Y = dataDict[setIdx]['nOscL'] / (nB(p['wL'] / p['TL']) + 0.)
        lbl = 'rGN={0}m'.format(p['GNL'] / 1e-3)
        plot(dataDict[setIdx][xKey(setIdx)], Y, psList[nidx], lw=lw, label=lbl)
        xlim(0 * wL, 0.7 * wL)
    ylim(0, 1)

    lgd = legend(
        loc=3,
        bbox_to_anchor=(0.1, 0.5),
        labelspacing=1.5,
        columnspacing=0.85,
        borderpad=0.35,
        handletextpad=0.1,
        ncol=1,
        handlelength=4,
        borderaxespad=0.,
        frameon=False)
    [setp(ltxt, fontsize=lgdsize) for ltxt in lgd.get_texts()]

    #================================
    axins.annotate(
        'GSInwL',
        xy=(0.3, -0.22),
        xycoords='axes fraction',
        fontsize=lblsize,
    )
    #   axins.annotate(
    #       'nLNorm',
    #       xy=(0.1, 0.36),
    #       xycoords='axes fraction',
    #       fontsize=lblsize,
    #   )
 #   sub[0].annotate(
 #       'A',
 #       xy=(0.01, 0.86),
 #       xycoords='axes fraction',
 #       fontsize=lblsize,
 #   )
 #   sub[1].annotate(
 #       'B',
 #       xy=(0.01, 0.93),
 #       xycoords='axes fraction',
 #       fontsize=lblsize,
 #   )
    sub[1].annotate(
        'cooling',
        xy=(0.75, 0.21),
        xycoords='axes fraction',
        fontsize=lblsize,
        rotation=0)
    sub[1].annotate(
        'epsCooling',
        xy=(0.905, 0.355),
        xycoords='axes fraction',
        fontsize=lblsize)

    setIdx = 2
    p = paramDict[setIdx]
    unitX = p['wL']
    XTickLst = arange(0 * unitX, 0.7 * unitX + unitX / 10., 0.35 * unitX)
    XTickLblLst = [
        '%.1f' % (l / unitX) if n % 2 == 0 else ''
        for n, l in enumerate(XTickLst)
    ]
    axins.set_xticks(XTickLst)
    axins.set_xticklabels(XTickLblLst)

    YTickLst = arange(0, 1 + 0.25, 0.25)
    YTickLblLst = [
        '%.1f' % (l) if n % 2 == 0 else '' for n, l in enumerate(YTickLst)
    ]
    axins.set_yticks(YTickLst)
    axins.set_yticklabels(YTickLblLst)
    axins.tick_params(pad=11)
    axins.set_ylabel('nLNorm', labelpad=40)

    for kdx, v in sub.iteritems():
        if kdx in [0]:
            setIdx = 0
            p = paramDict[setIdx]
            unitX = p['GS']
            unitY = p['GNL']
            XTickLst = arange(-3 * unitX, 3 * unitX + unitX / 1., unitX / 1.)
            XTickLblLst = []
            v.set_xticks(XTickLst)
            v.set_xticklabels(XTickLblLst)

            YTickLst = arange(0, 0.6 * unitY + unitY / 5., unitY / 5.)
            YTickLblLst = [
                '%.1f' % (l / unitY) if n % 2 == 0 else ''
                for n, l in enumerate(YTickLst)
            ]
            v.set_yticks(YTickLst)
            v.set_yticklabels(YTickLblLst)
            v.tick_params(pad=11)

    for kdx, v in sub.iteritems():
        if kdx in [1]:
            setIdx = 0
            p = paramDict[setIdx]
            unitX = p['GS']
            XTickLst = arange(-3 * unitX, 3 * unitX + unitX / 1., unitX / 1.)
            XTickLblLst = [
                '%.0f' % (l / unitX) if n % 2 == 1 else ''
                for n, l in enumerate(XTickLst)
            ]
            v.set_xticks(XTickLst)
            v.set_xticklabels(XTickLblLst)

            YTickLst = arange(0, 14 + 0.01, 2)
            YTickLblLst = [
                '%.0f' % (l) if n % 2 == 0 else ''
                for n, l in enumerate(YTickLst)
            ]
            v.set_yticks(YTickLst)
            v.set_yticklabels(YTickLblLst)
            v.tick_params(pad=11)

    subplots_adjust(
        left=0.13, bottom=0.13, right=0.995, top=0.99, wspace=0.4, hspace=0.10)
    if optionProcessing:
        savefig(ExportName, facecolor='none', edgecolor='none', dpi=400)
    else:
        show()


plotMultiData('0_')
