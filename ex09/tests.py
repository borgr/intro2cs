from hzlib import *
data = "aaaaac"
codebook = build_canonical_codebook(build_codebook(make_huffman_tree(symbol_count(data))))
code = "".join(str(bit) for bit in pad(join(compress(data,codebook), codebook)))
code = join(compress(data,codebook), codebook)
print(list(pad(code)))
result = unpad((int(bit) for bit in code))
print( list(unpad(pad(join(compress(data,codebook), codebook)))) ==
list(join(compress(data,codebook), codebook)))
x = "".join(str(bit) for bit in[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 80, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6])
y = (int(bit) for bit in x)
splited = split(result)
##print(splited[0], splited[1])
##decodebook = build_decodebook(splited[1])
##result = decompress(result, decodebook)
##print(decodebook)
