#
# @file   flickr.py
# @brief  A minimal interface to the flickr search api.
# @author ben <bwilliams@lincoln.ac.uk>
#

import requests
import json
import random
import re
import util

class FlickrPhotosAPI:

    def __init__(self, key):
        self.key = key;
        self.last_url = "";
        self.last_response = "";
        self.base_url = r"https://www.flickr.com/services/rest/?method=flickr.photos.search";

    def get_search_result(self, url) -> str:

        # Fire the request, get response
        response = requests.get(url);

        # Not a 200 OK? throw an error
        if response.status_code != 200:
            raise Exception("Flickr API unreachable.");

        # Otherwise:
        return response.text;

    def to_flickr_url(self, item) -> str:

        # Maps flickr img object to url according to the schema linked below.
        # <https://www.flickr.com/services/api/misc.urls.html>
        # ..
        #  
        suffix = 'b';
        return f"https://live.staticflickr.com/{item['server']}/{item['id']}_{item['secret']}_{suffix}.jpg";

    def remove_api_key(self, url) -> str:

        # Hide api_key for detailed error feedback without compromising your api use key
        return re.sub(r'\&api_key=(.+?)\&', '&api_key=<API_KEY>', url);

    def random_search(self, tags, text) -> str:

        # Start with the base
        url = self.base_url;

        # Add required params
        url += util.get_kv_format("nojsoncallback", "1");
        url += util.get_kv_format("api_key", self.key);
        url += util.get_kv_format("tags", tags);
        url += util.get_kv_format("text", text);
        url += util.get_kv_format("format", "json");
        url += util.get_kv_format("sort", "relevance")
        url += util.get_kv_format("content_type", "1"); # photos
        url += util.get_kv_format("per_page", "500");

        # Print the url for debug purposes
        print(url);

        # And get the result
        results = self.get_search_result(url);

        # Parse results and show items
        parsed_json = json.loads(results);
        self.last_response = parsed_json;
        items = parsed_json["photos"]["photo"];

        # Choose a random one
        item = random.choice(items);
        self.last_url = self.remove_api_key(url);

        # Find url from item and return it
        photo_url = self.to_flickr_url(item);
        return photo_url;
