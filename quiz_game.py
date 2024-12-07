print('Welcome to my Quiz game!')
Q1 = input("""
What is 28 - 21?
A: 10
B: 21
C: 3
D: 7
""")
Q2 = input("""
What does 'llabtoof' spell backwards?
A: Cricket
B: FOOTBALL
C: ballfoot
D: football
""")
Q3 = input("""
What is 28 MOD 3 in pseudocode?
A: 1
B: 9.3
C: 9
D: 87
""")


ans1 = ['7', 'D', 'd', 'seven']
ans2 = ['football', 'd', 'D']
ans3 = ['a', 'A', '1', 'one' ]

correct = 0

if Q1 in ans1:
    correct += 1
if Q2 in ans2:
    correct += 1
if Q3 in ans3:
    correct += 1
percent = ((correct / 3) * 100) // 1
print(f'You scored {percent}% !')

