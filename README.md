# PyWikiHow
[![Donate with Bitcoin](https://en.cryptobadges.io/badge/micro/1QJNhKM8tVv62XSUrST2vnaMXh5ADSyYP8)](https://en.cryptobadges.io/donate/1QJNhKM8tVv62XSUrST2vnaMXh5ADSyYP8)
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://paypal.me/jarbasai)
<span class="badge-patreon"><a href="https://www.patreon.com/jarbasAI" title="Donate to this project using Patreon"><img src="https://img.shields.io/badge/patreon-donate-yellow.svg" alt="Patreon donate button" /></a></span>
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/JarbasAl)

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
  
