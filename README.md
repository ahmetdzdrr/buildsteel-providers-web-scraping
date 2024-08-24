# BuildSteel Providers Web Scraping

![Screenshot 2024-08-25 at 01 32 34](https://github.com/user-attachments/assets/a456aec3-e74d-4b4f-9d54-b6b7d22cca41)

This project is a web scraping tool designed to collect data on steel providers listed on specific websites. The script extracts important details such as company names, contact information, and services provided. This data can be utilized for market research, business development, or data analysis.

## Features
- **Automated Scraping**: The script uses Python's `requests` and `BeautifulSoup` libraries to automate the data extraction process.
- **Data Export**: The scraped data is structured and saved in a CSV format, making it easy to analyze or import into other tools.
- **Configurable Targets**: The URLs to be scraped can be easily modified in the script to target different providers or websites.
- **Error Handling**: Basic error handling is implemented to manage connection issues and ensure the script runs smoothly.

## Requirements
- Python 3.x
- `requests`
- `BeautifulSoup`

You can install the required libraries using the following command:

```bash
pip install -r requirements.txt
```

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/ahmetdzdrr/buildsteel-providers-web-scraping.git
   ```
2. Navigate to the project directory:
   ```bash
   cd buildsteel-providers-web-scraping
   ```
3. Run the scraping script:
   ```bash
   python scrape.py
   ```

The output CSV file will be generated in the project directory, containing the extracted data.

## Customization
- **Target URLs**: Update the `urls` list in the `scrape.py` script to specify the web pages you want to scrape.
- **Data Fields**: Modify the parsing logic in the script to extract additional fields or adjust the structure of the output data.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.

## Contact
For any inquiries or issues, please contact [LinkedIn](https://www.linkedin.com/in/ahmet-dizdarr/).
