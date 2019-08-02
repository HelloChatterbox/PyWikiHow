import requests
import bs4


class WikiHow(object):

    @staticmethod
    def search(search_term):
        search_url = "http://www.wikihow.com/wikiHowTo?search="
        search_term_query = search_term.replace(" ", "+")
        search_url += search_term_query
        html = WikiHow._get_html(search_url)
        soup = bs4.BeautifulSoup(html, 'html.parser')
        list = []
        links = soup.findAll('a', attrs={'class': "result_link"})
        for link in links:
            url = link.get('href')
            if not url.startswith("http"):
                url = "http://" + url
            list.append(url)
        return list

    @staticmethod
    def _get_html(url):
        headers = {'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0"}
        r = requests.get(url, headers=headers)
        html = r.text.encode("utf8")
        return html

    @staticmethod
    def parse(url):
        # open url
        html = WikiHow._get_html(url)
        soup = bs4.BeautifulSoup(html, 'html.parser')

        # get title
        title_html = soup.findAll("h1", {"class": "firstHeading"})
        for html in title_html:
            url = html.find("a").get("href")
            if not url.startswith("http"):
                url = "http://" + url
        title = url.split("/")[-1].replace("-", " ")

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

    @staticmethod
    def how_to(subject, num=3):
        how_tos = {}
        links = WikiHow.search(subject)
        if not links:
            print("No wikihow results")
            return {}
        for idx, link in enumerate(links):
            if idx > num:
                break
            how_to = {}
            # get steps and pics
            title, steps, descript, pics, link = WikiHow.parse(link)
            how_to["title"] = title
            how_to["url"] = link

            items = []
            for i in range(len(steps)):
                item = {"step": steps[i],
                        "detailed": descript[i],
                        "pic": None}
                # there are only pics sometimes, but in general they seem to have the step number in the name
                for p in pics:
                    if "step-" + str(i+1) in p.split("/")[-1].lower():
                        item["pic"] = p
                        break
                items.append(item)

            how_to["steps"] = items

            how_tos[title] = how_to

        return how_tos

    @staticmethod
    def random():
        link = "http://www.wikihow.com/Special:Randomizer"
        title, steps, descript, pics, link = WikiHow.parse(link)
        how_to = {}
        how_to["title"] = title
        how_to["url"] = link
        items = []
        for i in range(len(steps)):
            item = {"step": steps[i],
                    "detailed": descript[i],
                    "pic": None}
            # there are only pics sometimes, but in general they seem to have the step-number in the name
            for p in pics:
                if "step-" + str(i + 1) in p.split("/")[-1].lower():
                    item["pic"] = p
                    break
            items.append(item)

        how_to["steps"] = items
        return how_to
