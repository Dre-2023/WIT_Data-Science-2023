#This is imporing Numpy and pandas while all but the data set into the var data 
import numpy as np
import pandas as pd
data = pd.read_csv('Crime_Data_from_2020_to_Present__.csv')

# Extract unique CRM codes from the 'Crm Cd' column of the 'data' DataFrame
crm_cds = np.unique(data['Crm Cd'])

# Extract all CRM codes from the 'Crm Cd' column and store them in 'cd_records'
cd_records = data['Crm Cd']

# Count the occurrences of each unique CRM code using NumPy's bincount
count_cds = np.bincount(cd_records)

# List of CRM codes related to specific genders
sex_cds = [121, 122, 810, 821, 822, 830, 840, 845, 860]

# Count the occurrences of each gender-related CRM code using the previously computed counts
sex_crm_occurrence = count_cds[sex_cds]

# Find the indices in the 'cd_records' array where the CRM codes match the specified gender-related CRM codes
sex_indices = np.where(np.isin(cd_records, sex_cds))[0]

# Print the total count of occurrences for the specified gender-related CRM codes
print("Total count of occurrences for specified gender-related CRM codes:", np.sum(sex_crm_occurrence))

# Display the indices in the 'cd_records' array where the gender-related CRM codes are found
sex_indices

# Extract the 'Vict Sex' column from 'data' based on indices where gender-related CRM codes occur
Vict_Sex = (data['Vict Sex'])[sex_indices]

# Print the count of occurrences of each gender in the 'Vict Sex' column for all gender-related CRM codes
print("Total count of occurrences for each gender:")
print(Vict_Sex.value_counts())

# Loop through each gender-related CRM code and print the count of occurrences for each gender
for i in range(len(sex_cds)):
    # Get the current gender-related CRM code
    current_crm_code = sex_cds[i]
    
    # Calculate the indices for the current gender-related CRM code
    indices = np.where(np.isin(cd_records, current_crm_code))[0]
    
    # Reshape the indices to match the number of occurrences for the current gender-related CRM code
    reshaped_indices = indices.reshape(np.sum(sex_crm_occurrence[i]))
    
    # Print the count of occurrences for the current gender-related CRM code along with the CRM code
    print(f"\nCount of occurrences for gender corresponding to CRM code {current_crm_code}:")
    print((data['Vict Sex'])[reshaped_indices].value_counts())
