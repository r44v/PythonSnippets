import os
import pickle


class EasyPickle:
    def __init__(self, always_save=True):
        """
        Creates dict file to store as pickle
        All keys and values will be stored as string format

        :param always_save:
        """
        self.__file = "str_dict.pickle"
        if os.path.exists(self.__file):
            self.__storage = self.__load()
        else:
            self.__storage = {}

        self.__always_save = always_save

    def __dump(self):
        """
        Stores dict as pickle file on disk

        :return:
        """
        with open(self.__file, "wb") as pickle_out:
            pickle.dump(self.__storage, pickle_out)

    def __load(self):
        """
        Loads existing pickle file from disk

        :return:
        """
        with open(self.__file, "rb") as pickle_in:
            storage_dict = pickle.load(pickle_in)
        return storage_dict

    def get(self, key):
        """
        Returns value assigned to key

        :param key:
        :return:
        """
        key = str(key)
        if key in self.__storage.keys():
            return self.__storage[key]
        else:
            return None

    def put(self, key, value):
        """
        Sets value for key

        if always_save is True it also writes data to disk

        :param key:
        :param value:
        :return:
        """
        self.__storage[str(key)] = str(value)
        if self.__always_save:
            self.__dump()

    def save(self):
        """
        Writes data to disk

        :return:
        """
        self.__dump()