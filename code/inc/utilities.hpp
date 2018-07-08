#ifndef H_UTILITIES
#define H_UTILITIES

#include "model_limits.hpp"

// System includes
#include <iostream>
#include <vector>

// ROOT includes
#include "TString.h"
#include "TH2D.h"
#include "TCanvas.h"
#include "TGraph.h"
#include "TFile.h"


void setCanvas(TCanvas &can, float lMargin, float tMargin, float rMargin, float bMargin);
TH2D baseHistogram(float Xmin, float Xmax, float Ymin, float Ymax, TString xtitle, TString ytitle);
TGraph* getGraph(TFile &flimit, TString gname);
void setGraphStyle(TGraph *graph, int color, int style, int width, double glu_lsp, bool ext_graph,
		   TString model_leg, model_limits& model, bool debug=false);
TGraph* joinGraphs(TGraph *graph1, TGraph *graph2);
void reverseGraph(TGraph *graph);
void changeDmCoordinates(TGraph *graph);
void printGraph(TGraph *graph, TString comment="");
void makeContinuousGraph(TGraph *graph);
void printExclGlu(TGraph *gobs, TGraph *gexp, std::vector<float> &mLSPs, TString label);
std::vector<float> intersectionLSP(TGraph *graph, std::vector<float> &mLSPs);
std::string execute(const std::string &cmd);


#endif
