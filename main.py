# import requests
# from bs4 import BeautifulSoup
# import json

# # Fonction pour récupérer tous les liens de pages
# def get_all_page_links(total_pages: int) -> list:
#     urls = []
#     for page in range(1, total_pages + 1):
#         url = f"https://www.idealwine.com/fr/acheter-du-vin/quantite-1-page-{page}?order-by=price-desc"
#         urls.append(url)
#     return urls

# # Fonction pour récupérer les liens de chaque vin sur une page
# def get_wine_links_from(page_link: str) -> list:
#     domain = "https://www.idealwine.com"
#     response = requests.get(page_link)
#     links = []
#     if response.status_code != 200:
#         print(f"ERROR - Status code: {response.status_code}")
#     else:
#         content_html = response.text
#         soup = BeautifulSoup(content_html, "html.parser")
#         all_tag_div = soup.find_all("a", class_="ProductCard_linkToProduct__5qsdl")
#         for tag_div in all_tag_div:
#             link = domain + tag_div.get("href")
#             links.append(link)
#     return links

# # Fonction pour extraire les informations d'un vin à partir de son lien
# def get_wine_info(wine_link: str) -> dict:
#     response = requests.get(wine_link)
#     wine_info = {}

#     if response.status_code == 200:
#         # Analyse le contenu de la page avec BeautifulSoup
#         soup = BeautifulSoup(response.text, 'html.parser')
        
#         # Extraction des caractéristiques détaillées
#         tags = soup.find_all('p', class_='DetailedCharacteristics_item__K7AGY')
        
#         for tag in tags:
#             text = tag.get_text().strip()
#             if ':' in text:
#                 key, value = text.split(":", 1)
#                 wine_info[key.strip()] = value.strip()
#             else:
#                 wine_info[text.strip()] = None

#         # Extraction du type de vente
#         sale_type_tag = soup.find('span', class_='ProductVariantMainDescription_mainTitle__mtqGi')
#         if sale_type_tag:
#             wine_info["Type de vente"] = sale_type_tag.get_text().strip()

#         # Extraction du nom du vin
#         wine_name_tag = soup.find('h1', class_='ProductVariantMainDescription_title__x4Ov4')
#         if wine_name_tag:
#             wine_info["Nom du vin"] = wine_name_tag.get_text().strip()

#         # Extraction du prix du vin 
#         wine_price_tag = soup.find('span',class_='Price_units__UHpM6')
#         if wine_price_tag:
#             wine_info["Prix"] = wine_price_tag.get_text().strip()
        
#     else:
#         print(f"Erreur lors de la requête HTTP : {response.status_code} pour le lien {wine_link}")

#     return wine_info

# # Fonction principale
# def main():
#     # Nombre de pages à traiter
#     total_pages = 2

#     # Récupère toutes les pages
#     page_links = get_all_page_links(total_pages)

#     # Liste pour stocker les informations de tous les vins
#     all_wines_info = []

#     # On itère sur toutes les pages pour récupérer les liens de chaque vin
#     for i, page_link in enumerate(page_links):
#         print(f"Getting links for page {i + 1}")
#         wine_links = get_wine_links_from(page_link)
        
#         for wine_link in wine_links:
#             print(f"Extracting information from {wine_link}")
#             wine_info = get_wine_info(wine_link)
#             all_wines_info.append(wine_info)

#     # Sauvegarde toutes les informations dans un fichier JSON
#     with open('all_wines_info.json', 'w', encoding='utf-8') as file:
#         json.dump(all_wines_info, file, ensure_ascii=False, indent=4)

#     print("Extraction terminée et enregistrée dans 'all_wines_info.json'")

# # Exécute le programme principal
# main()

import requests
from bs4 import BeautifulSoup
import json

# Fonction pour récupérer tous les liens de pages
def get_all_page_links(total_pages: int) -> list:
    urls = []
    for page in range(1, total_pages + 1):
        url = f"https://www.idealwine.com/fr/acheter-du-vin/quantite-1-page-{page}?order-by=price-desc"
        urls.append(url)
    return urls

# Fonction pour récupérer les liens de chaque vin sur une page
def get_wine_links_from(page_link: str) -> list:
    domain = "https://www.idealwine.com"
    response = requests.get(page_link)
    links = []
    if response.status_code != 200:
        print(f"ERROR - Status code: {response.status_code}")
    else:
        content_html = response.text
        soup = BeautifulSoup(content_html, "html.parser")
        all_tag_div = soup.find_all("a", class_="ProductCard_linkToProduct__5qsdl")
        for tag_div in all_tag_div:
            link = domain + tag_div.get("href")
            links.append(link)
    return links

# Fonction pour extraire les informations d'un vin à partir de son lien
def get_wine_info(wine_link: str) -> dict:
    response = requests.get(wine_link)
    wine_info = {}

    if response.status_code == 200:
        # Analyse le contenu de la page avec BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extraction des caractéristiques détaillées
        tags = soup.find_all('p', class_='DetailedCharacteristics_item__K7AGY')
        
        for tag in tags:
            text = tag.get_text().strip()
            if ':' in text:
                key, value = text.split(":", 1)
                wine_info[key.strip()] = value.strip()
            else:
                wine_info[text.strip()] = None

        # Extraction du type de vente
        sale_type_tag = soup.find('span', class_='ProductVariantMainDescription_mainTitle__mtqGi')
        if sale_type_tag:
            wine_info["Type de vente"] = sale_type_tag.get_text().strip()

        # Extraction du nom du vin
        wine_name_tag = soup.find('h1', class_='ProductVariantMainDescription_title__x4Ov4')
        if wine_name_tag:
            wine_info["Nom du vin"] = wine_name_tag.get_text().strip()

        # Extraction du prix du vin 
        wine_price_tag = soup.find('span', class_='Price_units__UHpM6')
        if wine_price_tag:
            wine_info["Prix"] = wine_price_tag.get_text().strip()
        
        # Extraction de l'encépagement
        enc_tags = soup.find_all('div', class_='DetailedCharacteristics_item__K7AGY')
        for enc_tag in enc_tags:
            enc_label = enc_tag.find('span', class_='DetailedCharacteristics_characteristic__NlZ4C')
            enc_value = enc_tag.find_all('span')[-1]  # Utilisation du dernier <span> pour la valeur de l'encépagement
            if enc_label and enc_value and "Encépagement" in enc_label.get_text():
                wine_info["Encépagement"] = enc_value.get_text().strip()
                break  # Arrête la recherche dès qu'on a trouvé l'encépagement
    
    else:
        print(f"Erreur lors de la requête HTTP : {response.status_code} pour le lien {wine_link}")

    return wine_info

# Fonction principale
def main():
    # Nombre de pages à traiter
    total_pages = 190

    # Récupère toutes les pages
    page_links = get_all_page_links(total_pages)

    # Liste pour stocker les informations de tous les vins
    all_wines_info = []

    # On itère sur toutes les pages pour récupérer les liens de chaque vin
    for i, page_link in enumerate(page_links):
        print(f"Getting links for page {i + 1}")
        wine_links = get_wine_links_from(page_link)
        
        for wine_link in wine_links:
            print(f"Extracting information from {wine_link}")
            wine_info = get_wine_info(wine_link)
            all_wines_info.append(wine_info)

    # Sauvegarde toutes les informations dans un fichier JSON
    with open('all_wines_info.json', 'w', encoding='utf-8') as file:
        json.dump(all_wines_info, file, ensure_ascii=False, indent=4)

    print("Extraction terminée et enregistrée dans 'all_wines_info.json'")

# Exécute le programme principal
main()


