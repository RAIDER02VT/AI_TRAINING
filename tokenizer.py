import tiktoken

model = tiktoken.encoding_for_model("gpt-4")
text = input("digita: ")
tokens = model.encode(text)
for t in tokens:
    print(f"Encoded token: {t}")
    print(f"Decoded token: {model.decode([t])}")