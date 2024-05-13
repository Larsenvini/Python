translation_table = str.maketrans({':)': '🙂 ', ':(': '🙁 '})
original_string = input()
translated_string = original_string.translate(translation_table)
print(translated_string)
