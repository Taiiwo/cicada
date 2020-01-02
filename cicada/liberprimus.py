import os

from .gematria import Runes

class LiberPrimus:
    def __init__(self, *args):
        if not len(args) > 0:
            with open(os.path.join(os.path.dirname(__file__), "liber_primus.txt"), encoding="utf-8") as f:
                # omit the key
                self.text = f.read()
        else:
            self.text = args[0]

        self.delimiters = {
            "word"     : "-",
            "clause"   : ".",
            "paragraph": "&",
            "segment"  : "$",
            "chapter"  : "§",
            "line"     : "/\n",
            "page"     : "%"
        }

    def __str__(self):
        return self.strip_delims(self.text)

    def strip_delims(self, input):
        input = input.replace("-", " ")
        input = input.replace(".", " ")
        input = input.replace("&", "")
        input = input.replace("$", "")
        input = input.replace("§", "")
        input = input.replace("/", "")
        input = input.replace("%", "")
        return Runes(input.strip())

    def split_by(self, delim_index):
        # split by the specified delimmiter and remove the rest
        return [self.strip_delims(a) for a in self.runes.split(self.delimiters[delim_index])]

    @property
    def pages(self):
        return self.split_by("page")

    @property
    def lines(self):
        return self.split_by("line")

    @property
    def chapters(self):
        return self.split_by("chapter")

    @property
    def segments(self):
        return self.split_by("segment")

    @property
    def paragraphs(self):
        return self.split_by("paragraph")

    @property
    def clauses(self):
        return self.split_by("clause")

    @property
    def words(self):
        return self.split_by("word")

if __name__ == "__main__":
    lp = LiberPrimus()
    print(lp.pages[0])
