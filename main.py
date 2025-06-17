from modules.wikipedia_search import get_wikipedia_content
from modules.collect_and_segment_to_vectors import collect_and_segment_to_vectors

collect_and_segment_to_vectors("Black hole")
question = input("What would you like to know?\n")
