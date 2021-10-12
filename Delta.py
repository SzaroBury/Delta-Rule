import numpy as np

# config
pattern_id = 1
k_max = 10
eta = 0.015
omega = 0.9

# input from pattern file
pattern_file = open("patterns" + str(pattern_id) + ".txt", "r")
M = int(pattern_file.readline().split(":")[1])
N = pattern_file.readline().count("x")
pattern = []
for line in pattern_file:
    pattern.append([float(i) for i in line.split()])
pattern_file.close()

print("M = " + str(M) )
print("N = " + str(N))

# prepare
w = np.random.uniform(-omega, omega, N)
for w_n in range(M): print("w_" + str(w_n) + ": " + str(w[w_n]))

print("------ Training ------")

# epochs loop
for k in range(k_max):
    print(f"k[{k}]")
    # patterns loop
    for m in range(M):
        # calulate output
        y=0.0
        for i in range(N):
            y += w[i] * pattern[m][i]
        print(f"y = {str(y)} (z: {pattern[m][-1]})")
        # refine weights
        for j in range(N):
            new_w = w[j] + eta * (pattern[m][-1] - y) * pattern[m][j]
            #print(f"m_{str(m)} : w_{str(j)} = {str(w[j])} -> {str(new_w)}")
            w[j] = new_w
    input("Press any key...")