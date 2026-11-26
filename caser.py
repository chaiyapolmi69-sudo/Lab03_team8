def capitalize_words(text):
    """ทำให้ตัวอักษรแรกของแต่ละคำเป็นตัวพิมพ์ใหญ่ เช่น "hello first year" → "Hello First Year" """
    return " ".join(word.capitalize() for word in text.split())
