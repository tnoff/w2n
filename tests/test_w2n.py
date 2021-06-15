import pytest
from word2number import w2n

def test_positives():
   assert w2n.word_to_num("two million three thousand nine hundred and eighty four") ==  2003984
   assert w2n.word_to_num("nineteen") ==  19
   assert w2n.word_to_num("two thousand and nineteen") ==  2019
   assert w2n.word_to_num("two million three thousand and nineteen") ==  2003019
   assert w2n.word_to_num('three billion') ==  3000000000
   assert w2n.word_to_num('three million') ==  3000000
   assert w2n.word_to_num('one hundred twenty three million four hundred fifty six thousand seven hundred and eighty nine') == 123456789
   assert w2n.word_to_num('eleven') ==  11
   assert w2n.word_to_num('nineteen billion and nineteen') ==  19000000019
   assert w2n.word_to_num('one hundred and forty two') ==  142
   assert w2n.word_to_num('112') ==  112
   assert w2n.word_to_num('11211234') ==  11211234
   assert w2n.word_to_num('five') ==  5
   assert w2n.word_to_num('two million twenty three thousand and forty nine') ==  2023049
   assert w2n.word_to_num('two point three') ==  2.3
   assert w2n.word_to_num('two million twenty three thousand and forty nine point two three six nine') == 2023049.2369
   assert w2n.word_to_num('one billion two million twenty three thousand and forty nine point two three six nine') == 1002023049.2369
   assert w2n.word_to_num('point one') ==  0.1
   assert w2n.word_to_num('point') ==  0
   assert w2n.word_to_num('one hundred thirty-five') ==  135
   assert w2n.word_to_num('hundred') ==  100
   assert w2n.word_to_num('thousand') ==  1000
   assert w2n.word_to_num('million') ==  1000000
   assert w2n.word_to_num('billion') ==  1000000000
   assert w2n.word_to_num('nine point nine nine nine') ==  9.999
   assert w2n.word_to_num('five thousand, six hundred') ==  5600
   assert w2n.word_to_num('hundred and fifteen million') ==  115000000
   assert w2n.word_to_num('forty-five hundred') ==  4500

def test_negatives():
    for word in ['112-', '-', 'on', 'million million', 'three million million', 'million four million',
                 'thousand million', 'one billion point two million twenty three thousand and forty nine point two three six nine',
                 'twothousand and one', 'seven point nineteen', 'point nineteen', 112]:
        with pytest.raises(ValueError) as exc:
            w2n.word_to_num(word)
        assert str(exc.value)