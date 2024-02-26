import json
import csv
import os

# Function to interpret sentiment score based on the provided definition
def interpret_sentiment(score, definition):
    # Split the definition into categories and their corresponding score ranges
    categories = definition.split('; ')
    for category in categories:
        # Example category: "x <= -0.35: Bearish"
        range_part, label = category.split(': ')
        if eval(range_part.replace("x", str(score))):
            return label
    return "Unknown"

def process_articles_to_csv(file_path, output_folder):
    with open(file_path, "r") as file:
        data = json.load(file)

    sentiment_definition = data.get("sentiment_score_definition", "")

    file_name = os.path.basename(file_path)
    csv_file_path = os.path.join(output_folder, file_name.replace('.json', '.csv'))

    with open(csv_file_path, 'w', newline='') as csv_file:
        fieldnames = ['title', 'url', 'sentiment_score', 'sentiment_interpretation', 'author', 'time_published']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        writer.writeheader()
        for article in data.get("feed", []):
            sentiment_score = article.get("overall_sentiment_score")
            sentiment_interpretation = interpret_sentiment(sentiment_score, sentiment_definition)
            writer.writerow({
                "title": article.get("title"),
                "url": article.get("url"),
                "sentiment_score": sentiment_score,
                "sentiment_interpretation": sentiment_interpretation,
                "author": ", ".join(article.get("authors", [])),
                "time_published": article.get("time_published")
            })

sentiment_data_dir = os.path.join(os.getcwd(), "sentiment_data")

if __name__ == "__main__":
    files = os.listdir(sentiment_data_dir)
    for file_name in files:
        if file_name.endswith('.json'):
            file_path = os.path.join(sentiment_data_dir, file_name)
            process_articles_to_csv(file_path, sentiment_data_dir)
            print(f"Processed and saved data from {file_name} to CSV.")
