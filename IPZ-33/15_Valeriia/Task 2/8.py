import textwrap

def format_text(text, n):
    paragraphs = text.split("\n\n")  # Split text into paragraphs
    formatted_paragraphs = []
    
    for paragraph in paragraphs:
        wrapped = textwrap.fill(paragraph, width=n)  # Format each paragraph
        formatted_paragraphs.append(wrapped)
    
    return "\n\n".join(formatted_paragraphs)  # Join paragraphs back together

# Get text and width from user input
text = input("Текст: ")
n = int(input("Число n (n > 50): "))
formatted_text = format_text(text, n)
print(formatted_text)
