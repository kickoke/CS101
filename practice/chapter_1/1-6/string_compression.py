"""
Compress a string using the counts of repeated chars.
You can assume that a string only has upper/lowercase letters.
If the length of the compressed string is not smaller than the original 
string, return the original string.
--- thoughts ---
single char makes it longer: a -> a1
two chars keep it the same aa -> a2
starting 3 chars, the string gets shorter aaa -> a3

Could be list of lists, where the string gets chunked 
into a new sublist every time a new char sequence starts.
The printing could then just count the length of a given sublist.
"""

def compress(uncompressed: str) -> str:
    
    compressed = []
    # Read and process uncompressed string
    for char in uncompressed:
        # Starting case: first char is always added.
        if len(compressed) == 0:
            compressed.append([char])
            continue

        # Lookback at most recent char
        if char == compressed[-1][-1]:
            compressed[-1].append(char)
        else:
            compressed.append([char])

    # assemble compressed string
    compressed_str = ""
    for chunk in compressed:
       compressed_str = compressed_str + "".join(chunk[0] + str(len(chunk)))
    
    # assemble compressed string
    if  len(compressed_str) >= len(uncompressed):
        return uncompressed
    return compressed_str


