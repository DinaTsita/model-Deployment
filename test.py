from predict import predict_url
from url_processor import process_url
url ='https://www.britannica.com'


features = process_url(url)
predictions = predict_url(features)

print(predictions)
