print("Выберите любой цвет из списка - крастный , розовый , фиолетовый,  черный , белый , серый , синий , голубой ,бирюзовый ")

color = ["крастный","розовый","фиолетовый",
         "черный","белый","серый",
         "синий","голубой","бирюзовый"] 

answers = ["Да Да Да Нет Нет Нет Нет Нет Нет ",
           "Да Да Нет Нет Нет Нет Нет Нет Нет ",
           "Да Нет Нет Нет Нет Нет Нет Нет Нет ",
           "Нет Нет Нет Да Да Да Нет Нет Нет ",
           "Нет Нет Нет Да Да Нет Нет Нет Нет ",
           "Нет Нет Нет Да Нет Нет Нет Нет Нет ",
           "Нет Нет Нет Нет Нет Нет Да Да Да ",
           "Нет Нет Нет Нет Нет Нет Да Да Нет ",
           "Нет Нет Нет Нет Нет Нет Да Нет Нет ",
]

def questions():
    question = input("Ваш цвет из семейство крастных?") + " "
    question += input("Ваш цвет крастный или розавый?") + " "
    question += input("Ваш цвет красный?") + " "
    question += input("Ваш цвет из семейство монохромных?") + " " 
    question += input("Ваш цвет черный или белый?") + " "
    question += input("Ваш цвет черный?") + " " 
    question += input("Ваш цвет из семейство синих?") + " "
    question += input("Ваш цвет синий или голубой?") + " "
    question += input("Ваш цвет синий?") + " "
    return question

question =questions()


def akinator(question):
    for i in range(len(answers)):
        if answers[i] == question:
            return color[i]
        else:
            return "Простите, но я не смог угадать ваш цвет :("    

print(akinator(question))          
          
