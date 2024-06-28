# 12. How can you replace string space with a given character in Python?


def str_replace(text, ch):
    result = ""
    for i in text:
        if i == " ":
            i = ch
        result += i
    return result


text = "D t C mpBl ckFrid yS le"
ch = "a"

print(str_replace(text, ch))
# 'DataCampBlackFridaySale'
