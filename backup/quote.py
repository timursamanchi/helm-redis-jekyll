import random

quotes = [
    ("I am so clever that sometimes I don’t understand a single word of what I am saying.", "Oscar Wilde"),
    ("I used to think I was indecisive, but now I'm not too sure.", "Anonymous"),
    ("Behind every great man is a woman rolling her eyes.", "Jim Carrey"),
    ("I'm writing a book. I've got the page numbers done.", "Steven Wright"),
    ("I always wanted to be somebody, but now I realize I should have been more specific.", "Lily Tomlin"),
    ("Why do they call it rush hour when nothing moves?", "Robin Williams"),
    ("If at first you don't succeed, then skydiving definitely isn't for you.", "Steven Wright"),
    ("A day without sunshine is like, you know, night.", "Steve Martin"),
    ("I find television very educating. Every time somebody turns on the set, I go into the other room and read a book.", "Groucho Marx"),
    ("The road to success is always under construction.", "Lily Tomlin"),
    ("The best way to get started is to quit talking and begin doing.", "Walt Disney"),
    ("Life is what happens when you're busy making other plans.", "John Lennon"),
    ("Your time is limited, so don’t waste it living someone else’s life.", "Steve Jobs"),
    ("Success is not final, failure is not fatal: It is the courage to continue that counts.", "Winston Churchill"),
    ("Don’t watch the clock; do what it does. Keep going.", "Sam Levenson"),
    ("Whether you think you can or you think you can’t, you’re right.", "Henry Ford"),
    ("The only limit to our realization of tomorrow is our doubts of today.", "Franklin D. Roosevelt"),
    ("Do what you can, with what you have, where you are.", "Theodore Roosevelt"),
    ("Hardships often prepare ordinary people for an extraordinary destiny.", "C.S. Lewis"),
    ("Believe you can and you're halfway there.", "Theodore Roosevelt"),
    ("The future belongs to those who believe in the beauty of their dreams.", "Eleanor Roosevelt")
]

def get_quote():
    quote, author = random.choice(quotes)
    return f'"{quote}" — {author}'

print("Quote of the day:", get_quote())
