from music21 import *
from music21 import corpus
# littleMelody = converter.parse("tinynotation: 3/4 c4 d8 f g16 a g f#")
# littleMelody.show()
# littleMelody.show('')
import os

fp = os.path.join(common.getSourceFilePath(), 'midi', 'testPrimitive',  'test05.mid')
mf = midi.MidiFile()
mf.open(fp)
mf.read()
mf.close()

print(type(mf))

s = midi.translate.midiFilePathToStream('test05.mid')
print(s.tracks)
print( s.show("text") )




# fp2 = mf.write('midi', fp2='pathToWhereYouWantToWriteIt.midi')
# a = converter.parse('test05.midi')

# littleMelody = converter.parse(mf)
# littleMelody.show('midi')
# mf.show('text')
# print( len(mf.tracks) )
#
#
# ks = key.KeySignature(2)
# print(ks)
# eventList = midi.translate.keySignatureToMidiEvents(ks)
# print(eventList)