import wikipedia
def search_wikipedia(query):
    try:
        page = wikipedia.page(query)
        result = f"\nTitle: {page.title}\nSummary: {page.summary}\nURL: {page.url}"
        return result 
        # print(result)
    except wikipedia.exceptions.PageError as e:
        # return HttpResponse("ERROR")
        print('error')
    except wikipedia.exceptions.DisambiguationError as e:
        print ('error ')

import wikipedia

def random_page():
    try:
        # Get a random Wikipedia page title
        random_title = wikipedia.random()

        # Retrieve the Wikipedia page using the random title
        page = wikipedia.page(random_title)
        
        # Return the page object
        return page

    except Exception as e:
        # Handle exceptions, returning None if an error occurs
        print(f"Error fetching random page: {e}")
        return None

# Call the random_page function to get a random Wikipedia page
random_result = random_page()

# Check if the result is valid (not None)
if random_result:
    # Access information from the page object
    print(f"Random Page Title: {random_result.title}")
    print(f"Random Page URL: {random_result.url}")
    print(f"Random Page Summary:\n{random_result.summary}")
else:
    print("Failed to fetch a random Wikipedia page.")

languages = {
    "en": "English",
    "ko": "Korean",
    "hi": "Hindi",
    "ar": "Arabic"
    # Add more languages as needed
}
def set_language(language_code):
        
        if language_code in languages:
            wikipedia.set_lang(language_code)
            # messagebox.showinfo("Success", f"Wikipedia language set to '{languages[language_code]}'.")
        else:
            print("error")

set_language("hi")
random_result = random_page()

# Check if the result is valid (not None)
if random_result:
    # Access information from the page object
    print(f"Random Page Title: {random_result.title}")
    print(f"Random Page URL: {random_result.url}")
    print(f"Random Page Summary:\n{random_result.summary}")
else:
    print("Failed to fetch a random Wikipedia page.")
