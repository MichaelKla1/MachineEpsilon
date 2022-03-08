epsilon = 1.0
while 1-(1+epsilon) != 0:
    oldeps = epsilon
    epsilon = epsilon/2

print(abs(3.0*(4.0/3.0-1)-1)-oldeps)