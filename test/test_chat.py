from toolkit.openai.chat import chat

results = chat([f'Who is considered the most famous NBA basketball player with number {i}' for i in range(0, 50)], seed=42)
for idx, res in enumerate(results):
    print(f'Q: Who is considered the most famous NBA basketball player with number {idx}?')
    print(f'A: {res}'.replace('\n', ' ') + '\n')
