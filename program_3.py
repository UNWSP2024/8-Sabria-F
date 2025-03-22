#By: Sabria Fafach
#Date: March 21, 2025
#Title: program_3.py


import random

CAPITALS={"Alabama":"Montgomery","Alaska":"Juneau","Arizona":"Phoenix","Arkansas":"Little Rock"
    ,"California":"Sacramento","Colorado":"Denver","Connecticut":"Hartford","Delaware":"Dover"
    ,"Florida":"Tallahassee","Georgia":"Atlanta","Hawaii":"Honolulu","Idaho":"Boise","Illinois":"Springfield"
    ,"Indiana":"Indianapolis","Iowa":"Des Moines","Kansas":"Topeka","Kentucky":"Frankfort","Louisiana":"Baton Rouge"
    ,"Maine":"Augusta","Maryland":"Annapolis","Massachusetts":"Boston","Michigan":"Lansing","Minnesota":"Saint Paul",
          "Mississippi":"Jackson","Missouri":"Jefferson City","Montana":"Helena","Nebraska":"Lincoln","Nevada":"Carson City"
    ,"New Hampshire":"Concord","New Jersey":"Trenton","New Mexico":"Santa Fe","New York":"Albany","North Carolina":"Raleigh"
    ,"North Dakota":"Bismarck","Ohio":"Columbus","Oklahoma":"Oklahoma City","Oregon":"Salem","Pennsylvania":"Harrisburg",
          "Rhode Island":"Providence","South Carolina":"Columbia","South Dakota":"Pierre","Tennessee":"Nashville",
          "Texas":"Austin","Utah":"Salt Lake City","Vermont":"Montpelier","Virginia":"Richmond","Washington":"Olympia"
    ,"West Virginia":"Charleston","Wisconsin":"Madison","Wyoming":"Cheyenne"}

def main():
    state_names = []
    for key in CAPITALS:
        state_names.append(key)
    num_correct = 0
    num_incorrect = 0




    continue_quiz=input("Do you want to take the states and capitals quiz? If yes enter y:")
    if continue_quiz=="y":

        x=0
        while x<10:
            x+=1
            state = random.choice(state_names)
            correct_answer = CAPITALS[state]

            answer = input(f"What is the capital of {state}?")

            if answer == correct_answer:
                num_correct += 1
                print(f"Congratulations! Your answer is correct. The capital of {state} is {correct_answer}.")

            else:
                num_incorrect += 1
                print(f"Your answer was incorrect. The capital of {state} is {correct_answer}.")

    print(f"You got {num_correct}/10 correct, and {num_incorrect}/10 incorrect.")

if __name__ == '__main__':
    main()


