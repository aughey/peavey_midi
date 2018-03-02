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

while True:
  for program in range(0,4):
    msg = mido.Message("program_change", program=program)
    output.send(msg)
    print(program)
    time.sleep(1)
