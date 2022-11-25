Greetings!

Over the course of the winter of 2021 period, I have conducted research on expanding Helium stars with the help of the MESA tool. As a result, I have run a number of experiments, plotted many graphs, and have written and run many scripts to collect and collate data. Most of the experiment files, graphs, and scripts are available for your disposal and modification and are located in the (hopefully) intuitively named directories. The graphs and plots are in the graphs directory and have intuitive filenames for your examination, wheras the project resources are all located in the project folder. The project folder thus contains data files, models, programs, scripts, etc., that you can take a look at. Another file in this directory should be a quick guide on setting up MESA and getting running with other useful companion tools. The primary purpose of my investigations was mostly concerning tweaking configurations, parameters, and variables in MESA, to determine what could change in how MESA runs, with an objective of potentially determining a set of parameters and variables that would allow for, and perhaps explain, how to potentially arrive at an evolved Helium star with luminosity and effective temperature specified in paper1.pdf: 5.3 and 6800K respectively. Unfortunately, achieving this objective seemed somewhat out of reach, however a number of observations has been made:

-the default resolution for mesh, time, and varcontrol is sufficient for experimental purposes with MESA and does 
 not need to be refined. (here the resolution specifies how fine-grained calculations are)
-higher metallicity definitely leads to larger radii
-lower mixing length definitely leads to larger radii
-overshoot hardly affects the outcome
-the current cause of MESA crashes/terminations is unknown and somewhat challenging to determine, but could be a crucial factor in tweaking how it runs

Best Wishes.
