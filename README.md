# Information Retrieval Project - English to French Query Translation
Project aim is to retrieve the relevant documents in French language given an English query. As part of the baseline approach, I am retrieving the English documents for the English query and finally matching two set of documents in both the languages. The motivation behind the task is to benefit different kind of users. Monolingual users who are keen to learn French language can be benefited specially by having the same document side by side in both the languages. It can also help the users who can read both the languages but inputs the query in most fluent language.
There are mainly three different ways in which cross-language information retrieval works – through query translation, document translation or both. We are using query translation technique in which we are converting an English query into a French query and then retrieving the documents in French language. There are four different techniques that uses translation resources such as Dictionary-Based, Parallel corpora, Comparable corpora and Machine translator. In our project, the focus is on Machine translator and Parallel corpora based CLIR techniques.

```
List of dependencies: ( No changes from prototype 2 )

Run on Python 2.7.11
PyLucene       :(http://lucene.apache.org/pylucene/)
MsTranslator   :https://pypi.python.org/pypi/mstranslator

```
```
Running the code:
Step 0. Download and extract the gzip to its own directory (you have probably done this already)
Step 1. Change directory to Code and Data Submission folder
Step 2. Build Indexes:
    2a. cd Corpus
    2b. python IndexFilesEn.py CorpusEn
    2c. python IndexFilesFr.py CorpusFr
    2d. cd ..
    2e. cd lCorpus
    2f. python IndexFilesEn.py lCorpusEn
    2g. python IndexFilesEn.py lCorpusFr
Step 3. cd ..
Step 4. You're set up and can run one of the four search files scripts.
They are hardcoded to use the correct index. Run whatever queries you feel like running.
ProjectQueries.rtf has the ones we used, and I threw in our excel document of results for good measure
```
