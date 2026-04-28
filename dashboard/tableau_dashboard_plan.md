# Tableau Dashboard Plan

## Dashboard Goal

Show which diabetic patient segments are most likely to be readmitted within 30 days and what operational actions hospitals should prioritize.

## Recommended Dashboard Pages

### 1. Executive Overview

- KPI card: total encounters
- KPI card: 30-day readmission rate
- KPI card: average time in hospital
- donut or bar chart for readmission classes
- short insight text box

### 2. Readmission Drivers

- bar chart: readmission rate by age group
- bar chart: readmission rate by admission type
- bar chart: readmission rate by prior inpatient group
- bar chart: readmission rate by prior emergency group
- heatmap or grouped bar: insulin status vs readmission

### 3. Action Dashboard

- highlight top high-risk segments
- compare average length of stay for readmitted vs non-readmitted
- recommendation panel with 3 to 5 actions

## KPI Definitions

- `30-day readmission rate` = percent of records where `readmitted_30 = 1`
- `average length of stay` = mean of `time_in_hospital`
- `high-risk segment` = subgroup with above-average 30-day readmission rate

## Suggested Filters

- age group
- gender
- race
- admission type
- insulin status

## Storyline

1. Readmission is not evenly distributed
2. Prior utilization is one of the strongest warning signs
3. Hospitals can act on these segments with targeted discharge support
