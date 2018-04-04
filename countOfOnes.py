# Finding the number of set bits (1's) in binary representation of a number.

N = int(input())

def count_one_in_binary(N):
    count = 0
    while(N):
        N = N & (N-1)
        count += 1
    return count

print(count_one_in_binary(N))
