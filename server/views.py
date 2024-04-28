from django.shortcuts import render, redirect
import wikipedia
import random

def index(request):
    return render(request, 'index.html')

def search_wikipedia(query):
    try:
        page = wikipedia.page(query)
        title = page.title
        summary = page.summary
        url = page.url
        return title, summary, url
    except wikipedia.exceptions.PageError:
        return None, None, None
    except wikipedia.exceptions.DisambiguationError:
        return None, None, None

def random_page():
    try:
        page = wikipedia.random()
        page = wikipedia.page(page)
        title = page.title
        summary = page.summary
        url = page.url
        return title, summary, url
    except Exception as e:
        return None, None, None

def submit_search(request):
    text = request.POST.get('name', 'default')
    title, summary, url = search_wikipedia(text)
    params = {'title': title, 'summary': summary, 'url': url}
    return render(request, 'index.html', params)

def random_page_search(request):
    title, summary, url = random_page()
    params = {'title': title, 'summary': summary, 'url': url}
    return render(request, 'index.html', params)

def change_language(request):
    if request.method == 'POST':
        language = request.POST.get('language')
        print(f"Language selected: {language}")
        wikipedia.set_lang(language)
        return redirect('index')
    return render(request, 'index.html')

def language_change_page(request):
    return render(request, 'change_lang.html')

def quiz(request):
    # Define quiz data as a list of dictionaries
    quiz_data = [
        {
            'question': 'What is the capital of France?',
            'options': ['Paris', 'London', 'Berlin', 'Madrid'],
            'correct_answer': 'Paris'
        },
        {
            'question': 'Which planet is known as the Red Planet?',
            'options': ['Mars', 'Jupiter', 'Saturn', 'Earth'],
            'correct_answer': 'Mars'
        },
        {
            'question': 'Who painted the Mona Lisa?',
            'options': ['Leonardo da Vinci', 'Vincent van Gogh', 'Pablo Picasso', 'Claude Monet'],
            'correct_answer': 'Leonardo da Vinci'
        }
        # Add more questions as needed...
    ]

    # Shuffle the quiz data to display questions randomly
    random.shuffle(quiz_data)

    # Store quiz data in session
    request.session['quiz_data'] = quiz_data
    request.session['quiz_index'] = 0  # Index to track current question
    request.session['score'] = 0  # Initialize score

    return render_question(request)

def render_question(request):
    quiz_data = request.session.get('quiz_data')
    quiz_index = request.session.get('quiz_index')

    if quiz_data and 0 <= quiz_index < len(quiz_data):
        question_data = quiz_data[quiz_index]
        context = {
            'question': question_data['question'],
            'options': question_data['options'],
            'quiz_index': quiz_index + 1,  # Display 1-based question number
            'total_questions': len(quiz_data)
        }
        return render(request, 'quiz.html', context)
    else:
        # No more questions or invalid quiz index
        return redirect('quiz_result')

def submit_answer(request):
    if request.method == 'POST':
        quiz_data = request.session.get('quiz_data')
        quiz_index = request.session.get('quiz_index')
        score = request.session.get('score', 0)

        if quiz_data and 0 <= quiz_index < len(quiz_data):
            selected_option = request.POST.get('answer')

            # Check if the selected answer is correct
            correct_answer = quiz_data[quiz_index]['correct_answer']
            if selected_option == correct_answer:
                score += 1

            # Update session variables
            request.session['score'] = score
            request.session['quiz_index'] = quiz_index + 1

    return render_question(request)

def quiz_result(request):
    score = request.session.get('score', 0)
    total_questions = len(request.session.get('quiz_data', []))
    context = {
        'score': score,
        'total_questions': total_questions
    }
    return render(request, 'quiz_result.html', context)
