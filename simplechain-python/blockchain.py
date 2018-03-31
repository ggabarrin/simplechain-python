from block import Block


DIFFICULTY = 5


class Blockchain:

    def __init__(self):
        self.chain = [create_genesis_block()]
        self.difficulty = DIFFICULTY

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, block):
        if block.is_valid(self.get_last_block()):
            self.chain.append(block)

    def is_valid(self):
        if not self.chain[0] == create_genesis_block():
            return False

        for i in range(1, len(self.chain)):
            previous_block = self.chain[i - 1]
            block = self.chain[i]
            if not block.is_valid(previous_block):
                return False

            return True


def create_genesis_block():
    return Block(0, None, 1509926400, 'Hello, world!', DIFFICULTY, 49358)
