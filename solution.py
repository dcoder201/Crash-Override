
def alias_gen(f_name, l_name):
    if ((f_name[0].upper()).isalpha()) and ((l_name[0].upper()).isalpha()):
        return (FIRST_NAME[f_name[0].upper()]+' '+SURNAME[l_name[0].upper()])
    else:
        return 'Your name must start with a letter from A - Z.'

basic_tests = (
    (('Mike', 'Millington'), 'Malware Mike'),
    (('Fahima', 'Tash'), 'Function T-Rex'),
    (('Daisy', 'Petrovic'), 'Data Payload'),
    (('Barny', 'White'), 'Beta Worm'),
    (('Hank', 'Kutz'), 'Half-life Killer'),
    (('123abc', 'Pinkman'), 'Your name must start with a letter from A - Z.'),
    (('walter', 'white'), 'WiFi Worm')
)

for names, result in basic_tests:
    test.it('{} {}'.format(*names))
    test.assert_equals(alias_gen(*names), result)
