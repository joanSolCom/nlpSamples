import spacy
from collections import Counter
from scipy.spatial.distance import cdist
import numpy as np

class TextAnalytics:

	def __init__(self, text):
		nlp = spacy.load("es_core_news_md", disable=["parser"])
		self.nlp = nlp
		self.text = text

		self.keywords = self.load_keywords()
		self.categoryCentroids = self.getCategoryCentroids()

		self.doc = nlp(text)
		self.tokens = []
		self.pos = []
		self.vectors = []
		self.lemmas = []

		for token in self.doc:
			self.tokens.append(token.text.lower())
			self.pos.append(token.pos_)

			if token.pos_.startswith("V") or token.pos_.startswith("N") or token.pos_.startswith("J") or token.pos_.startswith("R"):
				self.vectors.append(token.vector)
			
			self.lemmas.append(token.lemma_.lower())

		self.textCentroid = self.computeCentroid(self.vectors)

	def computeCategorySimilarities(self):
		distances = {}
		for category, centroid in self.categoryCentroids.items():
			dist = self.distance(centroid, self.textCentroid)
			distances[category] = dist[0][0]

		return distances

	def getCategoryCentroids(self):
		categoryCentroids = {}

		for category, wordList in self.keywords.items():
			vectorList = []
			for word in wordList:
				docW = self.nlp(word)
				vectorList.append(docW[0].vector)

			centroid = self.computeCentroid(vectorList)
			categoryCentroids[category] = centroid

		return categoryCentroids 

	def load_keywords(self):
		dictKeywords = {}

		fdS = open("social.txt","r")
		socialKeywords = fdS.read().lower().split("\n")
		dictKeywords["social"] = socialKeywords
		fdS.close()

		fdE = open("exterior.txt","r")
		exteriorKeywords = fdE.read().lower().split("\n")
		dictKeywords["exterior"] = exteriorKeywords
		fdE.close()

		fdEc = open("economia.txt","r")
		economyKeywords = fdEc.read().lower().split("\n")
		dictKeywords["economy"] = economyKeywords
		fdEc.close()
		return dictKeywords

	def keywordMatch(self):
		dictFrequencies = {}
		totalWords = len(self.lemmas)

		for lemma in self.lemmas:
			for category, wordList in self.keywords.items():
				if lemma in wordList:
					if category not in dictFrequencies:
						dictFrequencies[category] = 0
					print("Found ",lemma, "of category",category)
					dictFrequencies[category]+=1

		for category in dictFrequencies.keys():
			dictFrequencies[category] = dictFrequencies[category] / totalWords

		return dictFrequencies

	def distance(self, A, B, distance = "cosine"):
		return cdist([A],[B],distance)

	def computeCentroid(self, vectors):
		avgVector = np.mean(vectors,axis=0)
		return avgVector.tolist()

	def getMostCommon(self, N):
		mostCommon = Counter(self.tokens).most_common(N)
		return mostCommon

	def getMostCommonPos(self, N):
		mostCommon = Counter(self.pos).most_common(N)
		return mostCommon

	def wordsPerSentence(self):
		avg = 0
		nSents = len(list(self.doc.sents))
		for sent in self.doc.sents:
			avg += len(sent)
		return avg / nSents

	def charsPerWord(self):
		nTokens = len(self.tokens)
		avg = 0
		for token in self.tokens:
			avg += len(token)

		return avg / nTokens

	def entitiesPerWord(self):
		nEntities = len(list(self.doc.ents))
		nTokens = len(self.tokens)
		return nEntities/nTokens

	def wordsMoreSimilar(self):
		similarities = []
		inserted = []

		for token1 in self.doc:
			for token2 in self.doc:
				if token1!=token2 and (token2.text, token1.text) not in inserted:
					sim = token1.similarity(token2)
					similarities.append((sim, token1.text.lower(), token2.text.lower()))
					inserted.append((token1.text.lower(), token2.text.lower()))
		return sorted(similarities)
