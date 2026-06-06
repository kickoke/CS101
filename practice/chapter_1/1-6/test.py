from string_compression import compress

def test_compress():
    uncompressed = "aabcccccaaa"
    assert compress(uncompressed) == "a2b1c5a3"

def test_not_compress():
    uncompressed = "abcabbihj"
    assert compress(uncompressed) == uncompressed