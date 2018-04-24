
import sys
from optparse import OptionParser

def disList(l):
    print(len(l))
    for i in range(0,l.__len__()):
        print(l[i])

print(len(sys.argv))

# for i in range(0,sys.argv.__len__()):
#     print(sys.argv[i])
#
print(sys.argv[:1])
parser=OptionParser()
parser.add_option("-f","--file",dest="filename",help="write report to FILE",metavar="FILE")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options,args)=parser.parse_args()

print(options.filename)
disList(args)








