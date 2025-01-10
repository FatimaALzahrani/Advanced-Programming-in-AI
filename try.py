from colorama import init,Fore 
init(autoreset=True)


name = 'Fatimah'
age = 22

# print(f'with strip remove leading/tailing space : {name.strip()}')
# print(f'name with upper : {name.upper()}')
# print(f'name with lower : {name.lower()}')
# print(f'name with find : {name.find('atim')}')
# print(f'name rep : {name.replace(':)','**')}')
# print(f'name with len : {len(name)}')

# print(f'{'at' in name}')

# print(f"Name is {name}")
# print("Name is {}".format(name))
# print("Name is %d %s"%(name,age))



def count_characters(s,c):
    total = 0
    for ch in s:
        if(ch==c):
            total+=1
    return total




if __name__ == '__main__' :
    s = input(f"{Fore.BLUE}Enter String : {Fore.YELLOW}")
    c = input(f"{Fore.BLUE}Enter Char : {Fore.YELLOW}")
    print(f"{Fore.GREEN}Total apper of {c} in string '{s}' is {s.count(c)}")
    