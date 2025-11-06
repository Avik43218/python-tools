class TextToNumber:

    units = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
        "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
        "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19
    }

    tens = {
        "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
        "seventy": 70, "eighty": 80, "ninety": 90
    }

    scale = {
        "hundred": 100, "thousand": 1000, "million": 1_000_000,
        "billion": 1_000_000_000, "trillion": 1_000_000_000_000
    }

    def __init__(self, text: str):
        self.text = text

    def convert(self):
        words = self.text.lower().replace("-", " ").split()
        current = result = 0

        for word in words:
            if word in self.units:
                current += self.units[word]
            elif word in self.tens:
                current += self.tens[word]
            elif word == "hundred":
                current *= 100
            elif word in self.scale:
                if current == 0:
                    current = 1
                current *= self.scale[word]
                result += current
                current = 0
            elif word == "and":
                continue
            else:
                raise ValueError("Inavlid word encountered!")
            
        return result + current
    
if __name__ == "__main__":

    text = input("Enter a number as a string: ")
    converter = TextToNumber(text)

    print(converter.convert())
