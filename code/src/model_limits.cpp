#include "model_limits.hpp"
#include "TLatex.h"

using namespace std;

void model_limits::add(TString label, TString file, int color, TString obsname, TString expname, float iglu_lsp){
  labels.push_back(label);
  files.push_back(file);
  obsnames.push_back(obsname);
  expnames.push_back(expname);
  colors.push_back(color);
  glu_lsps.push_back(iglu_lsp);
}

model_limits::model_limits(TString imodel, TString ititle, float ilegScale):
  model(imodel),
  title(ititle),
  lumi(""),
  legScale(ilegScale),
  glu_lsp(25.),
  Xmin(-99),
  Xmax(-99),
  Ymin(-99),
  Ymax(-99){
  labMass = "";
  reverseOrder = true;
  xtitle = "m#kern[0.12]{_{#lower[-0.12]{#tilde{g}}}}";
  ytitle = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}";
  }

void model_limits::addLine(TString label, float dm, float maxHeight, bool above){
  lines.push_back(dm_line(label, dm, maxHeight, above));
}
void model_limits::addLabel(float X, float Y, TString label, int text_align){
  plot_labels.push_back(dm_label(X, Y, label, text_align));
}

dm_line::dm_line(TString ilabel, float idm, float imaxHeight, bool iabove):
  label(ilabel),
  dm(idm),
  maxHeight(imaxHeight),
  above(iabove){
  }

dm_label::dm_label(float iX, float iY, TString ilabel, int itext_align):
  X(iX),
  Y(iY),
  label(ilabel),
  text_align(itext_align){
  }

void model_limits::setRanges(float iXmin, float iXmax, float iYmin, float iYmax, float iglu_lsp){
  Xmin = iXmin;
  Xmax = iXmax;
  Ymin = iYmin;
  Ymax = iYmax;
  glu_lsp = iglu_lsp;
}

