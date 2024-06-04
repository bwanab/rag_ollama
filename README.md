# RAG Ollama - a simple example of RAG using ollama and llama-index
Ollama is an cross-platform executable that allows the use of LLMs locally. Llama-index is a platform that facilitates the building of RAG applications. Chroma is a vector database that is used to store embeddings.

# quick start:

### install ollama
Instructions for your system should be here: https://ollama.com/.

### clone the repository:

```
git clone https://github.com/bwanab/rag_ollama.git
cd rag_ollama
```

### set up a virtual environment (Optional, but highly recommended):

```
python3 venv venv
source venv/bin/activate
```

### get the python requirements:
```
python -m pip install -r requirements.txt
```

### execute the example:
```
python starter.py
```
When the process has completed it will print a --> at which point you can ask questions about the text. Examples are given below.



# Note on the text used as example:

The example passage given cd_data/cd_post.txt is a book review blog posting from Cory Doctorow from his Medium page https://doctorow.medium.com/https-pluralistic-net-2024-06-04-anom-nom-nom-the-call-is-coming-from-inside-the-ndrangheta-75d8c8fabfe4. No changes have been made to the original text. The text is licensed under the Creative Commons 4 license: https://creativecommons.org/licenses/by/4.0/legalcode.


# Example of running starter.py:

% python starter.py
--> Who is Joseph Cox?
 Joseph Cox is a tech reporter who wrote the book "Dark Wire." In his journalistic career, he has spent years reporting on crimephones, devices sold to criminal syndicates with the promise of being untraceable. He has spent years covering this beat before leaving Motherboard to co-found 404 Media. The book "Dark Wire" details his investigations into this world and the largest sting operation in history involving these crimephones.
--> What was the nature of the sting operation describd in "Dark Wire"?
 In the book "Dark Wire" by Joseph Cox, law enforcement carried out a large-scale sting operation to disrupt criminal activities involving modified phones sold to syndicates, which were believed to be untraceable. The operation was led by the FBI and involved setting up their own crimephone company called Anom, with the intention of selling these phones to criminals while maintaining a backdoor for law enforcement access. This allowed them to gather intelligence on criminal activities and disrupt them as needed. However, challenges arose when criminals discovered ways to clone the "black boxes" used in new Anom phones, leading to a surge in their use among criminal elements. The operation faced various hurdles due to its covert nature and the involvement of multiple governments, but ultimately resulted in a series of global arrests and revelations of those involved in the Anom conspiracy.
--> What kinds of crimes did the FBI uncover using the Anom phones?
 The FBI uncovered a wide range of crimes while using the Anom phones, including murders, kidnappings, tortures, firebombings, and other serious crimes. Some of these crimes were in the planning phase, while others had already been committed. The criminals involved in these activities were engaged in violent, global criminal conspiracies and were competing with one another to corner the market on these incredibly lucrative phones.
--> 