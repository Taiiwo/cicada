# Taiiwo's Cicada Library
This library contains a selection of tools for performing high level operations on the LiberPrimus

# Example usage:

```python
from cicada import LiberPrimus
from cicada.gematria import Latin, Runes

# load the lp from file
lp = LiberPrimus()

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
```

# API

## LiberPrimus()
A class for accessing the contents of the Liber Primus

    Property: pages - Returns an array of Runes() objects containing each page

    Property: lines - Returns an array of Runes() objects containing each line

    Property: chapters - Returns an array of Runes() objects containing each chapter

    Property: segments - Returns an array of Runes() objects containing each segment

    Property: paragraphs - Returns an array of Runes() objects containing each paragraph

    Property: clauses - Returns an array of Runes() objects containing each clause

    Property: words - Returns an array of Runes() objects containing each word

    Property: runes - Returns a Runes() object containing the entire LP

## Gematria()
A base class for translating and manipulating the runes

### Method: substitute(abc, cba, mutable=True)
    Runs a substitution cipher where abc is the plain alphabet, and cba is the desired alphabet.
    `mutable` determines whether the function modifies the object contents
    
### Method shift(n, alpha=False)
    Runs a caesar shift on the contents. `alpha` determines if the shift should be on the runic alphabet or the
    latin one

### Method to_runes()
    Converts text contents to runes

### Method to_latin()
    Converts text contents to latin

### Method to_numbers()
    Converts text contents to gematria values

## Runes(rune_string) inherits Gematria
    `rune_string`: The string of runes from which the object should be initialized

## Latin(latin_string) inherits Gematria
    `latin_string`: The string of latin characters from which the object should be initialized

## Number(number_string) inherits Gematria
    `number_string`: The string of number values from which the object should be initialized
