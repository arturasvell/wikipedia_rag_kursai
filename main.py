from modules.collect_and_segment_to_vectors import collect_and_segment_to_vectors, query, add_more_info
from modules.llm_verifier import VerifiedResponse, check_answer

(client, collection) = collect_and_segment_to_vectors("Black hole")

while True:
    question = input("What would you like to know? Write 'exit' to quit the program.\n")
    
    if('exit' in question):
        break
    
    result = query(question, collection)
    verified:VerifiedResponse = check_answer(question, result)
    if not verified.enough_information:
        missing_info_topic = verified.missing_concepts[0]
        print(f"The response did not contain enough information. The missing topics were {verified.missing_concepts}. Adding information about {missing_info_topic} to database")
        add_more_info(missing_info_topic, collection)
    else:
        print(result)
    
