import sys

def clean_text_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    # Strip spaces and remove empty lines
    cleaned_lines = [line.strip() for line in lines if line.strip()]

    with open(output_path, 'w', encoding='utf-8') as outfile:
        for line in cleaned_lines:
            outfile.write(line + '\n')

    print(f"Cleaned text saved to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python text_file_cleaner.py input.txt output.txt")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        clean_text_file(input_file, output_file)
