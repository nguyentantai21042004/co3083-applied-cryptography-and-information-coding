from Crypto.Util.number import * # type: ignore

str = '11515195063862318899931685488813747395775516287289682636499965282714637259206269'

m = long_to_bytes(int(str)) # type: ignore
print(m)