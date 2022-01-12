import requests
import json
# import related models here
from .models import CarDealer
from requests.auth import HTTPBasicAuth


# Create a `get_request` to make HTTP GET requests
# e.g., response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
#                                     auth=HTTPBasicAuth('apikey', api_key))
def get_request(url, **kwargs):
    print(kwargs)
    print("GET from {} ".format(url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(url, headers={'Content-Type': 'application/json'},
                                    params=kwargs)
    except:
        # If any error occurs
        print("Network exception occurred")
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data

# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)


# Create a get_dealers_from_cf method to get dealers from a cloud function
# def get_dealers_from_cf(url, **kwargs):
# - Call get_request() with specified arguments
# - Parse JSON results into a CarDealer object list
def get_dealers_from_cf(url, **kwargs):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url)
    print(json_result)
    if json_result:
        # Get the row list in JSON as dealers
        dealers = json_result["docs"]
        # For each dealer object
        for dealer in dealers:
            # Get its content in `doc` object
            dealer_str = json.dumps(dealer,sort_keys=True)
            dealer_json = json.loads(dealer_str)
            dealer_doc = dealer_json.items()

            p_address = ''
            p_city = ''
            p_id = ''
            p_lat = ''
            p_long = ''
            p_full_name = ''
            p_short_name = ''
            p_st = ''
            p_zip = ''

            for key,value in dealer_doc:
                if key == "address":
                    p_address = value
                elif key == "city":
                    p_city = value
                elif key == "id":
                    p_id = value
                elif key == "lat":
                    p_lat = value
                elif key == "long":
                    p_long = value
                elif key == "full_name":
                    p_full_name = value
                elif key == "short_name":
                    p_short_name = value
                elif key == "st":
                    p_st = value
                elif key == "zip":
                    p_zip = value
            
            # Create a CarDealer object with values in `doc` object
            # dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], full_name=dealer_doc["full_name"],
            #                        id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"],
            #                        short_name=dealer_doc["short_name"],
            #                        st=dealer_doc["st"], zip=dealer_doc["zip"])
            dealer_obj = CarDealer(address=p_address, city=p_city, full_name=p_full_name,
                                   id=p_id, lat=p_lat, long=p_long,
                                   short_name=p_short_name,
                                   st=p_st, zip=p_zip)
            results.append(dealer_obj)

    return results

# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
# def get_dealer_by_id_from_cf(url, dealerId):
# - Call get_request() with specified arguments
# - Parse JSON results into a DealerView object list


# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative



