from random import randint 

def determine_winner(player_choice, computer_choice):
    # Define the winning combinations
    wins = {
        "Камень": ["Ножницы"],      
        "Бумага": ["Камень", "Колодец"], 
        "Ножницы": ["Бумага"],       
        "Колодец": ["Камень", "Ножницы"]  
    }
    
    if player_choice == computer_choice:
        return "Ничья!"
    
    if computer_choice in wins[player_choice]:
        return f"Ты выиграл! {player_choice} побеждает {computer_choice}"
    else:
        return f"Ты проиграл! {computer_choice} побеждает {player_choice}"

t = ["Камень", "Бумага", "Ножницы", "Колодец"]
computer = t[randint(0,3)]  

player = False

while player == False: 
    player = input("Камень, Ножницы, Бумага или Колодец? > ") 
    
    if player not in t:
        print("Некорректный ход! Пожалуйста, выберите один из предложенных вариантов.")
        player = False
        continue
    
    result = determine_winner(player, computer)
    print(result)
    
    player = False
    computer = t[randint(0,3)]