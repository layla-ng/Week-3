"""
Created on Thu Jan 18 01:15:54 2024

@author: Layla Nguuyen - Seattle University - 24WQ - OMSBA 5270 02

Week 3 Assignment: Connection to public data through python API call

"""

# import modules
import requests
import pandas as pd

#create a request header
headers = {'User-Agent': "lnguyen24@seattleu.edu"}

# get all company data
companyTickers = requests.get("https://www.sec.gov/files/company_tickers.json" , headers=headers)

print(companyTickers.json())

print(companyTickers.json()['2024'])

print(companyTickers.json()['2024']['cik_str'])

companyCIK = pd.DataFrame.from_dict(companyTickers.json()['2024'], orient='index')


print(companyCIK)


companyCIK[0]= companyCIK[0].astype(str).str.zfill(10)

print(companyCIK)

cik = companyCIK[0:1]

print(cik)


#SEC filling API call
companyFilling = requests.get(f'http://data.sec.gov/submissions/CIK0001298946.json', headers=headers)

print(companyFilling.json().keys())



print(companyFilling.json()['filings'].keys())
allFillings = pd.DataFrame.from_dict(companyFilling.json()['filings']['recent'])

print(allFillings)

#print columns for cleaning up references 
print(allFillings.columns)

print(allFillings[['accessionNumber', 'reportDate', 'form']].head(50))


print(allFillings.iloc[17])


print(allFillings.iloc[77])








