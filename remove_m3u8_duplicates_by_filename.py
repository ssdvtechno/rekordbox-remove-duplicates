import os

def remove_duplicates_from_m3u8(input_file, output_file):
    if not os.path.isfile(input_file):
        print(f"Error: File {input_file} does not exist.")
        return

    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Remove duplicates by considering only the file name, ignoring directory paths
    unique_lines = []
    seen_filenames = set()

    for line in lines:
        line = line.strip()
        if line:
            # Get just the file name from the path
            file_name = os.path.basename(line)
            if file_name not in seen_filenames:
                unique_lines.append(line)
                seen_filenames.add(file_name)

    # Write the unique lines back to the output file
    with open(output_file, 'w') as f:
        for line in unique_lines:
            f.write(line + '\n')

    print(f"Duplicates removed by file name. Cleaned playlist saved to {output_file}.")

if __name__ == "__main__":
    # Get the current directory where the script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Define input and output files in the same directory
    input_file = os.path.join(current_dir, 'playlist.m3u8')
    output_file = os.path.join(current_dir, 'cleaned_playlist.m3u8')

    remove_duplicates_from_m3u8(input_file, output_file)
