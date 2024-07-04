import emoji


emoji_code = input('')

emojized_code = emoji.emojize(emoji_code, language='alias')

print(emojized_code)
