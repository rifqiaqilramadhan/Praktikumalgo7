def get_ordinal(number):
    if 10 <= number % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(number % 10, 'th')
    return number, suffix

while True:
    try:
        user_input = int(input("Masukkan angka (0 untuk keluar): "))

        if user_input == 0:
            break

        result = get_ordinal(user_input)
        print(result)
    except ValueError:
        print("Masukkan harus berupa angka.")
