import numpy as np
f = open('input/13.txt')
machines = f.read().strip().split('\n\n')
print(machines)
total = 0
for machine in machines:
    m = machine.split('\n')
    ax = int((m[0].split('X+')[-1]).split(', ')[0])
    ay = int(m[0].split('Y+')[-1])
    bx = int((m[1].split('X+')[-1]).split(', ')[0])
    by = int(m[1].split('Y+')[-1])
    px = int((m[2].split('X=')[-1]).split(', ')[0]) + 1000000000000
    py = int(m[2].split('Y=')[-1]) + 1000000000000
    mat = np.array([[ax, bx], [ay, by]])
    matinv = np.linalg.inv(mat)
    res = np.matmul(matinv, np.array([px, py]))
    rx = res[0]
    ry = res[1]
    if abs(rx - round(rx)) < 0.001 and abs(ry - round(ry)) < 0.001:  # and round(rx) <= 100 and round(ry) <= 100
        cost = int(3 * round(rx)) + int(round(ry))
        total += cost
print(total)