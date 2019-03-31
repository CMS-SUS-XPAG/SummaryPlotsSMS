#!/usr/bin/env python
import ROOT
import os, argparse, types, sys
import numpy as np
import matplotlib.pyplot as plt
#from matplotlib.ticker import MaxNLocator
#from collections import namedtuple
from inputs_BarPlot import *

path = os.getcwd()+'/'

#----------------------------#Configure plot from here#----------------------#
#bar_color = 'xkcd:medium blue'
#bar_color = 'xkcd:sky blue'
bar_color = 'xkcd:light orange'
bar_edge_color = 'xkcd:royal blue'
#bar_text_color = 'xkcd:light orange'
yaxis_label_color = 'black'
section_text_color = 'xkcd:royal blue'
desc_text_color = 'xkcd:royal blue'
comm_text_color = 'black'
title_color = 'xkcd:dark orange'
bar_height  =  0.30
line_color = ROOT.kBlue
#----------------------------#------------------------#----------------------#

#bar_color_36 = ROOT.kAzure+7  # use this!
#bar_color_13  = ROOT.kOrange -3

#
# some global options
#
commentOutsideBarLabels = [ "17-004-TChiWZ" ]  # force comment to be right of bar
preliminaryLabel = ""                          # "preliminary" label (filled automatically)
filename = 'barplot'                           # prefix for output files
#
# command line options
#
parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--cadi', '-c', help='always use CADI instead of arXiv number', dest='cadi', \
                        action='store_true', default=False)
parser.add_argument('--verbose', '-v', help='verbose output', dest='verbose', \
                        action='store_true', default=False)
parser.add_argument('--grid', help='show grid', dest='grid', \
                        action='store_true', default=False)
parser.add_argument('--batch', '-b', help='batch mode (produce pdf and exit)', dest='batch', \
                        action='store_true', default=False)
parser.add_argument('--output', '-o', help='output file', dest='output', type=str, default=None)
parser.add_argument('category', nargs=1, choices=['EWK', 'Squark', 'Gluino', 'GMSB'])
args = parser.parse_args()
verbose = args.verbose


#
# define category
#
analysis_group = args.category[0]
#
# create list of selected analysis
#
print(analysis_group)
allABs_list = allABs.getBars(analysis_group)
bins = 0
for al in allABs_list:
    # no name: skip
    if al.name=="":
        continue
    # special case subtitle: reserve two slots
    elif al.label==None:
        bins += 2
    # standard case: reserve one slot
    else:
        bins += 1
# reserve two slots for header
nsupp = 2
bins += nsupp
# minimum and maximum of y-axis
ymin = 0
ymax = bins

#----------- fill values --------------
index = 0
#
# get TeX title for category
#
name_tex = allABs.categories[analysis_group]["name_tex"]
print (8*"*" , "in the analysis group : " , name_tex , 8*"*") # e.g. Stop&Sbottom
#
# for option to indicate section ranges
#
sectionDecays = { }
sectionFrom = 0
sectionTo = 0
sectionDecay = None

index = 0
xmax = 0.

bar_positions = [ ]   # y-position of the bar (= index)
bar_vlows = [ ]       # lower limits
bar_vhighs = [ ]      # upper limits
bar_vdiffs = [ ]      # difference between upper and lower
bar_labels = [ ]      # bar labels

# print "Length",bins,ymax,len(allABs_list)
#
# loop over slots (starting from bottom)
#
for al in allABs_list[::-1]:
    # no name: skip
    if al.name=="":
        continue
    # special case subtitle: two slots without values
    elif al.label==None:
        bar_positions.append(index+1)
        bar_vlows.append(0.)
        bar_vhighs.append(0.)
        bar_labels.append("")
        bar_positions.append(index+2)
        bar_vlows.append(0.)
        bar_vhighs.append(0.)
        bar_labels.append("")
        index += 2
        continue

    # standard case
    if verbose:
        print ("Setting bin contents for bin",index+1,"to",al.upLim,al.decay)
    # set position
    bar_positions.append(index+1)
    # set lower limit (or 0 if none)
    if al.lowLim==None:
        bar_vlows.append(0.)
    else:
        bar_vlows.append(al.lowLim)
    # set upper limit
    bar_vhighs.append(al.upLim)
    # set label (in mathmode and bold)
    bar_labels.append(r"$\mathbf{"+al.decay+"}$")
    # keep trace of maximum limit
    if al.upLim>xmax:  xmax = al.upLim
    #
    # for section ranges
    #
#    prodLabels = al.decay[:].replace("#splitline{","").split(",")
#    if len(prodLabels)>1:
#        if prodLabels[0]!=sectionDecay:
#            if sectionDecay!=None:
#                assert not sectionDecay in sectionDecays
#                sectionDecays[sectionDecay] = (sectionFrom,index)
#            sectionDecay = prodLabels[0]
#            sectionFrom = index

    index += 1


#print "After filling",bins,ymax,len(bar_positions),len(bar_vhighs),len(bar_labels)
#
# fill unused positions (header) at the top with 0's
#
for i in range(len(bar_positions),bins):
    bar_positions.append(i)
    bar_vlows.append(0.)
    bar_vhighs.append(0.)
    bar_labels.append("")
#
# bars are stacked: subtract lower limits
#
for i in range(bins):
    bar_vdiffs.append(bar_vhighs[i]-bar_vlows[i])
#
# for bars with identical labels: show only first one
#
currbl = ""
for ibl in range(len(bar_labels))[::-1]:
    if bar_labels[ibl]==currbl:
        bar_labels[ibl] = ""
    else:
        currbl = bar_labels[ibl]
#print "After filling",bins,ymax,len(bar_positions),len(bar_vdiffs),len(bar_labels)


#
# define canvas size and margins
#
cnvSizeX = 10.
cnvMarginLeft = 3.
cnvMarginRight = 0.1
cnvMarginTop = 0.4
cnvMarginBottom = 1.
cnvSizeY = ymax*bar_height+cnvMarginTop+cnvMarginBottom
#
# customize canvas settings / analysis group
#
if (analysis_group == 'EWK'):
    cnvSizeX = 13.5
    cnvMarginLeft = 3.8
    xmax = 1210/1.05
#    pass
elif (analysis_group == 'Squark'):
    cnvSizeX = 13.5
elif (analysis_group == 'Gluino'):
#    xmax = 2500.
    pass
elif (analysis_group == 'GMSB'):
    cnvSizeX = 11.5
    cnvMarginLeft = 4.1
#    pass
#
# setup matplotlib
#
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
#plt.rcParams['text.latex.preamble'] = [r'\boldmath']
# create figure
fig, ax1 = plt.subplots(figsize=(cnvSizeX,cnvSizeY),frameon=True)
#print len(bar_positions),len(bar_vlows),len(bar_labels)
# define stacked bars (lower and upper limit)
barsLow = ax1.barh(bar_positions,bar_vlows,align='center',height=0.75,color='white',
                tick_label=bar_labels)
barsHigh = ax1.barh(bar_positions,bar_vdiffs,align='center',height=0.75,color=bar_color,
                left=bar_vlows,tick_label=bar_labels)
assert len(ax1.get_yticklabels())==len(barsHigh)
# set size of labels (85% of absolute bar height(inch) * relative height * 72 points/inch)
for i in range(len(barsHigh)):
    ax1.get_yticklabels()[i].set_size(0.85*bar_height*barsHigh[i].get_height()*72)
    ax1.get_yticklabels()[i].set_color(yaxis_label_color)
# adjust plot size
fig.subplots_adjust(left=cnvMarginLeft/cnvSizeX, right=1.-cnvMarginRight/cnvSizeX, \
                    top=1.-cnvMarginTop/cnvSizeY, bottom=cnvMarginBottom/cnvSizeY)
# fig.canvas.set_window_title(analysis_group)
# set x-axis label (size: see bar labels)
xlabel = ax1.set_xlabel(r"\textbf{mass scale [GeV]}",size=0.85*bar_height*barsHigh[i].get_height()*72)
# set size of x-axis values (75% of absolute bar height(inch) * relative height * 72 points/inch)
for tl in ax1.get_xticklabels():
    tl.set_size(0.75*bar_height*barsHigh[i].get_height()*72)
# x-axis tick marks inside the plot; no y-axis tick marks
plt.tick_params(axis='x',direction='in')
ax1.tick_params(axis='y',length=0.)
# leave 5% space on x-axis
ax1.set_xlim([0.,1.05*xmax])
ax1.set_ylim([0.,ymax])
# grid?
if args.grid:
    ax1.xaxis.grid(True, linestyle='--', color='grey', alpha=.25)


#if sectionDecay!=None:
#    sectionDecays[sectionDecay] = (sectionFrom,len(allABs_list))
#if verbose:
#    print sectionDecays


#i = 0

#
# add text to the bars. Start from bottom.
#
index = 0
bar_texts = [ ]
for al in allABs_list[::-1]:
    # no name: skip
    if al.name=="":
        continue
    # special case subtitle
    elif al.label==None:
#        print "Found label",al.category,al.name,al.label
        # height of bar
        height = barsHigh[index].get_height()
        # 1% from right border; centered with bar in y
        xloc = 0.01*xmax
        yloc = barsHigh[index].get_y() + barsHigh[index].get_height()/2.
        align = 'left'
        # add text (left-aligned), bold needs to be handled in tex, size = 90% of bar height in points
        bar_text = ax1.text(xloc, yloc, '$\mathbf{'+al.name+'}$', horizontalalignment='left', \
                            verticalalignment='center', color=section_text_color, weight='bold', \
                            clip_on=True, size=0.90*bar_height*0.90*72)
        bar_texts.append(bar_text)
        # advance by two slots
        index += 2
#!#        pas_place += 2*tex_width
        
    # standard case: analysis description, reference(s), comments
    else:
#        print "Found label",al.category,al.name,al.labels
        Pas_Label = '' 
        Pas = ''
        pasArxiv = False
        pasSep = ";"
        # use CADI or arXiv numbers
        if args.cadi:
            refs = al.labels
        else:
            refs = al.arxivs
        # build list of numbers
        for alArxiv in refs:
            # from 2nd one onwards: insert separator
            if len(Pas)>0:
                Pas += pasSep
                pasSep = ','
            # for arXiv numbers
            if alArxiv.startswith("arXiv:"):
                # if first arXiv number in sequence, keep prefix, otherwise remove
                if pasArxiv:
                    Pas += alArxiv.replace("arXiv:","")
                else:
                    Pas += alArxiv
                pasArxiv = True
            # for CADI numbers
            else:
                Pas += alArxiv
                pasArxiv = False
                # force preliminary label
                preliminaryLabel = " (preliminary)"
                
        Pas_Label = Pas


        if verbose:
            print ('This is the pas label', Pas_Label, ' ################## ' ,al.label)


        #
        # special treatment / category?
        #
        if analysis_group == 'EWK':
            pass

        elif analysis_group == 'Squark':
            pass

        elif analysis_group == 'Gluino':
            pass

        elif analysis_group == 'GMSB':
            pass


#!#        Pas_Place = float(pas_place)
#        height = barsHigh[index].get_height()
        #
        # analysis description and references
        #
        # 1% from right border; centered with bar in y
        xloc = 0.01*xmax + bar_vlows[index]
        yloc = barsHigh[index].get_y() + barsHigh[index].get_height()/2.
        # bad hack to compensate for shifted text in case of subscript
        if ( '$' in al.desc ) and ( '_' in al.desc ):
            yloc -= 0.1*barsHigh[index].get_height()
        align = 'left'
#            bar_text1.draw(fig.canvas.get_renderer())
#            ex = bar_text1.get_window_extent()
#            print ex,xloc,yloc
#            exTrans = ax1.transData.inverted().transform([ex.x0,ex.y0,ex.x1,ex.y1])
        # add text (analysis description in bold, the list of references): 90% of bar label size
#        bar_text = ax1.text(xloc, yloc, r"\textbf{"+al.desc+":} "+Pas_Label, horizontalalignment=align, \
        bar_text = ax1.text(xloc, yloc, r"\textbf{"+al.desc+":} "+Pas_Label, horizontalalignment=align, \
                            verticalalignment='center', color=desc_text_color, weight='bold', \
                            clip_on=True, size=0.90*ax1.get_yticklabels()[index].get_size())
        bar_texts.append(bar_text)
#            print barsHigh[index]
#            print ax1.get_yticklabels()[index].get_size(),bar_height*72

        #
        # comments on limit
        #
        comment = ""
        # general comment
        if al.comment!=None: 
            comment += al.comment
        # x-value
        if al.xValue!=None:
            if comment!="":
                comment += r"\textbf{, }"
            comment += r"$x="+str(al.xValue)+"$"
        # write comment
        if comment!="":
            # draw previous text in order to get size of the text box
            bar_text.draw(fig.canvas.get_renderer())
            ex = bar_text.get_window_extent()
            # transform box corners from dots to plot coordinates
            exTrans = ax1.transData.inverted().transform([ex.x0,ex.y0,ex.x1,ex.y1])
#            if exTrans[2]<0.5*barsHigh[index].get_width() and barsHigh[index].get_width()>0.40*xmax and\
            # add comment inside bar unless
            #   previous text takes >50% of the bar (bug: should be vhighs instead of vdiffs), or
            #   bar takes <40% of plot range, or 
            #   previous text exceeds length of bar, or
            #   analysis line is in list of exceptions
            if exTrans[2]<0.5*bar_vdiffs[index] and bar_vhighs[index]>0.40*xmax and \
                    not ( al.name in commentOutsideBarLabels ) and not exTrans[2]>bar_vhighs[index]:
                align = 'right'
                dxloc = -0.01*xmax
#                comment_color = 'white'
                comment_color = comm_text_color
            else:
                align = 'left'
                dxloc = 0.01*xmax
                if exTrans[2]>bar_vhighs[index]:
                    dxloc += ( exTrans[2] - bar_vhighs[index] )
                comment_color = comm_text_color
            dyloc = 0
            if ( '$' in comment ) and ( '_' in comment ):
                dyloc = - 0.15*barsHigh[index].get_height()
            bar_comment = ax1.text(bar_vhighs[index]+dxloc, yloc+dyloc, comment, \
                                   horizontalalignment=align, \
                                   verticalalignment='center', \
                                   color=comment_color, weight='bold', \
                                   clip_on=True, size=ax1.get_yticklabels()[index].get_size()*0.70)
            bar_texts.append(bar_comment)


        index += 1

#    if 'line' in interp:
##          print "empty from " , name_tex
##           exec('line_'+str(i)+' = ROOT.TLine(-320,(i*line_depence)+0.3,histo_xaxis_max,(i*line_depence)+0.5#)')#
#
#          exec('line_'+str(i)+' = ROOT.TLine(-320,(i*line_depence)+0.3,2100,(i*line_depence)+0.3)')
#          exec('line_'+str(i)+'.SetLineColor(line_color)')
#          exec('line_'+str(i)+'.SetLineStyle(7)')
#          exec('line_'+str(i)+'.Draw()')
#!#        pas_place += tex_width


#print barsHigh[index].get_y() - barsHigh[0].get_height()/2.,xmax
#print ax1.transData.transform([(0., 0.),(xmax,0.),(0,ymax),(xmax,ymax)])
#print ax1.get_xlim(),ax1.get_ylim()
#for i in range(len(barsHigh)):
#    print i,barsHigh[i].get_y(),barsHigh[i].get_width()
#ax1.plot([0.,xmax,0.,xmax],[0.,0.,ymax,ymax],markersize=5,color='green',marker='o')


##secLine = ROOT.TLine()
##secLine.SetLineColor(2)
##print cX1,cY1,cX2,cY2
##print tex_width
##sx = cX1+0.02*(cX2-cX1)
#for sd in sectionDecays:
#    sFrom,sTo = sectionDecays[sd]
#    yFrom = tex_width*sFrom
#    yTo = tex_width*sTo
##    secLine.DrawLine(sx,yFrom,sx,yTo)
##    sx += 0.01*(cX2-cX1)
##    print sFrom,sTo
##    print cX1+0.02*(cX2-cX1),yFrom,cX1+0.02*(cX2-cX1),yTo
#    latex_sec1.SetTextAlign(23)
#    latex_sec1.DrawLatex(cX1+0.002*(cX2-cX1),(yFrom+yTo)/2.,sd)
    
#------------CMS Headers ------------------------#

thdr1 = "Overview of SUSY results: "
if analysis_group=="Gluino":
    thdr1 += "gluino pair production"
elif analysis_group=="Squark":
    thdr1 += "squark pair production"
elif analysis_group=="EWK":
    thdr1 += "electroweak production"
elif analysis_group=="GMSB":
    thdr1 += "GMSB / GGM"
hdr3 = ax1.text(0.01*xmax,ymax-0.01*(ymax-ymin), \
                r"\textbf{"+thdr1+"}", \
                horizontalalignment='left',verticalalignment='top',color=title_color,weight='bold',
                size=bar_height*0.90*72)
hdr2 = ax1.text(xmax,ymax+0.01*(ymax-ymin), \
                "Moriond 2019", \
                horizontalalignment='right',verticalalignment='bottom',color='black',weight='bold',
                size=bar_height*0.90*72)
hdr1 = ax1.text(0.01*xmax,ymax+0.01*(ymax-ymin), \
                r"\textbf{CMS"+preliminaryLabel+"}", \
                horizontalalignment='left',verticalalignment='bottom',color='black',weight='bold',
                size=bar_height*0.90*72)
exTrans = ax1.transData.transform([(0.01*xmax,ymax-0.01*(ymax-ymin))])
#print exTrans,[(0.01*xmax,ymax-0.01*(ymax-ymin))],hdr3.get_size()/72.
exTransI = ax1.transData.inverted().transform([(exTrans[0][0],exTrans[0][1]-hdr3.get_size()/72.*fig.get_dpi())])
#print exTransI
hdr4 = ax1.text(0.03*xmax,exTransI[0][1], \
                r"36 $\mathrm{fb}^{-1}$ (13 TeV)", \
                horizontalalignment='left',verticalalignment='top',color='black',weight='bold',
                size=0.8*hdr3.get_size())
bar_texts.append(hdr1)
bar_texts.append(hdr2)
bar_texts.append(hdr3)
bar_texts.append(hdr4)
#print ax1.get_yticklabels()[0],ax1.get_yticklabels()[-1]



#-------------Foot note--------------------------#
exTrans = ax1.transData.transform([(0.01*xmax,ymin)])
#print exTrans,[(0.01*xmax,ymax-0.01*(ymax-ymin))],hdr3.get_size()/72.
#exTransI = ax1.transData.inverted().transform([(0.,3*ax1.get_yticklabels()[0].get_size()*0.70/72.*fig.get_dpi())])
exTransI = ax1.transData.inverted().transform([(0.03*cnvSizeX*fig.get_dpi(),
                                                3.5*ax1.get_yticklabels()[0].get_size()*0.70/72.*fig.get_dpi())])
#print exTransI
#caption = ax1.text(0.01*xmax,exTransI[0][1], \
caption = ax1.text(exTransI[0][0],exTransI[0][1], \
                r"Selection of observed limits at 95\% C.L. (theory uncertainties are not included). "+ \
                r"Probe \textbf{up to} the quoted mass limit for light LSPs unless stated otherwise. "+"\n"+ \
                r"The quantities $\Delta M$ and $x$ represent the absolute mass difference "+ \
                r"between the primary sparticle and the LSP, and the difference between the intermediate "+"\n"+ \
                r"sparticle and the LSP relative to $\Delta M$, respectively, unless indicated otherwise.", \
                horizontalalignment='left',verticalalignment='top',color='black',weight='bold',
                size=ax1.get_yticklabels()[0].get_size()*0.70)
bar_texts.append(caption)
if args.output!=None:
    fname = args.output
else:
    fname = path+filename+"_"+analysis_group+".pdf"
plt.savefig(fname=fname,format="pdf")
if not args.batch:
    plt.show()
sys.exit(0)


#------------put save directories----------------#

#if not os.path.exists(path):
#    os.makedirs(path)


