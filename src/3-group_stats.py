# Imports
import pandas as pd
import pingouin as pg

# --------------------------------------------------------------------------- #
# Load data "data.csv"
data_path = "../data/data.csv"
ma_data = pd.read_csv(data_path)
ma_data = ma_data.drop(labels=ma_data.columns[0], axis=1)     # delete first column with old indecies

# --------------------------------------------------------------------------- #
# Group comparison (Task)

# Is there a significant difference in prosodic performance between prosodic tasks?
# Task 1: Nacherzählung TV/ Buch --> book
# Task 2: Picture description --> pic
# Task 3: fictional story telling --> vac

# Repeated measuers ANOVAs per feature with paired t-tests as post-hoc (FDR corrected)
results_df = pd.DataFrame()

for var in ma_data.columns[:-5]:
    # anova docs: https://pingouin-stats.org/generated/pingouin.rm_anova.html#pingouin.rm_anova
    anova = pg.rm_anova(data=ma_data,
                        dv=var,
                        within='task',
                        subject='participant',
                        correction=True,
                        detailed=True,
                        effsize='n2')
    # If significant main effect in ANOVA, collect only significant post-hoc comparisons
    if anova.loc[0, "p-GG-corr"] <= 0.05:           # looking at corrected p-values (set to "p-unc" for uncorrected p-values)
        #ttest docs: https://pingouin-stats.org/generated/pingouin.ttest.html#pingouin.ttest
        t_test = pg.pairwise_ttests(data=ma_data,
                                    dv=var,
                                    within='task',
                                    subject='participant',
                                    alpha=0.05,
                                    tail='two-sided',
                                    padjust='fdr_bh',
                                    effsize='cohen')
                                    #, return_desc=True)
        t_test.loc[:, 'var_name'] = var
        t_test = t_test[t_test.loc[:, "p-corr"] <= 0.05]

    results_df = pd.concat([results_df, t_test])

# Rearrange columns to bring name of feature to front of DF & save to .csv
results_df.insert(0, "var_name", results_df.pop("var_name"))
results_df.to_csv("../results/stats_results.csv")
