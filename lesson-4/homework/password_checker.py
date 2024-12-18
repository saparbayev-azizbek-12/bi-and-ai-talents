password = input('Password : ')

upper_letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
cnt = 0

if len(password) < 8:
    print('Password is too short.')
else:
    for x in password:
        if x in upper_letters:
            cnt += 1
    if not cnt:
        print('Password must contain an uppercase letter.')
    else:
        print('Password is strong.')