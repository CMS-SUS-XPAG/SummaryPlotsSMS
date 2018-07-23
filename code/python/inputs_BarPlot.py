#
# List of analyses, labels, comments for summary bar plot
#
from AnalysisBar import *        

#
# list of names corresponding to different SMS
#
pp = r'pp \rightarrow'

N1            = r"\tilde{\chi}^{0}_{1}"
N2            = r"\tilde{\chi}^{0}_{2}"
C1            = r"\tilde{\chi}^{\pm}_{1}"
CNi           = r"\tilde{\chi}^{0,\pm}_{i}"
CNj           = r"\tilde{\chi}^{0,\pm}_{j}"
Wpm           = r"W^{\pm}"
Wpmstar       = r"W^{\pm*}"
Wstar       = r"W^{*}"
Zstar       = r"Z^{*}"

T2bb 	 	  = r'\tilde{b} \rightarrow b  '+N1
T2tt		  = r'\tilde{t} \rightarrow t  '+N1
T2tb		  = r'\tilde{t} \rightarrow (t  '+N1+'/ b '+C1+r'\rightarrow b '+'W'+N1+')'
T2cc		  = r'\tilde{t} \rightarrow c  '+N1
T6bbHH        = r'\tilde{b} \rightarrow b  '+N2+r'\rightarrow b H\tilde{\chi}_{1}^0'

T6bbWW 		  = r'\tilde{t}\rightarrow b '+C1+r' \rightarrow b W^{\pm} '+N1
T2bW3bdy  	  = r'\tilde{t}\rightarrow b '+C1+r' \rightarrow b f \bar{f}^\prime '+N1
T8bbllnunu    = r'\tilde{t}\rightarrow b '+C1+r' \rightarrow b \nu \tilde{\ell} \rightarrow b \nu \ell '+N1 
T6ttWW 		  = r'\tilde{b}\rightarrow t '+C1+r' \rightarrow t W^{\pm} '+N1
T8bllbZ       = r'\tilde{b}\rightarrow b '+N2+r' \rightarrow ( b \ell \tilde{\ell} \rightarrow b \ell \ell '+N1+ \
    ') / ( b Z '+N1+')'

T6ttHH        = r'\tilde{t}_{2} \rightarrow H \tilde{t}_{1} \rightarrow H t '+N1
T6ttZZ        = r'\tilde{t}_{2} \rightarrow Z \tilde{t}_{1} \rightarrow Z t '+N1
T6ttHZ        = r'\tilde{t}_{2} \rightarrow Z/H \tilde{t}_{1} \rightarrow Z/H t '+N1

T2llLR 		  = pp+r'\tilde{\ell}_{L/R}\tilde{\ell}_{L/R}, \tilde{\ell} \rightarrow \ell '+N1
T2llL 		  = pp+r'\tilde{\ell}_{L}\tilde{\ell}_{L}, \tilde{\ell} \rightarrow \ell '+N1
T2llR 		  = pp+r'\tilde{\ell}_{R}\tilde{\ell}_{R}, \tilde{\ell} \rightarrow \ell '+N1
T2eeLR 		  = pp+r'\tilde{e}_{L/R}\tilde{e}_{L/R}, \tilde{e} \rightarrow e '+N1
T2eeL 		  = pp+r'\tilde{e}_{L}\tilde{e}_{L}, \tilde{e} \rightarrow e '+N1
T2eeR 		  = pp+r'\tilde{e}_{R}\tilde{e}_{R}, \tilde{e} \rightarrow e '+N1
T2mumuLR 	  = pp+r'\tilde{\mu}_{L/R}\tilde{\mu}_{L/R}, \tilde{\mu} \rightarrow \mu '+N1
T2mumuL 	  = pp+r'\tilde{\mu}_{L}\tilde{\mu}_{L}, \tilde{\mu} \rightarrow \mu '+N1
T2mumuR 	  = pp+r'\tilde{\mu}_{R}\tilde{\mu}_{R}, \tilde{\mu} \rightarrow \mu '+N1
T2tautau 	  = pp+r'\tilde{\tau}\tilde{\tau}, \tilde{\tau} \rightarrow \tau '+N1

TChiChipmSlepL    = pp+' '+N2+' '+C1+r' \rightarrow \ell \tilde{\nu} \ell \tilde{\ell}' + \
    r' \rightarrow \ell \nu \ell \ell'+N1+' '+N1
TChiChipmSlepStau    = pp+' '+N2+' '+C1+r' \rightarrow \tilde{\tau} \nu \ell \tilde{\ell}' + \
    r' \rightarrow \tau \nu \ell \ell'+N1+' '+N1
TChiChipmStauStau = pp+' '+N2+' '+C1+r' \rightarrow \tilde{\tau} \nu \tau \tilde{\tau}' + \
    r' \rightarrow \tau\nu\tau\tau '+N1+' '+N1
TChipmChipmStauStau = pp+' '+C1+' '+C1+', '+C1+r' \rightarrow ( \tilde{\tau} \nu / \tau \tilde{\nu} )' + \
    r' \rightarrow \tau\nu'+N1
TChipmChipmSlepSnu = pp+' '+C1+' '+C1+', '+C1+r' \rightarrow ( \tilde{\ell} \nu / \ell \tilde{\nu} )' + \
    r' \rightarrow \ell\nu'+N1
TChiWZ 		  = pp+' '+N2+''+C1+r' \rightarrow W Z '+N1+' '+N1
TChiWH 		  = pp+' '+N2+''+C1+r' \rightarrow W H '+N1+' '+N1
TChiWZH		  = pp+' '+N2+''+C1+r' \rightarrow W Z/H '+N1+' '+N1
TChiWW 		  = pp+' '+C1+''+C1+', '+C1+r' \rightarrow W '+N1

THiggsino     = pp+' '+N2+C1+'/'+N1+C1+','+C1+'/'+N2+r'\rightarrow ('+Wstar+'/'+Zstar+')'+N1

T1qqqq     = r'\tilde{g} \rightarrow q q '+N1
T2qq     = r'\tilde{q} \rightarrow q '+N1
T1tttt = r'\tilde{g} \rightarrow t t '+N1
T1bbbb = r'\tilde{g} \rightarrow b b '+N1
T1tbtb = r'\tilde{g} \rightarrow  t b ' + C1 + r'\rightarrow t b f f^{\prime} ' + N1
T1ttbbbt = r'\tilde{g} \rightarrow ( t t ' + N1 + ' / b b ' + N1 + ' / t b ' + C1 + \
    r'\rightarrow t b f f^{\prime} ' + N1 + ')'

T5VV   = r'\tilde{g} \rightarrow q q ('+C1+'/'+N2+r') \rightarrow qq (W/Z) '+N1
T5WW   = r'\tilde{g} \rightarrow q q '+C1+r' \rightarrow q q W '+N1
T5HH   = r'\tilde{g} \rightarrow q q '+N2+r' \rightarrow q q H '+N1
T5HZ   = r'\tilde{g} \rightarrow q q '+N2+r' \rightarrow q q H/Z '+N1


T5tctc = r'\tilde{g} \rightarrow t \tilde{t} \rightarrow t c '+N1
T5tttt = r'\tilde{g} \rightarrow t \tilde{t} \rightarrow t t '+N1

T2bbWWoff = r'\tilde{t} \rightarrow b f  \bar{f}^\prime '+N1

T5ZZGMSB = r'\tilde{g} \rightarrow qq'+N1+', '+N1+r' \rightarrow Z \tilde{G}'

T5gg 	 	  = r'\tilde{g} \rightarrow q q '+N1+r' \rightarrow q q \gamma \tilde{G}'
T5Wg 	 	  = r'\tilde{g} \rightarrow (q q '+N1+r' \rightarrow q q \gamma \tilde{G} / q q '+C1+ \
    r' \rightarrow q q W \tilde{G})'
T6gg 	 	  = r'\tilde{q} \rightarrow q '+N1+r' \rightarrow q \gamma \tilde{G}'
T6Wg 	 	  = r'\tilde{q} \rightarrow (q '+N1+r' \rightarrow q \gamma \tilde{G} / q '+C1+ \
    r' \rightarrow q W \tilde{G})'

#TChiHHGG      = pp+N1+N1+', '+N1+r' \rightarrow h \tilde{G}' 
TChiHHGG      = pp+CNi+CNj+r' \rightarrow h h \tilde{G} \tilde{G} + X_{\mathrm{soft}}' 
#TChiZHGG      = pp+N1+N1+', '+N1+r' \rightarrow h/Z \tilde{G}' 
TChiZHGG      = pp+CNi+CNj+r' \rightarrow (h/Z) (h/Z) \tilde{G} \tilde{G} + X_{\mathrm{soft}}' 
TChiZZGG      = pp+CNi+CNj+r' \rightarrow Z Z \tilde{G} \tilde{G} + X_{\mathrm{soft}}' 

TChiWgGG      = pp+N1+C1+', '+N1+r' \rightarrow \gamma \tilde{G}'+', '+C1+r' \rightarrow W \tilde{G}'
#TChiNgGG      = pp+'('+N1+' '+C1+','+C1+' '+C1+'), '+N1+r' \rightarrow \gamma \tilde{G}'+', '+C1+ \
#  r' \rightarrow W \tilde{G}'
#TChiNgGG      = pp+N1+' '+C1+','+C1+' '+C1+ \
#  r'  \rightarrow ( Z / h / \gamma )  ( Z / h /\gamma ) \tilde{G} \tilde{G} X_\mathrm{soft}'
TChiNgGG      = pp+N1+' '+C1+','+C1+' '+C1+r'  \rightarrow 2 \times [( Z / h /\gamma ) \tilde{G}] + X_\mathrm{soft}'

#
# list of strings for comments
#
squarks = r'$\tilde{q}_{R}+\tilde{q}_{L}(\tilde{u},\tilde{d},\tilde{c},\tilde{s})$'  
squark = r'one light squark ($\tilde{u}$, $\tilde{d}$, $\tilde{c}$, or $\tilde{s}$)'


Max = r'(max. exclusion)'
Max80 = r'$\Delta M < 80$ GeV (max. exclusion)'
#Higgsinos = 'almost mass-degenerate $'+C1+'$,$'+N2+'$,$'+N1+'$'
#HiggsinosZH = 'almost mass-degenerate $'+C1+'$,$'+N2+'$,$'+N1+'$, BF(h/Z)=50\%'
#Higgsinos = 'almost mass-degenerate $'+C1+'$,$'+N2+'$,$'+N1+'$'
HiggsinosZH = 'BF = 50\%'


D_SUS_16_030 = r'$\Delta M = 20$ GeV'
T1tbtb_Comm = r'$\Delta M_{'+C1+'} = 5$ GeV, $M_{'+N1+'} = 200$ GeV'
T1tbtb_5_Comm = r'$\Delta M_{'+C1+'} = 5$ GeV'
T1ttbbbt_Comm = r'$\Delta M_{'+C1+'} = 5$ GeV, BF(tt:bb:tb) = 1:1:2'
T5tctc_Comm = r'$\Delta M_{\tilde{t}} = 20$ GeV'
T5tttt_Comm = r'$\Delta M_{\tilde{t}} = M_{t}$, $M_{'+N1+'} = 400$ GeV'
T8bllbZ_Comm = r'max. exclusion, $M_{'+N1+r'}=100$ GeV, $x_{\tilde{\ell}}=0.5$, BF = 50\%'
D_I_20 = r'$\Delta M_\mathrm{'+C1+'} = 20$ GeV'
M2_20 = '$M_\mathrm{LSP} = 20$ GeV'
M200_STOP1 = r'$\Delta M_{\tilde{t}_{1}} = M_{t}$, $M_{\tilde{t}_{1}} = 200$ GeV'
M200_STOP1_ZH = r'$\Delta M_{\tilde{t}_{1}} = M_{t}$, BF = 50\%, $M_{\tilde{t}_{1}} = 200$ GeV'
T2tb_5_Comm = r'$\Delta M_{'+C1+'} = 5$ GeV, BF=50\%'
T5VV_Comm = r'BF($'+C1+'$:$'+N2+'$) = 2:1'
T6ttWW_Comm = r'$M_{'+N1+'}=50$ GeV'
T6bbHH_Comm = r'$\Delta M_{'+N2+'}=130$ GeV'
TChiChipmSlepL_Comm = 'flavour democratic'
TChiChipmSlepStau_Comm = r'$\tau$ enriched'
TChiChipmStauStau_Comm = r'$\tau$ dominated'
TChiNgGG_Comm = r'BF(Z:H:$\gamma$) = 1:1:2'
T5xg_Comm = r'$\Delta M(\tilde{g},'+N1+') = 10$ GeV'

#
# CADI / arxiv numbers
#
cadiToArxiv = { }
cadiToArxiv["SUS-16-032"] = "1707.07274"
cadiToArxiv["SUS-16-033"] = "1704.07781"
cadiToArxiv["SUS-16-034"] = "1709.08908"
cadiToArxiv["SUS-16-035"] = "1704.07323"
cadiToArxiv["SUS-16-036"] = "1705.04650"
cadiToArxiv["SUS-16-037"] = "1705.04673"
cadiToArxiv["SUS-16-038"] = "1802.02110"
cadiToArxiv["SUS-16-039"] = "1709.05406"
cadiToArxiv["SUS-16-040"] = "1712.08920"
cadiToArxiv["SUS-16-041"] = "1710.09154"
cadiToArxiv["SUS-16-042"] = "1709.09814"
cadiToArxiv["SUS-16-043"] = "arXiv:1706.09933"
cadiToArxiv["SUS-16-044"] = "1709.04896"
cadiToArxiv["SUS-16-045"] = "1709.00384"
cadiToArxiv["SUS-16-046"] = "1711.08008"
cadiToArxiv["SUS-16-047"] = "1707.06193"
cadiToArxiv["SUS-16-048"] = "1801.01846"
cadiToArxiv["SUS-16-049"] = "1707.03316"
cadiToArxiv["SUS-16-050"] = "1710.11188"
cadiToArxiv["SUS-16-051"] = "1706.04402"
cadiToArxiv["SUS-17-001"] = "1711.00752"
cadiToArxiv["SUS-17-002"] = None
cadiToArxiv["SUS-17-003"] = "1807.02048"
cadiToArxiv["SUS-17-004"] = "1801.03957"
cadiToArxiv["SUS-17-005"] = "1805.05784"
cadiToArxiv["SUS-17-006"] = "1712.08501"
cadiToArxiv["SUS-17-009"] = "1806.05264"
cadiToArxiv["SUS-17-010"] = "1807.07799"
cadiToArxiv["SUS-17-012"] = None


#
# define all bars to appear in the plot (in groups, and in the sequence as below)
#
allABs = AnalysisBars()

# Gluino production
allABs.add('Gluino',r'pp \rightarrow \tilde{g}\tilde{g}')

allABs.add('Gluino','16-050-T1tttt',desc=r'$\mathbf{0\ell}$',label='SUS-16-050,SUS-16-033,SUS-16-036,SUS-16-038', \
               upLim=2035,decay=T1tttt)
allABs.add('Gluino','16-037-T1tttt',desc=r'$\mathbf{1\ell}$',label='SUS-16-037,SUS-16-042',upLim=1893,decay=T1tttt)
allABs.add('Gluino','16-035-T1tttt',desc=r'$\mathbf{2\ell}$ same-sign',label='SUS-16-035',upLim=1521,decay=T1tttt)
allABs.add('Gluino','16-041-T1tttt',desc=r'$\mathbf{\geq 3\ell}$',label='SUS-16-041',upLim=1625,decay=T1tttt)

allABs.add('Gluino','16-050-T5tttt',desc=r'$\mathbf{0\ell}$',label='SUS-16-050',upLim=2000,decay=T5tttt, \
               comment=T5tttt_Comm)
allABs.add('Gluino','16-037-T5tttt',desc=r'$\mathbf{1\ell}$',label='SUS-16-037',upLim=1900,decay=T5tttt, \
               comment=T5tttt_Comm)
allABs.add('Gluino','16-035-T5tttt',desc=r'$\mathbf{2\ell}$ same-sign',label='SUS-16-035',upLim=1416,decay=T5tttt, \
               comment=T5tttt_Comm)

allABs.add('Gluino','16-050-T5tctc',desc=r'$\mathbf{0\ell}$',label='SUS-16-050',upLim=1690,decay=T5tctc, \
               comment=T5tctc_Comm)
allABs.add('Gluino','16-035-T5tctc',desc=r'$\mathbf{2\ell}$ same-sign',label='SUS-16-035',upLim=1188,decay=T5tctc, \
               comment=T5tctc_Comm)
allABs.add('Gluino','16-050-T1tbtb',desc=r'$\mathbf{0\ell}$',label='SUS-16-033',upLim=1849,decay=T1tbtb, \
               comment=T1tbtb_Comm)
allABs.add('Gluino','16-035-T1btbt',desc=r'$\mathbf{2\ell}$ same-sign',label='SUS-16-035',upLim=1400,decay=T1tbtb, \
               comment=T1tbtb_5_Comm)
allABs.add('Gluino','16-050-T1ttbbbt',desc=r'$\mathbf{0\ell}$',label='SUS-16-050',upLim=1950,decay=T1ttbbbt, \
               comment=T1ttbbbt_Comm)
allABs.add('Gluino','16-036-T1bbbb',desc=r'$\mathbf{0\ell}$',label='SUS-16-036,SUS-16-033,SUS-16-038', \
               upLim=2028,decay=T1bbbb) #d
allABs.add('Gluino','16-036-T1qqqq',desc=r'$\mathbf{0\ell}$',label='SUS-16-036,SUS-16-033,SUS-16-038', \
               upLim=1861,decay=T1qqqq) #d


allABs.add('Gluino','16-033-T5VV',desc=r'$\mathbf{0\ell}$',label='SUS-16-033',upLim=1807,decay=T5VV, \
               comment=T5VV_Comm,xValue=0.5)
allABs.add('Gluino','16-041-T5VV',desc=r'$\mathbf{\geq 3\ell}$',label='SUS-16-041',upLim=1166,decay=T5VV, \
               comment=T5VV_Comm,xValue=0.5)
allABs.add('Gluino','16-042-T5WW',desc=r'$\mathbf{1\ell}$',label='SUS-16-042' ,upLim=1908,decay=T5WW,xValue=0.5)
allABs.add('Gluino','16-020-16-035-T5WW',desc=r'$\mathbf{2\ell}$ same-sign',label='SUS-16-035',upLim=1283, \
               decay=T5WW,xValue=0.5)
allABs.add('Gluino','16-020-16-035-T5WWDelta20',desc=r'$\mathbf{2\ell}$ same-sign',label='SUS-16-035', \
               upLim=1425,decay=T5WW,comment=D_I_20)
allABs.add('Gluino','17-006-T5HH',desc=r'$\mathbf{0\ell}$',label='SUS-17-006',upLim=2010,decay=T5HH)
allABs.add('Gluino','17-006-T5HZ',desc=r'$\mathbf{0\ell}$',label='SUS-17-006',upLim=1825,decay=T5HZ,comment='BF = 50\%')



'''
Stop
'''
allABs.add('Squark',r'pp \rightarrow \tilde{t}\tilde{t}')
allABs.add('Squark','16-036-T2tt',desc=r'$\mathbf{0\ell}$', \
               label='SUS-16-036,SUS-16-033,SUS-16-038,SUS-16-049,SUS-16-050',upLim=1066,decay=T2tt)
allABs.add('Squark','16-051-T2tt',desc=r'$\mathbf{1\ell}$',label='SUS-16-051',upLim=1114 ,decay=T2tt)
allABs.add('Squark','17-001-T2tt',desc=r'$\mathbf{2\ell}$ opposite-sign',label='SUS-17-001', \
               upLim=812,lowLim=247,decay=T2tt)
allABs.add('Squark','17-010-T2tt',desc=r'$\mathbf{2\ell}$ opposite-sign',label='SUS-17-010',upLim=690,decay=T2tt)
#allABs.add('Squark','17-001-T2tt',desc=r'$\mathbf{0,1,2\ell}$ combined',label='SUS-17-001,SUS-16-049,SUS-16-051' , \
#  upLim=,lowLim=,decay=T2tt)

allABs.add('Squark','16-036-T6bbWW',desc=r'$\mathbf{0\ell}$',label='SUS-16-036,SUS-16-049', \
upLim=904,decay=T6bbWW,xValue=0.5)
allABs.add('Squark','16-051-T6bbWW',desc=r'$\mathbf{1\ell}$',label='SUS-16-051', \
upLim=998,lowLim=272,decay=T6bbWW,xValue=0.5)
allABs.add('Squark','17-001-T6bbWW',desc=r'$\mathbf{2\ell}$ opposite-sign',label='SUS-17-001', \
upLim=738,lowLim=269,decay=T6bbWW,xValue=0.5)
allABs.add('Squark','17-010-T6bbWW',desc=r'$\mathbf{2\ell}$ opposite-sign',label='SUS-17-010', \
upLim=610,lowLim=250,decay=T6bbWW,xValue=0.5)

allABs.add('Squark','16-036-T2tb',desc=r'$\mathbf{0\ell}$',label='SUS-16-036,SUS-16-049',upLim=950,decay=T2tb, \
               comment=T2tb_5_Comm)
allABs.add('Squark','16-051-T2tb',desc=r'$\mathbf{1\ell}$',label='SUS-16-051',upLim=975 ,decay=T2tb)

allABs.add('Squark','16-049-T2bbWWoff',desc=r'$\mathbf{0\ell}$',label='SUS-16-049',upLim=584,decay=T2bbWWoff, \
               comment=Max80)
allABs.add('Squark','17-005-T2bbWWoff',desc=r'$\mathbf{1\ell}$ soft',label='SUS-17-005',upLim=560,decay=T2bbWWoff, \
               comment=Max80)
#allABs.add('Squark','16-035-T2bbWWoff',desc=r'$\mathbf{2\ell}$ opposite-sign',label='SUS-16-048',upLim=454, \
#  decay=T2bbWWoff,comment=Max)

allABs.add('Squark','16-049-T2bW3bdy',desc=r'$\mathbf{0\ell}$',label='SUS-16-049', \
               upLim=658,decay=T2bW3bdy,xValue=0.5,comment=Max80)
allABs.add('Squark','17-005-T2bW3bdy',desc=r'$\mathbf{1\ell}$ soft',label='SUS-17-005', \
               upLim=540,decay=T2bW3bdy,xValue=0.5,comment=Max80)
allABs.add('Squark','16-048-T2bW3bdy',desc=r'$\mathbf{2\ell}$ opposite-sign',label='SUS-16-048', \
               upLim=455,decay=T2bW3bdy,xValue=0.5,comment=Max80)

allABs.add('Squark','16-036-T2cc',desc=r'$\mathbf{0\ell}$',label='SUS-16-036,SUS-16-032,SUS-16-038,SUS-16-049', \
               upLim=571,decay=T2cc,comment=Max80)

allABs.add('Squark','17-001-T8bbllnunu',desc=r'$\mathbf{2\ell}$',label='SUS-17-001', \
               upLim=1194,decay=T8bbllnunu,xValue=0.5)

allABs.add('Squark','16-041-T6ttHH',desc=r'$\mathbf{\geq 3\ell}$',label='SUS-16-041',upLim=724,decay=T6ttHH, \
               comment=M200_STOP1)
allABs.add('Squark','16-041-T6ttHZ',desc=r'$\mathbf{\geq 3\ell}$',label='SUS-16-041',upLim=708,decay=T6ttHZ, \
               comment=M200_STOP1_ZH)
allABs.add('Squark','16-041-T6ttZZ',desc=r'$\mathbf{\geq 3\ell}$',label='SUS-16-041',upLim=753,decay=T6ttZZ, \
               comment=M200_STOP1)

'''
Sbottom
'''
allABs.add('Squark',r'pp \rightarrow \tilde{b}\tilde{b}')
allABs.add('Squark','16-032-T2bb',desc=r'$\mathbf{0\ell}$',label='SUS-16-032,SUS-16-033,SUS-16-036,SUS-16-038', \
               upLim=1233,decay=T2bb)
allABs.add('Squark','16-045-T6bbHH',desc=r'$\mathbf{h\rightarrow\gamma\gamma}$',label='SUS-16-045', \
               upLim=493,decay=T6bbHH,comment=T6bbHH_Comm)
allABs.add('Squark','16-035-T6ttWW',desc=r'$\mathbf{2\ell}$ same-sign',label='SUS-16-035',upLim=806,decay=T6ttWW, \
               comment=T6ttWW_Comm)
allABs.add('Squark','16-041-T6ttWW',desc=r'$\mathbf{\geq 3\ell}$',label='SUS-16-041', \
               upLim=560,comment=T6ttWW_Comm,decay=T6ttWW)
allABs.add('Squark','16-034-T8bllbZ',desc=r'$\mathbf{2\ell}$ opposite-sign',label='SUS-16-034', \
               upLim=1250,decay=T8bllbZ,comment=T8bllbZ_Comm)

'''
Squark
'''
allABs.add('Squark',r'pp \rightarrow \tilde{q}\tilde{q}')
allABs.add('Squark','16-036-T2qq-squarks',desc=r'$\mathbf{0\ell}$',label='SUS-16-036,SUS-16-033,SUS-16-038', \
               upLim=1544,decay=T2qq,comment=squarks)
allABs.add('Squark','16-036-T2qq-squark',desc=r'$\mathbf{0\ell}$',label='SUS-16-036,SUS-16-033,SUS-16-038', \
               upLim=1049,decay=T2qq,comment=squark)



'''
EWK
'''
allABs.add('EWK',r'pp \rightarrow'+N2+' '+C1)
allABs.add('EWK','16-039-TChiChipmSlepL050',desc=r'$\mathbf{3\ell}$',label='SUS-16-039',upLim=1145, \
               decay=TChiChipmSlepL,xValue=0.5,comment=TChiChipmSlepL_Comm)
allABs.add('EWK','16-039-TChiChipmSlepL005',desc=r'$\mathbf{\geq 3\ell}$ + $\mathbf{2\ell}$ same-sign', \
               label='SUS-16-039',upLim=1122,decay=TChiChipmSlepL,xValue=0.05,comment=TChiChipmSlepL_Comm)
allABs.add('EWK','16-039-TChiChipmSlepL095',desc=r'$\mathbf{\geq 3\ell}$ + $\mathbf{2\ell}$ same-sign', \
               label='SUS-16-039',upLim=1042,decay=TChiChipmSlepL,xValue=0.95,comment=TChiChipmSlepL_Comm)
allABs.add('EWK','16-039-TChiChipmSlepStau005',desc=r'$\mathbf{3\ell/\tau_{h}}$',label='SUS-16-039', \
               upLim=1032,decay=TChiChipmSlepStau,xValue=0.5,comment=TChiChipmSlepStau_Comm)
allABs.add('EWK','16-039-TChiChipmSlepStau050',desc=r'$\mathbf{3\ell/\tau_{h}}$',label='SUS-16-039', \
               upLim=1080,decay=TChiChipmSlepStau,xValue=0.05,comment=TChiChipmSlepStau_Comm)
allABs.add('EWK','16-039-TChiChipmSlepStau095',desc=r'$\mathbf{3\ell/\tau_{h}}$',label='SUS-16-039', \
               upLim=1048,decay=TChiChipmSlepStau,xValue=0.95,comment=TChiChipmSlepStau_Comm)
allABs.add('EWK','16-039-TChiChipmStauStau050',desc=r'$\mathbf{\geq 3\ell/\tau_{h}}$',label='SUS-16-039', \
               upLim=624,decay=TChiChipmStauStau,xValue=0.5,comment=TChiChipmStauStau_Comm)
#allABs.add('EWK','17-002-TChiChipmStauStau050',desc=r'$e\tau_{h},\mu\tau_{h},e\mu$',label='SUS-17-002', \
# upLim=560,decay=TChiChipmStauStau,xValue=0.5)
#allABs.add('EWK','17-002-TChiChipmStauStau005',desc=r'$\mathbf{2\ell}$/$\mathbf{\tau}$',label='SUS-17-002', \
# upLim=480,decay=TChiChipmStauStau,xValue=0.05)
#allABs.add('EWK','17-002-TChiChipmStauStau095',desc=r'$\mathbf{2\ell}$/$\mathbf{\tau}$',label='SUS-17-002', \
# upLim=520,decay=TChiChipmStauStau,xValue=0.95)

allABs.add('EWK','16-039-TChiWH',desc=r'$\mathbf{\geq 3\ell/\tau_{h}}$ + $\mathbf{2\ell}$ same-sign', \
               label='SUS-16-039',upLim=173,decay=TChiWH)
allABs.add('EWK','16-043-TChiWH',desc=r'$\mathbf{1\ell}$+jets',label='SUS-16-043',lowLim=231, \
               upLim=490,decay=TChiWH)
allABs.add('EWK','16-045-TChiWH',desc=r'$\mathbf{h \rightarrow \gamma\gamma}$',label='SUS-16-045', \
               upLim=172,decay=TChiWH)
allABs.add('EWK','17-004-TChiWH',desc='combined',label='SUS-17-004,SUS-16-043,SUS-16-045', \
               upLim=482,decay=TChiWH)
allABs.add('EWK','16-034-TChiWZ',desc=r'$\mathbf{2\ell}$ opposite-sign',label='SUS-16-034', \
               upLim=612,decay=TChiWZ)
allABs.add('EWK','16-039-TChiWZ',desc=r'$\mathbf{3\ell}$',label='SUS-16-039',upLim=446,decay=TChiWZ)
allABs.add('EWK','16-048-TChiWZ',desc=r'$\mathbf{2\ell}$ soft',label='SUS-16-048',upLim=230,decay=TChiWZ, \
               comment=r'$\Delta M=20$ GeV')
allABs.add('EWK','17-004-TChiWZ',desc='combined',label='SUS-17-004,SUS-16-034,SUS-16-048', \
               upLim=649,decay=TChiWZ)
allABs.add('EWK','17-004-TChiWZH',desc='combined',label='SUS-17-004',upLim=535,decay=TChiWZH, \
               comment='BF = 50\%')
allABs.add('EWK','16-048-THiggsino',desc=r'$\mathbf{2\ell}$ soft',label='SUS-16-048', \
               upLim=167,decay=THiggsino,comment=r'higgsino simplified model, $\Delta M = 15$--$20$ GeV')

allABs.add('EWK',r'pp \rightarrow'+C1+' '+C1)
allABs.add('EWK','17-010-TChiWW',desc=r'$\mathbf{2\ell}$ opposite-sign',label='SUS-17-010', \
               upLim=325,lowLim=225,decay=TChiWW,comment=r'$M_{'+N1+'} = 1$ GeV')
allABs.add('EWK','17-010-TChipmChipmSlepSnu050',desc=r'$\mathbf{2\ell}$ opposite-sign',label='SUS-17-010', \
               upLim=811,decay=TChipmChipmSlepSnu,xValue=0.5,comment=r'BF($\tilde{\ell}\nu$) = 50\%')
allABs.add('EWK','17-003-TChipmChipmStauStau050', \
               desc=r'$\mathbf{\tau_{h}\tau_{h},e\tau_{h},\mu\tau_{h},e\mu}$',label='SUS-17-003', \
               upLim=706,decay=TChipmChipmStauStau,xValue=0.5,comment=r'BF($\tilde{\tau}\nu$) = 50\%')

allABs.add('EWK',r'pp \rightarrow \tilde{\ell}\tilde{\ell}')
allABs.add('EWK','17-009-T2llLR',desc=r'$\mathbf{e^{+}e^{-},\mu^{+}\mu^{-}}$',label='SUS-17-009', \
               upLim=440,decay=T2llLR)
allABs.add('EWK','17-009-T2llL',desc=r'$\mathbf{e^{+}e^{-},\mu^{+}\mu^{-}}$',label='SUS-17-009', \
               upLim=400,decay=T2llL)
allABs.add('EWK','17-009-T2llL',desc=r'$\mathbf{e^{+}e^{-},\mu^{+}\mu^{-}}$',label='SUS-17-009', \
               upLim=285,decay=T2llR)
#allABs.add('EWK','17-009-T2eeLR',desc=r'$\mathbf{e^{+}e^{-}}$',label='SUS-17-009',upLim=,decay=T2eeLR)
#allABs.add('EWK','17-009-T2eeL',desc=r'$\mathbf{e^{+}e^{-}}$',label='SUS-17-009',upLim=,decay=T2eeL)
#allABs.add('EWK','17-009-T2eeL',desc=r'$\mathbf{e^{+}e^{-}}$',label='SUS-17-009',upLim=,decay=T2eeR)
#allABs.add('EWK','17-009-T2mumuLR',desc=r'$\mathbf{\mu^{+}\mu^{-}}$',label='SUS-17-009',upLim=,decay=T2mumuLR)
#allABs.add('EWK','17-009-T2mumuL',desc=r'$\mathbf{\mu^{+}\mu^{-}}$',label='SUS-17-009',upLim=,decay=T2mumuL)
#allABs.add('EWK','17-009-T2mumuL',desc=r'$\mathbf{\mu^{+}\mu^{-}}$',label='SUS-17-009',upLim=,decay=T2mumuR)




'''
GMSB
'''
allABs.add('GMSB',r'pp \rightarrow \tilde{g}\tilde{g}')
allABs.add('GMSB','16-046-T5gg',desc=r'$\mathbf{\gamma+\mathrm{ME}_{T}}$',label='SUS-16-046',upLim=2090,decay=T5gg, \
               comment=Max)
allABs.add('GMSB','16-047-T5gg',desc=r'$\mathbf{\gamma+\mathrm{H}_{T}}$',label='SUS-16-047',upLim=2095,decay=T5gg, \
               comment=Max)
allABs.add('GMSB','16-046-T5Wg',desc=r'$\mathbf{\gamma+\mathrm{ME}_{T}}$',label='SUS-16-046',upLim=1986,decay=T5Wg, \
               comment=Max)
allABs.add('GMSB','16-047-T5Wg',desc=r'$\mathbf{\gamma+\mathrm{H}_{T}}$',label='SUS-16-047',upLim=1953,decay=T5Wg, \
               comment=Max)
allABs.add('GMSB','17-012-T5Wg',desc=r'$\mathbf{\gamma+\ell+\mathrm{ME}_{T}}$',label='SUS-17-012', \
               upLim=1700,decay=T5Wg,comment=Max)
allABs.add('GMSB','16-034-T5ZZGMSB',desc=r'$\mathbf{2\ell}$ opposite-sign',label='SUS-16-034', \
               upLim=1784,decay=T5ZZGMSB,comment=Max)
allABs.add('GMSB',r'pp \rightarrow \tilde{q}\tilde{q}')
allABs.add('GMSB','16-046-T6gg',desc=r'$\mathbf{\gamma+\mathrm{ME}_{T}}$',label='SUS-16-046',upLim=1744,decay=T6gg, \
               comment=Max)
allABs.add('GMSB','16-047-T6gg',desc=r'$\mathbf{\gamma+\mathrm{H}_{T}}$',label='SUS-16-047',upLim=1700,decay=T6gg, \
               comment=Max)
allABs.add('GMSB','16-046-T6Wg',desc=r'$\mathbf{\gamma+\mathrm{ME}_{T}}$',label='SUS-16-046',upLim=1640,decay=T6Wg, \
               comment=Max)
allABs.add('GMSB','16-047-T6Wg',desc=r'$\mathbf{\gamma+\mathrm{H}_{T}}$',label='SUS-16-047',upLim=1580,decay=T6Wg, \
               comment=Max)
allABs.add('GMSB','17-012-T6Wg',desc=r'$\mathbf{\gamma+\ell+\mathrm{ME}_{T}}$',label='SUS-17-012', \
               upLim=1400,decay=T6Wg,comment=Max)
allABs.add('GMSB',r'pp \rightarrow'+N1+' '+C1+','+C1+' '+C1)
allABs.add('GMSB','16-046-TChiWgGG',desc=r'$\mathbf{\gamma+\mathrm{ME}_{T}}$',label='SUS-16-046', \
               upLim=784,lowLim=300,decay=TChiWgGG)
allABs.add('GMSB','17-012-TChiWgGG',desc=r'$\mathbf{\gamma+\ell+\mathrm{ME}_{T}}$',label='SUS-17-012', \
               upLim=930,decay=TChiWgGG,comment=Max) # approx
allABs.add('GMSB','16-046-TChiNgGG',desc=r'$\mathbf{\gamma+\mathrm{ME}_{T}}$',label='SUS-16-046', \
               upLim=952,decay=TChiNgGG,comment=TChiNgGG_Comm)
#allABs.add('GMSB',r'pp \rightarrow}$ pairs of $\approx$ mass-degenerate $\mathbf{'+C1+','+N2+','+N1)
allABs.add('GMSB',r'pp \rightarrow ('+C1+','+N2+','+N1+') ('+C1+','+N2+','+N1+')')
allABs.add('GMSB','16-039-TChiHHGG',desc=r'$\mathbf{\geq 3\ell/\tau_{h}}$',label='SUS-16-039', \
               upLim=174,lowLim=128,decay=TChiHHGG)
allABs.add('GMSB','16-044-TChiHHGG',desc=r'$\mathbf{h\rightarrow bb}$',label='SUS-16-044', \
               upLim=766,lowLim=229,decay=TChiHHGG)
allABs.add('GMSB','16-045-TChiHHGG',desc=r'$\mathbf{h\rightarrow \gamma\gamma}$',label='SUS-16-045', \
               upLim=213,lowLim=128,decay=TChiHHGG)
allABs.add('GMSB','17-004-TChiHHGG',desc='combined',label='SUS-17-004',upLim=750,lowLim=128,decay=TChiHHGG)
allABs.add('GMSB','16-034-TChiZHGG',desc=r'$\mathbf{2\ell}$ opposite-sign',label='SUS-16-034', \
               upLim=506,lowLim=128,decay=TChiZHGG,comment=HiggsinosZH)
allABs.add('GMSB','16-039-TChiZHGG',desc=r'$\mathbf{\geq 3\ell/\tau_{h}}$',label='SUS-16-039', \
               upLim=268,lowLim=128,decay=TChiZHGG,comment=HiggsinosZH)
allABs.add('GMSB','16-045-TChiZHGG',desc=r'$\mathbf{h\rightarrow \gamma\gamma}$',label='SUS-16-045', \
               upLim=135,lowLim=128,decay=TChiZHGG,comment=HiggsinosZH)
allABs.add('GMSB','17-004-TChiZHGG',desc='combined',label='SUS-17-004',upLim=640,lowLim=128,decay=TChiZHGG, \
               comment='BF = 50\%')
allABs.add('GMSB','16-034-TChiZZGG',desc=r'$\mathbf{2\ell}$ opposite-sign',label='SUS-16-034', \
               upLim=655,lowLim=120,decay=TChiZZGG)
allABs.add('GMSB','16-039-TChiZZGG',desc=r'$\mathbf{\geq 3\ell/\tau_{h}}$',label='SUS-16-039', \
               upLim=455,lowLim=100,decay=TChiZZGG)
allABs.add('GMSB','17-004-TChiZZGG',desc='combined',label='SUS-17-004',upLim=680,lowLim=128,decay=TChiZZGG)

#
# translate CADIs to arxiv #s
#
for al in allABs.allBars:
    if al.label==None:
        continue
    for l in al.labels:
        assert l in cadiToArxiv
        arxiv = cadiToArxiv[l]
        if arxiv!=None:
            al.arxivs.append("arXiv:"+arxiv)
        else:
            al.arxivs.append(l)
    assert len(al.arxivs)==len(al.labels)
    al.arxiv = al.arxivs[0]

#!#
#!# code to work with detailed list of analyses
#!#
#!# for al in allABs.allBars:
#!#     if al.label==None:
#!#         continue
#!#     assert al.arxiv==None and al.arxivs==[ ]
#!#     for l in al.labels:
#!#         filtered = filter(lambda x: x.label==l, allAnalyses)
#!#         assert len(filtered)<2
#!#         if len(filtered)==1 and filtered[0].arxiv!=None:
#!#             al.arxivs.append("arXiv:"+filtered[0].arxiv)
#!#         else:
#!#             al.arxivs.append(l)
#!#     assert len(al.arxivs)==len(al.labels)
#!#     al.arxiv = al.arxivs[0]

   
