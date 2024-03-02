from url_processor import process_url
from feature_extractor import extract_features, is_URL_accessible
#df = extract_features("https://medium.com")






import requests

page = requests.get('https://www.britannica.com')
print(page)