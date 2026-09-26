import decimal
from decimal import BasicContext, Decimal

decimal.setcontext(BasicContext)
with open("taskB1/inmap1.dat") as f:
    a, b = f.readline().split()
    a, b = int(a), Decimal(b)

    print("Timur Sivko")
    print("Simple Map Distance Computations")
    print()
    print(f"Map Scale Factor:      {b} miles per inch")
    print()
    print("       Map          Mileage")
    print("       Measure      Distance")
    print("========================================================================")

    total = 0
    for i in range(a):
        dist = Decimal(f.readline())
        print(f"#  {i + 1   }    {dist:<14}{round(dist * b, 1)}")
        total += dist * b

    print("========================================================================")
    print(f"Total Distance:       {total:.1f} miles")
