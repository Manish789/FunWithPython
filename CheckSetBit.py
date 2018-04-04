# Check if the ith bit is set in the binary form of the given number.

# Number in which to check the ith bit is set or unset
N = int(input())
# Bit which needs to be checked in the above numner
i = int(input())

# Function to check the set/unset for ith bit of number.
def check_ith_bit(N,i):
    if (N & (1<<i)):
        return True
    else:
        return False
