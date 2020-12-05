from __future__ import division
import math

def TermFrequency(document, matchingTerm):
    terms = document.lower().split()
    term_in_document = terms.count(matchingTerm.lower())
    len_of_document = float(len(terms))
    normalized_tf = term_in_document / len_of_document
    return normalized_tf

def InverseDocumentFrequency(documents, matchingTerm):
    num_docs_with_given_term = 0 
    for document in documents:
        terms = document.lower().split()
        if matchingTerm in terms:
            num_docs_with_given_term+=1
    if num_docs_with_given_term > 0:
        return math.log(len(documents)/num_docs_with_given_term)
    else:
        return 0


documents = {"I am unable to do my wor can you help me. Ofcourse, I'll help you",
             "Finding a Software Developer for my company min 3 years experience",
             "looking for a human resource people",
             "computer science engineer also fresher will be accepted"}

def TermFrequencyWithInverseDocumentFrequency(documents, matchingTerm):
    tf_idf = []
    idf = InverseDocumentFrequency(documents, matchingTerm)
    for document in documents:
        normalized_tf = TermFrequency(document, matchingTerm)
        tf_idf.append(normalized_tf * idf)
        print(document, tf_idf)
    print(tf_idf)

TermFrequencyWithInverseDocumentFrequency(documents, "unable")