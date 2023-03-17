def filtered_words():
    with open('words.txt', 'r') as infile:
        # Open the output file for writing
        with open('filtered_words.txt', 'w') as outfile:
            # Iterate over the lines in the input file
            for line in infile:
                # Strip leading and'em trailing whitespace from the line
                word = line.strip()
                # Check if the word is at least 3 characters long
                if len(word) >= 3:
                    # Write the word to the output file
                    outfile.write(word + '\n')
                


def generate_replacements(infile, outfile):
  # Open the input file for reading
  with open(infile, 'r') as infile:
    # Open the output file for writing
    with open(outfile, 'w') as outfile:
      # Iterate over the lines in the input file
      for line in infile:
        # Strip leading and trailing whitespace from the line
        word = line.strip()
        # Generate a replacement for the word
        for i in range(3, len(word)):
            replacement = word[:i] + r"\t"
            # Write the replacement to the output file
            outfile.write(f"  - trigger: \"{replacement}\"\n    replace: \"{word}\"\n")

# Example usage: generate replacements for the words in the words.txt file and write the results to the replacements.txt file
