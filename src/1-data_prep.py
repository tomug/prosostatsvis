# Imports
import pandas as pd

# --------------------------------------------------------------------------- #
# Load initial data "clean_final_no_NaNs.csv"
data_path = "../data/clean_final_no_NaNs.csv"
data = pd.read_csv(data_path)

# Split data according to task groups (_x = book, _y = picture, noEnd = fiction)
data_dependent = data[data.columns[2:266]]  # DF mit allen erhobenen prosody variablen
data_independent = data[data.columns[266:269]]  # DF mit SEX, AGE, EDU

grp1 = data_dependent[[var for var in data_dependent.columns if "_x" in var]]
grp1.loc[:, "participant"] = grp1.index.values
grp1.loc[:, "task"] = "book"
grp1 = pd.concat([grp1, data_independent], axis=1)

grp2 = data_dependent[[var for var in data_dependent.columns if "_y" in var]]
grp2.loc[:, "participant"] = grp2.index.values
grp2.loc[:, "task"] = "pic"
grp2 = pd.concat([grp2, data_independent], axis=1)

grp3 = data_dependent[[var for var in data_dependent.columns if "_x" not in var and '_y' not in var]]
grp3.loc[:, "participant"] = grp3.index.values
grp3.loc[:, "task"] = "vac"
grp3 = pd.concat([grp3, data_independent], axis=1)

col_labels = grp3.columns
grp1.columns = col_labels
grp2.columns = col_labels
data = pd.concat([grp1, grp2, grp3], ignore_index=True)
data.to_csv('../data/data.csv')

# --------------------------------------------------------------------------- #
# Manually created category labels (taken from "data/prosodic feature_grouping.numbers")

# Spectrale Kategorie (43)
spec_label = [
            'spectralFlux_sma3_amean',
            'spectralFlux_sma3_stddevNorm',
            'spectralFluxV_sma3nz_amean',
            'spectralFluxV_sma3nz_stddevNorm',
            'spectralFluxUV_sma3nz_amean',
            'mfcc1_sma3_amean',
            'mfcc1_sma3_stddevNorm',
            'mfcc2_sma3_amean',
            'mfcc2_sma3_stddevNorm',
            'mfcc3_sma3_amean',
            'mfcc3_sma3_stddevNorm',
            'mfcc4_sma3_amean',
            'mfcc4_sma3_stddevNorm',
            'mfcc1V_sma3nz_amean',
            'mfcc1V_sma3nz_stddevNorm',
            'mfcc2V_sma3nz_amean',
            'mfcc2V_sma3nz_stddevNorm',
            'mfcc3V_sma3nz_amean',
            'mfcc3V_sma3nz_stddevNorm',
            'mfcc4V_sma3nz_amean',
            'mfcc4V_sma3nz_stddevNorm',
            'logRelF0-H1-H2_sma3nz_amean',
            'logRelF0-H1-H2_sma3nz_stddevNorm',
            'logRelF0-H1-A3_sma3nz_amean',
            'logRelF0-H1-A3_sma3nz_stddevNorm',
            'alphaRatioV_sma3nz_amean',
            'alphaRatioV_sma3nz_stddevNorm',
            'alphaRatioUV_sma3nz_amean',
            'hammarbergIndexV_sma3nz_amean',
            'hammarbergIndexV_sma3nz_stddevNorm',
            'hammarbergIndexUV_sma3nz_amean',
            'slopeV0-500_sma3nz_amean',
            'slopeV0-500_sma3nz_stddevNorm',
            'slopeV500-1500_sma3nz_amean',
            'slopeV500-1500_sma3nz_stddevNorm',
            'slopeUV0-500_sma3nz_amean',
            'slopeUV500-1500_sma3nz_amean',
            'F1amplitudeLogRelF0_sma3nz_amean',
            'F1amplitudeLogRelF0_sma3nz_stddevNorm',
            'F2amplitudeLogRelF0_sma3nz_amean',
            'F2amplitudeLogRelF0_sma3nz_stddevNorm',
            'F3amplitudeLogRelF0_sma3nz_amean',
            'F3amplitudeLogRelF0_sma3nz_stddevNorm'
            ]

# Frequency Kategorie (24)
freq_label = [
            'F0semitoneFrom27.5Hz_sma3nz_amean',
            'F0semitoneFrom27.5Hz_sma3nz_stddevNorm',
            'F0semitoneFrom27.5Hz_sma3nz_percentile20.0',
            'F0semitoneFrom27.5Hz_sma3nz_percentile50.0',
            'F0semitoneFrom27.5Hz_sma3nz_percentile80.0',
            'F0semitoneFrom27.5Hz_sma3nz_pctlrange0-2',
            'F0semitoneFrom27.5Hz_sma3nz_meanRisingSlope',
            'F0semitoneFrom27.5Hz_sma3nz_stddevRisingSlope',
            'F0semitoneFrom27.5Hz_sma3nz_meanFallingSlope',
            'F0semitoneFrom27.5Hz_sma3nz_stddevFallingSlope',
            'jitterLocal_sma3nz_amean',
            'jitterLocal_sma3nz_stddevNorm',
            'F1frequency_sma3nz_amean',
            'F1frequency_sma3nz_stddevNorm',
            'F1bandwidth_sma3nz_amean',
            'F1bandwidth_sma3nz_stddevNorm',
            'F2frequency_sma3nz_amean',
            'F2frequency_sma3nz_stddevNorm',
            'F2bandwidth_sma3nz_amean',
            'F2bandwidth_sma3nz_stddevNorm',
            'F3frequency_sma3nz_amean',
            'F3frequency_sma3nz_stddevNorm',
            'F3bandwidth_sma3nz_amean',
            'F3bandwidth_sma3nz_stddevNorm'
            ]

# Energy/Amplitude Kategorie (14)
amp_label = [
            'loudness_sma3_amean',
            'loudness_sma3_stddevNorm',
            'loudness_sma3_percentile20.0',
            'loudness_sma3_percentile50.0',
            'loudness_sma3_percentile80.0',
            'loudness_sma3_pctlrange0-2',
            'loudness_sma3_meanRisingSlope',
            'loudness_sma3_stddevRisingSlope',
            'loudness_sma3_meanFallingSlope',
            'loudness_sma3_stddevFallingSlope',
            'shimmerLocaldB_sma3nz_amean',
            'shimmerLocaldB_sma3nz_stddevNorm',
            'HNRdBACF_sma3nz_amean',
            'HNRdBACF_sma3nz_stddevNorm'
            ]

# temporal Kategorie (7)
temp_label = [
              'loudnessPeaksPerSec',
              'VoicedSegmentsPerSec',
              'MeanVoicedSegmentLengthSec',
              'StddevVoicedSegmentLengthSec',
              'MeanUnvoicedSegmentLength',
              'StddevUnvoicedSegmentLength',
              'equivalentSoundLevel_dBp'
              ]

# Save as dict for furture purposes
df = pd.DataFrame([spec_label, freq_label, amp_label, temp_label]).T
df.columns = ['spectral', 'frequency', 'amplitude', 'temporal']
df.to_csv('../data/category_labels.csv')

# --------------------------------------------------------------------------- #
# Data prep to visalize feature data

# Data preparation
# Kopiere die erstellten Gruppen von oben, damit sie ohne Probleme manipuliert werden können
grp1_all = grp1.copy()[grp1.columns[:88]]
grp2_all = grp2.copy()[grp2.columns[:88]]
grp3_all = grp3.copy()[grp3.columns[:88]]

# Setzte alle Feature Namen gleich
grp1_all.columns = grp3_all.columns
grp2_all.columns = grp3_all.columns

# Reshape DataFrame for visualizing (all values in one column)
grp1_all = pd.DataFrame(grp1_all.T.stack())
grp2_all = pd.DataFrame(grp2_all.T.stack())
grp3_all = pd.DataFrame(grp3_all.T.stack())

# Add task names for group identificaiton
grp1_all.loc[:, "task"] = "book"
grp2_all.loc[:, "task"] = "pic"
grp3_all.loc[:, "task"] = "vac"

# Get feature names from multiindex & add them in additional column
feat_label, _ = zip(*list(grp1_all.index))

grp1_all.loc[:, "feature"] = feat_label
grp2_all.loc[:, "feature"] = feat_label
grp3_all.loc[:, "feature"] = feat_label

# Add all groups to one DataFrame
vis_data = pd.concat([grp1_all, grp2_all, grp3_all], ignore_index=True)
vis_data.columns = ['values', 'task', 'feature']      # rename columns (mean ist hier vllt. unpassend)

# Add category labels
vis_data.loc[vis_data['feature'].isin(spec_label), 'category'] = 'spectral'
vis_data.loc[vis_data['feature'].isin(freq_label), 'category'] = 'frequency'
vis_data.loc[vis_data['feature'].isin(amp_label), 'category'] = 'amplitude'
vis_data.loc[vis_data['feature'].isin(temp_label), 'category'] = 'temporal'

# Export DF as .csv!!
vis_data.to_csv('../data/data_to_visualize.csv')
