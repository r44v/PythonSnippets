class Callback:
    def __init__(self, func, *args, **kwargs):
        """
        Saves callback function and parameters in self object

        :param func:
        :param args:
        :param kwargs:
        """
        self.__func = func
        self.__args = args
        self.__kwargs = kwargs

    def __call__(self):
        """
        Makes object callable and executes callback function with correct parameters

        Does not expect any parameters for __call__

        :return:
        """
        return self.__func(*self.__args, **self.__kwargs)


class UncaringCallback:
    def __init__(self, func, *args, **kwargs):
        """
        Saves callback function and parameters in self object

        :param func:
        :param args:
        :param kwargs:
        """
        self.__func = func
        self.__args = args
        self.__kwargs = kwargs

    def __call__(self, *args, **kwargs):
        """
        Makes object callable and executes callback function with correct parameters

        Both params are ignored

        :param
        args:
        :param
        kwargs:
        :return:
        """

        return self.__func(*self.__args, **self.__kwargs)
