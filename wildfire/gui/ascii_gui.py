def render_grid(list2d: list[list[int]]):
    line = "-" * (2 * len(list2d) + 1)
    print(line)
    for i in range(len(list2d)):
        row = "|"
        for j in range(len(list2d[i])):
            match list2d[i][j]:
                case 1:
                    row += " "
                case 2:
                    row += "O"
                case 3:
                    row += "T"
                case 4:
                    row += "F"
                case 5:
                    row += "C"
                case 6:
                    row += "A"
                case _:
                    row += "-"
            row += "|"
        print(row)
        print(line)
