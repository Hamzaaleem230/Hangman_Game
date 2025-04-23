import streamlit as st
import random

# List of words
words = ["python", "streamlit", "hangman", "game", "developer", "code"]

# Start new game
def start_game():
    st.session_state.word = random.choice(words)
    st.session_state.guessed_letters = []
    st.session_state.lives = 6
    st.session_state.game_over = False

# First time setup
if "word" not in st.session_state:
    start_game()

st.title("🎯 Simple Hangman Game")


# Show the word with guessed letters
display_word = ""
for letter in st.session_state.word:
    if letter in st.session_state.guessed_letters:
        display_word += letter + " "
    else:
        display_word += "_ "
st.write("Word: " + display_word.strip())

# Show guessed letters and lives
st.write(f"Guessed Letters: {' '.join(st.session_state.guessed_letters)}")
st.write(f"Lives Left: {st.session_state.lives}")

# Input for letter and handle submission
with st.form(key="guess_form"):
    guess = st.text_input("Enter a letter").lower().strip()
    submitted = st.form_submit_button("Submit Guess")

    if submitted and not st.session_state.game_over:
        if guess and guess not in st.session_state.guessed_letters:
            st.session_state.guessed_letters.append(guess)
            if guess not in st.session_state.word:
                st.session_state.lives -= 1

        # Check for win or loss
        if all(letter in st.session_state.guessed_letters for letter in st.session_state.word):
            st.success("🎉 Congratulations! You won!")
            st.session_state.game_over = True
        elif st.session_state.lives <= 0:
            st.error(f"💀 You lost! The word was: {st.session_state.word}")
            st.session_state.game_over = True

# Restart the game
if st.session_state.game_over:
    if st.button("Play Again"):
        start_game()

# Footer
st.markdown("---")
st.write("Made with ❤️ by Hamza Syed~")