def singleTaxCal(income1,income2):
    BasicAllowance = 132000
    MPF1 = min(income1 * 0.05,15000)
    MPF2 = min(income2 * 0.05,15000)
    chargeableincome1 = income1 - MPF1 - BasicAllowance
    chargeableincome2 = income2 - MPF2 - BasicAllowance
    tax = [900,3150,5400]
    if (chargeableincome1 <= 45000):
        tax1 = chargeableincome1 * 0.02
        payTax1 = tax1 - min(tax1 * 0.75,20000)
    elif (45001 <= chargeableincome1 <= 90000):
        tax1 = (chargeableincome1 - 45000) * 0.07 + tax[0]
        payTax1 = tax1 - min(tax1 * 0.75,20000)
    elif (90001 <= chargeableincome1 <= 135000):
        tax1 = (chargeableincome1 - 45000 * 2) * 0.12 + tax[0] + tax[1]
        payTax1 = tax1 - min(tax1 * 0.75,20000)
    elif (135001 <= chargeableincome1):
        tax1 = (chargeableincome1 - 45000 * 3) * 0.17 + tax[0]+ tax[1] + tax[2]
        payTax1 = tax1 - min(tax1 * 0.75,20000)

    if (chargeableincome2 <= 45000):
        tax2 = chargeableincome2 * 0.02
        payTax2 = tax2 - min(tax2 * 0.75,20000)
    elif (45001 <= chargeableincome2 <= 90000):
        tax2 = (chargeableincome2 - 45000) * 0.07 + tax[0]
        payTax2 = tax2 - min(tax2 * 0.75,20000)
    elif (90001 <= chargeableincome2 <= 135000):
        tax2 = (chargeableincome2 - 45000 * 2) * 0.12 + tax[0] + tax[1]
        payTax2 = tax2 - min(tax2 * 0.75,20000)
    elif (135001 <= chargeableincome2):
        tax2 = (chargeableincome2 - 45000 * 3) * 0.17 + tax[0]+ tax[1] + tax[2]
        payTax2 = tax2 - min(tax2 * 0.75,20000)

    return payTax1 + payTax2

def marriedCouple(income1,income2):
    MPF1 = min(income1 * 0.05,15000)
    MPF2 = min(income2 * 0.05,15000)
    chargeableincome = (income1 - MPF1) + (income2 - MPF2)

    if chargeableincome <= 264000:
            income_tax = 0
            return income_tax
    elif chargeableincome >= 264000:
            if chargeableincome in range(264001,309000):
                tax1 = 0
                tax2 = 0.02 * (chargeableincome - 264000)
                income_tax = tax1 + tax2
                income_tax = income_tax - (income_tax * 0.75)
                return income_tax
            elif chargeableincome in range(309001,354000):
                tax1 = 0
                tax2 = 900
                tax3 = 0.07 * (chargeableincome - 264000 - 45000)
                income_tax = tax1 + tax2 + tax3
                income_tax = income_tax - (income_tax * 0.75)
                return income_tax
            elif chargeableincome in range(354001,399000):
                tax1 = 0
                tax2 = 900
                tax3 = 3150
                tax4 = 0.12 * (chargeableincome - 264000 - 90000)
                income_tax = tax1 + tax2 + tax3 + tax4
                income_tax = income_tax - (income_tax * 0.75)
                return income_tax
            elif chargeableincome >= 399000:
                tax1 = 0
                tax2 = 900
                tax3 = 3150
                tax4 = 5400
                tax5 = 0.17 * (chargeableincome - 264000 - 135000)
                income_tax = tax1 + tax2 + tax3 + tax4 + tax5
                income_tax = income_tax - (income_tax * 0.75)
                return income_tax


#call main function
def main():
    income1 = float(input("Enter the Husband income: "))
    income2 = float(input("Enter the Wife income: "))
    print("Single tax = ", format(singleTaxCal(income1,income2),"7.2f"))
    print("Couple tax = ", format(marriedCouple(income1,income2),"7.2f"))

    if (singleTaxCal(income1,income2) > marriedCouple(income1,income2)):
        print("Choose Married Tax")
    else:
        print("Choose single tax")

#main function
main()

