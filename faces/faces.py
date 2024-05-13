def cs50translate(text, translation_dict ):
    for key, value in translation_dict.items:
        text = text.replace(key, value)
    return text

text_to_translate = input()
