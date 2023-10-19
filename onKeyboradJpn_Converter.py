# こんにちは、又はこんばんわ！同じ狢工房ですm(__)m
# いつも興味を持ってくださってありがとうございます。
# 下記のプログラムはご自由にお使いください。
# ChatGPTと併用すると使い勝手がよりよくなると思いますよ(#^.^#)

def convert_to_B(text):
    conversion_dict = {
        'z': 'つ',
        'x': 'さ',
        'c': 'そ',
        'v': 'ひ',
        'b': 'こ',
        'n': 'み',
        'm': 'も',
        'a': 'ち',
        's': 'と',
        'd': 'し',
        'f': 'は',
        'g': 'き',
        'h': 'く',
        'j': 'ま',
        'k': 'の',
        'l': 'り',
        'q': 'た',
        'w': 'て',
        'e': 'い',
        'r': 'す',
        't': 'か',
        'y': 'ん',
        'u': 'な',
        'i': 'に',
        'o': 'ら',
        'p': 'せ',
        '1': 'ぬ',
        '2': 'ふ',
        '3': 'あ',
        '4': 'う',
        '5': 'え',
        '6': 'お',
        '7': 'や',
        '8': 'ゆ',
        '9': 'よ',
        '0': 'わ',
        '-': 'ほ',
        '+': 'れ',
    }

    result = ""
    for char in text:
        if char in conversion_dict:
            result += conversion_dict[char]

    return result

def convert_strings_to_B(strings_list):
    return [convert_to_B(s) for s in strings_list]

# この配列内の文字が変換されます。
input_strings = ["aclu", "alba", "amu", "bsec", "cis", "comesa", "csto", "eac", "ecowas", "eeu", "eib", "eiti", "esa", "gcc", "iaea", "icrc", "idb", "ifc", "iucn", "laia", "miga", "nato", "nepad", "oau", "ohchr", "opcw", "osa", "pif", "sica", "spc", "undp", "unfccc", "upu", "wb", "wef", "whc"]


converted_strings = convert_strings_to_B(input_strings)
for s in converted_strings:
    print(s)
