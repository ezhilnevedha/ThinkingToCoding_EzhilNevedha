import streamlit as st
import config
from pymongo import MongoClient
from datetime import datetime
def generate_left_aligned_triangle(rows, symbol):
    return "\n".join(symbol * i for i in range(1, rows + 1))
def generate_right_aligned_triangle(rows, symbol):
    output = ""
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        output += spaces + (symbol * i) + "\n"
    return output
def generate_inverted_left_aligned_triangle(rows, symbol):
    return "\n".join(symbol * i for i in range(rows, 0, -1))
def generate_inverted_right_aligned_triangle(rows, symbol):
    output = ""
    for i in range(rows, 0, -1):
        spaces = " " * (rows - i)
        output += spaces + (symbol * i) + "\n"
    return output
def generate_pyramid(rows, symbol):
    output = ""
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        symbols = symbol * (2 * i - 1)
        output += spaces + symbols + "\n"
    return output
def generate_inverted_pyramid(rows, symbol):
    output = ""
    for i in range(rows, 0, -1):
        spaces = " " * (rows - i)
        symbols = symbol * (2 * i - 1)
        output += spaces + symbols + "\n"
    return output
# MongoDB Connection
def connect_to_mongodb():
    try:
        client = MongoClient(
            config.DB_URL,
            serverSelectionTimeoutMS=3000
        )

        client.admin.command("ping")

        db = client[config.DB_NAME]
        return db[config.COLLECTION_NAME]

    except Exception:
        return None
# Streamlit App
def app():
    st.set_page_config(page_title="Advanced Pattern Generator", layout="centered")
    st.title("🔺 Advanced Pattern Generator")
    st.caption("Generate triangle and pyramid patterns with MongoDB integration.")
    st.markdown("---")
    # Session state
    if "pattern" not in st.session_state:
        st.session_state.pattern = None
    # Dropdown
    triangle_type = st.selectbox(
        "Select the type of pattern:",
        [
            "Select triangle type",
            "Left-Aligned Right Triangle",
            "Right-Aligned Right Triangle",
            "Inverted Left-Aligned Right Triangle",
            "Inverted Right-Aligned Right Triangle",
            "Center-Aligned Pyramid",
            "Inverted Center-Aligned Pyramid",
        ]
    )

    rows_input = st.text_input("Enter the number of rows:")
    symbol = st.text_input("Enter the symbol (single character):")

    generate = st.button("Generate Pattern")

    if generate:
        try:
            # Validation
            if triangle_type == "Select triangle type":
                raise ValueError("Please select a triangle type.")

            if not rows_input.isdigit():
                raise ValueError("Rows must be a positive integer.")

            if not symbol.strip():
                raise ValueError("Symbol cannot be empty.")

            rows = int(rows_input)
            symbol_char = symbol.strip()[0]
            # Connect to MongoDB FIRST
            collection = connect_to_mongodb()
            if collection is None:
                st.error("MongoDB connection failed!")
                st.session_state.pattern = None
                return

            st.success("MongoDB connected successfully.")
            # Generate Pattern
            if triangle_type == "Left-Aligned Right Triangle":
                pattern = generate_left_aligned_triangle(rows, symbol_char)

            elif triangle_type == "Right-Aligned Right Triangle":
                pattern = generate_right_aligned_triangle(rows, symbol_char)

            elif triangle_type == "Inverted Left-Aligned Right Triangle":
                pattern = generate_inverted_left_aligned_triangle(rows, symbol_char)

            elif triangle_type == "Inverted Right-Aligned Right Triangle":
                pattern = generate_inverted_right_aligned_triangle(rows, symbol_char)

            elif triangle_type == "Center-Aligned Pyramid":
                pattern = generate_pyramid(rows, symbol_char)

            elif triangle_type == "Inverted Center-Aligned Pyramid":
                pattern = generate_inverted_pyramid(rows, symbol_char)

            else:
                raise ValueError("Invalid triangle type selected.")
            # Store in MongoDB
            data = {
                "triangle_type": triangle_type,
                "rows": rows,
                "symbol": symbol_char,
                "pattern": pattern,
                "created_at": datetime.now()
            }

            collection.insert_one(data)

            st.success("Data stored successfully in MongoDB.")

            # Save to session state
            st.session_state.pattern = pattern

        except Exception as e:
            st.error(str(e))
            st.session_state.pattern = None


    # Display Pattern
    if st.session_state.pattern:
        st.subheader(f"Generated Pattern: {triangle_type}")
        st.code(st.session_state.pattern, language="text")
        st.info("Pattern generation completed successfully.")
# Run app
if __name__ == "__main__":
    app()
