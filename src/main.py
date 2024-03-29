import re
import os
import sys

from comp_stat import *

class Parser():

    def __init__(self,text):
        self.text = text
        self.start = None

    def parse(self):

        #strip away tabs, whitespaces and newline

        ####Don't touch this
        parts = re.split(r"""("[^"]*"|'[^']*')""", self.text)
        parts[::2] = map(lambda s: "".join(s.split()), parts[::2]) # outside quote
        self.text = "".join(parts)
        self.text = self.text.rstrip()
        ###Don't touch this

        self.start = CompoundStatement(self.text)
        return self.start

class Program(object):

    def __init__(self,text):
        self.parser = Parser(text)
        self.state = {}
        self.parsed_prog = None

    def parse(self):
        self.parsed_prog = self.parser.parse()

    def execute(self):
        self.parsed_prog.eval(self.state)

    def checkState(self):

        # print("Printing Current State of Program......")
        for x in self.state:
            print(x,"==>",self.state[x])


if __name__ == '__main__':

    filename = sys.argv[1]
    if filename.lower().endswith('.h') == False:
        print("syntax error")
    else:
        curr_file = open(filename, 'r')
        text = curr_file.read()

        P = Program(text)
        print("\n########################")
        print("Parsing ", filename)
        P.parse()
        print("Parsing is completed!")
        print("Output for ", filename, " : ")
        P.execute()
        print("########################")
