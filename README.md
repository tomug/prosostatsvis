# prosostatsvis

This repo contains code generated during a 2 week lab rotaion in the INM-7's brain variability group.

The task was to visualise as well as investigate group differences in 88 prosodic features over three prosodic tasks:
1. Recounting TV/ Buch --> book
2. Picture description --> pic
3. Fictional story telling --> vac

## Script 1 
Takes the provided input and organises it for further steps.
* Input: DF containing feature and further group info (see data/Clean_final_noNaNs.csv).
* Output: DF for statistical analysis in long format (data/data.csv) and DF for visualisation with added feature category labels (data_to_visualize.csv)).

## Script 2 
Generates bar polts (or box plots) to visualise all features grouped by prosodic category (spectral, frequency, amplitude, temporal). If inclusion of STD is wanted, comment out line 14.
Caution: Plots are scaled by hand. Including additional variables might lead to a need of rescaling. Just play around with the numbers of each "figsize" until it looks right ;)
* Input: DF with added category labels (see script 1).
* Output: 4 barplots and/or box plots (one per feature category) of non-STDDEV features.

## Script 3 
Compares the three presodic task groups per feature by running repeated measures ANOVA for each feature. Significant main effects (uncorrected and greenhouse-geisser corrected p-values provided) are investigated using post-hoc paired t-tests (FDR-corrected). Only significant resutls are saved in output.
* Input: DF in long format (see script 1)
* Output: DF with significant post-hoc results
