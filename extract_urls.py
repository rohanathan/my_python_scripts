import re

def extract_urls(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
        return urls

def save_urls_to_file(urls, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for url in urls:
            output_file.write(url + '\n')

def main():
    input_file_path = input("Enter the path to the input text file: ")
    output_dir_path = input("Enter the path to the output directory where you want to save the output file: ")
    output_file_path = output_dir_path + "/output.txt"
    
    urls = extract_urls(input_file_path)
    
    if urls:
        print("URLs found in the file:")
        for url in urls:
            print(url)
        
        save_urls_to_file(urls, output_file_path)
        print(f"Extracted URLs saved to {output_file_path}")
    else:
        print("No URLs found in the file.")

if __name__ == "__main__":
    main()
