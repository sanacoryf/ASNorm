# libraries and data
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
df=pd.DataFrame({'xvalues': range(1,101), 'yvalues': np.random.randn(100) })
 
# plot
plt.plot( 'xvalues', 'yvalues', data=df)
plt.show()
