# 10-10. Common Words
# Function to count occurrences of 'the' and 'the ' in the text
def count_words(file_path):
    try:
        # Open the file and read the content
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            
        # Convert the text to lowercase to ensure case-insensitive counting
        lower_text = text.lower()
        
        # Count occurrences of 'the' and 'the '
        the_count = lower_text.count('the')
        the_with_space_count = lower_text.count('the ')
        
        # Display the results
        print(f"Occurrences of 'the': {the_count}")
        print(f"Occurrences of 'the ' (with a space): {the_with_space_count}")
    
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = 'where_the_west_begins_by_austin_hall.txt'
count_words(file_path)