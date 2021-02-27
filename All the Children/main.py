def solve ():
    total = 0
    product = 17280
    sum_a = 40
    sum_b = 32

    for w in range(sum_a):
        for x in range(sum_a):
            for y in range(sum_a):
                for z in range(sum_b):
                    a = w + 1
                    b = x + 1
                    c = y + 1
                    d = z + 1

                    ages = [a, b, c, d]
                    ages.sort()

                    a = ages[0]
                    b = ages[1]
                    c = ages[2]
                    d = ages[3]


                    if a + b + c == sum_b and b + c + d == sum_a:
                        if a * b * c * d == 17280:
                            total = total + 1
                            print(a, end=", ")
                            print(b, end=", ")
                            print(c, end=", ")
                            print(d)

    print(total)

solve()
