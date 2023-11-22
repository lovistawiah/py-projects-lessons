#Common data archiving and compression formats are directly supported by modules including: zlib, gzip, bz2, lzma, zipfile and tarfile.
import zlib

#NOTE: b before string literal to make it byte
s = b'witch which has which witches wrist watch'
print(type(s))
print(len(s))

#compressing bytes to smaller size
t =zlib.compress(s)
print(type(t),t)
print(len(t))

#decompressing bytes to original size
decom = zlib.decompress(t)
print(type(decom), decom)
print(len(decom))


print(zlib.crc32(s))