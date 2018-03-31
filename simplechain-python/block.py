import hashlib


class Block:

    def __init__(self, index, previous_block_hash, timestamp, data, difficulty, nonce=0):
        self.index = index
        self.previous_block_hash = previous_block_hash
        self.timestamp = timestamp
        self.data = data
        self.difficulty = difficulty
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def get_header(self):
        return "{}-{}-{}-{}-{}-{}".format(
            self.index, self.previous_block_hash, self.timestamp, self.data,
            self.difficulty, self.nonce
        )

    def calculate_hash(self):
        return hashlib.sha256(self.get_header()).hexdigest()

    def is_valid(self, previous_block):
        if self.index != previous_block.index + 1:
            return False

        if self.previous_block_hash != previous_block.calculate_hash():
            return False

        if self.hash != self.calculate_hash():
            return False

        if not self.hash.startswith("0" * self.difficulty):
            return False

        return True
