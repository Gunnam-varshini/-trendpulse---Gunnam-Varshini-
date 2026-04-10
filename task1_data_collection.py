import requests

import time

import json

import os

from datetime import datetime



# API URLs

TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"

ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"



# Headers

headers = {"User-Agent": "TrendPulse/1.0"}



# Categories with keywords

CATEGORIES = {

  "technology": ["AI", "software", "tech", "code", "computer", "data", "cloud", "API", "GPU", "LLM"],

  "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],

  "sports": ["NFL", "NBA", "FIFA", "sport", "game", "team", "player", "league", "championship"],

  "science": ["research", "study", "space", "physics", "biology", "discovery", "NASA", "genome"],

  "entertainment": ["movie", "film", "music", "Netflix", "game", "book", "show", "award", "streaming"]

}



# Function to categorize title

def get_category(title):

  title_lower = title.lower()

  for category, keywords in CATEGORIES.items():

    for keyword in keywords:

      if keyword.lower() in title_lower:

        return category

  return "others"



# Step 1: Fetch top story IDs

def fetch_top_story_ids():

  try:

    response = requests.get(TOP_STORIES_URL, headers=headers)

    return response.json()

  except:

    print("Failed to fetch top stories")

    return []



# Step 2: Fetch story details

def fetch_story(story_id):

  try:

    url = ITEM_URL.format(story_id)

    response = requests.get(url, headers=headers)

    return response.json()

  except:

    print(f"Failed to fetch story {story_id}")

    return None



def main():

  story_ids = fetch_top_story_ids()



  collected_data = []

  category_count = {cat: 0 for cat in CATEGORIES}



  for story_id in story_ids:

    story = fetch_story(story_id)

    if not story or "title" not in story:

      continue



    category = get_category(story["title"])



    # Limit 25 per category

    if category not in category_count or category_count[category] >= 25:

      continue



    data = {

      "post_id": story.get("id"),

      "title": story.get("title"),

      "category": category,

      "score": story.get("score", 0),

      "num_comments": story.get("descendants", 0),

      "author": story.get("by"),

      "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    }



    collected_data.append(data)

    category_count[category] += 1



    # Stop when 125 stories collected

    if sum(category_count.values()) >= 125:

      break



  # Step 3: Save JSON

  if not os.path.exists("data"):

    os.makedirs("data")



  filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"



  with open(filename, "w") as f:

    json.dump(collected_data, f, indent=4)



  print(f"Saved {len(collected_data)} stories to {filename}")



# Run

if __name__ == "__main__":

  main()