import streamlit as st

# --- Pattern Generation Functions ---

def generate_left_aligned_triangle(rows, symbol="*"):
    """Generates a regular left-aligned right triangle."""
    output = ""
    for i in range(1, rows + 1):
        output += (symbol * i) + "\n"
    return output

def generate_right_aligned_triangle(rows, symbol="*"):
    """Generates a right-aligned right triangle."""
    output = ""
    for i in range(1, rows + 1):
        # Spaces needed before symbols
        spaces = " " * (rows - i)
        output += spaces + (symbol * i) + "\n"
    return output

def generate_inverted_left_aligned_triangle(rows, symbol="*"):
    """Generates an inverted left-aligned right triangle."""
    output = ""
    # Loop downwards from rows to 1
    for i in range(rows, 0, -1):
        output += (symbol * i) + "\n"
    return output

def generate_inverted_right_aligned_triangle(rows, symbol="*"):
    """Generates an inverted right-aligned right triangle."""
    output = ""
    # Loop downwards from rows to 1
    for i in range(rows, 0, -1):
        # Spaces needed before symbols
        spaces = " " * (rows - i)
        output += spaces + (symbol * i) + "\n"
    return output

def generate_pyramid_triangle(rows, symbol="*"):
    """Generates a center-aligned pyramid pattern."""
    output = ""
    for i in range(1, rows + 1):
        # Calculate spaces and symbols for centering
        spaces = " " * (rows - i)
        symbols = symbol * (2 * i - 1)
        output += spaces + symbols + "\n"
    return output

def generate_inverted_pyramid_triangle(rows, symbol="*"):
    """Generates an inverted center-aligned pyramid pattern."""
    output = ""
    # Loop from rows down to 1
    for i in range(rows, 0, -1):
        # Spaces (increases as rows decrease)
        spaces = " " * (rows - i)
        symbols = symbol * (2 * i - 1)
        output += spaces + symbols + "\n"
    return output

# --- Main Streamlit App ---

def app():
    # Configure the page settings
    st.set_page_config(page_title="Advanced Triangle Generator", layout="centered")
    
    # Header and description
    st.title("📐 Advanced Pattern Generator")
    st.markdown("---")
    st.caption("Generate various triangle and pyramid patterns based on your selection.")

    # --- User Input Widgets ---
    
    # 1. Triangle Type Selection (Expanded options)
    triangle_type = st.selectbox(
        "1. Select the type of pattern:",
        (
            "Left-Aligned Right Triangle", 
            "Right-Aligned Right Triangle",
            "Inverted Left-Aligned Right Triangle",
            "Inverted Right-Aligned Right Triangle",
            "Center-Aligned Pyramid",
            "Inverted Center-Aligned Pyramid"
        ),
        key="triangle_select"
    )

    # 2. Number of Rows Input (Now a number input field)
    rows = st.number_input(
        "2. Enter the number of rows:",
        min_value=1,
        max_value=20, # Keeping a reasonable limit to prevent huge outputs
        value=5,
        step=1,
        format="%d", # Ensures only integers are used
        key="rows_input"
    )

    # 3. Symbol Input
    symbol = st.text_input(
        "3. Enter the symbol to use (e.g., *, #, $):",
        value="*",
        max_chars=1,
        key="symbol_input"
    )
    
    # Clean up the symbol input to ensure it's not empty
    symbol_char = symbol.strip() if symbol.strip() else "*"

    # --- Generation Logic ---

    # Generate the pattern immediately when any input changes (Streamlit's default behavior)
    st.subheader(f"Generated Pattern: {triangle_type}")
    
    # Determine which function to call based on the selection
    if triangle_type == "Left-Aligned Right Triangle":
        pattern = generate_left_aligned_triangle(rows, symbol_char)
    elif triangle_type == "Right-Aligned Right Triangle":
        pattern = generate_right_aligned_triangle(rows, symbol_char)
    elif triangle_type == "Inverted Left-Aligned Right Triangle":
        pattern = generate_inverted_left_aligned_triangle(rows, symbol_char)
    elif triangle_type == "Inverted Right-Aligned Right Triangle":
        pattern = generate_inverted_right_aligned_triangle(rows, symbol_char)
    elif triangle_type == "Center-Aligned Pyramid":
        pattern = generate_pyramid_triangle(rows, symbol_char)
    elif triangle_type == "Inverted Center-Aligned Pyramid":
        pattern = generate_inverted_pyramid_triangle(rows, symbol_char)
    
    # Display the pattern in a fixed-width code block for correct alignment
    st.code(pattern, language="text")

    st.markdown("---")

if __name__ == '__main__':
    app()