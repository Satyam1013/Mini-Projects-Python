questions = [
  [
    "Which currency is used in Bangladesh?", "Rupee", "Taka", "Reyal", "Yen", 2
  ],
  ["Which currency is the strongest?", "Rubel", "Dollar", "Dinar", "Euro", 3],
  [
    "Which big cat is has the highest bite force", "Tiger", "Lion", "Puma",
    "Jaguar", 4
  ],
  [
    "Which is the strongest cat pound for pound", "Lion", "Leopard", "Tiger",
    "Jaguar", 4
  ],
  [
    "Which one is the biggest big cat?", "Lion", "Tiger", "Jaguar", "Cheetah",
    2
  ],
  ["Biggest Country by Size?", "Russia", "India", "China", "USA", 1],
  ["Biggest Country by Population?", "India", "China", "Russia", "USA", 1],
  ["Mousqito Free Country", "Ireland", "USA", "Finland", "Greenland", 1],
  ["Most Powerful Country?", "USA", "India", "China", "Pakistan", 1],
  [
    "Javascript Creator name?", "Brandon Allen", "Rafael", "Stefen King",
    "Steve Jobs", 1
  ],
  [
    "Who is the biggest star in India", "SRK", "Amitabh", "Salman", "Govinda",
    2
  ],
  [
    "Most Popular Reality Show Dancer", "Raghav", "Dharmesh", "Prince", "Paul",
    1
  ],
  [
    "Highest grossing Movie in India", "Bahubali 2", "Sultan", "Dangal", "RRR",
    3
  ],
  [
    "First India Song to receive Oscar", "Channa Mereya", 'Teri Mitti',
    "Natu Natu", "Hamari Adhuri Kahani", 3
  ],
]

prize = [
  1000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000,
  1200000, 2400000, 5000000, 10000000
]
money = 0

for i in range(0, len(questions)):
  question = questions[i]
  # print(f"Question for Rs. {prize[i]}")
  print(f"\n{question[0]}")
  print(f"a. {question[1]}      b. {question[2]}")
  print(f"c. {question[3]}      d. {question[4]}")
  reply = int(input('Enter the answer in number btw (1-4) : '))
  if (reply == question[5]):
    if (i == 3):
      money = 10000
    elif (i == 8):
      money = 320000
    elif (i == 13):
      money = 10000000
    print(f'You Have Won Rs.{prize[i]}')
  else:
    print('Wrong Answer')
    break

print(f'Congrats You Earned {money}')
