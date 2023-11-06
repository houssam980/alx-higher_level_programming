#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return sentence[0] == None
    else:
        return len(sentence) ,sentence[0]
