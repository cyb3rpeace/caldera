import abc


class LearningServiceInterface(abc.ABC):

    @staticmethod
    @abc.abstractmethod
    def add_parsers(directory):
        raise NotImplementedError

    @abc.abstractmethod
    def build_model(self):
        """
        The model is a static set of all variables used inside all ability commands
        This can be used to determine which facts - when found together - are more likely to be used together
        :return:
        """
        raise NotImplementedError

    @abc.abstractmethod
    def learn(self, facts, link, blob):
        raise NotImplementedError
