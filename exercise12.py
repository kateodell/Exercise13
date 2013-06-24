#!/usr/bin/env python

class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tokenize(string):
    return string.replace("(", " ( ").replace(")", " ) ").split()

def consume(token_list):
    return token_list.pop(0)

def isoperation(token):
    for operator in '+-/*':
        if operator == token:
            return True
    return False

def build_parse_tree(token_list):
    """Takes in a token list and produces a parse tree according to the rules in the README"""
    # REPLACE THIS WITH REAL CODE
    # root = BinaryTreeNode("+")
    # left = BinaryTreeNode(3)
    # right = BinaryTreeNode(2)
    # root.left = left
    # root.right = right
    # return root
    
    
    
    # Token_list[0] = either ( or a number

    current_node = BinaryTreeNode(None)

    # if it is an open paren, call build_parse_tree on the remaining input
    # and assign results to the left side of current node
    # print "building parse tree for ", token_list
    while len(token_list) > 0:
        t = token_list.pop(0)
        if t == '(':
            current_node.left = build_parse_tree(token_list)


        # if the token is an operator, set the current node's value to that operator and build_parse_tree
        # remaining input and assign 

        elif isoperation(t):
            current_node.value = t
            current_node.right = build_parse_tree(token_list)

        # if the token is a number, set the value of the current node to the number (converting it from a string)
        # and return that node

        elif is_num(t):
            current_node.value = int(t)
            return current_node

        # if the current token is ")", return current node
        elif t == ')':
            return current_node


# rewrite this just for fun

def is_num(string):
    try:
        int(string)
        return True
    except:
        return False

def evaluate_tree(node):
    if node is None:
        return
    if type(node.value) == int:
        return node.value
    elif node.value == "+":
        return evaluate_tree(node.left) + evaluate_tree(node.right)
    elif node.value == "*":
        return evaluate_tree(node.left) * evaluate_tree(node.right)
    elif node.value == "/":
        return evaluate_tree(node.left) / evaluate_tree(node.right)
    elif node.value == "-":
        return evaluate_tree(node.left) - evaluate_tree(node.right)

def main():
    sample_string = "(((3 + 2) * (4 - 1) / 3 + 7) * (1 + (-5 + 6)))"
    tokens = tokenize(sample_string)
    tree = build_parse_tree(tokens)
    print "the answer is ", evaluate_tree(tree)

if __name__ == "__main__":
    main()
