def create_playfair_matrix(key):
    key = key.upper().replace("J", "I")
    key_string = ""

    for char in key:
        if char.isalpha() and char not in key_string:
            key_string += char

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in key_string:
            key_string += char

    matrix = []
    for i in range(0, 25, 5):
        matrix.append(list(key_string[i:i+5]))

    return matrix
def find_position(matrix, letter):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == letter:
                return r, c
    return None
def prepare_text(text):
    text = text.upper().replace("J", "I")
    clean_text = ""

    for char in text:
        if char.isalpha():
            clean_text += char

    final_text = ""
    i = 0
    while i < len(clean_text):
        first = clean_text[i]
        if i + 1 < len(clean_text):
            second = clean_text[i + 1]
            if first == second:
                final_text += first + "X"
                i += 1
            else:
                final_text += first + second
                i += 2
        else:
            final_text += first + "X"
            i += 1

    return final_text
def encrypt_pair(matrix, first, second):
    r1, c1 = find_position(matrix, first)
    r2, c2 = find_position(matrix, second)

    if r1 == r2:
        c1 = (c1 + 1) % 5
        c2 = (c2 + 1) % 5
    elif c1 == c2:
        r1 = (r1 + 1) % 5
        r2 = (r2 + 1) % 5
    else:
        c1, c2 = c2, c1

    return matrix[r1][c1] + matrix[r2][c2]
def decrypt_pair(matrix, first, second):
    r1, c1 = find_position(matrix, first)
    r2, c2 = find_position(matrix, second)

    if r1 == r2:
        c1 = (c1 - 1) % 5
        c2 = (c2 - 1) % 5
    elif c1 == c2:
        r1 = (r1 - 1) % 5
        r2 = (r2 - 1) % 5
    else:
        c1, c2 = c2, c1

    return matrix[r1][c1] + matrix[r2][c2]
def playfair_encrypt(text, key):
    matrix = create_playfair_matrix(key)
    text = prepare_text(text)
    encrypted = ""

    i = 0
    while i < len(text):
        encrypted += encrypt_pair(matrix, text[i], text[i + 1])
        i += 2

    return encrypted
def playfair_decrypt(text, key):
    matrix = create_playfair_matrix(key)
    decrypted = ""

    i = 0
    while i < len(text):
        decrypted += decrypt_pair(matrix, text[i], text[i + 1])
        i += 2

    return decrypted



key = input("enter key: ")
text = input("enter text: ")
while True:
    e_or_d = input("==================\n"
                   "|e for encryption|\n"
                   "|d for decryption|\n"
                   "answer: ").lower().strip()
    if e_or_d == "e":
        print("Ciphertext:", playfair_encrypt(text, key))
        break
    elif e_or_d == "d":
        print("Plaintext:", playfair_decrypt(text, key))
        break
    else:
        print("invalid,try again")
