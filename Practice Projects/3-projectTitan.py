# Scenario:
# You have just been hired as the Lead Data Scientist for a high-profile Olympic athlete.
# Just weeks before the qualifiers, their expensive biometric smarwatch got damage during
# a heavy rainstorm. It started writing corrupted data to its internal CSV log.

# The athlete's coaching staff is panicking. They need to know the athlete's exact performance
# trends, but the data is littered with anomalies, missing values, and sensor ghosts. You must
# reconstruct the true physiological data, flag the sensor malfunctions, and engineer advanced
# metrics to clear them for the Olympic qualifiers.

# Phase 1: Temporal Recontruction (Time-Series Basics)
# The tracker's clock glitched, storing dates as messy strings and even dropping one entirely.

# 1. Strip and Cast: The Date column contains string literal quotes (e.g., '2020/12/01').
#    Clean these quotes and convert the column to actual Pandas datetime objects.

# 2. Chronological Imputation: There is exactly 1 missing date in the dataset (NaN). You are
#    not allowed to drop it. Find the missing row and deduce the correct date based on the
#    chronological sequence of the surrounding rows.

# 3. Set the index: Make the Date column the official index of the DataFrame so we can perform
#    time-series analysis later.

# Phase 2: Sensor Ghost & Outlier Detection (Statistical Cleaning)
# The heart rate and duration sensors picked up "ghost" signals. We need to find and fix them
# mathematically, not just by looking at them.

# 1. The IQR Method: Use the Interquartile Range (IQR) method to programmatically identify
#    outliers in the Duration column. (You should find at least one impossible workout
#    duration, like 450 minutes).

# 2. Contextual Replacement: Replace any Duration outliers with the median duration of all
#    other workouts that share a similar Pulse range (± 5 BPM).

# 3. Deduplication: The damaged sensor double-wrote some logs. Identify and remove any exact
#    duplicate rows in the dataset.

# Phase 3: Advanced Algoritchmic Imputation
# There are 2 missing values in the Calories column. A rookie would just fill this with the
# mean, but an Olympic athlete needs precision.

# 1. Correlation Check: Run a .corr() to see which variable (Duration, Pulse, or Maxpulse)
#    has the highest correlation with Calories.

# 2. Predictive Imputation: Instead of a simple mean, group the data by Duration. For the
#    rows with missing Calories, fill them in using the average Calories of other workouts
#    with the exact same Duration.

# Phase 4: Feature Engineering (Creating New Biometrics)
# The coaches need new metrics to understand the athlete's true effort levels.

# 1. Strain Index: Create a new column called Cardio_Strain. The formula is:
#    (Maxpulse - Pulse) / Duration.

# 2. Burn Rate: Create a new column called Calorie_Burn_Rate representing calories burned per
#    minute.

# 3. Categorical Binning: Create a new column called Workout_Type. Use pd.cut() to categorize
#    the workouts based on Pulse:
#    - < 100 = "Recovery"
#    - 100 - 115 = "Endurance"
#    - > 115 = "Anaerobic"

# Phase 5: Time-Series Smoothing (The Final Deliverable)
# The coaches don't want to see the jagged day-to-day noise; They want to see the underlying
# trend.

# 1. Rolling Averages: Create a new DataFrame called trend_df. Calculate a 3-day rolling mean
#    (moving average) for Pulse and Calories.

# 2. The Final Report: Find the day where the 3-day rolling average of calories peaked. This
#    was the athlete's hardest training block. What date was it?

# Tools to be used:
# pd.to_datetime(), df.shift(), df.quantile(), df.duplicated(), df.drop_duplicates(), df.corr(),
# df.groupby().transform(), pd.cut(), and df.rolling(window=3).mean()