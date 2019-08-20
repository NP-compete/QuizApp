def create_quiz(quiz_data, group):
    SCORE = 0
    for i in range(int(len(quiz_data.loc[group])/3)):
        i = str(i + 1)
        print("\n\n")
        if isinstance(quiz_data.loc[group]['q'+ i +'.question'], str):
            print("Question >>> " + quiz_data.loc[group]['q'+ i +'.question'])
            print("Options: ")
            for option_num in range(4):
                print("> " + quiz_data.loc[group]['q'+ i +'.options'][option_num])
            print("Answer >>> ", end="")
            answer = str(input()).lower()
            if (answer == quiz_data.loc[group]['q'+ i +'.answer'].lower()):
                SCORE = SCORE + 1
        else:
            return SCORE
    return SCORE
