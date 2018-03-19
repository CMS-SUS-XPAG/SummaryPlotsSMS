# SummaryPlotsSMS

Repository with the SUSY summary plots for the CMS experiment. For each conference folder (i.e., `2017_Moriond`), there are three internal folders:

  `input_root`: root files with individual graphs used to make the summary plots based on the code in `code`.

  `plots_pdf`: summary plots in .pdf format.

  `plots_root`: summary plots in .root files containing the TCanvas with each plot.
  
The plots are produced in the `code` folder by compiling the repository and running the executable, for instance:

    cd code
    ./compile.sh && ./run/plot_limits_summary.exe
