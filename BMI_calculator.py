Weight=float(input("Enter persons weight: "))
Height=float(input("Enter persons Height: "))
while Weight != 0.0 or Height != 0.0 :
   BMI = Weight/Height ** 2
   if BMI < 18.5 :
       print('BMI= ',BMI ,'  therefore Underweight') 
   elif BMI >= 18 and BMI < 25 :
       print('BMI= ',BMI ,'   therefore Normal')
   else : 
       print('BMI= ', BMI, '  therefore Overweight') 
   Weight=float(input("Enter persons weight: "))
   Height=float(input("Enter persons height: "))


