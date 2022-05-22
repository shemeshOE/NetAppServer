from sqlalchemy import exists
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Node, Edge, Base

engine = create_engine('sqlite:///NetApp.db?check_same_thread=False')


session = sessionmaker(bind=engine)
s=session()

if not engine.has_table('nodes'):
    Base.metadata.create_all(engine)
    nodes = [
        Node(1, 'winterfell.westeros.got'), Node(2, 'Computers'), Node(3, 'Domain Controllers'), Node(4, 'TheWall'),
        Node(5, 'Kylo-Ou')
    ]
    edges= [ Edge(1, 2), Edge(1, 3), Edge(1, 4), Edge(4, 5) ]
    for n in nodes:
        s.add(n)
    for e in edges:
        s.add(e)
    s.commit()

def getChildren(node_id):
    if(node_id is None):
        return list(map(Node.getDict, s.query(Node).filter(~exists().where(Node.node_id==Edge.child_id)).all()))
    node = s.query(Node).filter(Node.node_id==node_id).one_or_none()
    if node is None:
        return None
    return node.getChildrenList()