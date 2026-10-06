from django.shortcuts import render
import requests
from django.http import HttpResponse

def home_view(request):
    return render(request, 'githubProf/home.html')

def search_view(request):
    username = request.GET.get('q', '').strip()
    user_data = None
    error_message = None

    if username:
        api_url = f'https://api.github.com/users/{username}'

        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                user_data = response.json()
            elif response.status_code == 404:
                error_message = f"Github profile '{username}' not found."
            else:
                error_message = 'Failed to fetch data from Github API.'
        except requests.exceptions.RequestException:
            error_message = 'Network error. Could not connect to github.'
    context = {
        'query': username,
        'bio' : user_data.get('bio') if user_data else None,
        'public_repos': user_data.get('public_repos') if user_data else None,
        'user_data' : user_data,
        'error_message': error_message,
    }
    return render(request, 'githubProf/search.html', context)

