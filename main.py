#!/usr/bin/env python
import MinerFunctions as MF
import CaCClass
import json
from datetime import datetime
from os import path

with open("config.json") as config_file:
    config = json.load(config_file)

WalletInfo = MF.GetWalletInfoCaCPanel()
UniqueMinersArray = MF.UniqueMinerNumbers(WalletInfo)
MinerAmounts = []
TotalCaCBitcoinEarned = 0
for miner in UniqueMinersArray:
    MinerSum = MF.SummaryCaCMinerInfo(miner,WalletInfo)
    TotalCaCBitcoinEarned += float(MinerSum)
    MinerValue = MF.GetBTCValue(MinerSum)
    tempObj = (miner,MinerSum,MinerValue)
    MinerAmounts.append(tempObj)

TotalCaCBitcoinEarnedUSD = MF.GetBTCValue(TotalCaCBitcoinEarned)


if (config['credentials']['printoutputs']) == 'true':
    for row in MinerAmounts:
        print("Miner ID:",row[0])
        print("Total Bitcoin Earned:",row[1])
        print("Current Value USD(Real Value):",row[2])
        print("")

    print("Total Combined Value BTC:",TotalCaCBitcoinEarned)
    print("Total Combined Value USD:",TotalCaCBitcoinEarnedUSD)


if (config['cloudatcockscredentials']['enabled']) == 'true':
    MF.PostToCloudatCocksSite()
    if (config['scriptrunlogging']['enabled']) == 'true':
        FileLocation = (config['scriptrunlogging']['logfilelocation'])
        if path.exists(FileLocation) == False:
            f= open(FileLocation,'w+')
            f.close()
        with open((FileLocation), 'a') as file:
            now = datetime.now()
            date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
            str_TotalCaCBitcoinEarned=str(TotalCaCBitcoinEarned)
            OutputString = "Script ran at: "+date_time+" Ran Post to CloudAtCocks Site"'\n'
            file.write(OutputString)
            file.close()

if (config['scriptrunlogging']['enabled']) == 'true':
    FileLocation = (config['scriptrunlogging']['logfilelocation'])
    if path.exists(FileLocation) == False:
        f= open(FileLocation,'w+')
        f.close()
    with open((FileLocation), 'a') as file:
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        str_TotalCaCBitcoinEarned=str(TotalCaCBitcoinEarned)
        OutputString = "Script ran at: "+date_time+" Total Bitcoin Earned: "+ str_TotalCaCBitcoinEarned+'\n'
        file.write(OutputString)
        file.close()