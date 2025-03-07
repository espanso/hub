import sys
import codecs

# Ensure UTF-8 output
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

if len(sys.argv) < 3:
    print("Error: Please provide two parameters.")
    sys.exit(1)

param1 = sys.argv[1]
param2 = sys.argv[2]

print((chr(0x2605)*int(float(param1)))+(chr(0x2606)*int(float(param2))))