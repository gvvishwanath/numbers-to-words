Lakh = 10 ** 5
Crore = 100 * Lakh

HundredThousand = 100 * 1000
Million = 10 * Lakh
Billion = 1000 * Million

assert Lakh == HundredThousand, \
"Wrong value(s) in biggerNumbers.py : Lakh = %r, HundredThousand = %r" % (Lakh, HundredThousand) 

biggerNumbers = {
    100 : "hundred",
    1000 : "thousand",
    Lakh : "lakh",
    Million : "million",
    Crore : "crore",
    Billion : "billion"
}
