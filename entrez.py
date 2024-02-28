import os
from dotenv import load_dotenv
from Bio import Entrez
from Bio import Medline

load_dotenv()
api_key = os.getenv('BIOPYTHON_API_KEY')
api_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=gene&id=3269&api_key={api_key}"


def get_bio_data(search, user_email):
	'''

	This function uses the biopython API to search for specific requested papers. The search parameter determines what
	topic the user wants, and user_email provides a valid email address for using the database. This function also
	converts the collected papers into a dictionary.
	'''
	Entrez.email=user_email
	stream=Entrez.esearch(db="pubmed",term=f"{search}[title]",retmax="5")
	record=Entrez.read(stream)
	data = Medline.parse(Entrez.efetch(db="pubmed", id=record["IdList"], rettype="medline", retmode="text"))
	data = list(data)
	bio_dict = {'title': [], 'authors':[], 'source':[], 'abstract':[]}
	for d in data:
		title = (d.get("TI","?"))
		authors = (d.get("AU","?"))
		source = (d.get("SO","?"))
		abstract = (d.get("AB","?"))
		bio_dict['title'].append(title)
		bio_dict['authors'].append(authors)
		bio_dict['source'].append(source)
		bio_dict['abstract'].append(abstract)

	return bio_dict
