import mido
import sys
import time

midi_name = None
for name in mido.get_output_names():
  if name.startswith("VYPYR"):
    midi_name = name

if not midi_name:
  print("Could not find VYPYR interface")
  sys.exit(1)

output = mido.open_output(midi_name)
print("Opened: " + midi_name)

msg = mido.Message('sysex', data=[0x00,0x00,0x04,0x1b,0x12,0x00,0x04,0x63,0x7f,0x7f,0x05])
print(msg.hex())

output.send(msg)
