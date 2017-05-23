#!/usr/bin/env python
#-*- coding: utf-8 -*-
INDEX_DIR = "Corpus/IndexFilesEN.index."

import sys, os, lucene
import makeFrenchQuery
from java.nio.file import Paths
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.queryparser.classic import QueryParser
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.search import IndexSearcher
from org.apache.lucene.analysis.en import EnglishAnalyzer
from org.apache.lucene.search.similarities import ClassicSimilarity
"""
This script is loosely based on the Lucene (java implementation) demo class
org.apache.lucene.demo.SearchFiles.  It will prompt for a search query, then it
will search the Lucene index in the current directory called 'index' for the
search query entered against the 'contents' field.  It will then display the
'path' and 'name' fields for each of the hits it finds in the index.  Note that
search.close() is currently commented out because it causes a stack overflow in
some cases.
"""
def run(searcher, analyzer):
    while True:
        print
        print "Hit enter with no input to quit."
        command = raw_input("Query:")
        if command == '':
            return
        print
        print "Searching for:", command
        query = QueryParser("contents", analyzer).parse(command)
        scoreDocs = searcher.search(query, 50).scoreDocs
        print "%s total matching documents." % len(scoreDocs)

        for scoreDoc in scoreDocs:
            doc = searcher.doc(scoreDoc.doc)
            print 'path:', doc.get("path"), 'name:', doc.get("name"), ('score: %f' %(scoreDoc.score))


if __name__ == '__main__':
    lucene.initVM(vmargs=['-Djava.awt.headless=true'])
    print 'lucene', lucene.VERSION
    directory = SimpleFSDirectory(Paths.get(os.getcwd(), INDEX_DIR))
    searcher = IndexSearcher(DirectoryReader.open(directory))
    searcher.setSimilarity(ClassicSimilarity())
    analyzer = EnglishAnalyzer()
    run(searcher, analyzer)
    del searcher
