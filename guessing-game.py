import json
import random
import colorama
import sys
import os


colorama.init()

with open("config.json") as config:
    config = json.load(config)

target_num = random.randrange(0, 10)
curr_tries = 0
tries = int(config["tries"])


def quit():
    sys.exit()

def game():
    global target_num
    global curr_tries
    global tries

    while curr_tries < tries:
        print(colorama.Fore.GREEN + f"Tries remaining: {tries - curr_tries}")
        
        try:
            num = int(input(colorama.Fore.GREEN + "Enter a number between 0-10: "))
            if num == target_num:
                print(colorama.Fore.GREEN + f"Correct! You won in {curr_tries}")
                main()
            else:
                curr_tries += 1

            if curr_tries == tries:
                print(colorama.Fore.RED + f"You failed in {curr_tries} tries")
                input('')
                main()
        except ValueError as e:
            print(colorama.Fore.RED + "Must be a valid number")


def settings():
    settings_str, settings = list_translate(config.keys(), '. ', True, True)
 
    setting_input = input(colorama.Fore.GREEN + 'Which setting do you want to change\n' + settings_str).lower()

    if verify_input_comp_list(settings, setting_input):
        value_input = input(colorama.Fore.GREEN + f'What value do you want to set for {settings[settings.index(setting_input)]}? ').lower()
        config[settings[settings.index(setting_input)]] = value_input

        with open('config.json','w') as fp:
            fp.write(json.dumps(config))
    elif setting_input == 'back':
        main()
    else:
        print(colorama.Fore.RED + f'Please input a valid setting')
        quit()

menus = ['settings', 'game','quit']
menu_func = [settings, game, quit]

def verify_input_comp_list(list, input_):
    for list_item in list:
        if list_item in input_:
            return True

    return False



def list_translate(list,prefix,endline, enumerate_):
    if endline:
        list_str = ''
        list_list = []
        
        if enumerate_:
            for count, list_item in enumerate(list):
                list_list.append(list_item)
                list_str += f'{count}{prefix}{list_item}\n'

        return (list_str, list_list)
    else:
        list_str = ''
        list_list = []
        
        if enumerate_:
            for count, list_item in enumerate(list):
                list_list.append(list_item)
                list_str += f'{count}{prefix}{list_item}\n'
        else:
            for list_item in list:
                list_list.append(list_item)
                list_str += f'{prefix}{list_item}'

        return (list_str, list_list)

def clear():
    print(colorama.Style.RESET_ALL)
    
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')

def main():
    menu_str, menu_list = list_translate(menus, '>', True, False)

    clear()
    print(colorama.Fore.GREEN + menu_str)
    menu_input = input('Choose a page:\n' + menu_str)

    if verify_input_comp_list(menus, menu_input):
        if menu_input != 'back':
          menu_func[menus.index(menu_input)]()
        else:
            main()
    else:
        print(colorama.Fore.RED + f'Please input a valid page')
        main()



main()