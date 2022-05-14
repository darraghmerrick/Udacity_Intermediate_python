"""Write a function that prints a profile, given values."""

def create_profile(given_name, *surnames, **details):
    print('\n',given_name, *surnames)
    for key, value in details.items():
        print(key, value, sep=': ')

info = {
    'cofounded' : 'Udacity', 
    'experience' : "Stanford Professor",
    'Type' : 'Software Development'} 

if __name__ == '__main__':
    create_profile("Sam")
    create_profile("Martin", "Luther", "King", "Jr.", born=1929, died=1968)
    create_profile("Sebastian","Thrun",cofounded="Udacity", experience="Stanford Professor")
    create_profile("Sebastian","Thrun", "King", **info)





