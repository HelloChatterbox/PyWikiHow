

class ParseError(RuntimeError):
    """ Error parsing WikiHow page"""


class UnsupportedLanguage(ValueError):
    """ Unsupported lang, see https://www.wikihow.com/wikiHow:Language-Projects"""