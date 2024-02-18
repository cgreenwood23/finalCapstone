import pandas as pd
import matplotlib.pyplot as plt
import string
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("spacytextblob")


def clean_data(review):
    # Function to clean review text - convert to lower case, remove white space and stop words
    doc = nlp(review)
    clean_review = [token.text.lower().strip().translate(str.maketrans('', '', string.punctuation))
                    for token in doc if not token.is_stop]
    clean_review = ' '.join(clean_review)
    return clean_review


def sentiment_analysis(review):
    # Function for sentiment analysis, calculates polarity of a review
    doc = nlp(review)
    return doc._.blob.polarity


def similarity(first, second):
    # Function to determine similarity between two reviews
    return nlp(first).similarity(nlp(second))


df = pd.read_csv("Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products.csv")

amazon_reviews = df[['name', 'reviews.text']]

# Removes rows with missing values
amazon_reviews = amazon_reviews.dropna(subset=['reviews.text'])
# Creates new column and iterates through column to clean data in each row
amazon_reviews['reviews.clean'] = amazon_reviews['reviews.text'].apply(
    clean_data)
# Creates new column and iterates through rows to calculate polarity
amazon_reviews['reviews.sentiment'] = amazon_reviews['reviews.clean'].apply(
    sentiment_analysis)


# Calculates similarity between 2 Negative Reviews between 2 different products
print(f""" 2 Negative Reviews Between 2 Different Products:
Review One: {amazon_reviews['reviews.text'][0]}
Review Three: {amazon_reviews['reviews.text'][4976]}
--------
Similarity: {similarity(amazon_reviews['reviews.clean'][0], amazon_reviews['reviews.clean'][4976])}""")
# Calculates similarity between 2 Positive Reviews between 2 different products
print(f""" 2 Positive Reviews Between 2 Different Products:
Review Two: {amazon_reviews['reviews.text'][11]}
Review Four: {amazon_reviews['reviews.text'][4982]}
--------
Similarity: {similarity(amazon_reviews['reviews.clean'][11], amazon_reviews['reviews.clean'][4982])}""")
# Calculates the similarity between a Negative and Posititive Review between same product
print(f""" 1 Negative and 1 Positive Review Between the Same Product:
Review One: {amazon_reviews['reviews.text'][0]}
Review Two: {amazon_reviews['reviews.text'][11]}
--------
Similarity: {similarity(amazon_reviews['reviews.clean'][0], amazon_reviews['reviews.clean'][11])}""")

# Plot each product against the average sentiment product score
average_by_product = amazon_reviews.groupby(
    'name')['reviews.sentiment'].mean().reset_index()
average_by_product = average_by_product.sort_values(by='reviews.sentiment')

plt.figure(figsize=(8, 6))
plt.barh(average_by_product['name'],
         average_by_product['reviews.sentiment'], color='skyblue')


plt.xlabel('Average Sentiment Analysis')
plt.ylabel('Product Name')
plt.title('Average Sentiment Analysis per Product')

plt.show()
