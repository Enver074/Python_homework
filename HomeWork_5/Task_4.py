data = input()

def encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return ''

    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding

def decode(data):
    decoded_message = ""
    i = 0
    j = 0
    while (i <= len(data) - 1):
        run_count = int(data[i])
        run_word = data[i + 1]  
        for j in range(run_count):
            decoded_message = decoded_message+run_word
            j = j + 1
        i = i + 2
    return decoded_message


print(encode(data))
print(decode(encode(data)))