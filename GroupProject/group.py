import sys
import openai
import os

# api key
openai.api_key = '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'

# class for the chat responses and prompts from the user
class Chat:
    def __init__(self, message, result):
        self.message = message
        self.result = result

    def set_message(self, message):
        self.message = message

    def set_result(self, result):
        self.result = result 

    def get_message(self):
        return self.message

    def get_result(self):
        return self.result
    # __str__ to use with a specified output
    def __str__(self):
        return f'User: {self.message}\nChatGPT: {self.result}'

# main function with variables needed for the program
def main():
    message = ''
    result = ''
    the_tuple = ()
    the_list = list()
    the_dictionary = dict()
    count = 0
    messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
    ]

    chat = Chat(message, result)

    mainMenu(message, result, chat, the_tuple, the_list, the_dictionary, count, messages)
     
# mainMenu using the global variables
def mainMenu(message, result, chat, the_tuple, the_list, the_dictionary, count, messages):
    while True:
        while True:
            try:
                print('Welcome to our openAI implementation.')
                print('-' * 22)
                print('1. Enter message')
                print('2. Store result')
                print('3. Display the result')
                print('4. Exit')
                print('-' * 22)
                option = int(input('Option: '))

                if option == 1:
                    enterMessage(message, result, chat, messages)
                    break
                elif option == 2:
                    print()
                    the_tuple, the_list, the_dictionary, chat, count, messages = sortOption(the_tuple, the_list, the_dictionary, chat, count, messages)
                    break
                elif option == 3:
                    print()
                    displayOption(the_tuple, the_list, the_dictionary, chat, count, messages)
                    break
                elif option == 4:
                     os._exit(0)
                else:
                    print('ERROR 2: Invalid choice. Enter either 1, 2, 3, or 4.\n')
            except ValueError:
                print('ERROR 1: Invalid input. Enter either 1, 2, 3, or 4.\n')
                
        print()

# the sortOption function is to determine which container is going to be chosen to store the 
def sortOption(temp1, temp2, temp3, chat, count, messages):
    if hasattr(chat, "result") != True:
        print('Result is empty.')
    else:
        while True:
            try:
                print('Select where to store.')
                print('-' * 22)
                print('1. Tuple')
                print('2. List')
                print('3. Dictionary')
                print('4. Back to Main Menu')
                print('-' * 22)
                option = int(input('Option: '))
                
                # tuple option
                if option == 1:
                    temp1 = list(temp1)
                    temp1.append(chat.__str__())
                    temp1 = tuple(temp1)

                    print (f"Data has been saved in a tuple")
                    os.system("pause")

                    return (temp1, temp2, temp3, chat, count, messages)
                
                # list option
                elif option == 2:
                    temp2.append(chat.__str__())

                    print(f"Data has been saved in a list.")
                    os.system("pause")

                    return (temp1, temp2, temp3, chat, count, messages)

                # dictionary option
                elif option == 3:
                   
                    temp3[count] = (chat.__str__())
                    count = count + 1

                    print(f"Data has been saved in a dictionary.")
                    os.system("pause")

                    return (temp1, temp2, temp3, chat, count, messages)
                
                # go back to the main menu
                elif option == 4:
                    mainMenu('', '', chat, temp1, temp2, temp3, count, messages)
                else:
                    print('ERROR 5: Invalid choice. Enter either 1, 2, 3, or 4.\n')
            except ValueError:
                print('ERROR 3: Invalid input. Enter either 1, 2, 3 or 4.\n')


# the displayOption is to determine how to display 
def displayOption(temp1, temp2, temp3, chat, count, messages):
    if len(temp1) == 0 and len(temp2) == 0 and len(temp3) == 0:
        print('The tuple is empty.')
        print('The list is empty.')
        print('The dictionary is empty')
    else:
        while True:
            try:
                print()
                print('Select to display.')
                print('-' * 22)
                print('1. Tuple')
                print('2. List')
                print('3. Dictionary')
                print('4. Back to Main Menu')
                print('-' * 22)
                option = int(input('Option: '))
                
                # tuple option
                if option == 1:
                    if len(temp1) == 0:
                        print('The tuple is empty.')
                    else:
                        for i in range (len(temp1)):
                            print(f"\nQuestion #{i+1}\n")
                            print(f"{temp1[i]}")
                    break

                # list option
                elif option == 2:
                    if len(temp2) == 0:
                        print('The list is empty.')
                    else:
                        for i in range (len(temp2)):
                            print(f"\nQuestion #{i+1}\n")
                            print(f"{temp2[i]}")
                            print()
                    break

                # dictionary option
                elif option == 3:
                    if len(temp3) == 0:
                        print('The dictionary is empty.')
                    else:
                        for index in range(len(temp3)):
                            print(f"\nQuestion #{index+1}\n")
                            print(f'{temp3[index]}')
                            print()
                    break

                # go back to the main menu
                elif option == 4:
                    mainMenu('', '', chat, temp1, temp2, temp3, count, messages)
                
                # catches any values that isn't part of the 4 options
                else:
                    print('ERROR 6: Invalid choice. Enter either 1, 2, 3, or 4.\n')
            except ValueError:
                print('ERROR 4: Invalid input. Enter either 1, 2, 3, or 4.\n')

# enterMessage is to prompt the user to prompt the chatGPT 
def enterMessage(message, result, the_chat, messages):
    # prompt the user to enter the prompt for chatGPT
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    
    #take the first response of the message
    result = chat.choices[0].message.content
    
    
    print(f"ChatGPT: {result}")

    # append the result of the chatGPT to the messages
    messages.append({"role": "assistant", "content": result})

    # setting the messages and the results of the chat object
    the_chat.set_message(message)
    the_chat.set_result(result)

if __name__ == '__main__':
    main()