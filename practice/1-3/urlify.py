"""
Goal: Replace whitespace in strings with %20
"""


def urlify(s):
    if type(s) is not str:
        return
    url_fragments = s.split(" ")
    ## Check for trailing whitespace and remove
    while url_fragments[-1] == "":
        url_fragments.pop()

    delimiter = "%20"
    return delimiter.join(url_fragments)
