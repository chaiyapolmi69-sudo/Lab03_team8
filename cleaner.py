def clean_text(text):
    """
    Cleans the input text by:
    - Removing leading and trailing spaces
    - Replacing multiple spaces with a single space

    Args:
        text (str): The input string to clean.

    Returns:
        str: The cleaned string.
    """
    return " ".join(text.split())
clean_text(" hello world ")  # Output: "hello world"
clean_text("a  b ")          # Output: "a b"