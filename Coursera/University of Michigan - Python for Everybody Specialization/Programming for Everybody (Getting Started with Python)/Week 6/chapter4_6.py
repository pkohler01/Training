# 1. Write a program to prompt the user for hours and rate per hour using input
# to compute gross pay.
# 2. Pay should be the normal rate for hours up to 40 and time-and-a-half for
# the hourly rate for all hours worked above 40 hours.
# 3. Put the logic to do the computation of pay in a function called
# computepay() and use the function to do the computation.
# 4.The function should return a value.
# 5. Use 45 hours and a rate of 10.50 per hour to test the program.
# 6.  You should use input to read a string and float() to convert the string
# to a number.


def computepay(h, r):
    if h > 40:
        p = 1.5 * r * (h-40) + (40 *r)
    else:
        p = h * r
    return p

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Hourly Rate:")
r = float(rate)
p = computepay(h, r)
print("Pay", p)
