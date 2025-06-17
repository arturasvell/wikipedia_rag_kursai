from modules.collect_and_segment_to_vectors import collect_and_segment_to_vectors, query

(client, collection) = collect_and_segment_to_vectors("Black hole")

question = input("What would you like to know?\n")
result = query(question, collection)
