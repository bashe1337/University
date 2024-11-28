import pymorphy3
from translate import Translator

morph = pymorphy3.MorphAnalyzer()
translator = Translator(from_lang='ru', to_lang='en')

with open('data.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    words = text.split()

    count = {}

    for word in words:
        normalized = morph.parse(word)[0].normal_form
        translated = translator.translate(normalized) 

        if (normalized, translated) in count:
            count[(normalized, translated)] += 1
        else:
            count[(normalized, translated)] = 1

sortCount = sorted(count.items(), key=lambda item: item[1], reverse=True)

with open('result.txt', 'w', encoding='utf-8') as result:
    result.write("Исходное слово | Перевод | Количество повторений\n")
    for (word, translation), count in sortCount:
        result.write(f"{word} | {translation} | {count}\n")

print(f"Таблица сохранена!")