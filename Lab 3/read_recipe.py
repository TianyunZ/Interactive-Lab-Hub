import sys

dish = [''] * 4
dish[0] = sys.argv[1]
dish[1] = sys.argv[2]
dish[2] = sys.argv[3]
dish[3] = sys.argv[4]
dic = {
    "mashedpotatowithsteak": "recp/1.txt",
    "mashedpotatoandmushroom": "recp/2.txt",
    "tomatoandbeefsoup": "recp/3.txt",
}

#read txt method
dish = ''.join(dish)
# sys.exit(dic[dish])
f = open(dic[dish])
line = f.readline()
recp = ''
while line:
    recp = line
    line = f.readline()
f.close()
print(recp)
# sys.exit(recp)
 