from pymongo.errors import DuplicateKeyError
import entrez

class UserCollection():
    def __init__(self, database):
        self.database = database
        self.user_collection = database['papers']

    def add_response(self, title, authors, source, abstract):
        '''
        DESC
        '''
        try:
            new_user = {
                'title':title,
                'authors':authors,
                'source':source,
                'abstract': abstract

            }
            self.user_collection.insert_one(new_user)
            return True
        except DuplicateKeyError:
            print(f'no duplicated {title}')
            return False
