#!# from SMSdefs import *

#
# Class describing input for one bar in the summary plot.
#
class AnalysisBar:

    def __init__(self,category,name,label=None,desc=None,upLim=None,lowLim=None,decay="", \
                     xValue=None,comment=None):
        self.category = category               # model category
        self.name = name                       # (unique) name. Reserved names: "line", ""
        if label==None:
            self.label = None
            self.labels = [ ]
        else:
            self.labels = label.split(",")     # analysis label (CADI or arxiv)
            self.label = self.labels[0]        # analysis label (CADI or arxiv)
        self.arxivs = [ ]                      # analysis label (arxiv)
        self.arxiv = None                      # analysis label (arxiv)
        self.desc = desc                       # short description (LaTex)
        self.upLim = upLim                     # upper Limit
        self.lowLim = lowLim                   # (optional) lower Limit
        self.decay = decay                     # latex string describing the decay
        self.xValue = xValue                   # x-value for 3-particle models
        self.comment = comment                 # comment
#!# code to work with detailed list of analyses
#!#         self.analysis = None
#!#         if self.label!=None:
#!#             analyses = filter(lambda x: x.label==self.label,allAnalyses)
#!#             assert len(analyses)<2
#!#             if len(analyses)==1:
#!#                 self.analysis = analyses[0]
#!#             else:
#!#                 print "**** Unknown analysis '",self.label,"'"
#!#                 print category,name,label,desc

    def __str__(self):
        ''' Show object as string.
        '''
        result = "Analysis "+self.name
        result += "\n  Category: "+self.category
        if self.label!=None:
            result += "\n   Label: "+self.label
            if len(self.labels)>1:
                result += "\n   Others: "+str(self.labels[1:])
        result += "\n   Description: "+self.desc
        result += "\n   Limits: "+str(self.lowLim)+","+str(self.upLim)
        if self.comment!=None:
            result += "\n   Comment: "+self.comment
        if self.xValue!=None:
            result += "\n   xValue: "+str(self.xValue)
        return result

#
# Container for AnalysisBar objects
#
class AnalysisBars:

    def __init__(self):
        self.allBars = [ ]
        self.barsPerCat = { }

        self.categories = { 'Gluino' : { 'name_tex' : "Gluino" }, 
                            'Squark' : { 'name_tex' : "Squark" },
                            'EWK' : { 'name_tex' : "EWK Production" },
                            'GMSB' : { 'name_tex' : "GMSB" } }

    def add(self,category,name,label=None,desc=None,upLim=None,lowLim=None,decay="",xValue=None,comment=None):
        al = AnalysisBar(category,name,label,desc,upLim,lowLim,decay,xValue,comment)
        self.allBars.append(al)
        if not category in self.barsPerCat:
            assert category in self.categories
            self.barsPerCat[category] = [ ]
        self.barsPerCat[category].append(al)

    def getBars(self,category=None):
        if category==None:
            return self.allBars
        else:
            return self.barsPerCat[category]
        
