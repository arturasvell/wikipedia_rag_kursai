import wikipedia

def get_wikipedia_content(question:str) -> tuple[str, str]:
    print("Searching wikipedia")
    try:
        search_results = wikipedia.search(question)
        
        if not search_results:
            return (f"Sorry, I couldn't find anything related to {question}", "")
        
        page_title = search_results[0]

        print(f"Found page: '{page_title}'. Fetching content")
        
        wiki_page = wikipedia.page(page_title, auto_suggest=False)
        
        return wiki_page # type: ignore
    except wikipedia.exceptions.DisambiguationError as e:
        error_message = f"Your query '{question}' is ambiguous. Please be more specific.\n"
        error_message += "Did you mean one of these?\n"
        for i, option in enumerate(e.options[:5]): # Show top 5 options
            error_message += f"- {option}\n"
        return error_message  # type: ignore

    except wikipedia.exceptions.PageError as e:
        return f"Could not find a Wikipedia page for '{page_title}'. Error: {e}" # type: ignore
        
    except Exception as e:
        return f"An unexpected error occurred: {e}"  # type: ignore
        