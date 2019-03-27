#Chawarat Iampramoon 5980028
#Tommy Egnehall 5980011
#python 3

if __name__ == "__main__":
    n=int(input("Number of values given: "))
    print("X values: ")
    x=[float(x) for x in input().split()]
    y = [[0 for i in range(n)]
            for j in range(n)];
    print("F(x) values: ")
    hold=input().split()
    for i in range(len(y)):
        for j in range(len(y)):
            y[i][0]=float(hold[i])
# table
for i in range(1, n):
    for j in range(n - i):
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1];

# Display
for i in range(n):
    print(x[i], end = "\t");
    for j in range(n - i):
        print(y[i][j], end = "\t");
    print("");
def u_cal(u, n):
    temp = u;
    for i in range(1, n):
        temp = temp * (u - i);
    return temp;

def factorial(n):
    f = 1;
    for i in range(2, n + 1):
        f *= i;
    return f;
interpolated = int(input("Value to interpolate at x = "))
sum = y[0][0];
u = (interpolated - x[0]) / (x[1] - x[0]);
for i in range(1,n):
    sum = sum + (u_cal(u, i) * y[0][i]) / factorial(i);

print("\nValue at x ", interpolated, "is", round(sum, 6));
