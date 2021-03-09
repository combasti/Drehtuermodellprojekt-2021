x = input ("Bitte Zahl angeben")

prim = True

if x < 2:
    prim = False
elif x > 2:
    Y = range(1+1,x)    
    for y in Y:
        if (x % y) == 0:
            prim = False

if prim == True:
    print x, "ist eine Primzahl"
else:
    print x, "ist keine Primzahl"