import abc


class XmlParserAbc(abc.ABC):

    @abc.abstractmethod
    def is_valid(self):
        pass

    @abc.abstractmethod
    def parse_xml(self):
        pass
