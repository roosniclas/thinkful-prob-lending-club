import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData.dropna(inplace=True)

loansData.State.plot(kind = 'barh')

##loansData.boxplot(column = 'Amount.Requested', by='Loan.Purpose')

##loansData['funding_ratio'] = loansData['Amount.Funded.By.Investors'].astype('float16') / loansData['Amount.Requested'].astype('float16')

##loansData.hist(column='funding_ratio')
##plt.show()

##loansData.boxplot(column='Amount.Funded.By.Investors')
##plt.show()

##loansData.hist(column='Amount.Funded.By.Investors')
##loansData.hist(column='Amount.Requested')
##plt.show()

##plt.figure()
##graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
##graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
##plt.show()












