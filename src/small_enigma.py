from rotor import Rotor
from plugboard import Plugboard
from machine import EnigmaMachine

# erste Version
r3 = Rotor('my rotor1', 'CEADFB', ring_setting=0)#, stepping='A')
r2 = Rotor('my rotor2', 'CADFEB', ring_setting=0)#, stepping='A')
r1 = Rotor('my rotor3', 'ADFBCE', ring_setting=0)#, stepping='A')

# zweite Version / rotiert
# 1 3 2 <- chaotisch
# 2 3 1 <- weniger chaotisch
r1 = Rotor('my rotor1', 'CEADFB', ring_setting=0)#, stepping='A')
r3 = Rotor('my rotor2', 'CADFEB', ring_setting=0)#, stepping='A')
r2 = Rotor('my rotor3', 'ADFBCE', ring_setting=0)#, stepping='A')


#reflector = Rotor('my reflector', 'FVPJIAOYEDRZXWGCTKUQSBNMHL')
reflector = Rotor('my reflector', 'CFAEDB')

#pb = Plugboard.from_key_sheet('AF CD EB')
pb = Plugboard()

machine = EnigmaMachine([r1, r2, r3], reflector, pb)
#machine = EnigmaMachine([r1], reflector, pb)

def mapper(text):
    mapping = 'ENIGMA'
    new_text = ""
    for s in text:
        new_text += mapping[ord(s) - ord('A')] + " "
    return new_text

def test_female(msg):
    female = []
    for i in range(6):
        female.append(msg[i] == msg[i+3])
    return female

def lochkarte(bool_list):
    return str(['o' if _ else '.' for _ in bool_list])

for a in [chr(ord('A')+i) for i in range(6)]:
    for b in [chr(ord('A')+i) for i in range(6)]:
        # set machine initial starting position
        final_female = [False for _ in range(6)]
        for msg in [x * 9 for x in [chr(ord('A')+i) for i in range(6)]]:
            #print(msg)
            init = a + b + 'F'
            machine.set_display(init)

            # decrypt the message key
            msg_key = machine.process_text(msg)
            #print(msg_key)
            female = test_female(msg_key)
            final_female = [a or b for (a, b) in zip(female, final_female)]
            print("%s -> %s" % (mapper(msg_key), lochkarte(female)))
        print(lochkarte(final_female))
    print()

# decrypt the cipher text with the unencrypted message key
#machine.set_display(msg_key)

#ciphertext = 'ABCABCDEF'
#plaintext = machine.process_text(ciphertext)

#print(plaintext)
