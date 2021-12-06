# FileName: QAP5
# One Stop Insurance Company
# Author: Mike Wadden
# Date: December 3, 2021

#Open Default File and read values into Variables
f = open('OSICDef.dat', 'r')

Policy_Count = int(f.readline().strip())
BASIC_PREMIUM_RATE = float(f.readline().strip())
EXTRA_CAR_DISCOUNT = float(f.readline().strip())
LIABILITY_RATE = float(f.readline().strip())
GLASS_RATE = float(f.readline().strip())
LOANER_RATE = float(f.readline().strip())
HST_RATE = float(f.readline().strip())
PROCESSING_FEE = float(f.readline().strip())
f.close()

# Imports
import datetime
import time



# #Functions

def As_Dollars(Number):
    """Format Dollars amounts to strings"""
    Number_Display = f"${Number:,.2f}"
    return Number_Display

def Monthly_Start(Today):
    """Function design for next month payments that start at the beginning of the month.
    If the date is > than the 25th of the month it skips to the next month.
    IE: 25th of December would have a First payment Feb 1st. Less than the 25th day would be Jan 1st"""

    Day = Today.day
    # Code is written to add so many days to get to next month then replaces that day with the first day of the month
    if Day >= 25:
        Next_Month = (Today + datetime.timedelta(days=45)).replace(day=1)
    elif Day < 25:
        Next_Month = (Today + datetime.timedelta(days=32)).replace(day=1)
    return Next_Month


def Name_Validation(Name):
    """ Function to Validate a Name for Input: Allowing Spaces, - and '"""
    for Char in Name:
        if ("A" <= Char <= "Z" or "a" <= Char <= "z" or Char == " "
                or Char == "-" or Char == "'"):
            continue
        else:
            return False
    return True


def As_Dollars_Pad(Number):
    """Format Dollars amounts to strings & Pad Right 10 Spaces"""
    Number_Display = f"${Number:,.2f}"
    Number_Display = f"{Number_Display:>10}"
    return Number_Display


def Format_Phone(Phone):
    """Function to Format a Phone Number into (999)-999 9999)"""
    Phone = str(Phone)
    return f"({Phone[0:3]}) {Phone[3:6]}-{Phone[6:10]}"

def Write(Variable, f):
    """Function to Convert None Strings to Strings and Format to write to file with ,"""
    import datetime
    if isinstance(Variable, str) == False:
        if isinstance(Variable, datetime.date) == True:
            return f.write(f"{Variable.strftime('%Y-%m-%d')},")
        else:
            Variable = round(Variable, 2)
            return f.write(f"{str(Variable)},")
    elif isinstance(Variable, str) == True:
        return f.write(f"{(Variable)},")


def Write_Space(Variable, f):
    """Function to Convert None Strings to Strings and Format to write to file with Space"""
    import datetime
    if isinstance(Variable, str) == False:
        if isinstance(Variable, datetime.date) == True:
            return f.write(f"{Variable.strftime('%Y-%m-%d')}\n")
        else:
            Variable = round(Variable, 2)
            return f.write(f"{str(Variable)}\n")
    elif isinstance(Variable, str) == True:
        return f.write(f"{(Variable)}\n")

# Province Info

P = {"Newfoundland Labrador: NL", "Prince Edward Island: PE", "Nova Scotia: NS", "New Brunswick: NB",
     "Quebec: QC", "Ontario: ON", "Manitoba: MB", "Saskatchewan: SK", "Alberta: AB",
     "British Columbia: BC", "Yukon: YT", "Northwest Territories: NT", "Nunavut: NU"}

Province_List = ["NL", "PE", "NS", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU"]


# Inputs & Validations
while True: #Loop To continue program or end
    print()
    print("      One Stop Insurance Company")
    print("New Insurance Policy Information System")
    print()
    print("Enter Customer Details")
    print()

    # Customer Details

    while True:
        Cus_First_Name = input("   First Name: ").title().strip()
        if Cus_First_Name == "":
            print()
            print("   First Name cannot be blank: Please Re-Enter")
            print()
        elif len(Cus_First_Name) > 15:
            print()
            print("   Invalid Last Name Length: Cannot be longer than 20 letters ")
            print()
        elif Name_Validation(Cus_First_Name) == False:  # Function to Validate Name Input
            print()
            print("   Invalid Name Entered: Please use letters between (a-z), (-) and (') ")
            print()
        else:
            break

    while True:
        Cus_Last_Name = input("   Last Name: ").title().strip()
        if Cus_Last_Name == "":
            print()
            print("  Last Name cannot be blank: Please Re-Enter")
            print()
        elif len(Cus_Last_Name) > 25:
            print()
            print("  Invalid Last Name Length: Cannot be longer than 25 letters ")
            print()
        elif Name_Validation(Cus_Last_Name) == False:                               #Function to Validate Name Input
            print()
            print("   Invalid Name Entered: Please use letters between (a-z), (-) and (') ")
            print()
        else:
            break

    while True:
        Street_Address = input("   Street Address: ").lstrip().rstrip().title()
        if Street_Address == "":
            print()
            print("   Street Address Input cannot be blank: ")
            print()
        elif len(Street_Address) > 35:
            print()
            print("   Invalid Entry Street Address Length: Cannot be longer than 35 characters ")
            print()
        else:
            break

    while True:
        City = input("   City: ").lstrip().rstrip()
        if City == "":
            print()
            print("   City Input cannot be blank: ")
            print()
        elif len(City) > 20:
            print()
            print("   Invalid Entry City Length: Cannot be longer than 20 characters ")
            print()
        else:
            break

    while True:
        Province = input("   Enter Two Digit Province Code: ").upper()
        if Province in Province_List:
            break
        else:
            print()
            print("   Invalid Entry: Please Enter Two Digit Province Code: ")
            print()
            for Code in P:
                print(" " * 2,Code)
            print()
    while True:
        Postal_Code = input("   Postal Code: ").upper().strip()
        if Postal_Code == "":
            print()
            print("   Postal Code Entry Cannot be Blank. Please Re-enter")
            print()
        elif (Postal_Code[0].isalpha() == True and Postal_Code[1].isdigit() == True and len(Postal_Code) == 6
                and Postal_Code[2].isalpha() == True and Postal_Code[3].isdigit() == True and Postal_Code[4].isalpha()
                and Postal_Code[5].isdigit() == True):
            break
        else:
            print()
            print("   Invalid Postal Code: Please Re-Enter (A1A1A1)")
            print()

    while True:
        Phone_Number = input("   Enter 10 Digit Phone Number: ").strip().replace("-", "")
        if Phone_Number.isdigit() == False:
            print()
            print("   Invalid Entry!: Enter 10 Digit Phone Number")
            print()
        elif len(Phone_Number) != 10:
            print()
            print("   Invalid Entry!: Enter 10 Digit Phone Number")
            print()
        else:
            break

    #Car Details

    print()
    print("Enter Vehicle Details")
    print()
    print(f"({int(EXTRA_CAR_DISCOUNT * 100)}% Discount for Additional Cars)")
    print()

    while True:
        try:
            Number_Of_Cars =  int(input("   Enter the number of cars on the policy "))
        except:
            print("   Invalid Entry: Enter the Numbers of cars on the policy")
        else:
            if Number_Of_Cars < 1:
                print("   Number of cars on the policy cannot be less than 1")
            elif Number_Of_Cars > 90:
                print("  Number of cars on the policy cannot be more than 90 without supervisor approval")
            else:
                break

    # Extra Policy Details

    print()
    print("Extra Policy Options")
    print()
    print("Enter (Y)-Yes to opt in OR (N)-No to opt out")
    print()

    while True:

        Liability = input("   Extra Liability (Y) or (N): ").upper().strip()

        if Liability == "Y":
            Liability_Total = LIABILITY_RATE * Number_Of_Cars
            Liability_Msg = "OPTED IN"
            break
        elif Liability == "N":
            Liability_Total = 0
            Liability_Msg = "OPTED OUT"
            break
        else:
            print("   Invalid Input: Please Enter (Y) for Yes or (N) for No: ")

    while True:
        Glass = input("   Extra Glass Coverage (Y) (N): ").upper()

        if Glass == "Y":
            Glass_Total = GLASS_RATE * Number_Of_Cars
            Glass_Msg = "OPTED IN"
            break
        elif Glass == "N":
            Glass_Total = 0
            Glass_Msg = "OPTED OUT"
            break
        else:
            print("  Invalid Input: Please Enter (Y) for Yes or (N) for No: ")

    while True:
        Loaner = input("   Loaner Car Option: (Y) or (N) ").upper()

        if Loaner == "Y":
            Loaner_Total = LOANER_RATE * Number_Of_Cars
            Loaner_Msg = "OPTED IN"
            break
        elif Loaner == "N":
            Loaner_Total = 0
            Loaner_Msg = "OPTED OUT"
            break
        else:
            print("  Invalid Input: Please Enter (Y) for Yes or (N) for No: ")

    # Insurance Calculations

    Discount_Rate = BASIC_PREMIUM_RATE * (1 - EXTRA_CAR_DISCOUNT)

    if Number_Of_Cars == 1:
        Basic_Premium = BASIC_PREMIUM_RATE
    else:
        # calculates the discount rate the -1 is to not include the first vehicle when adding up the discount.
        Basic_Premium = BASIC_PREMIUM_RATE + (Discount_Rate * (Number_Of_Cars - 1))
        Total_Discount = (BASIC_PREMIUM_RATE * EXTRA_CAR_DISCOUNT) * (Number_Of_Cars -1)

    Extra_Cost = Liability_Total + Glass_Total + Loaner_Total
    Premium_Total = Basic_Premium + Extra_Cost
    Hst = Premium_Total * HST_RATE
    Total = Premium_Total + Hst
    Policy_Date = datetime.datetime.now().date()
    First_Payment = Monthly_Start(Policy_Date)
    Policy_Number = f"{Policy_Count}-{Cus_First_Name[0]}{Cus_Last_Name[0]}"

    # Payment Options

    print()
    print("Payment Details")
    print()
    print(f"The Total Insurance Premium Cost is {As_Dollars(Total)}")
    print()
    print(f"Enter (F)-(Pay In Full) OR (M)-(Monthly Payments)-(Has a {As_Dollars(PROCESSING_FEE)} Processing Fee)")
    print()

    while True:
        Payment_Type = input("   Pay in Full or Monthly Payments (F)-(M) ").upper()

        if Payment_Type == "F":
            Payment_Msg = "Pay in Full"
            Monthly_Payment = 0
            First_Payment = ""
            break
        elif Payment_Type == "M":
            Payment_Msg = "Monthly Payments"
            Monthly_Payment = (Total + PROCESSING_FEE) / 12
            First_Payment = Monthly_Start(Policy_Date)
            break
        else:
            print("  Invalid Input: Please Enter (F) for Pay in Full or (M) for Monthly Payments: ")

    print()
    AnyKey = input("Press any key to Continue....")

    # Customer Receipt Output
    print()
    print(f"{' '* 26}One Stop Insurance ")
    print(f"{' '*26} Customer Receipt ")
    print()
    print(f"Policy Number: {Policy_Number:7}{' ' * 14} Policy Date: {Policy_Date.strftime('%Y-%m-%d'):>10}")
    print("~"* 60)
    print(f" Customer Details {' '* 23} {Format_Phone(Phone_Number)} (P)")
    print("-"* 60)
    print(f" {Cus_First_Name} {Cus_Last_Name:<25}")
    print(f" {Street_Address}")
    print(f" {City}, {Province:2} {Postal_Code[0:3]} {Postal_Code[3:6]}")
    print("~"* 60)
    print(f" Vehicle Details: Number of Vehicles on the Policy: {Number_Of_Cars}")
    print("~"* 60)
    print(" Extra Policy Options")
    print("-" * 60)
    print(f" Liability up to $1,000,000{'.' * 24}{Liability_Msg}")
    print(f" Glass Coverage{'.' * 36}{Glass_Msg}")
    print(f" Loaner Car Option{'.' * 33}{Loaner_Msg}")
    print("~"* 60)
    print("                 Insurance Premium Cost Details")
    print()
    print(" Description                                         Cost")
    print(" -----------                                      ---------- ")
    print(f" Basic Premium {' ' * 34} {As_Dollars_Pad(Basic_Premium)}")
    if Number_Of_Cars > 1:
        print(f" Total Discount {' ' * 33} {As_Dollars_Pad(Total_Discount)}")

    # This section make it so the extra cost only print on the invoice if they been selected
    if Liability == "Y" or Glass == "Y" or Loaner == "Y":
        print(f" Extra Options {' '* 34} ----------")
        if Liability == "Y":
            print(f" Liability up to $1,000,000 {' ' * 21} {As_Dollars_Pad(Liability_Total)} ")
        if Glass == "Y":
            print(f" Glass Coverage {' ' * 33} {As_Dollars_Pad(Glass_Total)} ")
        if Loaner == "Y":
            print(f" Loaner Car Option {' ' * 30} {As_Dollars_Pad(Loaner_Total)}")

    #Payment section for the Non Extra Cost Invoice
    print("~" * 60)
    print(f" Payment Option {' ' * 17} Premium Total   {As_Dollars_Pad(Premium_Total)}")
    print(f" ---------------- {' ' * 15} Hst ({int(HST_RATE * 100)}%)       {As_Dollars_Pad(Hst)}")
    print(f" {Payment_Msg:17} {' ' * 28}   {'-'* 10}")
    print(f"{' ' * 33} Total           {As_Dollars_Pad(Total)}")
    print("~" * 60)
    # output statement for if the user selected monthly payments
    if Payment_Type == "M":
        print(f" First Monthly Payment {' ' * 10 } Processing Fee  {As_Dollars_Pad(PROCESSING_FEE)}")
        print(f" Date {First_Payment.strftime('%B %d, %y')} {' '* 12} Monthly Payment {As_Dollars_Pad(Monthly_Payment)}")
        print("~" * 60)

    print()
    AnyKey = input("Press any key to Save Entry....")

    # Writing files to Rentals.dat
    f = open('Policies.dat', 'a')
    Write(Policy_Number, f)
    Write(Policy_Date, f)
    Write(Cus_First_Name, f)
    Write(Cus_Last_Name, f)
    Write(Street_Address, f)
    Write(City, f)
    Write(Province, f)
    Write(Postal_Code, f)
    Write(Phone_Number, f)
    Write(Number_Of_Cars, f)
    Write(Liability, f)
    Write(Glass, f)
    Write(Loaner, f)
    Write(Payment_Type, f)
    Write_Space(Total, f)
    f.close()

    print()
    print(f"{Policy_Number} has been saved")
    print()

    # Update Policy Counter
    Policy_Count += 1

    while True:  #Promts users to Continue or End
        Continue = input("Do you want to make another Entry?  (Y) or (N) ").upper()
        if Continue == "Y":
            break
        elif Continue == "N":
            print()
            break
        else:
            print("Incorrect Value entered, Please Enter Y or N")



    if Continue == "N":
        print()
        print("Closing New Insurance Policy Information System ", end="")
        for wait in range(1, 11):
            print('*', end=' ')
            time.sleep(.2)
        print()
        break

# Write Defaults back
f = open('OSICDef.dat', 'w')
Write_Space(Policy_Count, f)
Write_Space(BASIC_PREMIUM_RATE, f)
Write_Space(EXTRA_CAR_DISCOUNT, f)
Write_Space(LIABILITY_RATE, f)
Write_Space(GLASS_RATE, f)
Write_Space(LOANER_RATE, f)
Write_Space(HST_RATE, f)
Write_Space(PROCESSING_FEE, f)
f.close()



# Details Report
print()
AnyKey = input("Press any key to see Details Report....")

# This is the the (Detailed Report)
Today = datetime.datetime.now().date()
print()
print("ONE STOP INSURANCE COMPANY")
print(f"POLICY LISTINGS AS OF {Today.strftime('%d-%b-%y')}")
print()
print(f" POLICY  CUSTOMER               INSURANCE    EXTRA      TOTAL")
print(f" NUMBER  NAME                    PREMIUM     COSTS     PREMIUM")
print("=" * 63)


Policies_Acc = 0
Insurance_Acc = 0
Extra_Cost_Acc = 0
Total_Acc = 0

# Report Details
f = open("Policies.dat", "r")
for CustomerData in f:
    CustomerLine = CustomerData.split(",")
    Policy_Number = CustomerLine[0]
    Cus_First_Name = CustomerLine[2].strip()
    Cus_Last_Name = CustomerLine[3].strip()
    Number_Of_Cars = int(CustomerLine[9].strip())
    Liability = CustomerLine[10].strip()
    Glass = CustomerLine[11].strip()
    Loaner = CustomerLine[12].strip()
    Customer_Name = f"{Cus_First_Name} {Cus_Last_Name}"

    #Processing

    Discount_Rate = BASIC_PREMIUM_RATE * (1 - EXTRA_CAR_DISCOUNT)

    if Liability == "Y":
        Liability_Total = Number_Of_Cars * LIABILITY_RATE
    else:
        Liability_Total = 0

    if Glass == "Y":
        Glass_Total = Number_Of_Cars * GLASS_RATE
    else:
        Glass_Total = 0

    if Loaner == "Y":
        Loaner_Total = Number_Of_Cars * LOANER_RATE
    else:
        Loaner_Total = 0

    if Number_Of_Cars == 1:
        Basic_Premium = BASIC_PREMIUM_RATE
    else:
        # calculates the discount rate the -1 is to not include the first vehicle when adding up the discount.
        Basic_Premium = BASIC_PREMIUM_RATE + (Discount_Rate * (Number_Of_Cars - 1))
        Total_Discount = (BASIC_PREMIUM_RATE * EXTRA_CAR_DISCOUNT) * (Number_Of_Cars - 1)

    Extra_Cost = Liability_Total + Glass_Total + Loaner_Total
    Premium_Total = Basic_Premium + Extra_Cost
    Hst = Premium_Total * HST_RATE

    # Accumlators to calculate totals
    Policies_Acc += 1
    Insurance_Acc += Basic_Premium
    Extra_Cost_Acc += Extra_Cost
    Total_Acc += Premium_Total
    print(f"{Policy_Number:7}  {Customer_Name:<20}  {As_Dollars_Pad(Basic_Premium)} "
          f"{As_Dollars_Pad(Extra_Cost)} {As_Dollars_Pad(Premium_Total)}")
f.close()
print("=" * 63)
print(f"Total Policies: {Policies_Acc:3}{' ' * 11} {As_Dollars_Pad(Insurance_Acc)}"
      f" {As_Dollars_Pad(Extra_Cost_Acc)} {As_Dollars_Pad(Total_Acc)}")

# Details Report
print()
AnyKey = input("Press any key to see Exception Report....")

# This report show customers paying monthly only

# This is the the (Exception Report)
Today = datetime.datetime.now().date()
print("ONE STOP INSURANCE COMPANY")
print(f"POLICY LISTINGS AS OF {Today.strftime('%d-%b-%y')}")
print()
print(f" POLICY  CUSTOMER                TOTAL                 TOTAL      MONTHLY")
print(f" NUMBER  NAME                   PREMIUM       HST      COST       PAYMENT")
print("=" * 73)

# set Accumulators back to 0
Policies_Acc = 0
Premium_Acc = 0
Total_Acc = 0
Monthly_Acc = 0
Hst_Acc = 0

# Report Details
f = open("Policies.dat", "r")
for CustomerData in f:
    CustomerLine = CustomerData.split(",")
    Policy_Number = CustomerLine[0]
    Cus_First_Name = CustomerLine[2].strip()
    Cus_Last_Name = CustomerLine[3].strip()
    Number_Of_Cars = int(CustomerLine[9].strip())
    Liability = CustomerLine[10].strip()
    Glass = CustomerLine[11].strip()
    Loaner = CustomerLine[12].strip()
    Payment_Type = CustomerLine[13].strip()
    Total = float(CustomerLine[14].strip())
    Customer_Name = f"{Cus_First_Name} {Cus_Last_Name}"

    #Processing

    Discount_Rate = BASIC_PREMIUM_RATE * (1 - EXTRA_CAR_DISCOUNT)

    if Liability == "Y":
        Liability_Total = Number_Of_Cars * LIABILITY_RATE
    else:
        Liability_Total = 0

    if Glass == "Y":
        Glass_Total = Number_Of_Cars * GLASS_RATE
    else:
        Glass_Total = 0

    if Loaner == "Y":
        Loaner_Total = Number_Of_Cars * LOANER_RATE
    else:
        Loaner_Total = 0

    if Number_Of_Cars == 1:
        Basic_Premium = BASIC_PREMIUM_RATE
    else:
        # calculates the discount rate the -1 is to not include the first vehicle when adding up the discount.
        Basic_Premium = BASIC_PREMIUM_RATE + (Discount_Rate * (Number_Of_Cars - 1))
        Total_Discount = (BASIC_PREMIUM_RATE * EXTRA_CAR_DISCOUNT) * (Number_Of_Cars - 1)


    Extra_Cost = Liability_Total + Glass_Total + Loaner_Total
    Premium_Total = Basic_Premium + Extra_Cost
    Hst = Premium_Total * HST_RATE

    if Payment_Type == "M":
        # Accumlators to calculate totals
        Policies_Acc += 1
        Hst_Acc += Hst
        Premium_Acc += Basic_Premium
        Total_Acc += Total
        # we have Total information from the file so no need to write again
        Monthly_Payment = (Total + PROCESSING_FEE) / 12
        Monthly_Acc += Monthly_Payment
        print(f"{Policy_Number:7}  {Customer_Name:<20}  {As_Dollars_Pad(Premium_Total)} {As_Dollars_Pad(Hst)}"
              f" {As_Dollars_Pad(Total)} {As_Dollars_Pad(Monthly_Payment)}")

f.close()
print("=" * 73)
print(f"Total Policies: {Policies_Acc:3}{' ' * 11} {As_Dollars_Pad(Premium_Acc)} {As_Dollars_Pad(Hst_Acc)}"
      f" {As_Dollars_Pad(Total_Acc)} {As_Dollars_Pad(Monthly_Acc)}")
