from time import time

from block import Block


def mine_block(blockchain, data):
    last_block = blockchain.get_last_block()

    index = last_block.index + 1
    timestamp = time()
    last_block_hash = last_block.hash
    difficulty = blockchain.difficulty

    block = Block(index, last_block_hash, timestamp, data, difficulty)
    while not block.is_valid(last_block):
        block.nonce += 1
        block.hash = block.calculate_hash()

    blockchain.add_block(block)
