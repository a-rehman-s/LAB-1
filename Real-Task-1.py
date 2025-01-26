units = int(input("Enter units Consumed: "))

if units<=100:
    rate = 30
elif units>=101 and units<=300:
    rate = 40
else:
    rate = 60

meter_rate = 1500
tax = 200

Total = (rate*units) + meter_rate + tax
print("Total Bill : ", Total)