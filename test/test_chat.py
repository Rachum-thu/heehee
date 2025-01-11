from toolkit.openai.chat import chat

results = chat([f'Who is considered the most famous NBA basketball player with number {i}' for i in range(0, 50)], seed=42)
for idx, res in enumerate(results):
    print(f'Q: Who is considered the most famous NBA basketball player with number {idx}?')
    print(f'A: {res}'.replace('\n', ' ') + '\n')

"""
Q: Who is considered the most famous NBA basketball player with number 0?
A: The most famous NBA player who wore the number 0 is Russell Westbrook. Westbrook is known for his explosive athleticism, triple-double performances, and has had a significant impact on the game during his career, notably with the Oklahoma City Thunder, where he won the NBA MVP award in 2017.

Q: Who is considered the most famous NBA basketball player with number 1?
A: The most famous NBA player to wear the number 1 is Allen Iverson. Iverson, known for his scoring ability and crossover dribble, had a prolific career primarily with the Philadelphia 76ers and is considered one of the greatest guards in NBA history. He won the NBA Most Valuable Player (MVP) award in 2001 and was an 11-time All-Star. His impact on the game and popularity have made him a significant figure in basketball history.

...

Q: Who is considered the most famous NBA basketball player with number 49?
A: The number 49 is not commonly associated with many prominent NBA players, as jersey numbers in the league generally range from 0 to 55, with 1-23 being the most iconic. If we look for players who wore 49, one name might come to mind: **Jamaal Wilkes**, who is primarily known for his number 52 but sometimes wore 49 in his early career. However, he is not as widely recognized as the biggest stars wearing more typical numbers. Overall, there isn't a well-known player who is particularly famous for wearing the number 49.
"""