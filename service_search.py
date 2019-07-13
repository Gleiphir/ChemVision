from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import send_from_directory


import func_searchTree as S


TREE = S.buildTree(S.test_chems)
"""
print(S.test_chems)
print("tree build done")
S.printTree(TREE)
"""

if __name__ == '__main__':
    app = Flask(__name__)
else:
    from server_def import app


@app.route('/search')
def search_getUserPattern():
    return render_template('search.html')

@app.route('/search/result', methods=['POST', 'GET'])
def search_search():
    userPattern=request.form['pattern']
    Rs = S.searchChem(TREE, S.ChemTree( userPattern) )
    fixedResults = S.Res2HTML(Rs)
    return render_template('searchresult.html',pattern = userPattern,results=fixedResults)

if __name__ == '__main__':
    app.run(port=5720,debug=True)
else:
    print("Loaded module : "+__name__)