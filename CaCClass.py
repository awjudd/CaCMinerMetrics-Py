#!/usr/bin/env python

class WalletLine(object):
    MinerID = ""
    PackageID = ""
    MinerType = ""
    Amount = int
    Date = ""
    Type = ""

    def __init__(self, MinerID, PackageID, MinerType, Amount, Date, Type):
        self.MinerID = MinerID
        self.PackageID = PackageID
        self.MinerType = MinerType
        self.Amount = Amount
        self.Date = Date
        self.Type = Type

class TwoMiners(object):
    Unpaid = ""
    TotalPaid = ""
    Last24hours = ""
    CurrentHashRate = ""
    AverageHashRate = ""

    def __init__(self, Unpaid, TotalPaid, Last24hours, CurrentHashRate, AverageHashRate):
        self.Unpaid = Unpaid
        self.TotalPaid = TotalPaid
        self.Last24hours = Last24hours
        self.CurrentHashRate = CurrentHashRate
        self.AverageHashRate = AverageHashRate

class MinerObject(object):
    MinerID = ""
    TotalPaid = ""

    def __init__(self, Unpaid, TotalPaid, Last24hours, CurrentHashRate, AverageHashRate):
        self.Unpaid = Unpaid
        self.TotalPaid = TotalPaid