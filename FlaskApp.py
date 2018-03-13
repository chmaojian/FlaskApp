import urllib3
from flask import Flask, redirect
from flask import request
from flask import Response
from flask import render_template
from py2neo import DBMS, Graph

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/assets/')
# def assets():
#     return 'hello'


# handle neo4j browser.
@app.route('/browser')
def browser():
    # return render_template('browser.html')
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://127.0.0.1/p/browser/')
    d = str(r.data, "utf-8").replace("src=", "src=/p/browser/")
    d = d.replace("src=/p/browser/\"", "src=\"/p/browser/")
    d = d.replace("href=", "href=/p/browser/")
    return d


@app.route('/search/')
def search():
    return render_template('search.html')


@app.route('/search_old/')
def search_old():
    return render_template('search_old.html')


@app.route('/p/search/graph/', methods=['GET'])
def search_json():
    # name = request.form['name']
    main_node = 'main'
    response_json = '''  {"nodes": · 
                {"id": "''' + main_node + '''","title":"", "content": "海城式沉积岩变质菱镁矿", "importance": 7},
                {"id": "n2","title":"", "content": "矿石按含钙、硅量的高低，可以划分出低硅低钙型矿石、高钙型矿石、高硅型矿石、高钙高硅型矿石四种类型", "importance": 3},
                {"id": "n3","title":"", "content": "以菱镁矿为主", "importance": 3},
                {"id": "n4","title":"", "content": "白云质大理岩", "importance": 2},
                {"id": "n7","title":"", "content": "矿体具一定层位，赋存于辽河群大石桥组第三段的镁质碳酸盐岩中，矿体产状与围岩基本一致，沿走向、倾向延伸稳定，有时可过渡到白云质岩层", "importance": 2},
                {"id": "s1","title":"", "content": "基性超基性岩型铜镍（银铬）矿", "importance": 4},
                {"id": "s2","title":"", "content": "陆相火山岩热液型锑矿床", "importance": 4},
                {"id": "s3","title":"", "content": "碳酸盐岩—细碎屑岩型铅锌银矿", "importance": 4},
                {"id": "s4","title":"", "content": "成矿要素", "importance": 6},
                {"id": "s5","title":"", "content": "相似矿", "importance": 5}
                ],
                "edges":[
                {"id": "main-n2", "source": "s4", "target": "n2", "fave_color": "#6FB1FC", "strength": 80, "label": "矿石矿物成分"},
                {"id": "main-n3", "source": "s4", "target": "n3", "fave_color": "#6FB1FC", "strength": 80, "label": "大地构造位置"},
                {"id": "main-n4", "source": "s4", "target": "n4", "fave_color": "#6FB1FC", "strength": 80, "label": "岩石类型"},
                {"id": "main-n7", "source": "s4", "target": "n7", "fave_color": "#6FB1FC", "strength": 80, "label": "矿体赋存部位"},
                {"id": "main-n5", "source": "s4", "target": "n5", "fave_color": "#6FB1FC", "strength": 80, "label": "矿石矿物特征"},
                {"id": "main-s1", "source": "s5", "target": "s1", "fave_color": "#6FB1FC", "strength": 80, "label": "相似矿(0.24)"},
                {"id": "main-s2", "source": "s5", "target": "s2", "fave_color": "#6FB1FC", "strength": 80, "label": "相似矿(0.22)"},
                {"id": "main-s3", "source": "s5", "target": "s3", "fave_color": "#6FB1FC", "strength": 80, "label": "相似矿(0.19)"},
                {"id": "main-s4", "source": "main", "target": "s4", "fave_color": "#6FB1FC", "strength": 80, "label": " "},
                {"id": "main-s5", "source": "main", "target": "s5", "fave_color": "#6FB1FC", "strength": 80, "label": " "}
                ]}
          '''
    resp = Response(response=response_json, status=200, mimetype="application/json")
    return resp


# @app.route('/p/query', methods=['GET'])
# def query():
#     graph = Graph(host="localhost", http_port=7474, bolt_port=7687, user='neo4j', password="123456")
#     li = graph.data('''start n = node(*) match (n)-[]->(m) return m,n''')
#     # query_result = '{}'
#     # print(query_result)
#     res_data = Response(response=li, status=200, mimetype="application/json")
#     return res_data


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050, debug=True)
