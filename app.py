import streamlit as st
from utils.groq_recipe import generate_recipe

# Explicitly set your API key here
API_KEY = "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"

# Set page layout and configuration
st.set_page_config(page_title="Healthy Recipe Generator", page_icon="🍽️", layout="wide")

# Add custom styling for a modern, lively design
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f5f5f5;
        }
        .title {
            font-size: 45px;
            font-weight: bold;
            color: #FF6347;
            text-align: center;
            margin-top: 20px;
            font-family: 'Comic Sans MS', cursive, sans-serif;
        }
        .description {
            font-size: 18px;
            color: #555;
            text-align: center;
            margin-bottom: 30px;
            font-style: italic;
        }
        .input-box {
            margin: 20px auto;
            padding: 15px;
            width: 70%;
            border-radius: 12px;
            border: 2px solid #FFD700;
            font-size: 18px;
            background-color: #FFE4B5;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            color: #333;
        }
        .button {
            background-color: #32CD32;
            color: white;
            border-radius: 12px;
            padding: 12px 25px;
            font-size: 18px;
            border: none;
            cursor: pointer;
            width: 70%;
            display: block;
            margin: 25px auto;
        }
        .button:hover {
            background-color: #228B22;
        }
        .recipe {
            font-size: 18px;
            line-height: 1.6;
            color: #2F4F4F;
            margin-top: 20px;
            background-color: #F0FFF0;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }
        .error-message {
            color: #FF4500;
            font-size: 20px;
            text-align: center;
        }
        .section-header {
            color: #FF6347;
            font-size: 22px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .ingredient {
            font-size: 20px;
            font-style: italic;
            color: #333;
        }
    </style>
""", unsafe_allow_html=True)

# Streamlit UI components
st.markdown('<div class="title">🍽️ Healthy Recipe Generator</div>', unsafe_allow_html=True)

st.markdown('<div class="description">Enter your favorite ingredients below, and we will generate a delicious recipe that is healthy and nutritious!</div>', unsafe_allow_html=True)

# Input box with better appearance
prompt = st.text_area(
    "Enter ingredients for the recipe:",
    "spinach, chickpeas, garlic",
    placeholder="e.g., spinach, chickpeas, garlic, tomatoes",
    height=100,
    key="ingredient_input",
    label_visibility="collapsed"
)

# Add a button for generating recipe
generate_button = st.button("Generate Recipe", key="generate_button", help="Click to generate your recipe!")

# Action when button is clicked
if generate_button:
    if prompt:
        st.write("Generating recipe... Please wait.")
        
        # Show a progress bar while waiting
        progress_bar = st.progress(0)
        with st.spinner('Generating your recipe... 🧑‍🍳'):
            recipe = generate_recipe(prompt, API_KEY)
        
        # Increment the progress bar (simulate processing)
        for i in range(100):
            progress_bar.progress(i + 1)
        
        if recipe:
            # Render the recipe section with formatted HTML using st.markdown
            st.markdown(f"<div class='recipe'>", unsafe_allow_html=True)
            st.markdown(f"### 🍽️ Your Recipe:")
            st.markdown(f"<div class='section-header'>Ingredients:</div><div class='ingredient'>{prompt}</div>")
            st.markdown(f"<div class='section-header'>Instructions:</div><div>{recipe}</div>")
            
            # Nutritional info and health benefits section
            st.markdown("<div class='section-header'>🥗 Nutritional Information:</div>", unsafe_allow_html=True)
            st.write("Calories, protein, fat, vitamins, and health benefits... (This section is dependent on the API response)")
            
            # Add balloons to celebrate the recipe generation
            st.balloons()
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="error-message">Sorry, we couldn\'t generate a recipe. Please try again. 😔</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="error-message">Please enter ingredients to generate a recipe.</div>', unsafe_allow_html=True)
