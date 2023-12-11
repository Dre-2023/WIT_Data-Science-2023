# WIT_Data-Science-2023


Data Science Individual Project on LA crime data:

I. **Introduction**
Working with records of crime has proven to be an engaging and thought-provoking endeavor. The intricacies of crime data in Los Angeles, a city constantly buzzing with myriad interactions, have captured my interest. The dataset at hand spans an extensive period, from January 8, 2020, to August 14, 2023, encompassing a staggering 779,803 records. This wealth of data holds the potential to unveil underlying patterns, offering valuable insights that can contribute to the well-being of the LA community. By deciphering these patterns, we aim to empower citizens and work towards fostering a safer and more secure environment for all residents. This project endeavors to harness the power of data science to not only understand but also positively impact the dynamics of crime in Los Angeles, ultimately striving for a better quality of life for its inhabitants.
II. **Problem Statement**
In this data science pursuit, my objective is to unravel the multifaceted landscape of crime in Los Angeles, with the aim of distilling valuable insights for the betterment of the community. The exploration kicks off by scrutinizing spatial patterns of stolen cars, specifically honing in on identifying neighborhoods or areas where car theft is most rampant. This inquiry arises from the recognition that car theft is already a prevalent crime, and discovering which areas it occurs most frequently adds an intriguing layer of complexity to the analysis. Moreover, I will delve into the gender distribution of victims in sexual assault crimes, seeking to unveil patterns that can guide targeted interventions and support services. An initial observation raised the question of whether the victims are predominantly young men, challenging the preconception that only young women are susceptible to such crimes. Extending the analysis, I will identify the least occurring crime in Los Angeles, casting light on areas where existing preventative measures may be effective or where resource reallocation could optimize impact. By addressing these three distinct questions, this project aspires to provide a nuanced understanding of crime dynamics, delivering insights crucial for the strategic endeavors of law enforcement, policymakers, and community initiatives, all aimed at fostering a safer and more secure environment in Los Angeles.
Thank you for providing additional details on the key variables used in the code. Here's a summary of the key variables based on the provided information:

1. **Date Rptd:**
   - **Description:** Represents the date when the crime was reported.
   - **Format:** MM/DD/YYYY
2. **AREA:**
   - **Description:** Represents the LAPD Geographic Area or Community Police Station responsible for the reported crime.
   - **Format:** Numeric values ranging from 1 to 21.
3. **Crm Cd:**
   - **Description:** Indicates the specific crime code, representing the type of crime committed.
   - **Format:** Numeric values.
4. **Vict Sex:**
   - **Description:** Indicates the gender of the victim.
   - **Possible Values:**
     - F: Female
     - M: Male
     - X: Unknown
5. **DayOfWeek:**
   - **Derived Feature:** Extracted from the 'Date Rptd' column, representing the day of the week.
6. **Month:**
   - **Derived Feature:** Extracted from the 'Date Rptd' column, representing the month.
7. **Year:**
   - **Derived Feature:** Extracted from the 'Date Rptd' column, representing the year.

These variables are used for feature engineering, model training, and evaluation in the provided machine learning code. 
IV. **Data Preparation**
   A. Data munging techniques for LA crime data
      1. Handling missing values
      2. Dealing with outliers
      3. Data cleaning and formatting specific to crime data
   B. Feature engineering for crime analysis
      1. Creating new features related to crime patterns
      2. Transforming existing features for better analysis

V. **Methodology**
### Data Munging Techniques:

1. **Handling Missing Values:**
   - The code utilizes `pd.to_datetime` with error handling (`errors='coerce'`) to convert the 'Date Rptd' column to datetime format, handling missing or erroneous date values.

2. **Dealing with Outliers:**
   - Outliers are not explicitly addressed in the provided code. Techniques like z-score analysis or IQR (Interquartile Range) could be applied to identify and handle outliers if deemed necessary for specific features.

3. **Data Cleaning and Formatting:**
   - The 'AREA' column is expected to contain categorical data representing LAPD Geographic Areas. The code could involve mapping these numeric values to corresponding area names for better interpretation.

### Feature Engineering for Crime Analysis:

1. **Creating New Features:**
   - The code extracts additional features from the 'Date Rptd' column:
     - 'DayOfWeek': Represents the day of the week.
     - 'Month': Represents the month.
     - 'Year': Represents the year.

2. **Transforming Existing Features:**
   - The 'Date Rptd' column is transformed into datetime format for better handling of temporal data.

### Additional Considerations:

- **Mapping AREA to Area Names:**
  - Depending on the dataset, mapping the numeric values in the 'AREA' column to corresponding area names, as mentioned in the code, enhances interpretability.

- **Handling Categorical Features:**
  - The 'Vict Sex' column is categorical, and the code could further encode it numerically for machine learning models.

**VII. Discussion**

A. **Interpretation of crime data analysis results:**
   The crime data analysis reveals compelling insights into the patterns of criminal activities in Los Angeles. Examining the spatial distribution of crimes across different areas exposes notable variations, with Area 12 having the highest total count (49,375) and Area 16 the lowest (26,152). Temporal trends suggest fluctuations in crime rates over the months and years, indicating potential seasonal influences.

B. **Insights gained regarding crime patterns in Los Angeles:**
   The analysis underscores specific crime patterns in Los Angeles. Notably, certain geographic areas, such as Area 12, exhibit higher crime rates, emphasizing the need for targeted law enforcement efforts in these regions. Exploring the gender-related distribution of crime victims reveals noteworthy patterns, with Crime Code 510 accounting for a significant percentage in multiple areas. Particularly, Area 13 stands out with the highest percentage of Crime Code 510 incidents, raising questions about the nature of these incidents in that specific location.

C. **Limitations of the study, considering the nature of crime data:**
   Despite the valuable insights gained, limitations persist. The study relies on reported crime data, potentially underestimating the actual crime rates. Variations in reporting practices and the presence of unreported incidents may introduce biases. Additionally, the analysis does not delve deeply into socio-economic factors, leaving potential influencers of crime unexplored.

D. **Suggestions for future work in addressing crime concerns:**
   Future research should consider a more comprehensive approach, incorporating socio-economic factors to understand the root causes of crime. Augmenting the analysis with external data sources could enhance predictive models. Implementing advanced machine learning techniques, particularly for predicting high-crime areas, may optimize resource allocation. Collaborative efforts with local communities and organizations can foster a more holistic understanding of crime patterns, leading to more effective prevention strategies.

Additionally, exploring advanced feature engineering techniques and comparing more columns could further refine predictive models and provide deeper insights into the dynamics of crime patterns in Los Angeles.
