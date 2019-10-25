import sqlite3
from memory_card import Memory_Card  # import the Memory_Card class
import random


conn = sqlite3.connect('memorybox.db')

c = conn.cursor()


def insert_memory_card(memory_card):
    with conn:
        c.execute("INSERT INTO memorycards VALUES (:question, :answer, :hint, :rank)",
                  {'question': memory_card.question,
                   'answer': memory_card.answer,
                   'hint': memory_card.hint,
                   'rank': memory_card.rank})


def get_memory_card_by_rank(rank):
    c.execute("SELECT * FROM memorycards WHERE rank=:rank", {'rank': rank})

    # returns a list of tuples
    return c.fetchall()


def update_rank(memory_card, rank):
    with conn:
        # take the incoming tuple and turn it into a Memory_Card
        temp_memory_card = Memory_Card(question=memory_card[0],
                                       answer=memory_card[1], hint=memory_card[2], rank=memory_card[3])

        # update the database with your Memory_Card
        c.execute("""UPDATE memorycards SET rank = :rank WHERE question = :question AND answer = :answer""",
                  {'question': temp_memory_card.question, 'answer': temp_memory_card.answer, 'rank': rank})


def remove_memory_card(memory_card):
    with conn:
        c.execute("DELETE from memorycards WHERE question = :question AND answer = :answer",
                  {'question': memory_card.question, 'answer': memory_card.answer})


# memory_card_1 = Memory_Card(question='example one?', answer='NO!', hint='no hints', rank=1)
# memory_card_2 = Memory_Card(question='example two?', answer='YES!', hint='no hints', rank=1)
#
# insert_memory_card(memory_card_1)
# insert_memory_card(memory_card_2)


mem_cards = get_memory_card_by_rank(rank=1)
print(mem_cards, len(mem_cards))





i = 0

while i < len(mem_cards):
    try:
        my_card = mem_cards.pop()
        my_rank = 1
        update_rank(my_card, my_rank)
        print("updated rank of {} to {}".format(my_card, my_rank))
    except IndexError:
        print("list was empty")
    i += 1

conn.close()

print("test test test")
print(mem_cards)
print(len(mem_cards))
