# This is a program to print a detailed report for policy listings.
# Program author: Steve Sharpe
# Program date: NOv 30, 2023

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
print(f"POLICY LISTING AS OF {today}")
print()
print("POLICY CUSTOMER                POLICY     INSURANCE     EXTRA       TOTAL ")
print("NUMBER NAME                     DATE       PREMIUM      COSTS      PREMIUM")
print("==========================================================================")

# Open the policy file for reading.

# Initialize counters and accumulators.

NumOfPolicies = 0
TotalPremiumCost = 0
TotalExtraCosts = 0
FinalTotalPremium = 0

f = open("./Policies.dat", "r")


for PolicyRecord in f:
    PolicyList = PolicyRecord.split(",")

    PolicyNum = int(PolicyList[0])
    PolicyDate = PolicyList[1].strip()
    PolicyDate = datetime.datetime.strptime(PolicyDate, "%Y-%m-%d")
    PolicyDate = PolicyDate.strftime("%Y-%m-%d")
    CustFirstName = PolicyList[2].strip()
    CustLastName = PolicyList[3].strip()
    StrAddress = PolicyList[4].strip()
    City = PolicyList[5].strip()
    Province = PolicyList[6].strip()
    PostalCode = PolicyList[7].strip()
    PhoneNum = PolicyList[8].strip()
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

    if PayType == "Monthly" or PayType == "Down Pay":
        ExtraCosts += MonthlyPayProcFee

    TotalPremium = PremiumCost + ExtraCosts

    TotalPremiumCost += PremiumCost
    TotalExtraCosts += ExtraCosts
    FinalTotalPremium += TotalPremium

    # Print the policy listing.
    CustNameStr = CustFirstName + " " + CustLastName
    PremiumCost = fv.FDollar2(PremiumCost)
    ExtraCosts = fv.FDollar2(ExtraCosts)
    TotalPremium = fv.FDollar2(TotalPremium)
    NextPolNum += 1
    NumOfPolicies += 1

    print(
        f" {PolicyNum:<4}  {CustNameStr:<20}   {PolicyDate:10}  {PremiumCost:>9}  {ExtraCosts:>9}   {TotalPremium:>9}  "
    )
print("==========================================================================")

# Print the policy summary.
TotalPremiumCost = fv.FDollar2(TotalPremiumCost)
TotalExtraCosts = fv.FDollar2(TotalExtraCosts)
FinalTotalPremium = fv.FDollar2(FinalTotalPremium)

print(
    f"Total policies: {NumOfPolicies:>3}                      {TotalPremiumCost:>9}  {TotalExtraCosts:>9}  {FinalTotalPremium:>9}"
)

print()


f.close()


# Complete any program housekeeping.
