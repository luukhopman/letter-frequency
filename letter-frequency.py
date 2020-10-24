import string
from collections import Counter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.corpus import words

nltk.download('words')

# Create counter with starting letters
letters = Counter(l.lower() for word in words.words()
                  for l in word if l in string.ascii_letters)

# Configure plot
plt.figure(figsize=(16, 6))
sns.set_style('whitegrid')

# Create DataFrame
df = pd.DataFrame({'letter': list(letters.keys()),
                   'count': list(letters.values())})
df.sort_values('letter', inplace=True)
vowels = ['a', 'e', 'i', 'o', 'u']
df['vowel'] = np.where(df['letter'].isin(vowels), True, False)

# Plot data
ax = sns.barplot(x='letter', y='count', hue='vowel', data=df, dodge=False)

# Set titles and lables
ax.set_title('Letters in English words', fontsize=20, fontweight='bold')
ax.set_xlabel('Letter', fontweight='bold')
ax.set_ylabel('Frequency', fontweight='bold')

# Add annotation
ax.annotate('\'j\' is the least used letter\nin the English language',
            fontweight='light', fontsize=12, color='#303030', style='italic',
            xy=(9, 0.20), xycoords='data',
            xytext=(11, 210000), textcoords='data',
            arrowprops=dict(facecolor='#454545', shrink=0.05,
                            connectionstyle='angle3, angleA=0, angleB=90'),
            )

# Hide legend and show plot
plt.legend('', frameon=False)
plt.savefig('letter-frequency.png', dpi=600, bbox_inches='tight')
plt.show()
