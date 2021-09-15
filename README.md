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
    page.atbash()
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
print(Latin("How would cicada type question everything?").to_runes().to_latin())
# HOW WOULD CICADA TYPE CWESTION EUERYTHING?
```

# API

## LiberPrimus()
A class for accessing the contents of the Liber Primus

### Property: pages
Returns an array of LiberPrimus() objects containing each page

### Property: lines
Returns an array of LiberPrimus() objects containing each line

### Property: chapters
Returns an array of LiberPrimus() objects containing each chapter

### Property: segments
Returns an array of LiberPrimus() objects containing each segment

### Property: paragraphs
Returns an array of LiberPrimus() objects containing each paragraph

### Property: clauses
Returns an array of LiberPrimus() objects containing each clause

### Property: words
Returns an array of LiberPrimus() objects containing each word

### Property: runes
Returns a Runes() object of the contents

## Gematria()
A base class for translating and manipulating the runes

## Cipher()
A base class for manipulating text given an alphabet

### Method: sub(abc, cba)
Runs a substitution cipher where abc is the plain alphabet, and cba is the desired alphabet.

### Method: shift(n)
Runs a caesar shift on the contents. `alpha` determines if the shift should be on the runic alphabet or the
latin one

### Method: gematria_sum()
Returns the gematria sum of the contents

### Method: atbash()
Returns atbashed contents

### Method gematria_sum()
Returns integer sum of prime values

### Method gematria_sum_words()
returns list of integer sums of prime values for each word

### Method gematria_sum_lines()
returns list of integer sums of prime values for each line

### Method: to_runes()
Converts text contents to runes

### Method: to_latin()
Converts text contents to latin

### Method: to_numbers()
Converts text contents to gematria values

## Runes(rune_string) inherits Cipher
`rune_string`: The string of runes from which the object should be initialized

## Latin(latin_string) inherits Cipher
`latin_string`: The string of latin characters from which the object should be initialized

## Hex(hex_string) inherits Cipher
`hex_string`: The string of hex characters from which the object should be initialized
