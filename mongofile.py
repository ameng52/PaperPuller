import sys
from loguru import logger
import entrez
from pymongo import MongoClient
import add_seq
import main

logger.remove()
logger.add("log_file_{time:YYYY_MMM_DD}.log")
logger.add(sys.stderr, level='INFO')


class MongoDBConnection():
    '''MongoDB Connection'''

    def __init__(self, host='127.0.0.1', port=27017):
        """ be sure to use the ip address not name for local windows"""
        self.host = host
        self.port = port
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(self.host, self.port)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

def analyze_paper():
    '''
    This function takes a user input, and sends it through the biopython module, which searches through the NCBI entrez
    database for articles containing said user input. Then the function will section the article into a title, authors,
    source, and abstract, and convert it to a dictionary. Subsequently, the function will call the add_seq function to
    add the converted dictionary to the mongoDB database.

    '''
    user_input = input('What would you like to look for:')
    email = input('Please enter your email:')
    logger.add(f'user input in entrez {user_input}')
    for i in range(len(entrez.get_bio_data(user_input,email)['title'])):
        paper_list = []
        for k, v in entrez.get_bio_data(user_input,email).items():
            if k == 'title':
                title = v[i]
                paper_list.append(f'Title: {title} ')
            if k == 'authors':
                authors = v[i]
                paper_list.append(f'Authors: {authors}')
            if k == 'source':
                source = v[i]
                paper_list.append(f'Sources: {source}')
            if k == 'abstract':
                abstract = v[i]
                paper_list.append(f'Abstract: {abstract}')
        print('\n')
        print(*paper_list, sep='\n')
        add_seq.UserCollection.add_response(user_collection, title, authors, source, abstract)


def quit_program():
    '''
    Quits program
    '''
    drop = input("Drop database? [Y/N]: ")
    if drop.lower() == 'y':
        UserAccounts.drop()
        UserPapers.drop()
    sys.exit()


if __name__ == '__main__':
    mongo = MongoDBConnection()
    with mongo:
        database = mongo.connection.user_info
        UserAccounts = database['Users']
        UserPapers = database['Papers']
        user_collection = main.init_user_collection()
        menu_options = {
            'A': analyze_paper,
            'Q': quit_program
        }
        while True:
            user_selection = input("""
                            A: analyze a topic
                            Q: quit_program
                            Please enter your choice: """)
            if user_selection.upper() in menu_options:
                menu_options[user_selection.upper()]()
            else:
                print("Invalid option")
