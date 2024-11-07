n = 5000000

import pandas as pd

inputs= pd.read_csv("./dataset/inputs.csv")
outputs = pd.read_csv("./dataset/outputs.csv")
transactions = pd.read_csv("./dataset/transactions.csv")


transactionsN=transactions.loc[0:n-1]

txidN=transactionsN.loc[n-1].txid

inputsN=inputs.loc[inputs['txid']<=txidN]
outputsN=outputs.loc[outputs['txid']<=txidN]

transactionsN.to_csv(f'dataset{n}/transactions.csv',index=False)
outputsN.to_csv(f'dataset{n}/outputs.csv',index=False)
inputsN.to_csv(f'dataset{n}/inputs.csv',index=False)
print('creazione dataset ridotto terminata')