def optimizer (l, r, a):
    if (l == r):
        return a[l]
    else:
        L = optimizer(l+1,r,a)
        R = optimizer(l,r-1,a)
        if (a[l] - L >= a[r] - R):
            return a[l] - L
        else:
            return a[r] - R
def main():
    n = int(input())
    board = list()
    for i in range(0,n):
        board.append(int(input()))
    difference = optimizer(0,n-1,board)
    if (difference > 0):
        print("Player 1 Wins")
    elif (difference == 0):
        print("It's a draw")
    else:
        print("Player 2 Wins")
main()# Write your code here
