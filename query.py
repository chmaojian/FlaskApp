from py2neo import Graph,Node,Relationship
from pandas import DataFrame
import json
from py2neo.ogm import GraphObject,Property,RelatedTo,RelatedFrom
from neo4j import GraphDatabase

graph = Graph(host="localhost", http_port=7474, bolt_port=7687, user='neo4j', password="123456")
li = graph.data('''start n = node(*) match (n)-[]->(m) return m,n''')
# df = DataFrame(li)
print(li)



# node = graph.find(label='Att')
# relationship = graph.match(rel_type='属性')
# print(node)
# print(relationship)
# for item in li:
#     print(item)




#
# a = Node('nameMin',name = '纯橄榄岩')
# b = Node('colorMin',name = '深绿色')
# c = Node('colorMin',name = '黄绿色')
# d = Node('mainMin',name = '橄榄石')
# e = Node('cenMin',name = '辉石')
# f = Node('cenMin',name = '角闪石')
# r1 = Relationship(a,'颜色',b)
# r2 = Relationship(a,'颜色',c)
# r3 = Relationship(a,'主要矿物成分',d)
# r4 = Relationship(a,'次要矿物成分',e)
# r5 = Relationship(a,'次要矿物成分',f)
# print(r1,r2,r3,r4,r5)
