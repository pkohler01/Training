hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Hourly Rate:")
rr = float(rate)
oh = h - 40
rh = 40
otr = rr * 1.5

if h < 41:
    print(h * rr)
elif h > 40:
    rp = rh * rr
    op = oh * otr
    print (rp + op)
