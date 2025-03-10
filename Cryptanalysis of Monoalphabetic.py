def get_letter_frequencies(text):
    freq = {}
    for char in text:
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
    return sorted(freq, key=freq.get, reverse=True)
def decrypt(text, mapping):
    result = ""
    for char in text:
        result += mapping.get(char, char)
    return result

english_order = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
cipher_text = input("enter text to decrypt:  ")
cipher_order = get_letter_frequencies(cipher_text)
mapping = {cipher_order[i]: english_order[i] for i in range(len(cipher_order))}
plain_text = decrypt(cipher_text, mapping)

while True:
    show_m = input("==============="
                   "|show mapping?|\n"
                   "|y for yes----|\n"
                   "|n for no-----|\n"
                   "answer: ")
    if show_m == "y":
        print("Mapping:", mapping)
        print("Decrypted Text:", plain_text)
        break
    elif show_m == "n":
        print("Decrypted Text:", plain_text)
        break
    else:
        print("invalid")
