"""import requests
import string
from bs4 import BeautifulSoup

Enter_input = input("Search: ")
u_i = string.capwords(Enter_input)
lists = u_i.split()
word = " ".join(lists)

url = "https://fr.wikipedia.org/wiki/"+word

def wikibot(url):
    url_open = requests.get(url)
    soup = BeautifulSoup(url_open.content, 'html.parser')
    details = soup('table', {'class': 'infobox'})
    for i in details:
        h =i.find_all('tr')
        for j in h:
            heading = j.find_all('th')
            detail = j.find_all('td')
            if heading is not None and detail is not None:
                for x, y in zip(heading, detail):
                    print("{} :: {}".format(x.test, y.test))
                    print("-------------")

    for i in range(1, 3):
        print(soup('p')[i].text)
        wikibot(url)"""

import requests
from bs4 import BeautifulSoup


def extract_wikipedia_content(url):
    # Fonction pour obtenir le contenu HTML d'une page Wikipédia
    response = requests.get(url)
    response.raise_for_status()  # Vérifie si la requête a réussi
    soup = BeautifulSoup(response.content, 'html.parser')

    # Fonction pour extraire le titre de l'article
    def get_title(soup):
        title = soup.find('h1').text
        return title

    # Fonction pour extraire le texte de l'article avec titres respectifs
    def get_paragraphs(soup):
        content = {}
        for header in soup.find_all(['h2', 'h3']):  # On prend en compte les titres de niveau 2 et 3
            title = header.text.strip()
            paragraphs = []
            for sibling in header.find_next_siblings():
                if sibling.name in ['h2', 'h3']:  # Arrêter à un autre titre
                    break
                if sibling.name == 'p':  # On ne garde que les paragraphes
                    paragraphs.append(sibling.text.strip())
            content[title] = ' '.join(paragraphs)  # Joint les paragraphes associés au titre
        return content

    # Fonction pour collecter les liens vers d'autres pages Wikipédia
    def get_links(soup):
        links = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.startswith('/wiki/') and not href.startswith('/wiki/File:'):
                full_url = f"https://fr.wikipedia.org{href}"
                links.append(full_url)
        return links

    # Regrouper les résultats
    title = get_title(soup)
    paragraphs = get_paragraphs(soup)
    links = get_links(soup)

    return {
        'title': title,
        'paragraphs': paragraphs,
        'links': links
    }


# Tester la fonction sur la page d'Al-Ghazali
url = "https://fr.wikipedia.org/wiki/Al-Ghazali"
result = extract_wikipedia_content(url)

# Afficher les résultats
print("Titre:", result['title'])
print("\nParagraphes:")
for title, text in result['paragraphs'].items():
    print(f"{title}: {text[:100]}...")  # Affiche les 100 premiers caractères
print("\nLiens:")
for link in result['links'][:5]:  # Affiche les 5 premiers liens
    print(link)