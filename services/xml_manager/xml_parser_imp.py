import os

from lxml import etree

from services.xml_manager.xml_parser_abc import XmlParserAbc
from utils.contants import JATS_SCHEMA_PATH
from utils.functions import find_resourcer_path


class XmlParserImp(XmlParserAbc):

    def __init__(self, xml_path):
        self.xml_path = xml_path

    def parse_xml(self):
        return etree.parse(self.xml_path)

    @staticmethod
    def __get_schema():
        resources_path = find_resourcer_path()
        schema_path = os.path.join(resources_path, JATS_SCHEMA_PATH)
        return etree.parse(schema_path)

    def is_valid(self):
        return etree.XMLSchema(self.__get_schema()).validate(etree.parse(self.xml_path))
