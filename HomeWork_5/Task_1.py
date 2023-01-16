# 38. Напишите программу, удаляющую из текста все слова, содержащие ""абв""

text = "фабвфв, фывфвооа, абсвфабв, фвыф1, вапап!"
text = text.split()
text_new = []
for i in text:
    if "абв" not in i:
        text_new.append(i)
print(text_new)
