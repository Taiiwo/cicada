

class Gematria:
    def __init__(self, text, type):
        self.text = text.upper()
        self.type = type
        self.lookup = {
            "lat sim": self.lat_to_sim,
            "sim lat": self.sim_to_lat,
            "run lat": self.run_to_lat,
            "run num": self.run_to_num,
            "lat run": self.lat_to_run,
            "lat num": self.lat_to_num,
            "num run": self.num_to_run,
            "num lat": self.num_to_lat
        }
        self.gematriaprimus = (
                (u'ᚠ',   'f',   2),
                (u'ᚢ',   'v',   3),
                (u'ᚢ',   'u',   3),
                (u'ᚦ',   'T',   5), # th
                (u'ᚩ',   'o',   7),
                (u'ᚱ',   'r',   11),
                (u'ᚳ',   'c',   13),
                (u'ᚳ',   'k',   13),
                (u'ᚷ',   'g',   17),
                (u'ᚹ',   'w',   19),
                (u'ᚻ',   'h',   23),
                (u'ᚾ',   'n',   29),
                (u'ᛁ',   'i',   31),
                (u'ᛄ',   'j',   37),
                (u'ᛇ',   'E',   41), # eo
                (u'ᛈ',   'p',   43),
                (u'ᛉ',   'x',   47),
                (u'ᛋ',   's',   53),
                (u'ᛋ',   'z',   53),
                (u'ᛏ',   't',   59),
                (u'ᛒ',   'b',   61),
                (u'ᛖ',   'e',   67),
                (u'ᛗ',   'm',   71),
                (u'ᛚ',   'l',   73),
                (u'ᛝ',   'G',   79), # ing
                (u'ᛝ',   'G',   79), # ng
                (u'ᛟ',   'O',   83), # oe
                (u'ᛞ',   'd',   89),
                (u'ᚪ',   'a',   97),
                (u'ᚫ',   'A',  101), # ae
                (u'ᚣ',   'y',  103),
                (u'ᛡ',   'I',  107), # ia
                (u'ᛡ',   'I',  107), # io
                (u'ᛠ',   'X',  109)  # ea
        )
        self.latsimple = (
                ('T','th'),
                ('E','eo'),
                ('G','ing'),
                ('G','ng'),
                ('O','oe'),
                ('A','ae'),
                ('I','ia'),
                ('I','io'),
                ('X','ea'),
        )

    def __repr__(self):
        return "Gematria<%s:%s>" % (self.type, self.text)

    def __str__(self):
        return self.text

    # algorithm taken from here: https://pastebin.com/6v1XC1kV
    def gem_map(self, x, src, dest):
        m = {p[src]:p[dest] for p in self.gematriaprimus}
        return [m[c] if c in m else c for c in x]

    def lat_to_sim(self, x):
        for sim in self.latsimple:
            x = x.replace(sim[1], sim[0])
        return x
    def sim_to_lat(self, x):
        for sim in self.latsimple:
            x = x.replace(sim[0], sim[1])
        return x

    def run_to_lat(self, x):
        return self.sim_to_lat("".join(self.gem_map(x, 0, 1)))
    def run_to_num(self, x):
        return self.gem_map(x, 0, 2)

    def lat_to_run(self, x):
        return self.gem_map(self.lat_to_sim(x.lower()), 1, 0)
    def lat_to_num(self, x):
        return self.gem_map(self.lat_to_sim(x.lower()), 1, 2)

    def num_to_run(self, x):
        return self.gem_map(x, 2, 0)
    def num_to_lat(self, x):
        return self.sim_to_lat("".join(self.gem_map(x, 2, 1)))

    def count(self, x):
        return sum(self.lat_to_num(x))
    def count_words(self, x):
        return [sum(self.lat_to_num(w)) for w in x.split(" ")]
    def count_letters(self, x):
        return [self.lat_to_num(w) for w in x.split(" ")]

    def convert(self,format):
        f = self.lookup[self.type + " " + format]
        return f(self.text)

    def substitute(self, plain, cipher):
        self.text = self.text.translate(str.maketrans(plain, cipher))
        return type(self)(self.text)

    def shift(self, n, alpha=False):
        if not alpha:
            if self.type == "run":
                alpha = "ᚠᚢᚦᚩᚱᚳᚷᚹᚻᚾᛁᛄᛇᛈᛉᛋᛏᛒᛖᛗᛚᛝᛟᛞᚪᚫᚣᛡᛠ"
            else:
                alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return self.substitute(alpha, alpha[n:] + alpha[:n])

class Runes(Gematria):
    def __init__(self, text):
        super().__init__(text, "run")

    def to_simple(self):
        return Simple("".join(self.convert("sim")))

    def to_number(self):
        return Number("".join(self.convert("num")))

    def to_latin(self):
        return Latin("".join(self.convert("lat")))

class Simple(Gematria):
    def __init__(self, text):
        super().__init__(text, "sim")

    def to_runes(self):
        return Runes("".join(self.convert("run")))

    def to_number(self):
        return Number("".join(self.convert("num")))

    def to_latin(self):
        return Latin("".join(self.convert("lat")))

class Number(Gematria):
    def __init__(self, text):
        super().__init__(text, "num")

    def to_runes(self):
        return Runes("".join(self.convert("run")))

    def to_simple(self):
        return Simple("".join(self.convert("sim")))

    def to_latin(self):
        return Latin("".join(self.convert("lat")))

class Latin(Gematria):
    def __init__(self, text):
        super().__init__(text, "lat")

    def to_runes(self):
        return Runes("".join(self.convert("run")))

    def to_simple(self):
        return Simple("".join(self.convert("sim")))

    def to_number(self):
        return Number("".join(self.convert("num")))

if __name__ == "__main__":
    a = Runes("""ᚱ-ᛝᚱᚪᛗᚹ.ᛄᛁᚻᛖᛁᛡᛁ-ᛗᚫᚣᚹ-ᛠᚪᚫᚾ-/
ᚣᛖᛈ-ᛄᚫᚫᛞ.ᛁᛉᛞᛁᛋᛇ-ᛝᛚᚱᛇ-ᚦᚫᛡ/
-ᛞᛗᚫᛝ-ᛇᚫ-ᛄᛁ-ᛇᚪᛡᛁ.ᛇᛁᛈᛇ-ᚣᛁ-ᛞ/
ᛗᚫᛝᚻᛁᚳᛟᛁ.ᛠᛖᛗᚳ-ᚦᚫᛡᚪ-ᛇᚪᛡᚣ.ᛁᛉ/
ᛋᛁᚪᛖᛁᛗᛞᛁ-ᚦᚫᛡᚪ-ᚳᚠᚣ.ᚳᚫ-ᛗᚫᛇ-ᛁᚳᛖᛇ-ᚫ/
ᚪ-ᛞᛚᚱᚹᛁ-ᚣᛖᛈ-ᛄᚫᚫᛞ.ᚫᚪ-ᚣᛁ-ᚾᛁᛈᛈᚱᛟᛁ-/
ᛞᚫᛗᛇᚱᛖᛗᛁᚳ-ᛝᛖᚣᛖᛗ.ᛁᛖᚣᛁᚪ-ᚣᛁ-ᛝᚫ/
ᚪᚳᛈ-ᚫᚪ-ᚣᛁᛖᚪ-ᛗᛡᚾᛄᛁᚪᛈ.ᛠᚫᚪ-ᚱᚻᚻ-ᛖ/
ᛈ-ᛈᚱᛞᚪᛁᚳ./""")
    print(a.translate("ᚠᚢᚦᚩᚱᚳᚷᚹᚻᚾᛁᛄᛇᛈᛉᛋᛏᛒᛖᛗᛚᛝᛟᛞᚪᚫᚣᛡᛠ"))
    print(a.to_latin())
    # ᚻᛖᛚᛚᚩ
    print(Latin("Hello"))
