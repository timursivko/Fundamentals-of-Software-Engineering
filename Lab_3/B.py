with open("B/5.ChaseData.txt") as f:
    n, m = map(int, f.readline().split())
    mouse = {"x": '?', "y": '?', "total": 0}
    cat = {"x": '?', "y": '?', "total": 0}
    animals = {"M": mouse, "C": cat}
    distance = ""
    msg = ""

    print("Cat and Mouse\n")
    print("  Cat        Mouse    Distance")
    print("------------------------------")

    while a := f.readline().split():
        command, *cords = a
        if cords:
            new_x, new_y = map(int, cords)

        if command == 'P':
            print(f"({cat['x']:>2}, {cat['y']:>2})     ({mouse['x']:>2}, {mouse['y']:>2}){distance:>7}")
        else:
            anim = animals[command]
            if anim['x'] != '?':
                anim['x'], anim['y'] = (new_x + anim['x']) % n, (new_y + anim['y']) % m
                anim['total'] += abs(new_x) + abs(new_y)

            else:
                anim['x'], anim['y'] = new_x, new_y

            if cat['x'] != '?' and mouse['x'] != '?':
                distance = abs(cat['x'] - mouse['x']) + abs(cat['y'] - mouse['y'])
                if distance == 0:
                    msg = f"Mouse caught at: ({cat['x']:>2},{cat['y']:>2})"
                    break

    else:
        msg = "Mouse evaded Cat"

    print("------------------------------\n\n")
    print("Distance   Mouse    Cat")
    print(f"{mouse['total']:>16} {cat['total']:>6}\n")

    print(msg)
