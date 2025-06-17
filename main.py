from modules.wikipedia_search import get_wikipedia_content

question = input("What would you like to know?\n")

if question.strip():
    content = get_wikipedia_content(question)
    print("Content: ")
    print(content)