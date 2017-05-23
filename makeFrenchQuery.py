#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys, os, lucene

from java.nio.file import Paths
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.document import Document, Field, FieldType
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.analysis.en import EnglishAnalyzer
from org.apache.lucene.search import Query
from org.apache.lucene.queryparser.classic import QueryParser
from org.apache.lucene.analysis.core import StopAnalyzer

import sys
from mstranslator import Translator
testWords = [unicode("awake"), unicode("asleep")]

# use Lucene to filter out stop words from query
# then split and return space-seperated values
def parseQuery(myQuery):
    parser = QueryParser("", StopAnalyzer())
    parsedQuery = parser.parse(myQuery);
    myQueryTerms = parsedQuery.toString().split(" ")
    return myQueryTerms

def makeFrenchQuery(myQuery):
    terms = parseQuery(myQuery)
    translator = Translator('myPythonTranslate64','YqNxIMdOAoaF5Am+/BT84sdQ1q7ZCNA1stU0viWcGi4=')
    frenchQuery = []
    for term in terms:
        translate = translator.translate(term, lang_from='en', lang_to='fr')
        frenchQuery.append(translate)
    return frenchQuery
