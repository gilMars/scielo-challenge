from utils.contants import EXTRACT_INFO_EXCEPTION


class ExtractInfoException(IOError):

    def __init__(self, message=EXTRACT_INFO_EXCEPTION):
        super().__init__(message)