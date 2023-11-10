def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

while True:
    try:
        user_input = int(input("Masukkan sebuah angka (0 untuk keluar): "))

        if user_input == 0:
            break

        result = is_prime(user_input)

        if result:
            print(f"{user_input} adalah bilangan prima.")
        else:
            print(f"{user_input} bukan bilangan prima.")
    except ValueError:
        print("Masukkan harus berupa angka.")
