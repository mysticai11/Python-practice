# bill= int(input("Amount: "))
# if bill >= 50000:
#     discount_amount30 = (30/ 100) * bill
#     discounted_price_30 = bill - discount_amount30
#     print(discount_amount30)
#     print(discounted_price_30)
#     # 25%
#     discount_amount25 = (25/ 100) * bill
#     discounted_price_25 = bill - discount_amount25
# elif bill >= 40000 or bill <= 49999:
#     discount_amount25 = (25/ 100) * bill
#     discounted_price_25 = bill - discount_amount25
#     formatted_number_discount="{:.2f}".format(discount_amount25)
#     formatted_number_price="{:.2f}".format(discounted_price_25)
#     print('Discount Amount: ' + formatted_number_discount)
#     print('Discounted Price: ' + formatted_number_price)

bill_amount=float(input("Enter bill amount = "))

if bill_amount>=50000:
  discount=30
elif bill_amount>=40000 and bill_amount<50000:
  discount=25
elif bill_amount>=30000 and bill_amount<40000:
  discount=20
elif bill_amount>=10000 and bill_amount<30000:
  discount=10
else:
  discount=0
print(f"you got{discount}% discount")
final_bill=bill_amount - (bill_amount*discount/100)
print(f"your final bill is {final_bill}")