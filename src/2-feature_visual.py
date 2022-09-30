# Imports
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --------------------------------------------------------------------------- #
# Load data to visualize "data_clean_final_no_NaNs.csv"
vis_data_path = "../data/data_to_visualize.csv"
vis_data = pd.read_csv(vis_data_path)

# --------------------------------------------------------------------------- #
# Bar plots without STDDEV features
# Exclude rows that contian values with STDDEV
vis_data = vis_data[~vis_data.feature.str.contains('tddev')]

# Barplots
fig1, ax1 = plt.subplots(1, 1, figsize=(24, 12))
sns.barplot(data=vis_data[vis_data['category'] == 'spectral'], x='values', y='feature', hue='task')
ax1.set(xlim=(-110, 30), title="Distribution of spectral features", xlabel='', ylabel='')
plt.savefig("/Users/tobi/Projects/Uni/Msc/Lab_rotation/brain_var/results/spec_feat_barplot.png")

fig2, ax2 = plt.subplots(1, 1, figsize=(30, 8))
sns.barplot(data=vis_data[vis_data['category'] == 'frequency'], x='values', y='feature', hue='task')
ax2.set(xlim=(0, 2650), title="Distribution of frequency features", xlabel='', ylabel='')
plt.savefig("/Users/tobi/Projects/Uni/Msc/Lab_rotation/brain_var/results/freq_feat_barplot.png")

fig3, ax3 = plt.subplots(1, 1, figsize=(20, 6))
sns.barplot(data=vis_data[vis_data['category'] == 'amplitude'], x='values', y='feature', hue='task')
ax3.set(title="Distribution of amplitude features", xlabel='', ylabel='')
plt.savefig("/Users/tobi/Projects/Uni/Msc/Lab_rotation/brain_var/results/amp_feat_barplot.png")

fig4, ax4 = plt.subplots(1, 1, figsize=(20, 6))
sns.barplot(data=vis_data[vis_data['category'] == 'temporal'], x='values', y='feature', hue='task')
ax4.set(title="Distribution of temporal features", xlabel='', ylabel='')
plt.savefig("/Users/tobi/Projects/Uni/Msc/Lab_rotation/brain_var/results/temp_feat_barplot.png")
# plt.show()

# --------------------------------------------------------------------------- #
# Box plots of feature data per catgory in multi grid (each feature one plot)
# Spectral features
boxp1 = sns.FacetGrid(vis_data[vis_data['category'] == 'spectral'],
                     col="feature", col_wrap=9, xlim=(-210, 210))    # xlim chosen for readablility, hides some extreme outliers
boxp1.map(sns.boxplot, "values", "task", showmean=True)
boxp1.set_axis_labels('', '')
boxp1.set_titles(col_template="{col_name}")
boxp1.tight_layout()
boxp1.savefig("/Users/tobi/Projects/Uni/Msc/Lab_rotation/brain_var/results/spec_feat_boxplot.png")

# Frequency features
boxp2 = sns.FacetGrid(vis_data[vis_data['category'] == 'frequency'],
                     col="feature", col_wrap=6)     # xlim not usefull due to large scaling differences between features
boxp2.map(sns.boxplot, "values", "task", showmean=True)
boxp2.set_axis_labels('', '')
boxp2.set_titles(col_template="{col_name}")
boxp2.tight_layout()
boxp2.savefig("/Users/tobi/Projects/Uni/Msc/Lab_rotation/brain_var/results/freq_feat_boxplot.png")
# plt.show()    # currently manuall scaling is needed (further tweaking needed on layout)

# Amplitude features
boxp3 = sns.FacetGrid(vis_data[vis_data['category'] == 'amplitude'],
                     col="feature", col_wrap=5, xlim=(-60, 75))   # xlim chosen for readablility, hides some extreme outliers
boxp3.map(sns.boxplot, "values", "task", showmean=True)
boxp3.set_axis_labels('', '')
boxp3.set_titles(col_template="{col_name}")
boxp3.tight_layout()
boxp3.savefig("/Users/tobi/Projects/Uni/Msc/Lab_rotation/brain_var/results/amp_feat_boxplot.png")

# Temporal features
boxp4 = sns.FacetGrid(vis_data[vis_data['category'] == 'temporal'],
                     col='feature', col_wrap=4, xlim=(-55, 15), palette="light:#5A9")     # xlim chosen for readablility, hides some extreme outliers
boxp4.map(sns.boxplot, "values", "task", showmean=True)
boxp4.set_axis_labels('', '')
boxp4.set_titles(col_template="{col_name}")
boxp4.tight_layout()
boxp4.savefig("/Users/tobi/Projects/Uni/Msc/Lab_rotation/brain_var/results/temp_feat_boxplot.png")
