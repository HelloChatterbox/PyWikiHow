# PyWikiHow

unofficial wikihow python api


    from pywikihow import WikiHow

    random_how_to = WikiHow.random()
    urls = WikiHow.search("buy bitcoin")
    how_tos = WikiHow.how_to("boil an egg")

    for how_to in how_tos:
      title = how_to["title"]
      url = how_to["url"]
      steps = how_to["steps"]
      for step in steps:
        text = step["step"]
        extended_description = step["detailed"]
        picture = step["pic"]
        
     title, steps, ex_steps, pic_links, url = WikiHow.parse("https://www.wikihow.com/Train-a-Dog")
  
