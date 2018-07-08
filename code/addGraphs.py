import ROOT
import sys,os,re
import argparse

def addGraphs(newGraph,oldGraphs,tf):
    n = newGraph.GetN() # should be 0
    print "Filling new graph",newGraph.GetName()," - starting with",n,"points"
    for sgn,nog in oldGraphs:
        og = tf.Get(nog)
        npog = og.GetN()
        xs = og.GetX()
        ys = og.GetY()
        for i in range(npog)[::sgn]:
            newGraph.SetPoint(n,xs[i],ys[i])
            n += 1
    print "Finished adding, final count =",newGraph.GetN()

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter, \
                                     description="add graphs")
parser.add_argument('-i', '--input', dest='input', help='input file', default=None)
parser.add_argument('-o', '--output', dest='output', help='output file', default=None)
parser.add_argument('-f', dest='force', help='replace output file', action="store_true", default=False)
parser.add_argument('toadd', nargs='*', default=None)
args = parser.parse_args()

if args.input==None:
    raise ValueError("Missing input file specification")
if args.output==None:
    raise ValueError("Missing output file specification")
if len(args.toadd)==0:
    raise ValueError("Missing conversion specification(s)")
    

oldgraphs = [ ]
toadd = { }
for c in args.toadd:
    fs = c.split("=")
    if len(fs)!=2:
        raise SyntaxError("Error in conversion specification "+c+"; syntax is <newgraph>=<oldgraph1>+<oldgraph2>+...")
    gnew = fs[0]
    if gnew in toadd:
        raise ValueError("Duplicate conversion specification for graph "+gnew)
    toadd[gnew] = [ ]    
    fs = re.split('([+-])',fs[1])
    # drop first element if lists starts with a sign
    if len(fs)>0 and fs[0]=="":
        fs = fs[1:]
    if len(fs)==0:
        raise SyntaxError("Error in conversion specification "+c+"; syntax is <newgraph>=<oldgraph1>+<oldgraph2>+...")
    # in case 1st element has no sign: add '+'
    if fs[0]!='+' and fs[0]!='-':
        fs.insert(0,'+')
    assert len(fs)%2==0
    for i in range(0,len(fs),2):
        sgn = 1 if fs[i]=='+' else -1
        g = fs[i+1]
        if g in oldgraphs:
            raise ValueError("Graph "+g+" is used in multiple conversions")
        toadd[gnew].append( (sgn,g) )
        oldgraphs.append(g)


assert os.path.exists(args.input) and ( args.force or not os.path.exists(args.output) )
tfin = ROOT.TFile(args.input)
if args.force:
    tfout = ROOT.TFile(args.output,"recreate")
else:
    tfout = ROOT.TFile(args.output,"new")

#
# first: check that new graphs do not exist in input file
#
for k in tfin.GetListOfKeys():
    o = k.ReadObj()
    if o in toadd:
        raise ValueError("New graph "+o+" already exists in input file")
        
#
# then: write all objects to new file
#
tfout.cd()
for k in tfin.GetListOfKeys():
    o = k.ReadObj()
    o.Write()
#
# then: add graphs
#
# tfout.cd()
print toadd
for ngnew in toadd:
    gnew = ROOT.TGraph()
    gnew.SetNameTitle(ngnew,ngnew)
    addGraphs(gnew,toadd[ngnew],tfout)
    gnew.Write()
tfout.Close()
tfin.Close()

