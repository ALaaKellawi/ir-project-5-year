import string
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.corpus import wordnet

stop_words = ["''", "``", "..", "n't", "'s", "u", "'m", "’", "'", "/", "...", ".", '”', '””', 'wa', 'hi',
              'doe',
              'ha', 'whi', "sometimes", "usually", "always"]
stop_words += set(stopwords.words('english'))
number_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
                'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen',
                'twenty']


class TextProcessingService:
    # def __init__(self):

    @staticmethod
    def lower(text):
        if isinstance(text, str):
            return text.lower()
        else:
            return ""

    @staticmethod
    def tokenize_text(text):
        return word_tokenize(text)

    @staticmethod
    def remove_stopwords(text):
        return [word for word in text if word not in stop_words]

    @staticmethod
    def remove_number_words(text):
        return [word for word in text if word.lower() not in number_words]

    @staticmethod
    def remove_punctuation(text):
        table = str.maketrans('', '', string.punctuation)
        stripped = [w.translate(table) for w in text]
        words = [word for word in stripped if word.isalpha()]
        return words

    @staticmethod
    def get_wordnet_pos(tag_parameter):
        tag = tag_parameter[0].upper()
        tag_dict = {"J": wordnet.ADJ, "N": wordnet.NOUN, "V": wordnet.VERB, "R": wordnet.ADV}
        return tag_dict.get(tag, wordnet.NOUN)

    @staticmethod
    def remove_links(text):
        return re.sub(r'http\S+|www\.\S+', '', text)

    @staticmethod
    def lemmatize_text(text):
        pos_tags = nltk.pos_tag(text)
        lemmatizer = WordNetLemmatizer()
        lemmatized_words = [lemmatizer.lemmatize(word, pos=TextProcessingService.get_wordnet_pos(pos_tag)) for word, pos_tag in pos_tags]
        return lemmatized_words

    @staticmethod
    def stemming(text):
        stemmer = PorterStemmer()
        return [stemmer.stem(word) for word in text]

    @staticmethod
    def process(text):
        text_processed = TextProcessingService.remove_links(text)
        text_processed = TextProcessingService.lower(text_processed)
        text_processed = TextProcessingService.tokenize_text(text_processed)
        text_processed = TextProcessingService.remove_stopwords(text_processed)
        text_processed = TextProcessingService.remove_number_words(text_processed)
        text_processed = TextProcessingService.remove_punctuation(text_processed)
        text_processed = TextProcessingService.lemmatize_text(text_processed)
        text_processed = TextProcessingService.stemming(text_processed)
        return text_processed

# text_processing_service = TextProcessingService()
# processed_text = text_processing_service.process("This is a sample text   for processing.")
# print(processed_text)
