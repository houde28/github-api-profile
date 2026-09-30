from django.shortcuts import render
import requests
from django.http import HttpResponse

def github_profile(request, username):
    response = requests.get(f'https://api.github.com/users/{username}')
    data = response.json()
    return HttpResponse(f"""
        <h1>{data['name']}</h1>
        <p>Bio: {data['bio']}</p>
        <p>Followers: {data['followers']}</p>
        <p>Public repos: {data['public_repos']}</p>
    """)

