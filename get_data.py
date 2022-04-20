import numpy as np
import pandas as pd

def prep_data(filepaths):
    dfs = [] #initialize a list of pd dataframes

    #go through each of the filepath strings and read the csv, then append to the dataframe
    for i in range(len(filepaths)):
        d = pd.read_csv(filepaths[i])
        dfs.append(d)

    df_out = dfs[0]#initializing the output dataframe with the arbitrary first dataframe
    name1 = df_out['Symbol'].iloc[0] #initializing the first name in the colnames list
    names = ['Date',f'Close_{name1}'] #adding Date to the colnames list

    for i in range(1,len(dfs)):
        name1,name2 = dfs[i-1]['Symbol'].iloc[0],dfs[i]['Symbol'].iloc[0]
        names.append(f'Close_{name2}')
        
        df_out = df_out.merge(dfs[i], how='outer', left_on='Date', right_on='Date',suffixes=(f'_{name1}', f'_{name2}'))

    df_out = df_out[names]
    df_out = df_out.set_index('Date',drop=True)
    
    return df_out.dropna()



if __name__ == '__main__':
    #set a to be the list of filenames to use
    a = ['/Users/manuelhanuch/Downloads/crypto_daily_data/coin_Bitcoin.csv'
    ,'/Users/manuelhanuch/Downloads/crypto_daily_data/coin_WrappedBitcoin.csv']
    name = 'btc_WrappedBtc'

    df = prep_data(a)
    df.to_csv(name)