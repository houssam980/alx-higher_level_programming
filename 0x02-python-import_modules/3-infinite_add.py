#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    rest = 0
    for i in range(1, len(sys.argv)):
	    rest += int(sys.argv[i])
	    print("{}".format(rest))
