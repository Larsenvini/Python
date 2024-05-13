translation_table = input().maketrans({':)', '🙂.', ':(', '🙁'})
original_string = ':)'
translated_string = original_string.translate(translation_table)
print(translated_string)
