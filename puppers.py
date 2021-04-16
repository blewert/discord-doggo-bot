#
# @file   puppers.py
# @brief  Builds atop the flickr search api to search for random cute dogs.
# @author ben <bwilliams@lincoln.ac.uk>
#

import random
import util
from flickr import FlickrPhotosAPI

class PuppersAPI(FlickrPhotosAPI):

    def __init__(self, key):

        # Call base constructor
        super().__init__(key);

        # Load all text data for use with bot
        self.types           = util.load_json(r"data/puppy_types.json");
        self.required_terms  = util.load_json(r"data/search_tags.json");
        self.random_errors   = util.load_json(r"data/random_errors.json");
        self.random_ratings  = util.load_json(r'data/rating_strings.json');

    def random_rating(self, text) -> str:
        return random.choice(self.random_ratings) % text;

    def random_error(self) -> str:
        return random.choice(self.random_errors);

    def random_pupper(self) -> str:

        # Aliases
        choice_terms = self.types;
        tags = self.required_terms.copy();

        # And now search for that url with those terms, return it
        return self.random_search(tags, random.choice(choice_terms));

