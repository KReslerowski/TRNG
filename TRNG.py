import hashlib
import numpy as np

def entropy1(labels, base=None):
  value,counts = np.unique(labels, return_counts=True)
  norm_counts = counts / counts.sum()
  base = 2 if base is None else base
  return -(norm_counts * np.log(norm_counts)/np.log(base)).sum()


# BUF_SIZE is totally arbitrary, change for your app!
BUF_SIZE = 160  # lets read stuff in 64kb chunks!

output = []

with open("peppers24.bmp", 'rb') as f: # open("example.png/bmp/jpg", 'rb')
    while True:
        data = f.read(BUF_SIZE)
        if not data:
            break
        output.append( hashlib.sha1(data) )

output2 = [ s.hexdigest() for s in output ] #Convert hash back to equivalent string in hex
split_strings = []
for a_string in output2:
    split_strings.append( [a_string[index : index + 2] for index in range(0, len(a_string), 2)] )
output3 = []
for _ in split_strings:
    for j in _:
        output3.append(j)

output4 = [ int(str(s), 16) for s in output3 ]       #Convert hex string to int

print(output4)
print(entropy1(output4, 2))