#!/usr/bin/env python
# coding: utf-8

# In[1]:


### Import Packages ###
import pandas as pd
import itertools
import statsmodels.api as sm
import matplotlib.pyplot as plt

### Define Parameter Ranges to Test ###

# Note: higher numbers will result in code taking much longer to run
# Here we have it set to test p,d,q each = 0, 1 & 2

# Define the p, d and q parameters to take any value between 0 and 3 (exclusive)
p = d = q = range(0, 3)

# Generate all different combinations of p, d and q triplets
pdq = list(itertools.product(p, d, q))

# Generate all different combinations of seasonal p, q and q triplets
# Note: here we have 12 in the 's' position as we have monthly data
# You'll want to change this according to your time series' frequency
pdqs = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

### Run Grid Search ###
industriales = pd.read_csv('Industriales.csv', header=0, squeeze=True)

ts = industriales[['Dia', 'ConsumoDia']]
ts = ts.set_index('Dia')
ts.head(10)
print(pdq)
print(pdqs)


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
                mod = sm.tsa.statespace.SARIMAX(ts,  # this is your time series you will input
                                                order=comb,
                                                seasonal_order=combs,

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
    ans_df = ans_df.sort_values(by=['bic'], ascending=True)[0:5]
    return ans_df


### Apply function to your time series data ###

# Remember to change frequency to match your time series data
# resultado = sarimax_gridsearch(ts, pdq, pdqs, freq='MS')

# print(resultado)
# ------------------------------------------------------------------------------------------------------------------------


# In[ ]:


# de lo anterior cogeemos os parametros que esten en el compromiso de bajo BIC pero bajo error cuadratico

# Build SARIMAX model w/optimal parameters
train = ts.loc['2014-01-01':'2019-06-01']
test = ts.loc['2019-07-01':]
sarimax = sm.tsa.statespace.SARIMAX(train,
                                    order=(0, 2, 2),
                                    seasonal_order=(0, 2, 2, 12),
                                    enforce_stationarity=False,
                                    enforce_invertibility=False,
                                    freq='MS')

# Fit the model
pred = sarimax.fit()
forecast = pred.forecast(12)
forecastdf = forecast.to_frame()
forecastdf = forecastdf.reset_index()
forecastdf = forecastdf.rename(columns={"index": "Dia"})
forecastdf['Dia'] = pd.to_datetime(forecastdf['Dia'])

test = test.reset_index()
test ['Dia'] = pd.to_datetime(test['Dia'])
train = train.reset_index()
train ['Dia'] = pd.to_datetime(train['Dia'])
print(forecastdf)
print (train)
print(test)
print(type(forecastdf))
print(type(test))

plt.plot (train['Dia'],train['ConsumoDia'], label = 'Valores de entrenamiento')
plt.plot(test['Dia'],test['ConsumoDia'], label ='Valor real')
plt.plot(forecastdf['Dia'],forecastdf['predicted_mean'], label = 'Predicción')
plt.title(label='Consumo de agua en la ETSII')
plt.xlabel('Fecha')
plt.ylabel('Consumo')
plt.legend()
plt.show()
# lot diagnostics
# output.plot_diagnostics(figsize=(16,10))

# -----------------------------------


# Build Model
