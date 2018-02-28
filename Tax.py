def singleTaxCal():
	BasicAllowance = 132000
	# Ask user enter the SingleIncome
	SingleIncome = float(input("Enter the taxable income: "))
	MPF = min(SingleIncome * 0.05,15000)
	print("SingleIncome = ",SingleIncome)
	print("MPF = ",MPF)

	# Cal the chargeableincome
	chargeableincome = SingleIncome - MPF - BasicAllowance
	print("chargeableincome is ",chargeableincome)
	
	# start cal the tax
	tax = [900,3150,5400]
	if (chargeableincome <= 45000):
		tax = chargeableincome * 0.02
		payTax = tax - min(tax * 0.7,20000)
		print("Tax is", format(payTax,"7.2f"))
		return payTax
	elif (45001 <= chargeableincome <= 90000):
		tax = (chargeableincome - 45000) * 0.07 + tax[0]
		payTax = tax - min(tax * 0.7,20000)
		print("Tax is", format(payTax,"7.2f"))
		return payTax
	elif (90001 <= chargeableincome <= 135000):
		tax = (chargeableincome - 45000 * 2) * 0.12 + tax[0] + tax[1]
		payTax = tax - min(tax * 0.7,20000)
		print("Tax is", format(payTax,"7.2f"))
		return payTax
	elif (135001 <= chargeableincome):
		tax = (chargeableincome - 45000 * 3) * 0.17 + tax[0]+ tax[1] + tax[2]
		payTax = tax - min(tax * 0.7,20000)
		print("Tax is", format(payTax,"7.2f"))
		return payTax

singleTaxCal()