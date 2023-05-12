from collections import defaultdict, deque

WHITESPACE = " "
SKIP_SUFFIX = "yab"
VALID_SUFFIX = WHITESPACE + SKIP_SUFFIX

def decode(encoded: str, codebook: dict[str, str]) -> str:
    reverse_map = defaultdict(list)
    for letter, code in codebook.items():
        reverse_map[code].append(letter)

    queue = deque([("", encoded)])
    visited = set(("", encoded))
    result = []

    while queue:
        decoded, encoded = queue.popleft()

        for code, letters in reverse_map.items():
            if not encoded.startswith(code):
                continue

            new_encoded = encoded.replace(code, "", 1)

            for letter in letters:
                # skips cases where there are consecutive whitespaces
                if letter == WHITESPACE and decoded.endswith(WHITESPACE):
                    continue

                new_decoded = decoded + letter
                
                if new_decoded.endswith(SKIP_SUFFIX) and not new_decoded.endswith(VALID_SUFFIX):
                    continue

                new_pair = (new_decoded, new_encoded)

                if new_pair in visited:
                    continue

                visited.add(new_pair)

                if new_encoded:
                    queue.append(new_pair)
                else:
                    result.append(new_decoded)
    
    if not result:
        raise ValueError("Cannot be decoded")
    
    if len(result) > 1:
        print("Multiple decoded values found...")
        print(result)
        print("Returning the first value...")

    return result[0]


codebook = {
    "a": "00",
    "b": "01",
    "c": "10",
    "d": "1100",
    "e": "1101",
    "f": "1110",
    "g": "111100",
    "h": "111101",
    "i": "111110",
    "j": "1111110000",
    "k": "1111110001",
    "l": "1111110010",
    "m": "1111110011",
    "n": "1111110100",
    "o": "1111110101",
    "p": "1111110110",
    "q": "1111110111",
    "r": "1111111000",
    "s": "1111111001",
    "t": "1111111010",
    "u": "1111111011",
    "v": "1111111100",
    "w": "1111111101",
    "x": "1111111110",
    "y": "1111111111",
    "z": "11111111110000",
    " ": "11111111110001",
}

encoded = "11111011111111110001111111001011111101011111111100110111111111110001001111110100111100110111111100101111010010111111000111111111110001101111110101110011011111111111000110111101001111110010111111001011011111110100111100110111111111110001011101100011111110111111111001110111111111110001111110111111101011111111110001111110111111100111111111110001111011111110111111110100111111111100010011111101001100111111111100011101111111111010111110111111101011111011111101001111001111111111000100111111010011001111111111000111111011111111110001110011111011111110011111110010111110111111000111011111111111000111111110101111011101111111111100011111111101111111010111111110001100111111111100011111111111000111111111110001111111101011110100111111101011111111110001001111110110111111011011010011111110001111111001111111111100011111101111110100111111111100011111111010111101110111111111110001111111011011110111111110000011111110011101"

print(decode(encoded, codebook))
