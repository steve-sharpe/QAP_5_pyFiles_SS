# This is a program to print a detailed report for monthly listings.
# Program author: Steve Sharpe
# Program date: Nov 30, 2023

# Import required libraries.

import datetime
import format_values as fv

# Define program constants.
today = datetime.datetime.now().strftime("%d-%b-%y")

f = open("./OSICDef.dat", "r")
NextPolNum = int(f.readline())
FirstCarPremium = float(f.readline())
AddCarDiscountRate = float(f.readline())
ExtraLiabilityRate = float(f.readline())
GlassCoveragreRate = float(f.readline())
LoanerCarOptionRate = float(f.readline())
HSTRate = float(f.readline())
MonthlyPayProcFee = float(f.readline())
f.close()

# Add user-defined functions.

# Start the main program.

print()
print("ONE STOP INSURANCE COMPANY")
print(f"MONTHLY LISTING AS OF {today}")
print()
print("POLICY CUSTOMER             TOTAL              TOTAL     DOWN      MONTHLY")
print("NUMBER NAME                PREMIUM      HST    COST     PAYMENT    PAYMENT")
print("==========================================================================")

# Open the policy file for reading.

# Initialize counters and accumulators.

NumOfPolicies = 0
TotalPremiumCostSum = 0
TotalHSTCostSum = 0
FinalTotalCostSum = 0
TotalDownPaymentCostSum = 0
TotalMonthlyPaymentCostSum = 0


f = open("./Policies.dat", "r")


for PolicyRecord in f:
    PolicyList = PolicyRecord.split(",")

    PolicyNum = int(PolicyList[0])
    CustFirstName = PolicyList[2].strip()
    CustLastName = PolicyList[3].strip()
    NumCars = int(PolicyList[9])
    Liablity = PolicyList[10].strip()
    Glass = PolicyList[11].strip()
    Loaner = PolicyList[12].strip()
    PayType = PolicyList[13].strip()
    Deposit = float(PolicyList[14])

    # Calculate the policy premium.
    if NumCars > 1:
        PremiumCost = (NumCars - 1) * (
            FirstCarPremium * AddCarDiscountRate
        ) + FirstCarPremium
    else:
        PremiumCost = FirstCarPremium

    ExtraCosts = 0

    if Liablity == "Y":
        ExtraCosts += ExtraLiabilityRate

    if Glass == "Y":
        ExtraCosts += GlassCoveragreRate

    if Loaner == "Y":
        ExtraCosts += LoanerCarOptionRate

    if PayType == "Monthly":
        ExtraCosts += MonthlyPayProcFee

    TotalPremium = PremiumCost + ExtraCosts
    HST = TotalPremium * HSTRate
    FinalTotalCost = TotalPremium + HST
    MonthlyPayments = (FinalTotalCost - Deposit) / 12

    if PayType == "Monthly" or PayType == "Down Pay":
        TotalPremiumCostSum += PremiumCost
        TotalHSTCostSum += HST
        FinalTotalCostSum += FinalTotalCost
        TotalDownPaymentCostSum += Deposit
        TotalMonthlyPaymentCostSum += MonthlyPayments

        # Print the policy listing.
        CustNameStr = CustFirstName + " " + CustLastName
        PremiumCost = fv.FDollar2(PremiumCost)
        TotalPremium = fv.FDollar2(TotalPremium)
        HST = fv.FDollar2(HST)
        FinalTotalCost = fv.FDollar2(FinalTotalCost)
        Deposit = fv.FDollar2(Deposit)
        MonthlyPayments = fv.FDollar2(MonthlyPayments)

        NextPolNum += 1
        NumOfPolicies += 1

        print(
            f"{PolicyNum:<4} {CustNameStr:<20} {TotalPremium:>9} {HST:>8} {FinalTotalCost:>9} {Deposit:>9} {MonthlyPayments:>9}  "
        )
    else:
        pass

print("==========================================================================")

# Print the policy summary.
TotalPremiumCostSum = fv.FDollar2(TotalPremiumCostSum)
TotalHSTCostSum = fv.FDollar2(TotalHSTCostSum)
FinalTotalCostSum = fv.FDollar2(FinalTotalCostSum)
TotalDownPaymentCostSum = fv.FDollar2(TotalDownPaymentCostSum)
TotalMonthlyPaymentCostSum = fv.FDollar2(TotalMonthlyPaymentCostSum)

print(
    f"Total policies: {NumOfPolicies:>3d}       {TotalPremiumCostSum:>9} {TotalHSTCostSum:>8} {FinalTotalCostSum:>9} {TotalDownPaymentCostSum:>9} {TotalMonthlyPaymentCostSum:>9}  "
)
print()

f.close()


# Complete any program housekeeping.
