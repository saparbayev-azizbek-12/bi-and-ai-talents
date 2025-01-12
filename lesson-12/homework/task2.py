import os
import requests
from dotenv import load_dotenv
from random import randint

load_dotenv()
api = os.getenv('API_2')

def list_to_str(genres: list) -> str:
    s = ''
    for genre in genres:
        s += str(genre) + ','
    return s[:-1]

def filter_by_genre(genre_ids):
    url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc&with_genres={list_to_str(genre_ids)}"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiMzkyODA4MjVjYmI5NTYyNTEyMTBmYmIwYTkzZjkwZiIsIm5iZiI6MTczNjY2MjQwMC43NzIsInN1YiI6IjY3ODM1ZDgwYzgxYWNhYTYzZGJiYzRjZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.frtd8ieubZ4GPOn3eq-3f4FxjR9AZgTUi1Y-12Of6So"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        movies = response.json()
        length = 20
        for i in range(10):
            print(f"{i+1}. Movie Name: {movies['results'][randint(0, length-1)]['original_title']}\n--Movie Language: {movies['results'][randint(0, length-1)]['original_language']}")
    else:
        print('Something went wrong')

def genre_list(): 
    url = "https://api.themoviedb.org/3/genre/movie/list"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiMzkyODA4MjVjYmI5NTYyNTEyMTBmYmIwYTkzZjkwZiIsIm5iZiI6MTczNjY2MjQwMC43NzIsInN1YiI6IjY3ODM1ZDgwYzgxYWNhYTYzZGJiYzRjZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.frtd8ieubZ4GPOn3eq-3f4FxjR9AZgTUi1Y-12Of6So"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        genres = response.json()
        genres = genres['genres']
        for i, genre in enumerate(genres):
            print(f"{i+1}.Genre ID: {genre['id']}  ||  Genre Name: {genre['name']}")
    else:
        print('Something went wrong')
    

def main():
    while True:
        print('\n1.Genre Movies')
        print('2.Filter Movies via Genre')

        choise = input('>>> ')

        if choise == '1':
            genre_list()
        elif choise == '2':
            genre_id = list(map(int, input('Enter Genre IDs: ').split()))
            print(genre_id)
            filter_by_genre(genre_id)
        else:
            break


if __name__ == "__main__":
    main()