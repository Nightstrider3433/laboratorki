import random

def generate_password():
    password = []
    
    for _ in range(random.randint(2, 4)):
        password.append(chr(random.randint(65, 90)))
    
    for _ in range(random.randint(2, 4)):
        password.append(chr(random.randint(97, 122)))
    
    for _ in range(random.randint(2, 4)):
        password.append(chr(random.randint(48, 57)))
    
    for _ in range(random.randint(2, 4)):
        password.append(chr(random.randint(33, 47)))

    random.shuffle(password)
    return ''.join(password)

while True:
    user_input = input("Введите сайт и логин (q чтобы выйти): ")
    
    if user_input.lower() == 'q':
        break
    
    try:
        site, login = user_input.split()
       
        password = generate_password()
        
        with open('passwords.txt', 'a') as f:
            f.write(f"{site}-{login}-{password}\n")
            
        print(f"Сгенерированный пароль: {password}")
        print("Данные сохранены в passwords.txt")
    
    except ValueError:
        print("Пожалуйста, введите сайт и логин раздельно")