def count_bits(n):
    return bin(n)[2:].count('1')
# I also wrote code to convert int to binary but decided to use the inbuilt functions as they are more efficient. Ran without issue
'''bi=''
while dec>=2:
	bi+=str(dec%2)
	dec//=2
bi+=str(dec)
bi = bi[::-1]'''
