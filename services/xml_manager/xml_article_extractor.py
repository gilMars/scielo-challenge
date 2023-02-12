import datetime
import re

from lxml.etree import tounicode

from services.xml_manager.xml_exceptions import ExtractInfoException
from services.xml_manager.xml_parser_imp import XmlParserImp


class XmlArticleExtractor:

    def __init__(self, xml_path):
        self.parser = XmlParserImp(xml_path)
        if not self.parser.is_valid():
            raise ExtractInfoException()

        self.xml_parsed = self.parser.parse_xml()

    def __issn(self):
        issn = self.xml_parsed.getroot().find('.//issn')
        return '' if issn is None else issn.text

    def __journal_tittle(self):
        journal_tittle = self.xml_parsed.getroot().find('.//journal-title')
        return '' if journal_tittle is None else journal_tittle.text

    def __article_tittle(self):
        article_tittle = self.xml_parsed.getroot().find('.//article-title')
        return '' if article_tittle is None else article_tittle.text

    def __volume(self):
        volume = self.xml_parsed.getroot().find('.//volume')
        return '' if volume is None else volume.text

    def __issue(self):
        issue = self.xml_parsed.getroot().find('.//issue')
        return '' if issue is None else issue.text

    def __date_publication(self):
        date_publication = self.xml_parsed.getroot().find('.//pub-date[@date-type="pub"]')
        if date_publication is not None:
            day = int(date_publication.find('day').text)
            month = int(date_publication.find('month').text)
            year = int(date_publication.find('year').text)
            return datetime.datetime(year, month, day)
        return ''

    def __authors(self):
        authors_elements = self.xml_parsed.getroot().findall('.//contrib[@contrib-type="author"]')
        authors = []
        for author in authors_elements:
            author_info = dict()
            author_info['surname'] = author.find('.//surname').text
            author_info['name'] = author.find('.//given-names').text
            author_info['contrib-id'] = author.find('.//contrib-id').text
            authors.append(author_info)
        return authors

    @staticmethod
    def __clear_element(element):
        new_string = tounicode(element, with_tail=False)
        nsmap = element.nsmap
        for k, v in nsmap.items():
            new_string = new_string.replace(f'xmlns:{k}="{v}"', '')

        attrib = element.attrib
        for k, v in attrib.items():
            new_string = new_string.replace(f'{k}="{v}"', '')

        return re.sub(r'<[/]?\s*title\s*>', '', new_string, 0, re.MULTILINE)

    def __figures(self):
        temp_figures = self.xml_parsed.getroot().findall('.//fig')
        filtered_figures = [fig for fig in temp_figures if fig.find('.//graphic') is not None]
        figures = []
        for fig in filtered_figures:
            figure_info = dict()
            figure_info['label'] = fig.find('.//label').text
            title = fig.find('.//title')
            figure_info['title'] = self.__clear_element(title)
            figure_info['url'] = fig.find('.//graphic').get('{http://www.w3.org/1999/xlink}href')

            figures.append(figure_info)
        return figures

    def extract_info(self):
        info = dict()
        info['issn'] = self.__issn()
        info['journal-title'] = self.__journal_tittle()
        info['article-title'] = self.__article_tittle()
        info['volume'] = self.__volume()
        info['issue'] = self.__issue()
        info['date'] = self.__date_publication()
        info['authors'] = self.__authors()
        info['figures'] = self.__figures()

        return info
