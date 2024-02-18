# NLP- Sentiment Analysis of Amazon Reviews

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Table of Contents
| Section |
|-------- |
| [Introduction](#Introduction) |
| [Strengths & Limitations](#Strengths-and-Limitation-of-the-SpaCy-Module) |
| [Example Output](#Example-Output) |
| [Run Locally](#Run-Locally) |
| [Usage](#Usage) |
| [Licence](#Licence) |

## Introduction
This is a Basic Natural Language Process Model using SpaCy Module. It is analysing reviews from Amazon customers about a product they have purchased (such as Kindle, Amazon Fire Stick etc). Each column provides basic product information, rating, review text, and more, for each product. These reviews were collected by Datafiniti's Product Database and the dataset was downloaded from Kaggle in CSV format (https://www.kaggle.com/datasets/datafiniti/consumer-reviews-of-amazon-products).

Analysing Amazon reviews using NLP is useful to efficiently get a sense of whether reviewing surrounding a particular product are positive or negative. 

## Strengths and Limitation of the SpaCy Module:
### Strengths:
* The ‘en_core _web_sm’ model is efficient, it requires limited computation resources making its application suitable for all users.
* The ‘en_core _web_sm’ model is widely used, so it is easy to integrate sentiment analysis with other NLP.

### Limitations:
* The ‘en_core _web_sm’ model may not be capable of identifying more nuanced language and context. Therefore, it may not be as accurate as other models.
* The ‘en_core _web_sm’ model may have limited vocabulary/lack domain knowledge resulting in inaccurate sentiment predictions. 
* The sentiment analysis we performed gave us the average sentiment score per product, however this did not indicate the total number of reviews, or the distribution of sentiment scores. Additionally, the date of each review was not considered - older positive reviews may be less accurate than more recent, negative reviews, e.g.: if the product has changed supplier and suffered a defect in quality.
* When SpaCy removes the stop words from the reviews, it can completely change the meaning of the reviews in the cleaned reviews (See example below).

| Text Review | Cleaned Text Review |
| ----------- | ------------------- |
| ‘Very cheap and was not impressed at all never again’ | ‘cheap impressed’ |




## Example Output
Bar plot shows all of the reviewed Amazon products against their average sentiment analysis score. 
![Average Sentiment Analysis per Product](https://github.com/cgreenwood23/finalCapstone/assets/153872154/aef94e25-2954-4d93-8cbb-1d59a0af4794)


## Run Locally:

### Install dependencies:

Using pip:
```sh
pip install -r requirements.txt
```

## Usage:

Using pip:
```sh
python3 sentiment_analysis.py
```

## License
MIT License
