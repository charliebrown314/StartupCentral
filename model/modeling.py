import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class Model:
    def __init__(self, projects_matrix):
        self.idx_to_name = {}
        self.name_to_idx = {}
        self.tag_id = {}
        self.cosign_matrix = self.vectorize(projects_matrix)
        self.cosign_sim = cosine_similarity(self.cosign_matrix)

    def vectorize(self, input_matrix):
        # input matrix is the project name in the first col, all features are in following cols
        # first feature is the index, all the rest are 0 or 1 to represent if a tag is used for them
        arr = []
        for r in input_matrix:
            for tag in r[1:]:
                if tag not in self.tag_id:
                    self.tag_id[tag] = len(self.tag_id)
        for row in input_matrix:
            idx = len(self.idx_to_name)
            self.idx_to_name[idx] = row[0]
            self.name_to_idx[row[0]] = idx
            r = [idx]+[0]*len(self.tag_id)
            tags = row[1:]
            for tag in tags:
                r[1+self.tag_id[tag]] = 1
            arr.append(r)
        return arr

    def recommendations(self, project_name):
        idx = self.name_to_idx[project_name]
        sor = list(enumerate(self.cosign_sim[idx]))
        sor = sorted(sor, key=lambda x: x[1], reverse=True)[1:]
        return [self.idx_to_name[i[0]] for i in sor[:50]]
