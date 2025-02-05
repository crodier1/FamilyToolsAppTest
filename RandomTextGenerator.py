import random
import string
class RandomTextGenerator:
    def get(self, min_length=1, max_length=50):
        if min_length > max_length:
            return ""  # Or raise an exception if you prefer

        length = random.randint(min_length, max_length)  # Generates a random length
        characters = string.ascii_letters + string.digits  # Includes letters and digits
        random_string = ''.join(random.choice(characters) for i in range(length))
        return random_string