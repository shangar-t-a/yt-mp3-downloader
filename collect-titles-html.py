from bs4 import BeautifulSoup


def extract_titles(html_script):
    titles = []
    soup = BeautifulSoup(html_script, "html.parser")
    td_tags = soup.find_all("td", class_="column-3")
    for td_tag in td_tags:
        a_tag = td_tag.find("a")
        if a_tag:
            title = a_tag.get_text().strip()
            titles.append(title)
    return titles


# Example usage
with open("song-list.html", "r") as file:
    html = file.read()

title_list = extract_titles(html)
print(title_list)
