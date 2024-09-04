import requests
from bs4 import BeautifulSoup

# URL de la page à scraper
url = 'https://pubmed.ncbi.nlm.nih.gov/29717108/'

# Envoyer une requête GET pour récupérer le contenu de la page
response = requests.get(url)

# Vérifier que la requête a réussi
if response.status_code == 200:
    # Parser le contenu HTML avec BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Trouver l'élément <div> avec la classe "abstract-content"
    abs_block = soup.find('div', {'class': 'abstract-content'})

    # Extraire le texte de l'élément <p> à l'intérieur de cette <div>
    if abs_block:
        p_abs = abs_block.find('p').get_text(strip=True)
        print(p_abs)
    else:
        print("Aucun élément 'abstract' trouvé")
    # Extract title
    title_block = soup.find('h1', {'class': 'heading-title'})
    if title_block:
        p_tit = title_block.get_text(strip=True)
        print(p_tit)
    else:
        print("Aucun élément 'titre' trouvé")
    author_section = soup.find('div', {'class': 'inline-authors'})
    if author_section:
        authors = author_section.find_all('a', {'class': 'full-name'})
        for name in authors:
            print(name.text)
    else:
        print("Aucun élément 'auteur' trouvé")
    doi_section = soup.find('span', {'class': "identifier doi"})
    doi_block = doi_section.find('a', {'class': 'id-link'})
    if doi_block:
        p_doi = doi_block.get_text(strip=True)
        print(p_doi)
    else:
        print("Aucun élément 'doi' trouvé")
    journal_block = soup.find('button', {'id': 'full-view-journal-trigger'})
    if journal_block:
        p_journal = journal_block.get_text(strip=True)
        print(p_journal)
    else:
        print("Aucun élément 'journal' trouvé")
    ref_block = soup.find('span', {'class': 'cit'})
    if ref_block:
        p_ref = ref_block.get_text(strip=True)
        print(p_ref)
    else:
        print("Aucun élément 'ref' trouvé")
    aff_section = soup.find('div', {'class': 'affiliations'})
    if aff_section :
        aff_blocks = aff_section.find_all('li')
        aff = list(set([aff_block.get_text(strip=True) for aff_block in aff_blocks]))
        for affi in aff_blocks:
            print(affi.text[2:])
        conflict_block = soup.find('div', {'class': 'statement'})
    if conflict_block:
        p_conflict = conflict_block.find('p').get_text(strip=True)
        print(p_conflict)
    else:
        print("Aucun élément 'conflict' trouvé")


else:
    print(f"Échec de la requête, code d'erreur: {response.status_code}")
