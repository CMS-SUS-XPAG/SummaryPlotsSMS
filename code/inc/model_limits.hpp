#ifndef H_MODEL_LIMITS
#define H_MODEL_LIMITS

// System includes
#include <iostream>
#include <vector>

// ROOT includes
#include "TString.h"

class dm_line {
public:
  TString label;
  float dm, maxHeight, labHeight;
  bool above;

  dm_line(TString ilabel, float idm, float imaxHeight, bool iabove=true, float labHeight=-9999);
};

class dm_label {
public:
  float X, Y;
  TString label;
  int text_align;

  dm_label(float iX, float iY, TString ilabel, int itext_align=11);
};

class model_limits {
public:
  TString model, title, labMass;
  TString lumi, xtitle, ytitle;
  float legScale, glu_lsp;
  bool reverseOrder;
  bool vsDM;
  bool do_prelim;
  std::vector<TString> labels, files, obsnames, expnames;
  std::vector<int> colors;
  std::vector<float> glu_lsps;
  std::vector<bool> ext_graph;
  std::vector<dm_line> lines;
  std::vector<dm_label> plot_labels;
  float Xmin, Xmax, Ymin, Ymax;

  void add(TString label, TString file, int color, TString obsname, TString expname, float glu_lsp=-1., bool extend=true);
  void addLine(TString ilabel, float idm, float imaxHeight, bool above=true, float labHeight=-9999);
  void addLabel(float X, float Y, TString label, int text_align=11);
  void setRanges(float iXmin, float iXmax, float iYmin, float iYmax, float iglu_lsp=25.);
  model_limits(TString imodel, TString ititle, float ilegScale=1.);
};



#endif
