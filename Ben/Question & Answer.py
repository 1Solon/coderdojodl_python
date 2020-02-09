STORE = 0
SET = 1

QA = [
    ["What is your name?","Pass", STORE, False],
    ["What is your age?","Pass", STORE, False],
    ["Where is Dublin?","Ireland",SET, False],
    ["What is this computer?","Mac",SET, False],
    ["What is the best Coderdojo?","Coderdojo DL",SET, False]
]
NOT_ASKED = []

NAME_REF = 0

QUESTION_COUNT = 2

def main():
    i = 0
    while(i < len(QA)):
        NOT_ASKED.append(i)
    points = 0
    i = 0
    while(i < QUESTION_COUNT):
        selected_question = 0
        stg = input(QA[i][0])
        if(QA[i][2] == STORE):
            QA[i][1] = stg
        elif(QA[i][2] == SET):
            if(stg == QA[i][1]):
                print("Correct!")
                points += 1
            else:
                print("Wrong!")
                points -= 1
        else:
            print("Invalid question type, report this!")
            exit(1)
        i += 1
    print("Great Job " + QA[NAME_REF][1] + " you got " + str(points) + " points!")
    i = None

if( __name__ == "__main__"):
    main()