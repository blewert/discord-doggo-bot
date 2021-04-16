import requests
import json
import random

class FlickrPhotosAPI:

    def __init__(self, key):
        self.key = key;
        self.base_url = r"https://www.flickr.com/services/rest/?method=flickr.photos.search";

    def get_kv_format(self, key, value):

        # List? Return csv format
        if isinstance(value, list):
            return f"&{key}={','.join(value)}";

        # Otherwise return normal format
        else:
            return f"&{key}={value}";


    def get_search_result(self, url):

        # Fire the request, get response
        response = requests.get(url);

        # Not a 200 OK? throw an error
        if response.status_code != 200:
            raise Exception("Flickr API unreachable.");

        # Otherwise:
        return response.text;

    def to_flickr_url(self, item):
        suffix = 'b';
        return f"https://live.staticflickr.com/{item['server']}/{item['id']}_{item['secret']}_{suffix}.jpg";

    def random_search(self, tags):

        # Start with the base
        url = self.base_url;

        # Add required params
        url += self.get_kv_format("api_key", self.key);
        url += self.get_kv_format("nojsoncallback", "1");
        url += self.get_kv_format("tags", tags);
        url += self.get_kv_format("format", "json");
        url += self.get_kv_format("sort", "date-posted-asc");
        url += self.get_kv_format("per_page", "500");
        url += self.get_kv_format("content_type", "1"); # photos

        # And get the result
        results = self.get_search_result(url);

        # Parse results and show items
        parsed_json = json.loads(results);
        items = parsed_json["photos"]["photo"];

        # Choose a random one
        item = random.choice(items);

        # Find url from item and return it
        photo_url = self.to_flickr_url(item);
        return photo_url;
