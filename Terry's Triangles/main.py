def find_triangles(sum):
    iterations = 0
    num_triangles = 0
    sum = sum - 1

    for i in range(sum):
        y = i + 1
        remain = sum - i

        for j in range(remain):
            x = j + 1
            remain - j

            for k in range(remain):
                iterations = iterations + 1
                z = k + 1

                a = y - x #Set values a, b, c
                b = x + z
                c = y - z

                if x + y + z < sum + 1 and (a > 0) and (c > 0): #Check for sum rule
                    sides = [a, b, c]
                    sides.sort()

                    if sides[0] + sides[1] > sides[2]: #Check for possible triangle
                        if sides[0] == sides[1] or sides[1] == sides[2]: #Check for isoceles
                            num_triangles = num_triangles + 1
    return iterations

for i in range(120): #Iterate for 120 values
    print(find_triangles(i + 6)) #Check values > 6
