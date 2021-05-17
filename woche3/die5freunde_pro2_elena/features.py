# -*- coding: utf-8 -*-
# Elena Kröner
# Python 3.8

from abc import ABC, abstractmethod
from nltk.corpus import words


class TemplateFeature(ABC):

    def __init__(self, texts):
        self.texts = texts  # list of strings
        self.features = list()

    @abstractmethod
    def normalize(self):
        pass


class Features(TemplateFeature):

    def word_based_features(self):
        """
        Returns
        -------
        list
            with sublist per string, containing average word lenght, normalized
            spelling errors and vocabulary richness (type-token-ratio).

        """
        for text in self.texts:
            text_feats = []
            text = text.split(" ")
            total_len = 0
            errors = 0
            types = set()
            for word in text:
                word = word.lower().strip(".,!?\"\'")
                total_len += len(word)  # length of text without whitespace
                if word not in words.words():
                    errors += 1  # number of spelling errors
                types.add(word)  # unique words
            text_feats.append(self.normalize(total_len, text))
            text_feats.append(self.normalize(errors, text))
            text_feats.append(self.normalize(len(types), text))
            self.features.append(text_feats)
        return self.features

    def normalize(self, feature, text):
        return round(feature/len(text), 2)


def main():
    t = ["Use this easy crêpe mix to make sweet or savoury pancakes.",
         "secind example, second example."]
    features = Features(t)
    feat = features.word_based_features()
    print(feat)


if __name__ == "__main__":
    main()
