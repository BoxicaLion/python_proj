#Home work 2

user_input=input("Please enter the charge for the food: \n")

price1=float(user_input)

tax_rate=0.07

tip=0.18

subtotal=price1

tax_amount=subtotal*tax_rate

tip_amount=subtotal*tip

total=subtotal+tax_amount+tip_amount



print("Subtotal:\t$",format(subtotal, "8,.2f"),sep='')
print("Tax(7.00%):\t$",format(tax_amount,"8.2f"),sep='')
print("Tip(18.00%):\t$",format(tip_amount,"8.2f"),sep='')
print('============','=========',sep='    ')
print("Total:\t\t$",format(total,"8.2f"),sep='')
