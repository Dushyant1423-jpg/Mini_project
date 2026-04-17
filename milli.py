questions = [
    ["Who is Shah Rukh Khan?", "WWE wrestler", "Actor", "Astronaut", "plumber", 2],
    ["What is the capital of India?", "Lucknow", "New Delhi", "Chennai", "Mumbai", 2],
    ["What is the largest lake in the World?", "Caspian Sea", "Baikal", "Lake Superior", "Ontario", 2],
    ["Which planet in the solar system is known as  the 'Red Planet'?", "venus", "Earth", "Mars", "Jupiter", 3],
    ["What is the Capital of Japan?", "Beijing", "Tokyo", "Seol", "Bangkok", 2], 
    ["Which River is the longest in the World?", "Amazon", "Mississippi", "Nile", "Yangtze", 3], 
    ["when the First Afgan War took place in", "1839", "1843", "1833", "1848", 1],
    ["Which is the largest island?", "New Guinea", "Andaman Nicobar", "Greenland", "Hawaii", 3],  
    ["What is the official currency of japan?", "Won", "Yuan", "Yen", "Dollars", 3],
    ["Which is the richest Country in the world?", "Qatar","Russia", "The USA", "The UAE", 1]

]

prizes = [100000, 300000, 1100000, 1300000, 1900000, 25000000, 3000000, 35000000, 4000000, 4500000]


i = 0
for question in questions:
   print(question[0])
   print(f"a. {question[1]}")
   print(f"b. {question[2]}")
   print(f"c. {question[3]}")
   print(f"d. {question[4]}")
   
   # check whether the answer is correct or not
   a = int(input("Enter Your answer. 1 for a, 2 for b, 3 for c, 4 for d \n"))
   if (question[5] == a):
       print("Correct Answer")
       
   else :
        print(f"Incorrect, the correct answer was {question[5]}")       
        print("Better luck next time")
        break
   print(f"You won {prizes[i]}")
   i +=1   