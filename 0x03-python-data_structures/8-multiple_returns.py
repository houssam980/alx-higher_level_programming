def multiple_returns(sentence):
    if len(sentence) == 0 :
        return sentence[0] == 0 ,"None"
    else:
        return len(sentence) ,sentence[0]
