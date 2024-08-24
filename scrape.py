import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time

class SteelSupplierScraper:
    def __init__(self, base_url, categories, load_wait_time=3):
        self.base_url = base_url
        self.categories = categories
        self.load_wait_time = load_wait_time

    def fetch_item_links(self, url):
        print(f"Fetching item links from URL: {url}\n")
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        item_links = []
        for link in soup.find_all('a', class_='wpupg-item-link'):
            href = link.get('href', '')
            if href:
                full_url = requests.compat.urljoin(url, href)
                item_links.append(full_url)

        print(f"Filtered down to {len(item_links)} item links.")
        return item_links

    def extract_details_from_item(self, item_url):
        print(f"Extracting details from item URL: {item_url}")
        response = requests.get(item_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        details = {'company_name': 'N/A', 'supplier_name': 'N/A', 'street': 'N/A', 'address': 'N/A', 'phone': 'N/A', 'mail': 'N/A', 'website': 'N/A', 'facebook': 'N/A', 'instagram': 'N/A', 'linkedin': 'N/A'}

        # Extract company name
        h3_tag = soup.find('h1')
        if h3_tag:
            details['company_name'] = h3_tag.get_text(strip=True)
            print(f"Company name: {details['company_name']}")

        # Extract other details
        widget_div = soup.find('div', class_='supplier--hide-mobile')
        if widget_div:
            p_tags = widget_div.find_all('p')
            print(f"Found {len(p_tags)} <p> tags.")
            
            if len(p_tags) > 0:
                # 1. p etiketi
                text = p_tags[0].get_text().split('\n')
                print(f"1st <p> text: {text}")
                if len(text) == 3:
                    details['supplier_name'] = text[0]
                    details['street'] = text[1]
                    details['address'] = text[-1]

                elif len(text) >= 4:
                    # 4 değer varsa: supplier_name, position, street, address
                    details['supplier_name'] = text[0]
                    details['position'] = text[1]
                    details['street'] = text[2]
                    details['address'] = text[-1]

            if len(p_tags) > 1:
                # 2. p etiketi
                a_tag = p_tags[1].find('a')
                if a_tag:
                    details['phone'] = a_tag.get_text(strip=True)
                    print(f"Phone number: {details['phone']}")

            if len(p_tags) > 2:
                # 3. p etiketi
                a_tag = p_tags[2].find('a')
                if a_tag:
                    mailto_href = a_tag.get('href', '')
                    details['mail'] = mailto_href.replace('mailto:', '').strip()
                    print(f"Email: {details['mail']}")

            if len(p_tags) > 3:
                # 4. p etiketi
                a_tag = p_tags[3].find('a')
                if a_tag:
                    details['website'] = a_tag.get_text(strip=True)
                    print(f"Website: {details['website']}")

        # Find social media links
        socials_div = soup.find('div', class_='supplier--socials')
        if socials_div:
            facebook = socials_div.find('a', class_='facebook')
            if facebook:
                details['facebook'] = facebook.get('href', 'N/A')
                print(f"Facebook URL: {details['facebook']}")

            instagram = socials_div.find('a', class_='instagram')
            if instagram:
                details['instagram'] = instagram.get('href', 'N/A')
                print(f"Instagram URL: {details['instagram']}")

            linkedin = socials_div.find('a', class_='linkedin')
            if linkedin:
                details['linkedin'] = linkedin.get('href', 'N/A')
                print(f"LinkedIn URL: {details['linkedin']}")

        return details

    def scrape_all_categories(self):
        all_details = []
        for category in self.categories:
            url = f'{self.base_url}#fas+steel-supplier-cat:{category}'
            print(f"Scraping category: {category}")
            print(f"Constructed URL: {url}")

            item_links = self.fetch_item_links(url)
            print(f"Found {len(item_links)} item links.")

            for link in item_links:
                details = self.extract_details_from_item(link)
                all_details.append(details)
                print(f"Details extracted for item: {link}\n")

        df = pd.DataFrame(all_details)
        df.to_csv('supplier_details.csv', index=False, encoding='utf-8-sig')
        print(f"Supplier details have been saved to 'supplier_details.csv'.")

if __name__ == "__main__":
    base_url = 'https://buildsteel.org/products-and-providers/#fas+steel-supplier-cat:'
    categories = ['cfs-manufacturer']
    scraper = SteelSupplierScraper(base_url=base_url, categories=categories)
    scraper.scrape_all_categories()
