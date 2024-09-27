import sys
import tiktoken

def estimate_tokens(text):
    # Load the cl100k_base encoding (used by Claude 3.5 Sonnet)
    enc = tiktoken.get_encoding("cl100k_base")
    
    # Encode the content to get token count
    tokens = enc.encode(text)
    return len(tokens)

def main():
    # Check if there's input from a pipe
    if not sys.stdin.isatty():
        content = sys.stdin.read()
    else:
        # If no pipe input, check for file arguments
        if len(sys.argv) > 1:
            try:
                with open(sys.argv[1], 'r', encoding='utf-8') as file:
                    content = file.read()
            except FileNotFoundError:
                print(f"Error: File '{sys.argv[1]}' not found.", file=sys.stderr)
                sys.exit(1)
        else:
            print("Error: No input provided. Use a pipe or provide a filename.", file=sys.stderr)
            sys.exit(1)

    token_count = estimate_tokens(content)
    print(f"{token_count}")

if __name__ == "__main__":
    main()
