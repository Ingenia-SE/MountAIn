#!/usr/bin/env python
# coding: utf-8

# In[1]:



### Import Packages ###
import pandas as pd
import itertools
import statsmodels.api as sm

### Define Parameter Ranges to Test ###

# Note: higher numbers will result in code taking much longer to run
# Here we have it set to test p,d,q each = 0, 1 & 2

# Define the p, d and q parameters to take any value between 0 and 3 (exclusive)
p = d = q=  range(0,3)

# Generate all different combinations of p, d and q triplets
pdq = list(itertools.product(p, d, q))

# Generate all different combinations of seasonal p, q and q triplets
# Note: here we have 12 in the 's' position as we have monthly data
# You'll want to change this according to your time series' frequency
pdqs = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

### Run Grid Search ###
industriales = pd.read_csv('Industriales.csv', header=0, squeeze=True)


ts= industriales[['Dia', 'ConsumoDia']]
ts=ts.set_index('Dia')
ts.head(10)
print (pdq)
print (pdqs)


# In[ ]:



# Note: this code will take a while to run

# Define function
def sarimax_gridsearch(ts, pdq, pdqs, maxiter=50, freq='MS'):
    '''
    Input: 
        ts : your time series data
        pdq : ARIMA combinations from above
        pdqs : seasonal ARIMA combinations from above
        maxiter : number of iterations, increase if your model isn't converging
        frequency : default='M' for month. Change to suit your time series frequency
            e.g. 'D' for day, 'H' for hour, 'Y' for year. 
        
    Return:
        Prints out top 5 parameter combinations
        Returns dataframe of parameter combinations ranked by BIC
    '''

    # Run a grid search with pdq and seasonal pdq parameters and get the best BIC value
    ans = []
    for comb in pdq:
        for combs in pdqs:
            try:
                mod = sm.tsa.statespace.SARIMAX(ts, # this is your time series you will input
                                                order=comb,
                                                seasonal_order=combs,
                                                enforce_stationarity=False,
                                                enforce_invertibility=False,
                                                freq=freq)
               
                output = mod.fit(maxiter=maxiter) 
                ans.append([comb, combs, output.bic])
                print('SARIMAX {} x {}12 : BIC Calculated ={}'.format(comb, combs, output.bic))
            except:
                print('error')
                continue
            
    # Find the parameters with minimal BIC value

    # Convert into dataframe
    ans_df = pd.DataFrame(ans, columns=['pdq', 'pdqs', 'bic'])

    # Sort and return top 5 combinations
    ans_df = ans_df.sort_values(by=['bic'],ascending=True)[0:5]
    return ans_df
    
### Apply function to your time series data ###

# Remember to change frequency to match your time series data
resultado = sarimax_gridsearch(ts, pdq, pdqs, freq='MS')

print(resultado)
#------------------------------------------------------------------------------------------------------------------------


# In[ ]:


'''
#de lo anterior cogeemos os parametros que esten en el compromiso de bajo BIC pero bajo error cuadratico

# Build SARIMAX model w/optimal parameters
sarimax = sm.tsa.statespace.SARIMAX(ts, 
                                    order=(1,0,1), 
                                    seasonal_order=(1,1,1,12),
                                    enforce_stationarity=False, 
                                    enforce_invertibility=False,
                                    freq='MS')
                                    
# Fit the model
output = sarimax.fit()
    
# Print output summary
print(output.summary())

# Plot diagnostics
output.plot_diagnostics(figsize=(16,10));


#  
'''