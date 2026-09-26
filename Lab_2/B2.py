import decimal
from decimal import BasicContext, Decimal

decimal.setcontext(BasicContext)

A = Decimal("35.74")
B = Decimal("0.6125")
C = Decimal("0.4275")
D_val = Decimal("35.75")
E = Decimal("0.16")

with open("taskB2/1.WCData.txt") as f:
    f.readline(), f.readline() # заглушка

    print("Time     WC temp     WC Effect")
    print("------------------------------")

    temp_list = []
    while a := f.readline().split():
        time, t, v= a[0], Decimal(a[1]), Decimal(a[2])

        result = A + B * t + (C * t - D_val) * Decimal(v) ** E
        temp_list.append(result)
        print(f"{time}{round(result, 1):>8}{round(result - t, 1):>14}")

    print("------------------------------")
    print()
    print(f"The average adjusted temperature, based on {len(temp_list)} observations, was {round(sum(temp_list) / len(temp_list), 1)}")
