from ortools.linear_solver import pywraplp

# projected points for females and males
c = [0, 1000, 966, 974, 977, 955, 991, 996, 951, 953, 939, 927, 931, 944, 949, 965, 976, 912, 928, 914, 928, 926, 924, 954, 948, 909, 902, 918, 912, 912, 902, 920, 844, 894, 884, 903, 879, 857, 892, 884]
d = [0, 995, 979, 947, 967, 920, 933, 968, 877, 926, 957, 984, 957, 954, 931, 937, 903, 951, 914, 943, 949, 919, 873, 921, 899, 921, 887, 926, 922, 908, 906, 892, 889, 860, 852, 928, 918, 894, 888, 923, 866, 876, 854, 829, 926, 884]

p = [0, 56, 48, 46, 43, 37, 36, 34, 34, 32, 32, 32, 29, 28, 26, 25, 24, 24, 23, 23, 19, 19, 19, 17, 17, 17, 17, 16, 16, 16, 15, 14, 14, 13, 13, 12, 12, 12, 11, 11]
q = [0, 42, 33, 33, 32, 32, 31, 29, 27, 26, 25, 25, 25, 25, 25, 24, 24, 23, 23, 21, 19, 19, 19, 18, 18, 17, 17, 16, 16, 16, 16, 16, 16, 16, 16, 14, 14, 14, 14, 13, 13, 12, 11, 11, 10, 10]

# get mip solver 
solver = pywraplp.Solver.CreateSolver("SAT")
if not solver:
    print("Error generating linear program solver")

# declare decision variables
x1 = solver.IntVar(0, 1, 'x1')
x2 = solver.IntVar(0, 1, 'x2')
x3 = solver.IntVar(0, 1, 'x3')
x4 = solver.IntVar(0, 1, 'x4')
x5 = solver.IntVar(0, 1, 'x5')
x6 = solver.IntVar(0, 1, 'x6')
x7 = solver.IntVar(0, 1, 'x7')
x8 = solver.IntVar(0, 1, 'x8')
x9 = solver.IntVar(0, 1, 'x9')
x10 = solver.IntVar(0, 1, 'x10')
x11 = solver.IntVar(0, 1, 'x11')
x12 = solver.IntVar(0, 1, 'x12')
x13 = solver.IntVar(0, 1, 'x13')
x14 = solver.IntVar(0, 1, 'x14')
x15 = solver.IntVar(0, 1, 'x15')
x16 = solver.IntVar(0, 1, 'x16')
x17 = solver.IntVar(0, 1, 'x17')
x18 = solver.IntVar(0, 1, 'x18')
x19 = solver.IntVar(0, 1, 'x19')
x20 = solver.IntVar(0, 1, 'x20')
x21 = solver.IntVar(0, 1, 'x21')
x22 = solver.IntVar(0, 1, 'x22')
x23 = solver.IntVar(0, 1, 'x23')
x24 = solver.IntVar(0, 1, 'x24')
x25 = solver.IntVar(0, 1, 'x25')
x26 = solver.IntVar(0, 1, 'x26')
x27 = solver.IntVar(0, 1, 'x27')
x28 = solver.IntVar(0, 1, 'x28')
x29 = solver.IntVar(0, 1, 'x29')
x30 = solver.IntVar(0, 1, 'x30')
x31 = solver.IntVar(0, 1, 'x31')
x32 = solver.IntVar(0, 1, 'x32')
x33 = solver.IntVar(0, 1, 'x33')
x34 = solver.IntVar(0, 1, 'x34')
x35 = solver.IntVar(0, 1, 'x35')
x36 = solver.IntVar(0, 1, 'x36')
x37 = solver.IntVar(0, 1, 'x37')
x38 = solver.IntVar(0, 1, 'x38')
x39 = solver.IntVar(0, 1, 'x39')

y1 = solver.IntVar(0, 1, 'y1')
y2 = solver.IntVar(0, 1, 'y2')
y3 = solver.IntVar(0, 1, 'y3')
y4 = solver.IntVar(0, 1, 'y4')
y5 = solver.IntVar(0, 1, 'y5')
y6 = solver.IntVar(0, 1, 'y6')
y7 = solver.IntVar(0, 1, 'y7')
y8 = solver.IntVar(0, 1, 'y8')
y9 = solver.IntVar(0, 1, 'y9')
y10 = solver.IntVar(0, 1, 'y10')
y11 = solver.IntVar(0, 1, 'y11')
y12 = solver.IntVar(0, 1, 'y12')
y13 = solver.IntVar(0, 1, 'y13')
y14 = solver.IntVar(0, 1, 'y14')
y15 = solver.IntVar(0, 1, 'y15')
y16 = solver.IntVar(0, 1, 'y16')
y17 = solver.IntVar(0, 1, 'y17')
y18 = solver.IntVar(0, 1, 'y18')
y19 = solver.IntVar(0, 1, 'y19')
y20 = solver.IntVar(0, 1, 'y20')
y21 = solver.IntVar(0, 1, 'y21')
y22 = solver.IntVar(0, 1, 'y22')
y23 = solver.IntVar(0, 1, 'y23')
y24 = solver.IntVar(0, 1, 'y24')
y25 = solver.IntVar(0, 1, 'y25')
y26 = solver.IntVar(0, 1, 'y26')
y27 = solver.IntVar(0, 1, 'y27')
y28 = solver.IntVar(0, 1, 'y28')
y29 = solver.IntVar(0, 1, 'y29')
y30 = solver.IntVar(0, 1, 'y30')
y31 = solver.IntVar(0, 1, 'y31')
y32 = solver.IntVar(0, 1, 'y32')
y33 = solver.IntVar(0, 1, 'y33')
y34 = solver.IntVar(0, 1, 'y34')
y35 = solver.IntVar(0, 1, 'y35')
y36 = solver.IntVar(0, 1, 'y36')
y37 = solver.IntVar(0, 1, 'y37')
y38 = solver.IntVar(0, 1, 'y38')
y39 = solver.IntVar(0, 1, 'y39')
y40 = solver.IntVar(0, 1, 'y40')
y41 = solver.IntVar(0, 1, 'y41')
y42 = solver.IntVar(0, 1, 'y42')
y43 = solver.IntVar(0, 1, 'y43')
y44 = solver.IntVar(0, 1, 'y44')
y45 = solver.IntVar(0, 1, 'y45')

# declare objective function
solver.Maximize(c[1]*x1 + c[2]*x2 + c[3]*x3 + c[4]*x4 + c[5]*x5 + c[6]*x6 + c[7]*x7 + c[8]*x8 + c[9]*x9 + c[10]*x10 + c[11]*x11 + c[12]*x12 + c[13]*x13 + c[14]*x14 + c[15]*x15 + c[16]*x16 + c[17]*x17 + c[18]*x18 + c[19]*x19 + c[20]*x20 + c[21]*x21 + c[22]*x22 + c[23]*x23 + c[24]*x24 + c[25]*x25 + c[26]*x26 + c[27]*x27 + c[28]*x28 + c[29]*x29 + c[30]*x30 + c[31]*x31 + c[32]*x32 + c[33]*x33 + c[34]*x34 + c[35]*x35 + c[36]*x36 + c[37]*x37 + c[38]*x38 + c[39]*x39 + d[1]*y1 + d[2]*y2 + d[3]*y3 + d[4]*y4 + d[5]*y5 + d[6]*y6 + d[7]*y7 + d[8]*y8 + d[9]*y9 + d[10]*y10 + d[11]*y11 + d[12]*y12 + d[13]*y13 + d[14]*y14 + d[15]*y15 + d[16]*y16 + d[17]*y17 + d[18]*y18 + d[19]*y19 + d[20]*y20 + d[21]*y21 + d[22]*y22 + d[23]*y23 + d[24]*y24 + d[25]*y25 + d[26]*y26 + d[27]*y27 + d[28]*y28 + d[29]*y29 + d[30]*y30 + d[31]*y31 + d[32]*y32 + d[33]*y33 + d[34]*y34 + d[35]*y35 + d[36]*y36 + d[37]*y37 + d[38]*y38 + d[39]*y39 + d[40]*y40 + d[41]*y41 + d[42]*y42 + d[43]*y43 + d[44]*y44 + d[45]*y45)

# declare constraints
# budget
solver.Add(p[1]*x1 + p[2]*x2 + p[3]*x3 + p[4]*x4 + p[5]*x5 + p[6]*x6 + p[7]*x7 + p[8]*x8 + p[9]*x9 + p[10]*x10 + p[11]*x11 + p[12]*x12 + p[13]*x13 + p[14]*x14 + p[15]*x15 + p[16]*x16 + p[17]*x17 + p[18]*x18 + p[19]*x19 + p[20]*x20 + p[21]*x21 + p[22]*x22 + p[23]*x23 + p[24]*x24 + p[25]*x25 + p[26]*x26 + p[27]*x27 + p[28]*x28 + p[29]*x29 + p[30]*x30 + p[31]*x31 + p[32]*x32 + p[33]*x33 + p[34]*x34 + p[35]*x35 + p[36]*x36 + p[37]*x37 + p[38]*x38 + p[39]*x39 + q[1]*y1 + q[2]*y2 + q[3]*y3 + q[4]*y4 + q[5]*y5 + q[6]*y6 + q[7]*y7 + q[8]*y8 + q[9]*y9 + q[10]*y10 + q[11]*y11 + q[12]*y12 + q[13]*y13 + q[14]*y14 + q[15]*y15 + q[16]*y16 + q[17]*y17 + q[18]*y18 + q[19]*y19 + q[20]*y20 + q[21]*y21 + q[22]*y22 + q[23]*y23 + q[24]*y24 + q[25]*y25 + q[26]*y26 + q[27]*y27 + q[28]*y28 + q[29]*y29 + q[30]*y30 + q[31]*y31 + q[32]*y32 + q[33]*y33 + q[34]*y34 + q[35]*y35 + q[36]*y36 + q[37]*y37 + q[38]*y38 + q[39]*y39 + q[40]*y40 + q[41]*y41 + q[42]*y42 + q[43]*y43 + q[44]*y44 + q[45]*y45 <= 200)
# number of females
solver.Add(x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10 + x11 + x12 + x13 + x14 + x15 + x16 + x17 + x18 + x19 + x20 + x21 + x22 + x23 + x24 + x25 + x26 + x27 + x28 + x29 + x30 + x31 + x32 + x33 + x34 + x35 + x36 + x37 + x38 + x39 <= 4)
# number of males
solver.Add(y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18 + y19 + y20 + y21 + y22 + y23 + y24 + y25 + y26 + y27 + y28 + y29 + y30 + y31 + y32 + y33 + y34 + y35 + y36 + y37 + y38 + y39 + y40 + y41 + y42 + y43 + y44 + y45 <= 4)

# solve
results = solver.Solve()

# print results
if results == pywraplp.Solver.OPTIMAL: print(f'The solution is optimal.')
print(f'Objective value: z* = {solver.Objective().Value()}')
print(f'Solution: x1* = {x1.solution_value()}, x2* = {x2.solution_value()}, x3* = {x3.solution_value()}, x4* = {x4.solution_value()}, x5* = {x5.solution_value()}, x6* = {x6.solution_value()}, x7* = {x7.solution_value()}, x8* = {x8.solution_value()}, x9* = {x9.solution_value()}, x10* = {x10.solution_value()}, x11* = {x11.solution_value()}, x12* = {x12.solution_value()}, x13* = {x13.solution_value()}, x14* = {x14.solution_value()}, x15* = {x15.solution_value()}, x16* = {x16.solution_value()}, x17* = {x17.solution_value()}, x18* = {x18.solution_value()}, x19* = {x19.solution_value()}, x20* = {x20.solution_value()}, x21* = {x21.solution_value()}, x22* = {x22.solution_value()}, x23* = {x23.solution_value()}, x24* = {x24.solution_value()}, x25* = {x25.solution_value()}, x26* = {x26.solution_value()}, x27* = {x27.solution_value()}, x28* = {x28.solution_value()}, x29* = {x29.solution_value()}, x30* = {x30.solution_value()}, x31* = {x31.solution_value()}, x32* = {x32.solution_value()}, x33* = {x33.solution_value()}, x34* = {x34.solution_value()}, x35* = {x35.solution_value()}, x36* = {x36.solution_value()}, x37* = {x37.solution_value()}, x38* = {x38.solution_value()}, x39* = {x39.solution_value()}, y1* = {y1.solution_value()}, y2* = {y2.solution_value()}, y3* = {y3.solution_value()}, y4* = {y4.solution_value()}, y5* = {y5.solution_value()}, y6* = {y6.solution_value()}, y7* = {y7.solution_value()}, y8* = {y8.solution_value()}, y9* = {y9.solution_value()}, y10* = {y10.solution_value()}, y11* = {y11.solution_value()}, y12* = {y12.solution_value()}, y13* = {y13.solution_value()}, y14* = {y14.solution_value()}, y15* = {y15.solution_value()}, y16* = {y16.solution_value()}, y17* = {y17.solution_value()}, y18* = {y18.solution_value()}, y19* = {y19.solution_value()}, y20* = {y20.solution_value()}, y21* = {y21.solution_value()}, y22* = {y22.solution_value()}, y23* = {y23.solution_value()}, y24* = {y24.solution_value()}, y25* = {y25.solution_value()}, y26* = {y26.solution_value()}, y27* = {y27.solution_value()}, y28* = {y28.solution_value()}, y29* = {y29.solution_value()}, y30* = {y30.solution_value()}, y31* = {y31.solution_value()}, y32* = {y32.solution_value()}, y33* = {y33.solution_value()}, y34* = {y34.solution_value()}, y35* = {y35.solution_value()}, y36* = {y36.solution_value()}, y37* = {y37.solution_value()}, y38* = {y38.solution_value()}, y39* = {y39.solution_value()}, y40* = {y40.solution_value()}, y41* = {y41.solution_value()}, y42* = {y42.solution_value()}, y43* = {y43.solution_value()}, y44* = {y44.solution_value()}, y45* = {y45.solution_value()}')

# Solution: x1* = 0.0, x2* = 0.0, x3* = 0.0, x4* = 0.0, x5* = 0.0, x6* = 1.0, x7* = 1.0, x8* = 0.0, x9* = 0.0, x10* = 0.0, x11* = 0.0, x12* = 0.0, x13* = 0.0, x14* = 0.0, x15* = 0.0, x16* = 1.0, x17* = 0.0, x18* = 0.0, x19* = 0.0, x20* = 0.0, x21* = 0.0, x22* = 0.0, x23* = 1.0, x24* = 0.0, x25* = 0.0, x26* = 0.0, x27* = 0.0, x28* = 0.0, x29* = 0.0, x30* = 0.0, x31* = 0.0, x32* = 0.0, x33* = 0.0, x34* = 0.0, x35* = 0.0, x36* = 0.0, x37* = 0.0, x38* = 0.0, x39* = 0.0, y1* = 0.0, y2* = 1.0, y3* = 0.0, y4* = 0.0, y5* = 0.0, y6* = 0.0, y7* = 0.0, y8* = 0.0, y9* = 0.0, y10* = 0.0, y11* = 1.0, y12* = 0.0, y13* = 0.0, y14* = 0.0, y15* = 0.0, y16* = 0.0, y17* = 0.0, y18* = 0.0, y19* = 0.0, y20* = 1.0, y21* = 0.0, y22* = 0.0, y23* = 0.0, y24* = 0.0, y25* = 0.0, y26* = 0.0, y27* = 0.0, y28* = 0.0, y29* = 0.0, y30* = 0.0, y31* = 0.0, y32* = 0.0, y33* = 0.0, y34* = 0.0, y35* = 0.0, y36* = 0.0, y37* = 0.0, y38* = 0.0, y39* = 0.0, y40* = 0.0, y41* = 0.0, y42* = 0.0, y43* = 0.0, y44* = 1.0, y45* = 0.0
