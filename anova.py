import pandas as pd
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Read the data from Excel files
data_sample1 = pd.read_excel("sample1.xlsx")
data_sample2 = pd.read_excel("sample2.xlsx")

# Combine the data from both samples
data = pd.concat([data_sample1, data_sample2])

# Rename the column "OVERALL ACCEPTABILITY" to "ACCEPTABILITY"
data.rename(columns={"OVERALL ACCEPTABILITY": "ACCEPTABILITY"}, inplace=True)

# Perform ANOVA regression
model = sm.OLS.from_formula('ACCEPTABILITY ~ COLOUR + FLAVOUR + TEXTURE + TASTE + APPEARANCE', data=data).fit()
anova_table = sm.stats.anova_lm(model)

# Create a PDF file to save the results and graphs
pdf = PdfPages('anova_results.pdf')

# Save the ANOVA table and explanation to the PDF file
with open('anova_results.txt', 'w') as f:
    f.write(str(anova_table))
    f.write('\n\n')

    # Explanation of the ANOVA results
    f.write("Explanation of the ANOVA Results:\n")
    f.write("=================================\n\n")
    f.write("The ANOVA table provides information about the statistical significance of each independent variable (COLOUR, FLAVOUR, TEXTURE, TASTE, and APPEARANCE) in relation to the ACCEPTABILITY of the food samples.\n\n")
    f.write("The 'F' column represents the F-statistic, which is a measure of the variation between groups relative to the variation within groups. A larger F-value indicates a more significant effect.\n")
    f.write("The 'PR(>F)' column represents the p-value, which indicates the probability of observing a result as extreme as the one obtained if the null hypothesis is true. A smaller p-value indicates a more significant effect.\n")
    f.write("If the p-value is below a certain significance level (e.g., 0.05), it suggests that the independent variable has a statistically significant effect on ACCEPTABILITY.\n\n")

# Plot boxplots for each independent variable
fig, axes = plt.subplots(1, 5, figsize=(15, 4))
sns.boxplot(x='COLOUR', y='ACCEPTABILITY', data=data, ax=axes[0])
sns.boxplot(x='FLAVOUR', y='ACCEPTABILITY', data=data, ax=axes[1])
sns.boxplot(x='TEXTURE', y='ACCEPTABILITY', data=data, ax=axes[2])
sns.boxplot(x='TASTE', y='ACCEPTABILITY', data=data, ax=axes[3])
sns.boxplot(x='APPEARANCE', y='ACCEPTABILITY', data=data, ax=axes[4])
plt.tight_layout()
pdf.savefig()
plt.close()

# Plot mean plots for each independent variable
columns = ['COLOUR', 'FLAVOUR', 'TEXTURE', 'TASTE', 'APPEARANCE']
for column in columns:
    plt.figure(figsize=(10, 6))
    sns.barplot(x=column, y='ACCEPTABILITY', data=data)
    plt.xlabel(column)
    plt.ylabel('Mean Acceptability')
    plt.title(f'Mean Acceptability by {column}')
    pdf.savefig()
    plt.close()

# Save and close the PDF file
pdf.close()

