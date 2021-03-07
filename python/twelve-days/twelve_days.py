days = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
]
gifts = [
    "a Partridge in a Pear Tree",
    "two Turtle Doves",
    "three French Hens",
    "four Calling Birds",
    "five Gold Rings",
    "six Geese-a-Laying",
    "seven Swans-a-Swimming",
    "eight Maids-a-Milking",
    "nine Ladies Dancing",
    "ten Lords-a-Leaping",
    "eleven Pipers Piping",
    "twelve Drummers Drumming"
]
def recite(start_verse, end_verse):
    verse = "On the {days[start_verse]} day of Christmas my true love gave to me: {gifts[start_verse]}. ".format()
    while (start_verse != end_verse):
        verse += "On the " + {days[start_verse]} + " day of Christmas my true love gave to me: " + {gifts[start_verse + 1]} + ", and a " + {gifts[start_verse]} + "."
        start_verse += 1
    return verse

