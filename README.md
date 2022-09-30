# prosostatsvis

This Repo contains code generated during a 2 week lab rotaion in the INM-7's brain variability group.

The task was to visualise as well as investigate group differences in 88 prosodic features over three prosodic tasks:
1. Nacherzählung TV/ Buch --> book
2. Picture description --> pic
3. fictional story telling --> vac

# Script 1 
is taking the provided input and organises it for further steps.

Input: DF containing feature and further group info
Output: DF for statistical analysis (long format) and DF for visualisation (added category labels)

# Script 2 
generates bar polts (or box plots) to visualise all features grouped by prosodic category (spectral, frequency, amplitude, temporal). If inclusion of STD is wanted, comment out line xx to xx and run the ploting. Caution: Plots are scaled by hand so including addiitonal variables might lead to a need of rescaling. Just play around with the numbers of each "figsize" until it looks right ;)

Input: DF with added category labels (see script 1)
Output: 4 barplots and box plots (one per prosodic category) of non STDDEV features  

# Script 3 
compares the 3 task groups per feature by running repeated measures ANOVA for each feature. Significant main effects (uncorrected and greenhouse-geisser corrected p-values provided) are investigated using post-hoc paired t-tests (FDR-corrected). Only significant resutls are saved in output.

Input: DF in long format (see script 1)
Output: Table with significant post-hoc results
