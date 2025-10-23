# Write a program to create a dictionary of hindi words with values as english tracslation.
# provide user with an option to look it up!

hindi_to_english = {
    "Namsate": "Hello",
    "Dhanyawad": "Thank you",
    "Pani": "Water",
    "khana": "Food",
    "ghar": "House",
    "Haa": "Yes",
    "nahi": "No",
    "kripya": "Please",
    "subah": "Morning",
    "shaam": "Evening"
}

word = input("Enter the word that you want meaning of: ")

print(hindi_to_english[word])

