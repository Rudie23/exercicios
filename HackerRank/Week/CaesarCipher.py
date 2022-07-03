print("Caesar Cipher")


def caesarcipher(s, k):
    rot_by = k
    s = s.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # Keep punctuation and whitespace
    if s not in alphabet:
        return s
    rotated_pos = ord(s) + rot_by
    # If the rotation is inside the alphabet
    if rotated_pos <= ord(alphabet[-1]):
        return chr(rotated_pos)
    # If the rotation goes beyond the alphabet
    return chr(rotated_pos - len(alphabet))


string = "a"
ro = 3
print(caesarcipher(string, ro))
print()

print("Caeser Cipher 2")


def ceasarcipher(s, k):
    temp = []

    for letter in s:
        temp.append(ord(letter))

    for i in range(len(temp)):
        if 65 <= temp[i] <= 90:
            temp[i] = (65 + (temp[i] - 65 + k) % 26)
        elif 97 <= temp[i] <= 122:
            temp[i] = (97 + (temp[i] - 97 + k) % 26)

    return "".join(map(chr, temp))


s = 'a'
k = 3
print(ceasarcipher(s, k))
