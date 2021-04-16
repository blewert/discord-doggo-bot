import random
import json
from flickr import FlickrPhotosAPI


class PuppersAPI(FlickrPhotosAPI):

    def __init__(self, key):
        super().__init__(key);
        self.types = self.load_json(r"data/puppy_types.json");
        self.required_terms = self.load_json(r"data/search_tags.json");
        self.random_errors = self.load_json(r"data/random_errors.json");
        self.random_ratings = self.load_json(r'data/rating_strings.json');

    def load_json(self, uri):
        with open(uri, 'r') as fp:
            return json.load(fp);

    def random_rating(self, text):
        return random.choice(self.random_ratings) % text;

    def random_error(self):
        return random.choice(self.random_errors);

    def random_pupper(self):

        # Aliases
        choice_terms = self.types;
        tags = self.required_terms.copy();

        # And now search for that url with those terms, return it
        return self.random_search(tags, random.choice(choice_terms));

