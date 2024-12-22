import csv
from googlesearch import search
from tqdm import tqdm

# Function to perform the search and write results
def search_and_write_results(query, output_writer):
    try:
        output_writer.writerow([f"Results for query: {query}"])
        # Perform the search
        for result in search(query, tld="co.in", num=1, stop=1, pause=2):
            output_writer.writerow([result])
        output_writer.writerow([])  # Add an empty row to separate queries
    except Exception as e:
        print(f"Error processing query '{query}': {e}")

# Main function to process the CSV and automate the search
def automate_google_search(input_file_path, output_file_path):
    try:
        with open(output_file_path, "w", newline="", encoding="utf-8") as output_file:
            output_writer = csv.writer(output_file)
            
            # Open the CSV file containing the queries
            with open(input_file_path, "r", newline="", encoding="utf-8") as csv_file:
                csv_reader = csv.reader(csv_file)
                
                # Get total number of rows (used for tqdm progress bar)
                total_rows = sum(1 for row in csv_reader)
                csv_file.seek(0)  # Reset file pointer to the beginning

                # Iterate over each row in the CSV file
                for row in tqdm(csv_reader, total=total_rows, desc="Processing Queries"):
                    if row:  # Check if the row is not empty
                        query = row[0]  # Assuming the query is in the first column
                        search_and_write_results(query, output_writer)
            
            print(f"Search results saved to {output_file_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Set file paths
input_file_path = "queries.csv"
output_file_path = "intern_data_link.csv"

# Run the automation
automate_google_search(input_file_path, output_file_path)
