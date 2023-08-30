#!/usr/bin/python3
def multiple_returns(sentence):
    count_sen = len(sentence)
    if (count_sen == 0):
        new_tuple = (count_sen, None)
    else:
        new_tuple = (count_sen, sentence[0])
    return (new_tuple)
