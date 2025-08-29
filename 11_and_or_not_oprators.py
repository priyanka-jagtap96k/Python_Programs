"""and or not oprators

   and → All conditions must be True

   or → At least one condition must be True

   not → Reverses condition"""

#and Operator - Returns True if both conditions are True.

print("and Operator Example")
age = 25
city = "Pune"

if age > 18 and city == "Pune":
    print("Eligible")
else:
    print("Not Eligible")

# or Operator - Returns True if at least one condition is True.

print("or Operator Example")
age = 16
city = "Pune"

if age > 18 or city == "Pune":
    print("Allowed")
else:
    print("Not Allowed")


# not Operator - Reverses the result (True becomes False, False becomes True).

print("not Operator Example")
is_raining = False

if not is_raining:
    print("You can go outside")
else:
    print("Stay home")


print("and or Operator Example")
marks = 85
subject = "Math"

if marks >= 35 and (subject == "Math" or subject == "Science"):
    print("Pass in required subject")
else:
    print("Fail")
