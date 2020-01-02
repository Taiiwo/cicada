from cicada import LiberPrimus
from cicada.gematria import Latin, Runes

# load the lp from file
lp = LiberPrimus()

"""
shift = 0
# for pages 0 - 3 of the lp
for page in lp.pages[0:3]:
    # page is a Runes() object so we can do some cool things:
    # atbash substitution
    page.substitute("ᚠᚢᚦᚩᚱᚳᚷᚹᚻᚾᛁᛄᛇᛈᛉᛋᛏᛒᛖᛗᛚᛝᛟᛞᚪᚫᚣᛡᛠ", "ᛠᛡᚣᚫᚪᛞᛟᛝᛚᛗᛖᛒᛏᛋᛉᛈᛇᛄᛁᚾᚻᚹᚷᚳᚱᚩᚦᚢᚠ")
    # caesar shift
    page.shift(shift)
    # use .text to get the contents of a Gematria() object such as Runes()
    # Note: it will also convert to str with str(Runes()) or equiv
    print("Runes: %s" % page.text)
    print("Plaintext: %s" % page.to_latin())
    # example of automated shifting
    shift += 1

print(Runes("ᚠᚢᚦᚩᚱᚳᚷᚹᚻᚾᛁᛄᛇᛈᛉᛋᛏᛒᛖᛗᛚᛝᛟᛞᚪᚫᚣᛡᛠ").to_latin())
# FUTHORKGWHNIJEOPXZTBEMLINGOEDAAEYIAEA
print(Latin("Hello World!").to_runes())
# ᚻᛖᛚᛚᚩ ᚹᚩᚱᛚᛞ!
print(Latin("How would cicada type this?").to_runes().to_latin())
# HOW WOULD KIKADA TYPE THIZ?
"""
cipher = Latin("crack me, baby. This is some text to crack. Let's see if we can crack it")
cipher.substitute("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "QWERTYUIOPASDFGHJKLZXCVBNM")
#cipher.substitute("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ABCDEFGHIJKLMNOPQRSUTVWXYZ")
print(cipher)
cipher = cipher.to_runes().text

print("Cracking: %s" % cipher)

from cicada import Validator
from itertools import permutations

v = Validator()

# convert the cipher string from runes to latin
cipher = Runes(cipher).to_latin()

# Try every combination of substitutes
from cicada.pybar import PyBar
import math
bar = PyBar(max=math.factorial(19), poll=1)
for combination in permutations("YRABMSTHFLNETCXIOWK"):
    text = cipher.substitute("YRABMSTHFLNETCXIOWK", "".join(combination), mutable=False)
    bar.update(bar.percent(), bar.progress(), bar.bar(), bar.rate(time=1), "Current: ", text, next=True)
    if v.is_cicadian(text):
        bar.echo(text)
