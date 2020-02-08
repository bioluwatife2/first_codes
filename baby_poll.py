# Imports
import datetime


#project name baby poll
#this fuction return initials of the first and or middlename
def get_initial(name):
    """
    Returns Initials
    """
    if len(name) >= 10:
        initials = name[0].upper() + '. '
        return initials
    else:
        return name
    # if force_uppercase:
    #     initial = name[0:1].upper()
    # else:
    #     initial = name[0:1]
    # return initial  
def print_time():
    print('task completed')
    print(datetime.datetime.now())
    print()


def main():
    print("Welcome to Baby Academy, Please follow the these steps to register your baby")
    name = get_baby_name()
    while len(name) == 0:
        name = get_baby_name()
    # eye_color = get_eye_color()
    skin_color = get_skin_color()
    country, region = get_country()
    nationality = get_nationality(country, region)

    # Check baby data
    check_baby_data(name, skin_color, country, nationality)



def get_baby_name():
    """
    Gets baby's name
    """
    baby_name = input('kindly enter the name of the baby name: ')
    return baby_name

def get_eye_color():
    """
    get baby's eye color
    """
    color_of_eye = input('kindly enter the color of the eye of the baby: ')
    return color_of_eye

def get_skin_color():
    """
    get baby's skin color
    """
    skin_color = ['black','light','fair','brown','olive','medium']
    new_skin_color = input('kindly enter the skin color the baby: ').lower()
    if new_skin_color.lower() not in skin_color:
        new_skin_color_request = input('Skin color does not exist. Add new? (Y/N): ').lower()
        if new_skin_color_request == 'y':
            skin_color.append(new_skin_color)
    return skin_color

# Africa Region
africa = [
    'nigeria',
    'ghana',
    'south africa',
    'egypt',
]

# Europe Region
europe = [
    'new york',
    'america',
    'london',
    'britain'
]

def get_country():
    """
    get baby's country
    """
    country = input('what country do you live in? ')
    if country in africa:
        region = 'Africa'
    elif country in europe:
        region = 'Europe'
    else:
        new_country_request = input('Country does not exist. Add new? (Y/N) ').lower()
        if new_country_request == 'y':
            new_region = input('What region? ').title()
            if new_region == 'Africa':
                africa.append(country)
                region = new_region
            else:
                europe.append(country)
                region = new_region
    return country, region

def get_nationality(country, region):
    """
    get nationlity
    """
    # Perform a condition to check the skin color and nationality of the baby
    if country in africa and region == 'Africa':
        nationality = 'African'
    elif country in europe and region == 'Europe':
        nationality = 'European'
    else:
        nationality = 'Halfcaste'
    
    return nationality


def check_baby_data(baby_name, skin_color, country, nationality):
    baby_data = [baby_name.title(), skin_color, country]
    if len(baby_data) == 0:
        print('Baby data not complete')
    else:
        print(f'hello,your baby {baby_name.title()}:  is {nationality} ')
        #getting initial
        name_initial = input('would you mind to get your baby intial? (Y/n): ').lower()
        if name_initial == 'y':
            baby_name = baby_name.split(' ')
            print(baby_name)
            if len(baby_name) > 1:
                middle_name = baby_name[1]
                middle_name_initial = middle_name[0].upper() + '. '
                print ("your baby's names are: " + baby_name[0].title() + ' ' + middle_name_initial)
    # print ("your baby's initials are: " + baby_name[0].title() + ' ' + middle_name_initial)
    print_time()


if __name__ == '__main__':
    main()