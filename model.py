from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Node(Base):
    __tablename__ = 'nodes'
    node_id = Column(Integer, primary_key=True)
    node_name = Column(String)
    edges = relationship('Edge', foreign_keys='[Edge.parent_id]', back_populates='parent')

    def __init__(self, id, name) -> None:
        self.node_id=id
        self.node_name=name

    def getChild(edge):
        return dict(node_id=edge.child.node_id, node_name=edge.child.node_name)

    def getChildrenList(self):
        return list(map(Node.getChild, self.edges))

    def getDict(self):
        return dict(node_id=self.node_id, node_name=self.node_name)

class Edge(Base):
    __tablename__ = 'edges'
    parent_id = Column(Integer, ForeignKey('nodes.node_id'), primary_key=True)
    parent = relationship('Node', foreign_keys=[parent_id])
    child_id = Column(Integer, ForeignKey('nodes.node_id'), primary_key=True)
    child = relationship('Node', foreign_keys=[child_id], back_populates='edges')

    def __init__(self, parent_id, child_id) -> None:
        self.parent_id=parent_id
        self.child_id=child_id