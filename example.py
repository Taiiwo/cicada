from cicada import LiberPrimus
from cicada.gematria import Latin, Runes

# load the lp from file
lp = LiberPrimus()

cipher = Latin("crack me, baby. This is some text to crack. Let's see if we can crack it")
cipher.sub("ABCDEFGHIJKLMN", "QWERTYUIOPASDF")
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
    text = cipher.sub("YRABMSTHFLNETCXIOWK", "".join(combination))
    bar.update(bar.percent(), bar.progress(), bar.bar(), bar.rate(time=1), "Current: ", text.text, next=True)
    if v.is_cicadian(text.text):
        bar.echo(text)
