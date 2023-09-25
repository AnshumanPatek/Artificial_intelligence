def water_jug_problem(capacity_a, capacity_b, target):
    jug_a = 0
    jug_b = 0

    while jug_a != target and jug_b != target:
        if jug_a == 0:
            jug_a = capacity_a
        else:
            pour_amount = min(jug_a, capacity_b - jug_b)
            jug_a -= pour_amount
            jug_b += pour_amount

        if jug_a == target or jug_b == target:
            break

        if jug_a == 0:
            jug_a = capacity_a
        else:
            jug_b = 0

    return jug_a, jug_b


capacity_a = 4
capacity_b = 3
target_amount = 4

result = water_jug_problem(capacity_a, capacity_b, target_amount)
print(f"Jug A: {result[0]} units, Jug B: {result[1]} units")
