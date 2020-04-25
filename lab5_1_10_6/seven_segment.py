a = {1:
"""
  #
  #
  #
  #
  #
""",
     2:
"""
###
  #
###
#
###
""",
     3:
"""
###
  #
###
  #
###
""",
     4:
"""
# #
# #
###
  #
  #
""",
     5:
"""
###
#
###
  #
###
""",
     6:
"""
###
#
###
# #
###
""",
     7:
"""
###
  #
  #
  #
  #
""",
     8 :
"""
###
# #
###
# #
###
""",
     9:
"""
###
# #
###
  #
###
""",
     0:
"""
###
# #
# #
# #
###
"""}

b = ""

while b != "exit":
    b = input("""Please enter a number: (up to 9999999999
 or enter exit to exit)
""")
    if b != "exit":
        list = [int(c) for c in str(b)]

        d_list = []
        for d in list:
            if d == 1:
                d_list.append(a[1])
            if d == 2:
                d_list.append(a[2])
            if d == 3:
                d_list.append(a[3])
            if d == 4:
                d_list.append(a[4])
            if d == 5:
                d_list.append(a[5])
            if d == 6:
                d_list.append(a[6])
            if d == 7:
                d_list.append(a[7])
            if d == 8:
                d_list.append(a[8])
            if d == 9:
                d_list.append(a[9])
            if d == 0:
                d_list.append(a[0])


        parts = [s.split('\n') for s in d_list]
        f_list = [""] * len(parts[0])
        for p in parts:
            for i in range(len(p)):
                e = p[i]
                f_list[i] = f_list[i] + e + " "

        print('\n'.join(f_list))
