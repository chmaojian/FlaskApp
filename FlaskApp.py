from flask import Flask
from flask import request
from flask import Response
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search/')
def search():
    return render_template('search.html')


@app.route('/search/graph/', methods=['GET'])
def search_json():
    # name = request.form['name']
    main_node = 'main'
    response_json = '''  {"nodes": [
                {"id": "''' + main_node + '''","title":"", "content": "海城式沉积岩变质菱镁矿", "importance": 7},
                {"id": "n2","title":"", "content": "矿石按含钙、硅量的高低，可以划分出低硅低钙型矿石、高钙型矿石、高硅型矿石、高钙高硅型矿石四种类型", "importance": 3},
                {"id": "n3","title":"", "content": "以菱镁矿为主", "importance": 3},
                {"id": "n4","title":"", "content": "白云质大理岩", "importance": 2},
                {"id": "n5","title":"", "content": "菱镁矿-白色-灰白色，少数为粉红色，半自形晶，主要为中粗粒，局部有巨粒自形菱镁矿晶体呈放射状排列；白云石—主要见于一、四、五、六矿层中。在矿石中呈以下几种形式存在：第一种为细粒他形-半自形晶散布在矿石中，第二种为白云石大理岩包体大小一般为几厘，第三种呈中粗粒自形晶零星散布或呈脉状充填；透闪石—白色，纤维状、放射状集合体，或呈长柱状单晶，常被滑石交代，透闪石分布不均，一般是沿层分布，亦有呈细脉斜交矿层的。", "importance": 1},
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


if __name__ == '__main__':
    app.run()
