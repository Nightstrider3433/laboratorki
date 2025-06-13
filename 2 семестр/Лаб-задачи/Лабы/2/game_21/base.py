import random
import os
import time

def main():
    score_player = 0
    score_bot = 0
    DIFFICULTY = 0.5
    all_carts = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    
    print("Поиграем в 21? \nЕсли хотите играть нажмите Enter, если хотите выйти, то нажмите Ctrl+C")
    input()
    
    while True:
        if score_player == 21:
            print("Больше карт не надо, у вас 21")
            print("Вы автоматически победили бота, так как у вас 21.")
            input("Нажмите Enter, чтобы закрыть окно.")
            return
        
        if score_player > 21:
            print("Вы проиграли, так как набрали больше 21")
            print("Попытайте свою попытку в другой раз.")
            input("Нажмите Enter, чтобы закрыть окно.")
            return
        
        yes_or_no = input("Будете ли вы брать карту?\nВведите yes, если хотите брать карту или введите no, если не берете карту.\n")
        os.system('cls')
        
        if yes_or_no.lower() == 'yes':
            score_carts = random.choice(all_carts)
            print("Вы взяли карту выпало:", score_carts)
            score_player += score_carts
            print("Сейчас у вас ", score_player)
            
        elif yes_or_no.lower() == 'no':
            print("У вас ", score_player, "очков.")
            print("Ход бота")
            time.sleep(3)
            os.system('cls')
            
            while True:
                if score_bot < 15:
                    if random.random() > DIFFICULTY:
                        print("Бот берет карту случайным образом")
                        score_carts = random.choice(all_carts)
                    else:
                        print("Бот использует стратегию для оптимальной игры")
                        ideal_card = min((21 - score_bot), max(2, 21 - score_bot))
                        score_carts = min(all_carts, key=lambda x: abs(x - ideal_card))
                    
                    print("Боту выпало", score_carts, "очков.")
                    score_bot += score_carts
                    print("У бота ", score_bot, "очков.")
                    time.sleep(3)
                    os.system('cls')
                
                if score_bot > 21:
                    print("Бот проиграл.\nТак как у него", score_bot, "очков, а у вас ", score_player)
                    input("Нажмите Enter, чтобы закрыть")
                    return
                
                if score_bot > score_player:
                    print("Бот победил.\nТак как у него", score_bot, "очков, а у вас ", score_player, "\nНе растраивайтесь. Попробуйте ещё раз.")
                    input("Нажмите Enter, чтобы закрыть")
                    return
                
                if score_bot == score_player:
                    print("Вы набрали равное количество очков и у вас ничья")
                    input("Нажмите Enter, чтобы закрыть")
                    return

if __name__ == "__main__":
    main()