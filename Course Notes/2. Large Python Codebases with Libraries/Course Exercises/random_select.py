##my solution
import random

cat_string = "--Whiskers--, --Spot--, --Meowmeow--, --Tiger--, --Kitty--, --Henry--, --Mr.Paws--"

def convert_string_to_list(string):
    string_clean = string.replace('-', '') 
    new_list = list(string_clean.split(", "))
    return new_list
    
def random_choice(list): 
    random_item = random.choice(list)
    return random_item
      
def main():
    cat_list = convert_string_to_list(cat_string)
    random_cat = random_choice(cat_list) 
    print("Random Cat: ",random_cat)

if __name__=="__main__":
    main()