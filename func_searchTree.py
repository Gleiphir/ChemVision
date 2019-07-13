'''
class Pattern:
    def __init__(self):
'''
import re



DOUBLE_BIND = '='
TRI_BIND = '#'
END_LEAF = chr(4443)
FORK_POINT = chr(4444)
BEGIN_ROOT = chr(4445)

def trace2str(tr):
    texts = [o._s for o in tr]
    return ''.join(texts)

def fixbrace(s:str):
    N = 0
    for i in range(len(s)-1,-1,-1):
        if s[i] == ')':
            N+=1
        if s[i] == '(':
            if N == 0:
                s = s[:i]+s[i+1:]
            else:
                N-= 1

bracematch = lambda s: s.count('(') == s.count(')')

class Node:
    def __init__(self,s,index,parent = None):
        #print(s[index])
        self._parent = parent
        if index >= len(s):
            self._s = END_LEAF
            self._next = []
            self._chem = s
        else:
            self._chem = None
            if s[index] == '(':
                self._s = FORK_POINT
                forks = s.find(')', index)
                subs = s[index + 1:forks+1]
                #print(subs)
                self._next = [
                    Node(s, forks+1,parent=self),
                    Node(subs, 0,parent=self)
                ]

            else:
                self._s = s[index]
                self._next = [Node(s, index + 1,parent=self)]


    def __lt__(self, other):
        return self._s < other._s

Tree = Node(BEGIN_ROOT,0)

def printTree(root):
    list = [root]
    for o in list:
        for x in o._next:
            list.append(x)
        print(o._s,[t._s for t in o._next])

def merge(nodeO:Node,nodeN:Node):
    """
    nodeO and nodeN has same _s
    :param nodeO:
    :param nodeN:
    :return:
    """
    if len(nodeN._next )==0:
        return
    if len(nodeO._next )==0:
        nodeO._next = nodeN._next
        nodeO._next.sort()
        return
    for x in nodeN._next:
        newFlag = True
        for y in nodeO._next:
            if x._s == y._s:
                merge(y,x)
                newFlag = False
                break
        if newFlag:
            nodeO._next.append(x)
    nodeO._next.sort()

    """
    nodeO._next += nodeN._next
    nodeO._next.sort()  
    last = None
    for o in nodeO._next:
        if last ==None:
            last = o
        elif o._s == last._s:
            #common children
            merge(o,last)
            del o
        else:
            last = o

    last = None
    for o in nodeO._next:
        if o._s == last:
            del o
        else:
            last = o._s
 
    for i in range(len(nodeO._next) - 1 ):
        if nodeO._next[i + 1]._s == nodeO._next[i]._s:
            del nodeO._next[i+1]
    """

def match(Tree:Node,pattern:Node,res:list):
    if Tree._s == pattern._s:
        for i in range(len(pattern._s)):
            for j in range(len(Tree._next)):
                match(Tree._next[j],pattern._next[i],res)

    if pattern._s == END_LEAF:
        res.append(Tree)
        return
    else:
        return

def findDown(point:Node,L:list):
    if point._s == END_LEAF:
        L.append(point)
    else:
        for o in point._next:
            findDown(o,L)

def findUp(point:Node):
    trace = []
    p = point
    while p._parent != None:
        trace.append(p)
        p = p._parent
    #print([x._s for x in trace])
    trace.reverse()
    return tuple(trace)

def searchChem(Tree:Node,pattern:Node):
    mtcs = []
    match(Tree, pattern, mtcs)
    #print([t._s for t in R])
    tails_all = []
    for mtc in mtcs:
        tails = []
        findDown(mtc, tails)
        tails_all += tails
    #trs = [findUp(t) for t in tails_all]
    trs = [t._chem for t in tails_all]
    return trs

def ChemTree(s:str):
    return Node(BEGIN_ROOT+s,0)

def Add2Tree(tree:Node,s:str):
    merge(tree, Node(BEGIN_ROOT+s,0))

def Res2HTML(Rs:list):
    res = []
    if len(Rs) == 0:
        return "* No matching case found *"
    for R in Rs:
        if not bracematch(R):
            continue

        rawR = re.sub(r"`", r'', R)
        '''
        rawR = trace2str(R)
        rawR = re.sub(r"@+", r'(', rawR)
        fixbrace(rawR)
        rawR = re.sub(r"\?$", r'', rawR)
        
        '''
        res.append(rawR)
    return res

def buildTree(chems:list):
    TREE = ChemTree(chems[0])
    for s in chems[1:]:
        Add2Tree(TREE,s)
    return TREE

test_chems = [
    "CCSC",
    "CCNO",
    "CCOC(=O)C",
    "CCOCNOC",
]

if __name__ =='__main__':

    tree = Node(BEGIN_ROOT+'ABC(=CO)(=O)D#E',0)
    y = Node(BEGIN_ROOT+'ABDY',0)
    z = Node(BEGIN_ROOT+'ABERF',0)

    ptn = Node(BEGIN_ROOT+'ABC@@',0)

    merge(tree, y)
    merge(tree, z)

    TREE = buildTree(test_chems)

    R = searchChem(tree,ptn)
    for r in R:
        print(trace2str(r))

    printTree(tree)
    '''
    n = tree._next[0]._next[0]._next[0]

    tails =[]
    findDown(n,tails)
    tr = findUp(n)
    tr2 = findUp(tails[0])
    '''

    '''
    print([t._s for t in tr])
    print([t._s for t in tr2])
    print([t._s for t in tails])
    for t in tails:
        print([t._s for t in findUp(t)])
    '''

    #printTree(x)

    input()