import requests
import bs4

def search_wikihow(search_term):
    #print "Seaching wikihow for " + search_term
    search_url = "http://www.wikihow.com/wikiHowTo?search="
    search_term_query = search_term.replace(" ", "+")
    search_url += search_term_query
    # print search_url
    # open url
    html = get_html(search_url)
    soup = bs4.BeautifulSoup(html, "lxml")
    # parse for links
    list = []
    links = soup.findAll('a', attrs={'class': "result_link"})
    for link in links:
        url = "http:" + link.get('href')
        list.append(url)
    return list


def get_html(url):
    headers = {'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0"}
    r = requests.get(url, headers=headers)
    html = r.text.encode("utf8")
    return html


def get_steps(url):
    # open url
    html = get_html(url)
    soup = bs4.BeautifulSoup(html, "lxml")

    # get title
    title_html = soup.findAll("h1", {"class": "firstHeading"})
    for html in title_html:
        url = "http:" + html.find("a").get("href")
    title = url.replace("http://www.wikihow.com/", "").replace("-", " ")

    # get steps
    steps = []
    ex_steps = []
    step_html = soup.findAll("div", {"class": "step"})
    for html in step_html:
        step = html.find("b")
        step = step.text

        trash = str(html.find("script"))
        trash = trash.replace("<script>", "").replace("</script>", "").replace(";", "")
        ex_step = html.text.replace(trash, "")

        trash_i = ex_step.find("//<![CDATA[")
        trash_e = ex_step.find(">")
        trash = ex_step[trash_i:trash_e+1]
        ex_step = ex_step.replace(trash, "")

        trash_i = ex_step.find("http://")
        trash_e = ex_step.find(".mp4")
        trash = ex_step[trash_i:trash_e + 4]
        ex_step = ex_step.replace(trash, "")

        trash = "WH.performance.mark('step1_rendered');"
        ex_step = ex_step.replace(trash, "")
        ex_step = ex_step.replace("\n", "")

        steps.append(step)
        ex_steps.append(ex_step)

    # get step pic
    pic_links = []
    pic_html = soup.findAll("a", {"class": "image lightbox"})

    for html in pic_html:
        html = html.find("img")
        i = str(html).find("data-src=")
        pic = str(html)[i:].replace('data-src="', "")
        i = pic.find('"')
        pic = pic[:i]
        pic_links.append(pic)

    # link is returned in case of random link
    return title, steps, ex_steps, pic_links, url


def get_how_tos(subject):
    how_tos = {}
    links = search_wikihow(subject)
    if links == []:
        print "No wikihow results"
        return
    for link in links:
        how_to = {}
        # get steps and pics
        title, steps, descript, pics, link = get_steps(link)
        how_to["title"] = title
        how_to["steps"] = steps
        how_to["detailed"] = descript
        how_to["pics"] = pics
        how_to["url"] = link
        how_tos[title] = how_to
    return how_tos

def random_how_to():
    link = "http://www.wikihow.com/Special:Randomizer"
    # get steps and pics
    title, steps, descript, pics, link = get_steps(link)
    how_to = {}
    how_to["title"] = title
    how_to["steps"] = steps
    how_to["detailed"] = descript
    how_to["pics"] = pics
    how_to["url"] = link
    return how_to


#### example

def main():
    # get random how to

    how_to = random_how_to()
    print how_to["title"]
    print how_to["steps"]

    # search how tos about
    subject = "boil an egg"
    how_tos = get_how_tos(subject)

    print "searched for " + subject + " and found following the how tos:"
    for how in how_tos:
        print "\nHow to " + how

    # get detailed info of how to
    for how in how_tos:
        print "\nDetailed description of : " + how
        i = 0
        for step in how_tos[how]["steps"]:
            print "\nstep " + str(i+1) + " : " + step
            print how_tos[how]["detailed"][i]
            # TODO check pic link, some steps dont have pics!, parsing is wrong
            try:
                print how_tos[how]["pics"][i]
            except:
                print "parse the damn pic links for missing step pics"
            i += 1
        print "\n\n"
        break

main()
