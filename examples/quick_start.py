from pywikihow import WikiHow

# get a random how to
random_how_to = WikiHow.random()

# search wikihow pages
urls = WikiHow.search("buy bitcoin")

# parse a specific page
title, steps, ex_steps, pic_links, url = WikiHow.parse("https://www.wikihow.com/Train-a-Dog")

# search how to X
results = WikiHow.how_to("boil an egg")

# navigate results
for how_to in results:
    data = results[how_to]
    title = data["title"]
    url = data["url"]
    steps = data["steps"]
    for step in steps:
        text = step["step"]
        extended_description = step["detailed"]
        picture = step["pic"]
