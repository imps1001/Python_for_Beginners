"""
Program to print the net salary of the employee whose basic salary will be given by the user.
Extra allowances
TA - 30% of basic
DA - 25% of basic 
PF - 10% of basic
Net Salary = Basic + DA + TA - PF
"""
basic = int(input())
da = 0.25 * basic
ta = 0.3 * basic
pf = 0.1 * basic

net_salary = da +ta +basic -pf
print(net_salary)
