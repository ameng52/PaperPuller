# ResearchPaperCollector

Introduction:
  This project utilizes a Python program that uses the BioPython API to pull scientific papers from the entrez NCBI database. The user can ask for a specific input, ie COVID and the program will search the NCBI's Entrez database for 4 categories of information. The data will be presented in a dictionary with key, value pairs of title : title contents, authors : authors contents, source : source contents, and abstract : abstract contents. After successfully pulling a set amount of papers, then the program will add these papers to the UserPapers mongoDB collection, allowing for further interaction.

Inputs/Outputs:
  Once you run the mongofile program, you will be prompted to enter an option, a or b. Captialization doesn't matter for this input, but you must enter A, a or b, B for something to happen. When you enter a, The first  input required will be the topic of interest, simply input a science related query into mongofile.py and allow the program to find it. One common example could be COVID, or the flu.Given that this project uses the Entrez database, the next input requrires a valid email address. This input (email) will be prompted for by mongofile.py and simply enter your email with a valid API key. After these two inputs, the outputs you should expect are a printed orderly rundown of the obtained papers, in the order of title, authors, source, and abstract. Then you can enter the mongoDB database in mongoDB compass to see the created UserPapers collection,and view the added documents.When you enter b or B, you'll be prompted to enter another input, asking if you'd like to drop the database. If you enter Y, then the collection UserPapers will delete any stored entries, and if you enter N, the collection will retain the currently stored entries. 

Procedure:
  This program uses Python, so ensure that Python is installed and working. Python can be installed here.
  
  https://www.python.org/downloads/
  
  After Python is up and running, please install mongoDB compass at this link.
  
  https://www.mongodb.com/try/download/shell
  
  Next, this program uses loguru, and if python is installed with pip, simply run in the command line:
  
  pip install loguru
  
  Next, ensure that you have a valid API key for accessing the NCBI Entrez database. First, create and account with NCBI, and remember your email as it is one of the required inputs. 
  Then follow the instructions in this link.
  
  https://support.nlm.nih.gov/knowledgebase/article/KA-05317/en-us
  
  When running this program, simply clone the repository, and run mongofile.py in your computer's command line interface. 
  
  python mongofile.py
  
  You should recieve a menu with two options, one of which is to analyze a paper, or to quit the program.
  If you select A, then prepare your email, and topic of interest. If you select B, then decide whether you would like to delete your data in the collection.
  
  

References:
  
