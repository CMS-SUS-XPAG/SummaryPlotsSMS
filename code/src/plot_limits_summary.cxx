//// plot_limits_summary: Plots various limit curves on same canvas

//
// Publications
//  SUS-16-033 - arXiv:1707.07274 - PLB 778 (2018) 263
//  SUS-17-004 - arXiv:1801.03957 - JHEP 03 (2018) 160
// System includes
#include <fstream>
#include <iostream>
#include <cmath>
#include <iomanip>  // setw

// ROOT includes
#include "TStyle.h"
#include "TLatex.h"
#include "TLegend.h"
#include "TH1D.h"
#include "TROOT.h"
#include "TList.h"
#include "TLine.h"
#include "TROOT.h"
#include "TPad.h"
#include "TError.h" // Controls error level reporting

// User includes
#include "utilities.hpp"
#include "model_limits.hpp"

using namespace std;
namespace{
  bool do_prelim = true;
  bool no_shade = true;
  bool debug = false;
  int arxivIdx = 1;

  int LineWidth = 4;
  float cmsH = 0.075;
  float legLineH = 0.039;
  float legTextSize = 0.035;
  float TopMargin = 0.08;
  float legY = 1-TopMargin-cmsH-0.025;
  //float fillTransparency = 0.06;

  TString lsp = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}";
  TString chipm = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{#pm}}}#kern[-1.3]{#scale[0.85]{_{1}}}";
  TString wpm = "W#lower[0.2]{#scale[0.85]{^{#pm}}}";
  TString chip = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{+}}}#kern[-1.3]{#scale[0.85]{_{1}}}";
  TString chim = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{-}}}#kern[-1.3]{#scale[0.85]{_{1}}}";
  TString wp = "W#lower[0.2]{#scale[0.85]{^{+}}}";
  TString chi2 = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1]{#scale[0.85]{_{2}}}";
  TString ifb("fb#lower[.2]{^{-1}}");
  TString xl("x#lower[-.2]{_{l}}");

  TString flavDem = chipm+chi2+"#rightarrowl#tilde{#nu}l#tilde{l}, BF(ll)=0.5";
  TString flavDemC1C1 = chip+chim+"#rightarrowl#tilde{#nu}#nu#tilde{l}";
  TString tauDomC1C1 = chip+chim+"#rightarrow#tau#tilde{#nu}#nu#tilde{#tau}";
  TString tauRich = chipm+chi2+"#rightarrow#tilde{#tau}#nul#tilde{l}";
  TString tauDom  = chipm+chi2+"#rightarrow#tilde{#tau}#nu#tau#tilde{#tau}";
  TString WZ  = chipm+chi2+"#rightarrowWZ"+lsp+lsp;
  TString WH  = chipm+chi2+"#rightarrowWH"+lsp+lsp;

  TString slep  = "#tilde{e}_{L/R}#tilde{e}_{L/R}, #tilde{#mu}_{L/R}#tilde{#mu}_{L/R}";

  TString WZdecay = "BF("+chi2+"#rightarrowZ#kern[0.3]{"+lsp+"})";
  TString WHdecay = "BF("+chi2+"#rightarrowH#kern[0.3]{"+lsp+"})";

  //int cBenchmark(no_shade?kGray+2:1);
  int cSus15003(kRed);
  int cSus15004(kGreen+2);
  int cSus16002(kOrange+1), cSus16007A(kMagenta), cComb(kBlack);
  int cSus16007alpha(kOrange+1);
  int cSus16033(kBlue), cSus16036(kRed);
  int cSus16037(kGreen+1);
  int cSus16035(kCyan+1), cSus16042(kMagenta+1);

  int c5050 = kBlue, c5005 = kAzure+7, c5095 = kSpring-6;
  int c1c15050 = kViolet;
  int c1c1tau5050 = kAzure-3;
  int c10050 = kOrange-2, c10005 = kGray+1, c10095 = kOrange+2;
  int ctau50 = kPink+1;
  int slepAll = kGray+2;
  int cwh = kMagenta+1, cwh43 = kGreen+1, cwz39 = kRed, cwz48 = 1, cwz34 = kCyan+2;


}


void addLabelsTitle(float lMargin, float tMargin, float rMargin, TString title, TString lumi);
TString pp_to_xx(TString x){
  TString bar = "#bar{", bar2 = "}";
  if(x=="g"){bar=""; bar2="";}
    
  return "pp #rightarrow #tilde{"+x+"}#kern[0.4]{"+bar+"#tilde{"+x+bar2+"}},  #tilde{"+x+"} #rightarrow ";}

int main(){
  gErrorIgnoreLevel=kWarning; // Turns off ROOT INFO messages

  vector<TString> sus16032; sus16032.push_back("SUS-16-032"); sus16032.push_back("1707.07274");
  vector<TString> sus16033; sus16033.push_back("SUS-16-033"); sus16033.push_back("1704.07781");
  vector<TString> sus16034; sus16034.push_back("SUS-16-034"); sus16034.push_back("1709.08908");
  vector<TString> sus16035; sus16035.push_back("SUS-16-035"); sus16035.push_back("1704.07323");
  vector<TString> sus16036; sus16036.push_back("SUS-16-036"); sus16036.push_back("1705.04650");
  vector<TString> sus16037; sus16037.push_back("SUS-16-037"); sus16037.push_back("1705.04673");
  vector<TString> sus16038; sus16038.push_back("SUS-16-038"); sus16038.push_back("1802.02110");
  vector<TString> sus16039; sus16039.push_back("SUS-16-039"); sus16039.push_back("1709.05406");
  vector<TString> sus16040; sus16040.push_back("SUS-16-040"); sus16040.push_back("1712.08920");
  vector<TString> sus16041; sus16041.push_back("SUS-16-041"); sus16041.push_back("1710.09154");
  vector<TString> sus16042; sus16042.push_back("SUS-16-042"); sus16042.push_back("1709.09814");
  vector<TString> sus16043; sus16043.push_back("SUS-16-043"); sus16043.push_back("1706.09933");
  vector<TString> sus16044; sus16044.push_back("SUS-16-044"); sus16044.push_back("1709.04896");
  vector<TString> sus16045; sus16045.push_back("SUS-16-045"); sus16045.push_back("1709.00384");
  vector<TString> sus16046; sus16046.push_back("SUS-16-046"); sus16046.push_back("1711.08008");
  vector<TString> sus16047; sus16047.push_back("SUS-16-047"); sus16047.push_back("1707.06193");
  vector<TString> sus16048; sus16048.push_back("SUS-16-048"); sus16048.push_back("1801.01846");
  vector<TString> sus16049; sus16049.push_back("SUS-16-049"); sus16049.push_back("1707.03316");
  vector<TString> sus16050; sus16050.push_back("SUS-16-050"); sus16050.push_back("1710.11188");
  vector<TString> sus16051; sus16051.push_back("SUS-16-051"); sus16051.push_back("1706.04402");
  vector<TString> sus17001; sus17001.push_back("SUS-17-001"); sus17001.push_back("1711.00752");
  vector<TString> sus17003; sus17003.push_back("SUS-17-003"); sus17003.push_back("1807.02048");
  vector<TString> sus17004; sus17004.push_back("SUS-17-004"); sus17004.push_back("1801.03957");
  vector<TString> sus17005; sus17005.push_back("SUS-17-005"); sus17005.push_back("1805.05784");
  vector<TString> sus17009; sus17009.push_back("SUS-17-009"); sus17009.push_back("1806.05264");
  vector<TString> sus17010; sus17010.push_back("SUS-17-010"); sus17010.push_back("1807.07799");
  vector<TString> sus19005; sus19005.push_back("SUS-19-005"); sus19005.push_back("1909.03460");
  vector<TString> sus19006; sus19006.push_back("SUS-19-006"); sus19006.push_back("1908.04722");
  vector<TString> sus19007; sus19007.push_back("SUS-19-007"); sus19007.push_back("1911.07558");
  vector<TString> sus19008; sus19008.push_back("SUS-19-008"); sus19008.push_back("2001.10086");
  vector<TString> sus19009; sus19009.push_back("SUS-19-009"); sus19009.push_back("1912.08887");
  vector<TString> sus19011; sus19011.push_back("SUS-19-011"); sus19011.push_back("2008.05936");
  vector<TString> sus19010; sus19010.push_back("SUS-19-010"); sus19010.push_back("2103.01290");
  vector<TString> sus20002; sus20002.push_back("SUS-20-002"); sus20002.push_back("SUS-20-002");
  vector<TString> sus20001; sus20001.push_back("SUS-20-001"); sus20001.push_back("2012.08600");
  vector<TString> sus20003; sus20003.push_back("SUS-20-003"); sus20003.push_back("SUS-20-003");
  vector<TString> sus18004; sus18004.push_back("SUS-18-004"); sus18004.push_back("SUS-18-004");
  vector<TString> sus19012; sus19012.push_back("SUS-19-012"); sus19012.push_back("SUS-19-012");


  // Label definitions
  TString mj("M#lower[-.1]{_{J}}"), dphi("#Delta#phi");
  TString mt2("M#lower[-.1]{_{T2}}"), mht("H_{#lower[-.4]{T}}^{miss}"), aT("#alpha#lower[-.1]{_{T}}");
  TString alphat("#alpha_{T}");

  // Folder with root files containing the TGraphs
  //  TString basefolder("rootfiles/2017_Moriond/");
  TString basefolder("rootfiles/2021_Moriond/");
  TString folder(basefolder+"input_root/");
    TString basefolder2016("rootfiles/2018_Summer/");
    TString folder2016(basefolder2016+"input_root/");

    vector<model_limits> models;

  vector<float> mLSPs({0., 200.}); // mLSP values for which excluded mGlu is printed
  TString energy=""; // " (13 TeV)"; // Used when there are 8 and 13 TeV results


  ///////////////////////////////    Defining WH only plot   //////////////////////////////                                                                                                                 
  models.push_back(model_limits("WH","pp #rightarrow "+chi2+"#kern[0.3]{"+chipm+"}"));
  models.back().lumi = "137"; models.back().reverseOrder = false;
  models.back().addLine("m_{"+chipm+"} = m_{"+lsp+"}+m_{H}", 125, 300);
  models.back().setRanges(120, 1000, 0, 500); // Xmin, Xmax, Ymin, Ymax                                                                                                                                      
  models.back().xtitle = "m_{"+chi2+"} = m_{"+chipm+"}";
  models.back().do_prelim = true;


  models.back().add(sus17004[arxivIdx]+", 1l+b#bar{b}, 36 fb^{-1}", folder2016+"ewkino_sus17_004_wh.root", kGray, "gr_obs", "gr_exp", 124.5);
  models.back().add(sus19012[arxivIdx]+", 2l SS + #geq3l (WH)", folder+"TChiWH_sus19_012.root",cwh, "obs", "exp",124.5);
  models.back().add(sus20003[arxivIdx]+", 1l+b#bar{b} (WH)", folder+"TChiWH_sus20_003.root", cwh43, "TChiWHObservedLimit", "TChiWHExpectedLimit",150.5);


  ///////////////////////////////    Defining WZ only plot   //////////////////////////////                                                                                                                


  models.push_back(model_limits("WZ","pp #rightarrow "+chi2+"#kern[0.3]{"+chipm+"}"));                                                                                                                   
  models.back().lumi = "137"; models.back().reverseOrder = false;                                                                                                                                       
  models.back().addLine("m_{"+chipm+"} = m_{"+lsp+"}", 0, 375);                                                                                                                                          
  models.back().addLine("m_{"+chipm+"} = m_{"+lsp+"}+m_{Z}", 91, 375);                                                                                                                                   
  models.back().setRanges(100, 1100, 0, 600); // Xmin, Xmax, Ymin, Ymax                                                                                                                                   
  models.back().xtitle = "m_{"+chi2+"} = m_{"+chipm+"}";                                                                                                                                                 
  models.back().do_prelim = true;                                                                                                                                                                       

                                                                                                                                                                                                        
  models.back().add(sus17004[arxivIdx]+", combination, 36 fb^{-1}", folder2016+"ewkino_sus17_004_wz.root",kGray, "gr_obs", "gr_exp", 7);  
  models.back().add(sus20001[arxivIdx]+", 2l OS (WZ)", folder+"TChiWZ_sus20_001.root",cwz34, "ex_obs_smoothed_graph", "ex_exp_smoothed_graph", 9999);                                            
  models.back().add(sus19012[arxivIdx]+", 2l SS + #geq3l (WZ)", folder+"TChiWZ_sus19_012.root",cwz39, "obs", "exp", 7);                                                                        
  models.back().add(sus18004[arxivIdx]+", soft 2/3-lep (WZ)", folder+"TChiWZ_sus18_004.root",cwz48, "Observed", "Expected", 3);                                                                                                                            
  // models.back().add(sus17004[arxivIdx]+", combined (WZ)", folder+"ewkino_sus17_004_wz.root",                                                                                                             
  //                cwz39+2, "gr_obs", "gr_exp", 7);        



  ///////////////////////////////    Defining EWK-best plot    /////////////////////////////////                                                                                                          
  models.push_back(model_limits("EWK-best","pp #rightarrow "+chi2+"#kern[0.3]{"+chipm+"} ", 0.9));
  models.back().lumi = "137"; models.back().reverseOrder = true;
  models.back().addLine("m_{"+chipm+"} = m_{"+lsp+"}", 0, 850);
  models.back().addLine("m_{"+chipm+"} = m_{"+lsp+"}+m_{Z}", 91, 850);
  models.back().addLine("m_{"+chipm+"} = m_{"+lsp+"}+m_{H}", 125, 1000, false);
  models.back().setRanges(100, 1500, 0, 1700); // Xmin, Xmax, Ymin, Ymax                                                                                                                                  
  models.back().xtitle = "m_{"+chi2+"}=m_{"+chipm+"}}";
  models.back().do_prelim = true;


  models.back().add(sus20001[arxivIdx]+", 2l OS (WZ)", folder+"TChiWZ_sus20_001.root",cwz34, "ex_obs_smoothed_graph", "ex_exp_smoothed_graph", 9999);
  models.back().add(sus19012[arxivIdx]+", 2l SS + #geq3l (WZ)", folder+"TChiWZ_sus19_012.root",cwh43, "obs", "exp", 7);
  models.back().add(sus20003[arxivIdx]+", 1l+b#bar{b} (WH)", folder+"TChiWH_sus20_003.root", cwz39, "TChiWHObservedLimit", "TChiWHExpectedLimit",150.5);
  models.back().add(sus18004[arxivIdx]+", soft 2/3-lep (WZ)", folder+"TChiWZ_sus18_004.root",cwz48, "Observed", "Expected", 3);
  models.back().add(sus19012[arxivIdx]+", 2l SS + #geq3l ("+flavDem+", "+xl+"=0.5)", folder+"TChiSlepSnu_sus19_012.root",
		    c5050, "obs", "exp");
  //#models.back().add(sus16039[arxivIdx]+", 3l ("+tauRich+", "+xl+"=0.5)", folder+"ewkino_sus16_039_bf1_x0p5_gr.root",
  //		    c10050, "gr_obs_smoothed", "gr_exp_smoothed");


  models.back().add(sus19012[arxivIdx]+", 2l SS + #geq3l ("+tauDom+", "+xl+"=0.5)",folder+"TChiStauSnu_sus19_012.root", ctau50, "obs", "exp");



  ///////////////////////////////    Defining T1tttt plot    /////////////////////////////////
  models.push_back(model_limits("T1tttt", pp_to_xx("g")+"t#kern[0.4]{#bar{t}}#kern[0.4]{"+lsp+"}"));
  models.back().lumi = "137";
  models.back().setRanges(700, 2500, 0, 2000, 225); // Xmin, Xmax, Ymin, Ymax, glu_lsp
  models.back().xtitle = "m#kern[0.12]{_{#lower[-0.12]{#tilde{g}}}}";
  models.back().do_prelim = false;
  models.back().legScale = 0.8;

  models.back().add(sus19006[arxivIdx]+", 0-lep ("+mht+")", folder+"t1tttt_sus19_006.root",
  		    cSus16033, "ObsLim", "ExpLim");
  models.back().add(sus19005[arxivIdx]+", 0-lep ("+mt2+")", folder+"t1tttt_sus19_005.root",
   		    cSus16036, "ObsLim", "ExpLim");
  // models.back().add(sus16036[arxivIdx]+", 0-lep ("+mt2+")", folder+"t1tttt_sus16_036.root", 
  // 		    cSus16036-10, "ObsLim", "ExpLim");
  models.back().add(sus19010[arxivIdx]+", 0-lep (stop)", folder+"t1tttt_sus19_010.root",
                    kGray, "graph_smoothed_Obs", "graph_smoothed_Exp");
  models.back().add(sus19007[arxivIdx]+", 1-lep ("+mj+")", folder+"t1tttt_sus19_007.root", 
		    cSus16037, "T1ttttObservedLimit", "T1ttttExpectedLimit");
  models.back().add(sus19008[arxivIdx]+", #geq2-lep (same-sign)", folder+"t1tttt_sus19_008.root",
   		    cSus16035, "ssobs", "ssexp");
  models.back().add(sus16050[arxivIdx]+", 0-lep (stop), 36 fb^{-1}", folder2016+"t1tttt_sus16_050.root",
		   kGray, "ObsLim", "ExpLim");


  ///////////////////////////////    Defining T1bbbb plot    /////////////////////////////////
  models.push_back(model_limits("T1bbbb", pp_to_xx("g")+"b#kern[0.23]{#bar{b}}#kern[0.2]{"+lsp+"}"));
  models.back().lumi = "137";
  models.back().setRanges(700, 2500, 0, 2000); // Xmin, Xmax, Ymin, Ymax
  models.back().xtitle = "m#kern[0.12]{_{#lower[-0.12]{#tilde{g}}}}";
  models.back().do_prelim = false;
  models.back().legScale = 0.8;

  models.back().add(sus16036[arxivIdx]+" ("+mt2+"), 36 fb^{-1}", folder2016+"t1bbbb_sus16_036.root",
  		    kGray, "ObsLim", "ExpLim");

  models.back().add(sus19006[arxivIdx]+", 0-lep ("+mht+")", folder+"t1bbbb_sus19_006.root",
  		    cSus16033, "ObsLim", "ExpLim");
  models.back().add(sus19005[arxivIdx]+", 0-lep ("+mt2+")", folder+"t1bbbb_sus19_005.root",
                      cSus16036, "ObsLim", "ExpLim");


  ///////////////////////////////    Defining T1qqqq plot    /////////////////////////////////
  models.push_back(model_limits("T1qqqq", pp_to_xx("g")+"q#kern[0.23]{#bar{q}}#kern[0.2]{"+lsp+"}"));
  models.back().lumi = "137";
  models.back().setRanges(700, 2500, 0, 2000); // Xmin, Xmax, Ymin, Ymax
  models.back().xtitle = "m#kern[0.12]{_{#lower[-0.12]{#tilde{g}}}}";
  models.back().do_prelim = false;
  models.back().legScale = 0.8;

  models.back().add(sus16033[arxivIdx]+" ("+mht+"), 36 fb^{-1}", folder2016+"t1qqqq_sus16_033.root",
  		    kGray, "ObsLim", "ExpLim");
  models.back().add(sus19006[arxivIdx]+", 0-lep ("+mht+")", folder+"t1qqqq_sus19_006.root",
  		    cSus16033, "ObsLim", "ExpLim");
  models.back().add(sus19005[arxivIdx]+" ("+mt2+")", folder+"t1qqqq_sus19_005.root",
  		    cSus16036, "ObsLim", "ExpLim");

    ///////////////////////////////    Defining T1qqqq+LLP plot    /////////////////////////////////
  //    models.push_back(model_limits("T1qqqqLLP", pp_to_xx("g")+"q#kern[0.23]{#bar{q}}#kern[0.2]{"+chipm+"/"+lsp+"}"));
  models.push_back(model_limits("T1qqqqLLP", pp_to_xx("g")+"q#kern[0.23]{#bar{q}}#kern[0.2]{"+chipm+"}"));//,#kern[0.2]{"+chipm+"#rightarrow"+lsp+"+#pi^{#pm}}"));
    models.back().lumi = "137";
    models.back().setRanges(700, 2600, 0, 3000); // Xmin, Xmax, Ymin, Ymax
    models.back().xtitle = "m#kern[0.12]{_{#lower[-0.12]{#tilde{g}}}}";
    models.back().do_prelim = false;
    models.back().legScale = 0.8;
    models.back().addLabel(0.17,0.62,"#kern[0.2]{"+chipm+"#rightarrow"+lsp+"+#pi^{#pm}}");

    models.back().add(sus16033[arxivIdx]+" ("+mht+"), 36 fb^{-1}", folder2016+"t1qqqq_sus16_033.root",
                      kGray, "ObsLim", "ExpLim");
    models.back().add(sus19005[arxivIdx]+" ("+mt2+")", folder+"t1qqqq_sus19_005.root",
                      cSus16036, "ObsLim", "ExpLim");
    models.back().add(sus19005[arxivIdx]+" ("+mt2+"+LLP), c#tau("+chipm+")=10 cm", folder+"t1qqqq-10_sus19_005.root",
                      kOrange-3, "ObsLim", "ExpLim");
    models.back().add(sus19005[arxivIdx]+" ("+mt2+"+LLP), c#tau("+chipm+")=50 cm", folder+"t1qqqq-50_sus19_005.root",
                      kGreen+2, "ObsLim", "ExpLim");
    models.back().add(sus19005[arxivIdx]+" ("+mt2+"+LLP), c#tau("+chipm+")=200 cm", folder+"t1qqqq-200_sus19_005.root",
                      kAzure, "ObsLim", "ExpLim");
    
  ///////////////////////////////    Defining T5qqqqVV plot    /////////////////////////////////
  models.push_back(model_limits("T5qqqqVV",
				"pp#kern[0.]{#rightarrow}#tilde{g}#kern[0.2]{#tilde{g}},#tilde{g}#kern[0.]{#rightarrow}"
				"q#kern[0.]{#bar{q}}#kern[0.]{("+chipm+"/"+chi2+
				")}#kern[0.]{#rightarrow}q#kern[0.2]{#bar{q}}#kern[0.]{("+wpm+"/Z)}#kern[0.2]{"+lsp+"}     "));
  models.back().lumi = "137";
  models.back().setRanges(700, 2200, 0, 1850); // Xmin, Xmax, Ymin, Ymax
  models.back().xtitle = "m#kern[0.12]{_{#lower[-0.12]{#tilde{g}}}}";
  models.back().do_prelim = false;
  models.back().legScale = 0.8;

  models.back().labMass = "m_{"+chipm+", "+chi2+"} = 0.5(m_{#lower[-0.12]{#tilde{g}}} + m_{"+lsp+"})";
  models.back().add(wpm+"/Z: "+sus16033[arxivIdx]+", 0-lep ("+mht+"), 36 fb^{-1}", folder2016+"t5qqqqvv_sus16_033.root",
  		    kGray, "ObsLim", "ExpLim");
  models.back().add(wpm+"/Z: "+sus19006[arxivIdx]+", 0-lep ("+mht+")", folder+"t5qqqqvv_sus19_006.root",
  		    kBlue, "ObsLim", "ExpLim_new");
  models.back().add(wpm+"/Z: "+sus19008[arxivIdx]+", #geq2-lep (same-sign)", folder+"t5qqqqvv_sus19_008.root",
  		    kCyan, "ssobs", "ssexp");
  models.back().add(wpm+": "+sus19008[arxivIdx]+", #geq2-lep (same-sign)", folder+"t5qqqqww_sus19_008.root",
  		    kRed, "ssobs", "ssexp");

    ///////////////////////////////    Defining T2qq plot    /////////////////////////////////
    models.push_back(model_limits("T2qq", pp_to_xx("q")+"q#kern[0.4]{"+lsp+"}"));
    models.back().lumi = "137";
    models.back().setRanges(350, 2000, 0, 1400); // Xmin, Xmax, Ymin, Ymax
    models.back().xtitle = "m#kern[0.12]{_{#lower[-0.12]{#tilde{q}}}}";
    models.back().do_prelim = false;
    models.back().legScale = 0.8;
    models.back().addLabel(0.22,0.27,"one light #tilde{q}");
    // models.back().addLabel(0.15,0.18,"one light #lower[0.10]{#tilde{q}}");
    models.back().addLabel(0.5,0.675,"#lower[-0.12]{#tilde{q}}_{L}+#lower[-0.12]{#tilde{q}}_{R} (#lower[-0.12]{#tilde{u}},#lower[-0.12]{#tilde{d}},#lower[-0.12]{#tilde{s}},#lower[-0.12]{#tilde{c}})");
    
    
    models.back().add(sus16036[arxivIdx]+", 0-lep ("+mt2+"), 36 fb^{-1}", folder2016+"t2qq_sus16_036.root",
                      kGray, "ObsLim_1squark", "ExpLim_1squark");
    models.back().add("", folder2016+"t2qq_sus16_036.root",
                      kGray, "ObsLim", "ExpLim");
    models.back().add(sus19005[arxivIdx]+", 0-lep ("+mt2+")", folder+"t2qq_sus19_005.root",
                      cSus16036, "ObsLim_1squark", "ExpLim_1squark");
    models.back().add("", folder+"t2qq_sus19_005.root",
                      cSus16036, "ObsLim", "ExpLim");
    models.back().add(sus19006[arxivIdx]+", 0-lep ("+mht+")", folder+"t2qq_sus19_006.root",
		      cSus16033, "ObsLim_new", "ExpLim");
    models.back().add("", folder+"t2qq_sus19_006.root",
                      cSus16033, "ObsLim2", "ExpLim2");

    
    
  ///////////////////////////////    Defining T2qqLLP8 plot    /////////////////////////////////
  models.push_back(model_limits("T2qqLLP8", pp_to_xx("q")+"q#kern[0.1]{"+chipm+"/"+lsp+"}"));//, #lower[-0.12]{#tilde{q}}_{L}+#lower[-0.12]{#tilde{q}}_{R} (#lower[-0.12]{#tilde{u}},#lower[-0.12]{#tilde{d}},#lower[-0.12]{#tilde{s}},#lower[-0.12]{#tilde{c}})"));
  models.back().lumi = "137";
  models.back().setRanges(350, 2000, 0, 2000); // Xmin, Xmax, Ymin, Ymax
  models.back().xtitle = "m#kern[0.12]{_{#lower[-0.12]{#tilde{q}}}}";
  models.back().do_prelim = false;
  models.back().legScale = 0.8;
  models.back().addLabel(0.2,0.57,"#lower[-0.12]{#tilde{q}}_{L}+#lower[-0.12]{#tilde{q}}_{R} (#lower[-0.12]{#tilde{u}},#lower[-0.12]{#tilde{d}},#lower[-0.12]{#tilde{s}},#lower[-0.12]{#tilde{c}})");  

    models.back().add(sus16036[arxivIdx]+", 0-lep ("+mt2+"), 36 fb^{-1}", folder2016+"t2qq_sus16_036.root",
                      kGray, "ObsLim", "ExpLim");


    models.back().add(sus19005[arxivIdx]+", 0-lep ("+mt2+")", folder+"t2qq_sus19_005.root",
                      cSus16036, "ObsLim", "ExpLim");


    
    models.back().add(sus19005[arxivIdx]+", 0-lep ("+mt2+"+LLP), c#tau("+chipm+")=10 cm", folder+"t2qq-10_sus19_005.root",
                      kOrange-3, "ObsLim", "ExpLim");


    models.back().add(sus19005[arxivIdx]+", 0-lep ("+mt2+"+LLP), c#tau("+chipm+")=50 cm", folder+"t2qq-50_sus19_005.root",
                      kGreen+2, "ObsLim", "ExpLim");


    models.back().add(sus19005[arxivIdx]+", 0-lep ("+mt2+"+LLP), c#tau("+chipm+")=200 cm", folder+"t2qq-200_sus19_005.root",
                      kAzure, "ObsLim", "ExpLim");

    
    ///////////////////////////////    Defining T2qqLLP1 plot    /////////////////////////////////
    models.push_back(model_limits("T2qqLLP1", pp_to_xx("q")+"q#kern[0.1]{"+chipm+"/"+lsp+"}"));//, one light #tilde{q}"));
    models.back().lumi = "137";
    models.back().setRanges(350, 2000, 0, 2000); // Xmin, Xmax, Ymin, Ymax
    models.back().xtitle = "m#kern[0.12]{_{#lower[-0.12]{#tilde{q}}}}";
    models.back().do_prelim = false;
    models.back().legScale = 0.8;
    models.back().addLabel(0.2,0.5,"one light #tilde{q}");

    models.back().add(sus16036[arxivIdx]+", 0-lep ("+mt2+"), 36 fb^{-1}", folder2016+"t2qq_sus16_036.root",
                      kGray, "ObsLim_1squark", "ExpLim_1squark");
    
    models.back().add(sus19005[arxivIdx]+", 0-lep ("+mt2+")", folder+"t2qq_sus19_005.root",
                      cSus16036, "ObsLim_1squark", "ExpLim_1squark");
    
    
    models.back().add(sus19005[arxivIdx]+", 0-lep ("+mt2+"+LLP), c#tau("+chipm+")=10 cm", folder+"t2qq-10_sus19_005.root",
                      kOrange-3, "ObsLim_1squark", "ExpLim_1squark");
    
    models.back().add(sus19005[arxivIdx]+", 0-lep ("+mt2+"+LLP), c#tau("+chipm+")=50 cm", folder+"t2qq-50_sus19_005.root",
                      kGreen+2, "ObsLim_1squark", "ExpLim_1squark");
    
    models.back().add(sus19005[arxivIdx]+", 0-lep ("+mt2+"+LLP), c#tau("+chipm+")=200 cm", folder+"t2qq-200_sus19_005.root",
                      kAzure, "ObsLim_1squark", "ExpLim_1squark");
    
    
    
  ///////////////////////////////    Defining T2bb plot    /////////////////////////////////
  models.push_back(model_limits("T2bb", pp_to_xx("b")+"b#kern[0.4]{"+lsp+"}"));
  models.back().lumi = "137";
  models.back().setRanges(350, 1500, 0, 1150); // Xmin, Xmax, Ymin, Ymax
  models.back().xtitle = "m#kern[0.12]{_{#lower[-0.12]{#tilde{b}}}}";
  models.back().do_prelim = false;
  models.back().legScale = 0.8;

    models.back().add(sus16036[arxivIdx]+", 0-lep ("+mt2+"), 36 fb^{-1}", folder2016+"t2bb_sus16_036.root",
                    kGray, "ObsLim", "ExpLim");
    models.back().add(sus19006[arxivIdx]+", 0-lep ("+mht+")", folder+"t2bb_sus19_006.root",
		      cSus16033, "ObsLim", "ExpLim");
    models.back().add(sus19005[arxivIdx]+", 0-lep ("+mt2+")", folder+"t2bb_sus19_005.root",
                      cSus16036, "ObsLim", "ExpLim");


  ///////////////////////////////    Defining T2tt plot    ///////////////////////////////// 
  models.push_back(model_limits("T2tt", pp_to_xx("t")+"t#kern[0.4]{"+lsp+"}"));
  models.back().lumi = "137";
  models.back().setRanges(100, 1500, 0, 1150, 85); // Xmin, Xmax, Ymin, Ymax, glu_lsp
  models.back().xtitle = "m#kern[0.12]{_{#lower[-0.12]{#tilde{t}}}}";
  models.back().do_prelim = true;
  models.back().legScale = 0.8;
     
  models.back().add(sus20002[arxivIdx]+", 0-, 1- and 2-lep combination", folder+"t2tt_sus20_002.root",
		    cComb, "contour_obs", "contour_exp");
    models.back().add(sus17001[arxivIdx]+", 0-, 1- and 2-lep (stop), 36 fb^{-1}", folder2016+"t2tt_sus17_001_comb_gr.root",
  		    kGray, "gObs", "gExp");

    //graph_smoothed_Exp
    models.back().add(sus19010[arxivIdx]+", 0-lep (stop)", folder+"t2tt_sus19_010.root",                                                                                                              
			cSus16033, "graph_smoothed_Obs", "graph_smoothed_Exp"); 
    //cSus16033, "ObsLim", "ExpLim");
    //models.back().add(sus19005[arxivIdx]+", 0-lep ("+mt2+")", folder+"t2tt_sus19_005.root",
    //                  cSus16036, "ObsLim", "ExpLim");
    models.back().add(sus19009[arxivIdx]+", 1-lep (stop)", folder+"t2tt_sus19_009.root",
		      cSus16036, "gObs", "gExp");
    models.back().add(sus19011[arxivIdx]+", 2-lep (stop)", folder+"t2tt_sus19_011.root",
                      cSus16035, "contour_obs", "contour_exp");
    models.back().add("", folder+"t2tt_sus19_011.root",
                      cSus16035, "contour_corr_obs", "contour_exp");
    

    ///////////////////////////////    Defining T6ttHZ plot    /////////////////////////////////
    models.push_back(model_limits("T6ttHZ",
                                  "pp#kern[0.]{#rightarrow}#tilde{t}_{2}#kern[0.2]{#bar{#tilde{t}}_{2}}, #tilde{t}_{2}#kern[0.]{#rightarrow}#tilde{t}_{1}#kern[0.]{(H/Z)}#kern[0.]{#rightarrow}t#kern[0.]{(H/Z)}#kern[0.2]{"+lsp+"}     "));
    models.back().lumi = "137";
    models.back().setRanges(300, 1000, 200, 900); // Xmin, Xmax, Ymin, Ymax
    models.back().xtitle = "m#kern[0.12]{_{#lower[-0.12]{#tilde{t_{2}}}}}";
    models.back().ytitle = "m#kern[0.12]{_{#lower[-0.12]{#tilde{t_{1}}}}}";
    models.back().reverseOrder = false;
    models.back().do_prelim = false;
    models.back().legScale = 0.8;
    
    models.back().labMass = "m_{#tilde{t}_{1}} - m_{"+lsp+"} = 175 GeV";
    models.back().add(sus19008[arxivIdx]+", #geq2-lep (same-sign):", folder+"t6tthzbrz_sus19_008.root",
                      kWhite, "ssobs", "ssexp");
    models.back().add("#it{#Beta}(#tilde{t}_{2}#kern[0.]{#rightarrow}#tilde{t}_{1}#kern[0.]{Z})=100%", folder+"t6tthzbrz_sus19_008.root",
                      kRed, "ssobs", "ssexp");
    models.back().add("#it{#Beta}(#tilde{t}_{2}#kern[0.]{#rightarrow}#tilde{t}_{1}#kern[0.]{Z})=50%", folder+"t6tthzbrb_sus19_008.root",
                      kOrange-3, "ssobs", "ssexp");
    models.back().add("#it{#Beta}(#tilde{t}_{2}#kern[0.]{#rightarrow}#tilde{t}_{1}#kern[0.]{Z})=0%", folder+"t6tthzbrh_sus19_008.root",
                      kGreen+2, "ssobs", "ssexp");

    models.back().addLine("m_{#tilde{t}_{2}} = m_{#tilde{t}_{1}}+m_{H}", 125, 630, true, 400);

    
  ///////////////////////////////    Defining T2tt+compressed plot    ///////////////////////////////// 
/*  models.push_back(model_limits("T2tt234body",
				pp_to_xx("t")+"t#lower[0.2]{#scale[0.85]{^{(*)}}}#kern[0.4]{"+lsp+"}"));
  models.back().lumi = "35.9"; 
  models.back().setRanges(100, 1200, 0, 900, 5); // Xmin, Xmax, Ymin, Ymax, glu_lsp
  models.back().addLine("m_{#tilde{t}} = m_{"+lsp+"}+m_{b}", 5, 560, true, 300);
  models.back().addLine("m_{#tilde{t}} = m_{"+lsp+"}+m_{W}+m_{b}", 85, 600, true, 400);
  models.back().addLine("m_{#tilde{t}} = m_{"+lsp+"}+m_{t}", 175, 600);
  models.back().xtitle = "m#kern[0.12]{_{#lower[-0.12]{#tilde{t}}}}";
  models.back().do_prelim = false;
  models.back().legScale = 0.8;

  // models.back().add("", folder+"t2tt_comb.root", 
  //   		    cComb, "gObs", "gExp", 80.);
  models.back().add(sus16049[arxivIdx]+", 0-lep (stop)", folder+"t2tt_sus16_049.root", 
		    cSus16007A, "graph_smoothed_Obs", "graph_smoothed_Exp",85.);
  models.back().add("", folder+"t2tt_sus16_049.root", 
    		    cSus16007A, "graph_smoothed_Obs_12", "graph_smoothed_Exp",85.);
  models.back().add("", folder+"t2tt_sus16_049.root",
    		    cSus16007A, "graph_smoothed_Obs_8", "graph_smoothed_Exp",85.);
  models.back().add("", folder+"t2tt_sus16_049.root",
   		    cSus16007A, "graph_smoothed_Obs_6", "graph_smoothed_Exp",85.);
  // // models.back().add(sus16050[arxivIdx]+", 0-lep stop / top ID", folder+"t2tt_sus16_050.root", 
  // //  		    kGray, "ObsLim", "ExpLim");
  models.back().add(sus16051[arxivIdx]+", 1-lep (stop)", folder+"t2tt_sus16_051.root",
   		    cSus16002, "gObs", "gExp", 85.);
  models.back().add(sus17001[arxivIdx]+", 2-lep (stop)", folder+"t2tt_sus17_001.root", 
    		    cSus15004, "contour_obs", "contour_exp", 85.);
  // models.back().add("Combination 0-, 1- and 2-lep stop", folder+"t2tt_comb.root", 
  //   		    cComb, "gObs", "gExp", 80.);
  models.back().add(sus17005[arxivIdx]+", soft 1-lep + 0-lep", folder+"t2tt4c_sus17_005_gr.root", 
    		    kRed, "gOBSOut0", "gEXPOut0");
  models.back().add(sus17005[arxivIdx]+", soft 1-lep (MVA)", folder+"t2tt4bdy_sus17_005_mva_gr.root", 
    		    kGreen, "gOBSOut0", "gEXPOut0");
  // models.back().add(sus17010[arxivIdx]+", 2-lep (EWK/stop)", folder+"t2tt_sus17_010.root", 
  //   		    kBlue, "gr_Obs", "gr_Exp");

  ///////////////////////////////    Defining T6bbWW    ///////////////////////////////// 
  models.push_back(model_limits("T6bbWW", pp_to_xx("t")+"b#kern[0.1]{"+chip+"} #rightarrow b#kern[0.1]{"+wp+"}#kern[0.0]{"+lsp+"}      "));
  models.back().lumi = "35.9"; 
  models.back().setRanges(100, 1200, 0, 900, 5); // Xmin, Xmax, Ymin, Ymax, glu_lsp
  models.back().addLine("m_{t~} = m_{"+lsp+"}+m_{b}", 5, 630);
  models.back().addLine("m_{t~} = m_{"+lsp+"}+m_{W}+m_{b}", 85, 630, true, 240);
  models.back().addLine("m_{t~} = m_{"+lsp+"}+m_{t}", 175, 630);
  models.back().labMass = "m_{"+chipm+", "+chi2+"} = 0.5(m_{#lower[-0.12]{#tilde{t}}} + m_{"+lsp+"})";
  models.back().xtitle = "m#kern[0.12]{_{#lower[-0.12]{#tilde{t}}}}";
  models.back().do_prelim = false;
  models.back().legScale = 0.8;

  // models.back().add(sus16036[arxivIdx]+", 0-lep ("+mt2+")", folder+"t6bbWW_sus16_036.root", 
  //    		    kYellow, "ObsLim", "ExpLim", 175.);
  models.back().add(sus17001[arxivIdx]+", 0-, 1-, 2-lep (stop)", folder+"t2bW_sus17_001_comb_gr.root", 
    		    cComb, "gObs", "gExp", 175.);
  models.back().add(sus16036[arxivIdx]+", 0-lep ("+mt2+")", folder+"t6bbWW_sus16_036.root", 
   		    cSus16036, "ObsLim", "ExpLim", 175.);
  // models.back().add(sus16049[arxivIdx]+", 0-lep (stop)", folder+"t2bW_sus16_049.root", 
  //  		    cSus16007A, "graph_smoothed_Obs", "graph_smoothed_Exp", 175.);
  // models.back().add(sus16051[arxivIdx]+", 1-lep (stop)", folder+"t6bbWW_sus16_051.root",
  // 		    cSus16002, "gObs", "gExp", 175., false);
  // models.back().add("", folder+"t6bbWW_sus16_051.root",
  // 		    cSus16002, "gObs_2", "gExp_2", 175., false);
  // models.back().add(sus17001[arxivIdx]+", 2-lep (stop)", folder+"t2bW_sus17_001_gr.root", 
  //   		    cSus15004, "contour_obs", "contour_exp", 175.);
  models.back().add(sus17005[arxivIdx]+", soft 1-lep + 0-lep", folder+"t2bWc_sus17_005_gr.root", 
     		    kRed, "gOBSOut0", "gEXPOut0", 5.);
  models.back().add(sus16048[arxivIdx]+", soft 2-lep", folder+"t6bbWW_sus16_048.root", 
     		    kBlue, "ex_obs_smoothed_graph", "ex_exp_smoothed_graph", 5.);
  // models.back().add(sus17010[arxivIdx]+", 2-lep (EWK/(stop))", folder+"t2bW_sus17_010.root", 
  //    		    kBlack, "gr_Obs", "gr_Exp", 175.);

  ///////////////////////////////    Defining stop compressed 4-body / cc   //////////////////////////
  // TString titleStopCompressed = "pp #rightarrow #tilde{t}#kern[0.3]{#bar{#tilde{t}}}, ";
  // titleStopCompressed += "(m#kern[0.24]{_{#lower[-0.12]{#tilde{t}}}} - m#kern[0.24]{_{#lower[-0.12]{";
  // titleStopCompressed += lsp+"}}})";
  // titleStopCompressed += " < m#kern[0.24]{_{#lower[-0.12]{W}}}";
  models.push_back(model_limits("T2tt4body-c", 
				pp_to_xx("t")+"(#kern[0.4]{b}#kern[0.4]{f}#kern[0.4]{#bar{f}'} / c)#kern[0.4]{"+lsp+"}"));
  models.back().lumi = "35.9"; 
  models.back().setRanges(200, 700, 10, 135, 80); // Xmin, Xmax, Ymin, Ymax, glu_lsp
  models.back().legScale = 0.8;
  models.back().vsDM = true;
  models.back().do_prelim = false;
  models.back().xtitle = "m#kern[0.24]{_{#lower[-0.12]{#tilde{t}}}}";
  models.back().ytitle = "m#kern[0.24]{_{#lower[-0.12]{#tilde{t}}}} - m#kern[0.24]{_{#lower[-0.12]{"+
    lsp+"}}}";
  models.back().addLine("m#kern[0.24]{_{#lower[-0.12]{#tilde{t}}}} = m#kern[0.24]{_{#lower[-0.12]{"+
			lsp+"}}} + m#kern[0.24]{_{#lower[-0.12]{W}}}", 80, 600, true);

  models.back().add("#tilde{t}#rightarrow#kern[0.4]{b}#kern[0.4]{f}#kern[0.4]{#bar{f}'}#kern[0.4]{"+lsp+"}: "+
		    sus17005[arxivIdx]+", soft 1-lep + 0-lep", 
		    folder+"t2tt4c_sus17_005_gr_dm.root",
		    kGreen+3, "gOBSOut0", "gEXPOut0");
  models.back().add("#tilde{t}#rightarrow#kern[0.4]{b}#kern[0.4]{f}#kern[0.4]{#bar{f}'}#kern[0.4]{"+lsp+"}: "+
		    sus17005[arxivIdx]+", soft 1-lep (MVA)", 
		    folder+"t2tt4bdy_sus17_005_mva_gr_dm.root", 
    		    kGreen-9, "gOBSOut0", "gEXPOut0");
  models.back().add("#tilde{t}#rightarrow#kern[0.4]{c} "+lsp+": "+sus16032[arxivIdx]+", 0-lep (stop/sbottom)", 
		    folder+"t2cc_sus16_032_dm.root", 
    		    kRed+2, "smoothed_obs", "smoothed_Exp");
  models.back().add("#tilde{t}#rightarrow#kern[0.4]{c} "+lsp+": "+sus16036[arxivIdx]+", 0-lep ("+mt2+")", 
		    folder+"t2cc_sus16_036_dm.root", 
    		    kRed-4, "ObsLim", "ExpLim");
  models.back().add("#tilde{t}#rightarrow#kern[0.4]{c} "+lsp+": "+sus16049[arxivIdx]+", 0-lep (stop)", 
		    folder+"t2cc_sus16_049_dm.root", 
    		    kMagenta, "graph_smoothed_Obs", "graph_smoothed_Exp");
  models.back().add("#tilde{t}#rightarrow#kern[0.4]{c} "+lsp+": "+sus16038[arxivIdx]+", 0-lep ("+alphat+")", 
		    folder+"t2cc_sus16_038_dm.root", 
    		    kOrange, "contour_Obs_0", "contour_Exp_0");
  // models.back().add("#tilde{t}#rightarrow b "+chip+": "+sus17005[arxivIdx]+" (soft 1-lep + 0-lep)",
  // 		    folder+"t2bWc_sus17_005_gr_dm.root", 
  //   		    kBlue+3, "gOBSOut0", "gEXPOut0");
  // models.back().add("#tilde{t}#rightarrow b "+chip+": "+sus16048[arxivIdx]+" (soft 2-lep)", 
  // 		    folder+"t6bbWW_sus16_048_dm.root", 
  //   		    kBlue-9, "ex_obs_smoothed_graph", "ex_exp_smoothed_graph");
*/
   //////////////////////////////////////////////////////////////////////////////////////// 
  //////////////////////////////////    Making plots    //////////////////////////////////
  //////////////////////////////////////////////////////////////////////////////////////// 
  
  //// Creating canvas
  gStyle->SetOptStat(0);  
  float lMargin(0.14), tMargin(TopMargin), rMargin(0.04), bMargin(0.14);
  TCanvas can("canvas","", 600, 600);
  setCanvas(can, lMargin, tMargin, rMargin, bMargin);

  //// Creating base legend for observed/expected
  TH1D hobs("hobs","",1,0,1), hexp("hexp","",1,0,1);
  hobs.SetLineColor(1); hobs.SetLineWidth(LineWidth);
  hexp.SetLineColor(1); hexp.SetLineStyle(2); hexp.SetLineWidth(LineWidth);

  double legX(1-rMargin-0.045), baselegY = 1-tMargin-cmsH-0.02;
  double legW = 0.14, legH = 0.07;
  TLegend baseleg(legX-legW, baselegY-legH, legX, baselegY);
  baseleg.SetTextSize(0.031); baseleg.SetFillColor(0); 
  baseleg.SetFillStyle(0); baseleg.SetBorderSize(0);
  baseleg.AddEntry(&hexp, "Expected");
  baselegY = baselegY - 0.038;
  TLegend obsleg(legX-legW, baselegY-legH, legX, baselegY);
  obsleg.SetTextSize(0.031); obsleg.SetFillColor(0); 
  obsleg.SetFillStyle(0); obsleg.SetBorderSize(0);
  obsleg.AddEntry(&hobs, "Observed");

  //// General line and label
  TLatex labMass; labMass.SetNDC();  
  labMass.SetTextAlign(33); labMass.SetTextFont(42); 
  TLine line;

  //// Looping over each model
  cout<<endl;
  for(size_t imodel(0); imodel < models.size(); imodel++){
    model_limits mod(models[imodel]);

    TLatex label;
    //// Creating base histogram and drawing lumi labels
    float Xmin(mod.Xmin), Xmax(mod.Xmax), Ymin(mod.Ymin), Ymax(mod.Ymax), glu_lsp(mod.glu_lsp);
    TString xtitle = mod.xtitle;

    TH2D hbase = baseHistogram(Xmin, Xmax, Ymin, Ymax, xtitle, mod.ytitle);
    hbase.Draw();
    do_prelim = mod.do_prelim;
    addLabelsTitle(lMargin, tMargin, rMargin, mod.title, mod.lumi);

    //// Plot lines at constant dM
    float degrees;
    if (mod.vsDM) {
      degrees = 0.;
    }
    else {
      degrees = 180/3.141593*atan2((1-tMargin-bMargin)/(Ymax-Ymin) , (1-lMargin-rMargin)/(Xmax-Xmin));
    }
    int lcolor(kGray+2);
    line.SetLineStyle(2); line.SetLineWidth(2); line.SetLineColor(lcolor);
    label.SetTextSize(0.027); label.SetTextAngle(degrees); label.SetTextColor(lcolor);
    for(size_t iline=0; iline<mod.lines.size(); iline++){
      float dM = mod.lines[iline].dm;
      float minGlu=dM;
      float maxh = mod.lines[iline].maxHeight;
      float labh = mod.lines[iline].labHeight;
      if(dM<Xmin) minGlu = Xmin;
      if (mod.vsDM) {
	line.DrawLine(Xmin,dM,Xmax,dM);
	// offsetX controls where along the line to put the label, offsetY how far from it
	float offsetX=(Xmax-Xmin)/38, offsetY=0.;
	if(mod.lines[iline].above){
	  label.SetTextAlign(31); 
	  offsetY += 0.02*(Ymax-Ymin);
	} else {
	  label.SetTextAlign(33);
	  offsetY -= 0.02*(Ymax-Ymin);
	}
	label.DrawLatex(Xmax-offsetX, dM+offsetY, mod.lines[iline].label);
	// label.DrawLatex(200., 200., mod.lines[iline].label);
      }
      else {
	line.DrawLine(minGlu, minGlu-dM, dM+maxh, maxh);
	// offsetX controls where along the line to put the label, offsetY how far from it
	float offsetX=(Xmax-Xmin)/38, offsetY=(Xmax-Xmin)/38;
	if(mod.lines[iline].above){
	  label.SetTextAlign(31); 
	} else {
	  label.SetTextAlign(33);
	  offsetX *= -0.4;
	  offsetY *= -0.7;
	}
	label.DrawLatex(dM+labh-offsetX, labh-offsetX+offsetY, mod.lines[iline].label);
	// label.DrawLatex(200., 200., mod.lines[iline].label);
	if (debug)
	  cout << "Drawing label " << dM+labh-offsetX << " " << labh-offsetX+offsetY << " " 
	       << mod.lines[iline].label << endl;
      }
    }// Loop over lines

    for(size_t ilabel=0; ilabel<mod.plot_labels.size(); ilabel++){
      label.SetNDC(); label.SetTextAngle(0); label.SetTextColor(1); 
      label.SetTextFont(42);
       label.SetTextSize(0.04);
      label.SetTextAlign(mod.plot_labels[ilabel].text_align);

      label.DrawLatex(mod.plot_labels[ilabel].X, mod.plot_labels[ilabel].Y, mod.plot_labels[ilabel].label);
    }// Loop over labels
    //// Plotting limits
    size_t ncurves(mod.files.size()), ncurvesleg = mod.files.size();
    vector<TGraph*> obs(ncurves, 0), exp(ncurves, 0);
    // Getting all graphs first because the ones that come from TCanvas mess up the colors
    for(size_t file(0); file < ncurves; file++){
      cout<<"Loading "<<mod.files[file]<<endl;
      TFile flimit(mod.files[file]);
      exp[file] = getGraph(flimit, mod.expnames[file]);
      obs[file] = getGraph(flimit, mod.obsnames[file]);
      if(mod.labels[file] == "") ncurvesleg--;
    }
    cout<<endl<<"Model "<<mod.model<<endl<<"============================="<<endl;
    for(size_t file(0); file < ncurves; file++){
      if (debug) cout<<"Doing "<<mod.files[file]<<endl;
      float mod_gl = glu_lsp;
      if(mod.glu_lsps[file]>0) mod_gl = mod.glu_lsps[file];

      if((mod.labels[file].Contains("1801.01846")||mod.labels[file].Contains("SUS-16-048"))&&
	 !mod.model.BeginsWith("T6")){ //16-048
       	changeDmCoordinates(exp[file]);
       	changeDmCoordinates(obs[file]);
      }
      setGraphStyle(exp[file], mod.colors[file], 2, LineWidth, mod_gl, mod.ext_graph[file], 
		    mod.model+"_"+mod.labels[file], mod, debug);
      setGraphStyle(obs[file], mod.colors[file], 1, LineWidth, mod_gl, mod.ext_graph[file],
		    mod.model+"_"+mod.labels[file], mod, debug);
      //printExclGlu(obs[file], exp[file], mLSPs, mod.labels[file]);
      obs[file]->Draw("f same");

      TString obsname("obs"); obsname += imodel; obsname += file;
      obs[file]->SetName(obsname);
    } // Loop over curves in each model
    //// Plotting the lines on top of the fills
    if(mod.reverseOrder)
      for(size_t file(ncurves-1); file < ncurves; file--){
	if(exp[file])  exp[file]->Draw("same");
	obs[file]->Draw("same");
      }// Loop over curves in each model
    else
      for(size_t file(0); file < ncurves; file++){
	if(exp[file])  exp[file]->Draw("same");
	obs[file]->Draw("same");
      }// Loop over curves in each model

    /* if(mod.model.Contains("T2tt") && !mod.vsDM ){ // T2tt tweaks
      // Blocking out the top corridor at low LSP mass
      Float_t diagX[4] = {176.+25.,287.5,262.5,175.-24.};
      Float_t diagY[4] = {1,87.5,112.5,1};
      TGraph *gdiagonal = new TGraph(4, diagX, diagY);
      gdiagonal->SetName("MtopDiagonal");
      gdiagonal->SetFillColor(kGray);
      gdiagonal->SetLineColor(kBlack);
      gdiagonal->Draw("LFSAME");
      TLatex* tdiagonal = new TLatex(180+0.5, 180-172.5,"m_{#tilde{t}} = m_{t} + m_{#tilde{#chi}_{1}^{0}}");
      //tdiagonal->SetTextAngle(TMath::RadToDeg()*TMath::ATan(float(800)/float(500)));
      tdiagonal->SetTextAngle(48);
      tdiagonal->SetTextColor(kGray+4);
      tdiagonal->SetTextAlign(11);
      tdiagonal->SetTextSize(0.015);
      tdiagonal->Draw("SAME");
      } */

    // Drawing legends
    baseleg.Draw();
    obsleg.Draw();
    legX = lMargin+0.03; //legY = 1-tMargin-cmsH-0.035;
    legW = 0.13; 
    legH = legLineH * ncurvesleg * mod.legScale;
    TLegend limleg(legX, legY-legH, legX+legW, legY);
    limleg.SetTextSize(legTextSize * mod.legScale); limleg.SetFillColor(0); 
    limleg.SetFillStyle(0); limleg.SetBorderSize(0);
    for(size_t file(0); file < ncurves; file++)
      if(mod.labels[file] != "") limleg.AddEntry(obs[file]->GetName(), mod.labels[file], "fl");
    limleg.Draw();
    labMass.SetTextSize(legTextSize * mod.legScale * 1.2);
    labMass.DrawLatex(0.93, legY-legH-0.5*legLineH, mod.labMass);

    TString plotname(basefolder+"plots_pdf/"+mod.model+"_limits_summary_cms"+(!no_shade?"_shade":"")+".pdf");
    can.SaveAs(plotname);
    cout<<" open "<<plotname<<endl<<endl;
    can.SaveAs(plotname.ReplaceAll(".pdf",".root").ReplaceAll("_pdf", "_root"));
    // can.SaveAs(plotname.ReplaceAll(".root",".png").ReplaceAll("_root", "_png"));
  } // Loop over models
  cout<<endl<<endl;
}

void addLabelsTitle(float lMargin, float tMargin, float rMargin, TString title, TString lumi){
  TLatex label; label.SetNDC();  
  // Printing CMS Preliminary
  double offsetx(0.025), ycms(1-tMargin-0.075);
  label.SetTextAlign(11); label.SetTextFont(61); label.SetTextSize(0.75*tMargin);
  label.DrawLatex(lMargin+offsetx, ycms, "CMS");
  label.SetTextAlign(11); label.SetTextFont(52); label.SetTextSize(0.038);
  if(do_prelim) label.DrawLatex(0.27+offsetx, ycms, "Preliminary");

  // Printing top title
  label.SetTextAlign(21); label.SetTextFont(42); label.SetTextSize(0.56*tMargin);
  label.DrawLatex((1-rMargin-lMargin)/2.+lMargin-0.05, 1-tMargin+0.024, title);
  // Printing date
  label.SetTextAlign(31); label.SetTextFont(52); label.SetTextSize(0.45*tMargin);
  //  if(do_prelim) label.DrawLatex(1-rMargin-0.02, 1-tMargin+0.018, "Moriond 2017");
  label.DrawLatex(1-rMargin, 1-tMargin+0.018, "Moriond 2021");
  // Printing energy
  label.SetTextAlign(31); label.SetTextFont(42); label.SetTextSize(0.53*tMargin);
  if(lumi=="") lumi = "13 TeV";
  else lumi += " "+ifb+" (13 TeV)";
  label.DrawLatex(1-rMargin-0.04, ycms+0.005, lumi);
}

