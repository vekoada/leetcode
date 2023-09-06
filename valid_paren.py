def isValid2(s: str):
    pair = {"(":")", "[":"]", "{":"}"}
    opens = []
    for el in s:
        if el in pair.keys():
            opens.append(el)
        elif el not in pair.keys():
            if len(opens)==0 or el != pair[opens[-1]]:
                return False
            else:
                opens.pop()
    return len(opens)==0
