# Day_64-Flask-Project-Top-10-Movies
This is my solution to the project on Day 64 of 100 Days of Code.

The purpose of this project was to create a simple Flask website that takes in a 
movie name via a Flask WTForm, does an API call to [The Movie Database](https://developer.themoviedb.org/?language=en-US) and displays 
the results. The user can then choose one of results to add it to their own database
and rate and review. The Flask page will then display all the movies in a list. 

For my solution, I moved the code for the forms and the API calls into their own 
modules and stored the API token to TMDB in an environment variable. The instructor's
solution uses two different API calls to TMDB to get the required data, but I found 
that the first API call already returned all the needed data and did not implement a 
second API call. 

While this project is called "Top 10 Movies" there is no code to restrict the list to
ten items. An improvement could be made to either programmatically enforce the movie
list size or update the HTML to make it into a "Favorite Movie List" and not worry
about the length. Other improvements could also be made to the design and UI, but 
these changes are beyond the scope of this project. 

---
![image](https://github.com/SentientCyborg/Day_64-Flask-Project-Top-10-Movies/assets/85462620/1083ad16-7a58-4f80-b0f3-c9b3da2c8099)
---

[100 Days of Code by Dr. Angela Yu](https://www.udemy.com/course/100-days-of-code/)
