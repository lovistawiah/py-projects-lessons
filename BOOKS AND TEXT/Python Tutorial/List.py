"""
List are ordered collection of objects that can grow, shrink,updated and deleted.
"""

L = [1, 2, 4, 5, 6]
alphabet = ['abc', 'ABCD', 'Abc']
# Normalize by lower case
alphabet.sort(key=str.lower)
print(alphabet)

#change sort order
alphabet.sort(reverse=True)
print(alphabet)


#NOTE: tuples can also be used as dictionary keys for compound keys such as (dates and IP address)