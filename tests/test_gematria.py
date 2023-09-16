from cicada.gematria import Runes, Latin
import unittest

class TestGematria(unittest.TestCase):
    def test_runes_to_latin(self):
        r = Runes(
            """ᛈᚪᚱᚪᛒᛚᛖ ᛚᛁᚳᛖ ᚦᛖ ᛁᚾᛋᛏᚪᚱ ᛏ
            ᚢᚾᚾᛖᛚᛝ ᛏᚩ ᚦᛖ ᛋᚢᚱᚠᚪᚳᛖ 
            ᚹᛖ ᛗᚢᛋᛏ ᛋᚻᛖᛞ ᚩᚢᚱ ᚩᚹᚾ ᚳ
            ᛁᚱᚳᚢᛗᚠᛖᚱᛖᚾᚳᛖᛋ ᚠᛁᚾᛞ ᚦ
            ᛖ ᛞᛁᚢᛁᚾᛁᛏᚣ ᚹᛁᚦᛁᚾ ᚪᚾᛞ ᛖᛗᛖᚱᚷᛖ"""
        )
        self.assertEqual(
            r.to_latin().text,
            """PARABLE LICE THE INSTAR T
            UNNELING TO THE SURFACE 
            WE MUST SHED OUR OWN C
            IRCUMFERENCES FIND TH
            E DIUINITY WITHIN AND EMERGE"""
        )
    
    def test_latin_to_runes(self):
        l = Latin(
            """PARABLE LIKE THE INSTAR T
            UNNELING TO THE SURFACE 
            WE MUST SHED OUR OWN C
            IRCUMFERENCES FIND TH
            E DIVINITY WITHIN AND EMERGE"""
        )
        self.assertEqual(
            l.to_runes().text,
            """ᛈᚪᚱᚪᛒᛚᛖ ᛚᛁᚳᛖ ᚦᛖ ᛁᚾᛋᛏᚪᚱ ᛏ
            ᚢᚾᚾᛖᛚᛝ ᛏᚩ ᚦᛖ ᛋᚢᚱᚠᚪᚳᛖ 
            ᚹᛖ ᛗᚢᛋᛏ ᛋᚻᛖᛞ ᚩᚢᚱ ᚩᚹᚾ ᚳ
            ᛁᚱᚳᚢᛗᚠᛖᚱᛖᚾᚳᛖᛋ ᚠᛁᚾᛞ ᚦ
            ᛖ ᛞᛁᚢᛁᚾᛁᛏᚣ ᚹᛁᚦᛁᚾ ᚪᚾᛞ ᛖᛗᛖᚱᚷᛖ"""
        )
    
    def test_runes_to_numbers(self):
        r = Runes(
            "ᛈᚪᚱᚪᛒᛚᛖ ᛚᛁᚳᛖ ᚦᛖ ᛁᚾᛋᛏᚪᚱ ᛏ"
        )
        # 43,97,11,97,61,73,67,1,1,73,31,13,67,1,1,5,67,1,1,31,29,53,59,97,11,1,1,59
        self.assertEqual(
            r.to_numbers(),
            [43,97,11,97,61,73,67,0,73,31,13,67,0,5,67,0,31,29,53,59,97,11,0,59]
        )
    
    def test_q_to_cw(self):
        l = Latin(
            "QWERTYQUEENPARQ"
        )
        self.assertEqual(
            l.to_runes().to_latin().text,
            "CWWERTYCWEENPARCW"
        )

    def test_double_runes(self):
        r = Latin("IOEA EOE EOEO OEOE AEO AEOE IOE IAE IAEO IAEA")
        self.assertEqual(
            r.to_runes().text,
            "ᛡᛠ ᛇᛖ ᛇᛇ ᛟᛟ ᚫᚩ ᚫᛟ ᛡᛖ ᛡᛖ ᛡᛇ ᛡᛠ"
        )

    def test_runes_across_spaces(self):
        r = Latin("I O")
        self.assertEqual(
            r.to_runes().text,
            "ᛁ ᚩ"
        )
