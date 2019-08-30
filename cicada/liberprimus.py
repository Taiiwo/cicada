import os

from .gematria import Runes

class LiberPrimus:
    def __init__(self, *args):
        if not len(args) > 0:
            with open(os.path.join(os.path.dirname(__file__), "liber_primus.txt"), encoding="utf-8") as f:
                # omit the key
                self.runes = f.read()
        else:
            self.runes = args[0]

        self.delimiters = {
            "word"     : "-",
            "clause"   : ".",
            "paragraph": "&",
            "segment"  : "$",
            "chapter"  : "§",
            "line"     : "/",
            "page"     : "%"
        }

    def strip_delims(self, input):
        input = input.replace("-", " ")
        input = input.replace(".", " ")
        input = input.replace("&", " ")
        input = input.replace("$", " ")
        input = input.replace("§", " ")
        input = input.replace("/", " ")
        input = input.replace("%", " ")
        return Runes(input.strip())

    @property
    def pages(self):
        return [self.strip_delims(page) for page
                in self.runes.split(self.delimiters["page"])]

    @property
    def lines(self):
        return [self.strip_delims(line) for line
                in self.runes.split(self.delimiters["line"])]

    @property
    def chapters(self):
        return [self.strip_delims(chapter) for chapter
                in self.runes.split(self.delimiters["chapter"])]

    @property
    def segments(self):
        return [self.strip_delims(segment) for segment
                in self.runes.split(self.delimiters["segment"])]

    @property
    def paragraphs(self):
        return [self.strip_delims(paragraph) for paragraph
                in self.runes.split(self.delimiters["paragraph"])]

    @property
    def clauses(self):
        return [self.strip_delims(clause) for clause
                in self.runes.split(self.delimiters["clause"])]

    @property
    def words(self):
        return [self.strip_delims(word) for word
                in self.runes.split(self.delimiters["word"])]


if __name__ == "__main__":
    lp = LiberPrimus()
    print(lp.pages[0])
