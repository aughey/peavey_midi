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

msg = mido.Message("program_change", program=int(sys.argv[1]))
output.send(msg)
