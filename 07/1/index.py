import os
import re
import pprint
from pathlib import Path

currentPath = os.path.dirname(os.path.realpath(__file__))
class Node:
  def __init__(self, value, number, parent = None):
    self.parent = parent
    self.value = value
    self.number = number
    self.children = []

  def addChild(self, node):
    node.parent = self
    self.children.append(node)

  def __str__(self, prefix = ''):
    return '%sNode<%s [%d]>%s' % (
      prefix,
      self.value,
      int(self.number),
      '\n' + '\n'.join(child.__str__(prefix + '  ') for child in self.children) if len(self.children) > 0 else ''
    )

def findNode(value, tree):
  found = False
  if tree.value == value:
    found = True
    yield tree
  elif tree.children:
    for node in tree.children:
      for res in findNode(value, node):
        if res is not None:
          found = True
          yield res

  if found is False:
    yield

def countContainers(value, tree):
  containers = {}
  for node in findNode(value, tree):
    if node is None:
      continue
    while node.parent is not None:
      if node.value != value:
        containers[node.value] = True
      node = node.parent

  pprint.pprint(containers)

  return len(containers)

def createSubTree(tree: Node, container, reference):
  node = Node(container, 1)
  tree.addChild(node)

  for child in reference[container]:
    createSubTree(node, child, reference)

tree = Node(None, 0)
containersRef = {}
rootContainers = []

with Path(f'{currentPath}/input').open() as file:
  for line in map(lambda x: x.replace(' bags', '').replace(' bag', '').strip(' .\n'), file):
    container, bags = line.split(' contain ')
    bags = bags.split(', ')
    bagColors = list(map(lambda x: x[2:], [bag for bag in bags if bag[:2] != 'no']))
    containersRef[container] = containersRef[container] + bagColors if container in containersRef else bagColors

isRootBag = lambda container: sum(1 for bag in containersRef if container in containersRef[bag]) == 0
for container in containersRef:
  if isRootBag(container):
    rootContainers.append(container)

print(rootContainers)

for container in rootContainers:
  createSubTree(tree, container, containersRef)

print(tree)
print('Shiny gold containers:', countContainers('shiny gold', tree))
