#############################################
"""Create a program that:
1. prompts the user to enter a new member.
2. adds that member to members.txt at the end of the existing members. For example, the user here has entered the member Solomon Right.
In the above example, Solomon Right will be added to members.txt updating the content of the file to:"""
#############################################

def get_input():
    input_name : str = input("Add a new member or type 'exit' : ")
    return input_name

def exec_the_prog() -> None :
    while True :
        input_prompt : str = get_input()

        match input_prompt :
            case "exit":
                break

            case _:
                file = open("/Users/sevakkulinkian/Documents/PYTHON/members.txt","r")
                existing_content : list = file.readlines()
                file.close()

                existing_content.append(f'{input_prompt}\n')

                file = open("/Users/sevakkulinkian/Documents/PYTHON/members.txt","w")
                file.writelines(existing_content)
                file.close()

exec_the_prog()