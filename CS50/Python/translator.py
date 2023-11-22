def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation+"l"
        else:
            translation = translation+letter
            #always return the value
    return translation

print(translate("Lovis"))
