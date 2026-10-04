# Import necessary packages
import pandas as pd
import numpy as np

# Import CSV for prices
airbnb_price = pd.read_csv('data/airbnb_price.csv')

# Import Excel file for room types
airbnb_room_type = pd.read_excel('data/airbnb_room_type.xlsx')

# Import TSV for review dates
airbnb_last_review = pd.read_csv('data/airbnb_last_review.tsv', sep='\t')

# Join the three data frames together into one
listings = pd.merge(airbnb_price, airbnb_room_type, on='listing_id')
listings = pd.merge(listings, airbnb_last_review, on='listing_id')

# What are the dates of the earliest and most recent reviews?
# To use a function like max()/min() on last_review date column, it needs to be converted to datetime type
listings['last_review_date'] = pd.to_datetime(listings['last_review'], format='%B %d %Y')
first_reviewed = listings['last_review_date'].min()
last_reviewed = listings['last_review_date'].max()

# How many of the listings are private rooms?
# Since there are differences in capitalization, make capitalization consistent
listings['room_type'] = listings['room_type'].str.lower()
private_room_count = listings[listings['room_type'] == 'private room'].shape[0]

# What is the average listing price?
# To convert price to numeric, remove " dollars" from each value
listings['price_clean'] = listings['price'].str.replace(' dollars', '').astype(float)
avg_price = listings['price_clean'].mean()

review_dates = pd.DataFrame({
    'first_reviewed': [first_reviewed],
    'last_reviewed': [last_reviewed],
    'nb_private_rooms': [private_room_count],
    'avg_price': [round(avg_price, 2)]
})

print(review_dates)