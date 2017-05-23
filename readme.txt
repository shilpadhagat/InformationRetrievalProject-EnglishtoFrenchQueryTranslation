Instructions to run the code

Required installations:
- Python 2.7.12 (available in debian repository)
- PyLucene 6.2 (http://lucene.apache.org/pylucene/) # good luck with this!
- MsTranslator (https://pypi.python.org/pypi/mstranslator)
    (just need to install MsTranslator, I have my own key hardcoded into the relevant code)
    (also it's my own key so please don't distribute it)

Instructions to run the code

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

Happy Holidays!
