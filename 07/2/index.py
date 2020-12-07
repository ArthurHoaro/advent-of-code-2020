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

def countChildrenNumber(node: Node):
  total = 0

  if len(node.children):
    for child in node.children:
      total += child.number if child.children else 0
      total += child.number * countChildrenNumber(child)
  else:
    return 1

  return total

def createSubTree(tree: Node, container, number, reference):
  node = Node(container, number)
  tree.addChild(node)

  for color, number in reference[container].items():
    createSubTree(node, color, number, reference)

tree = Node(None, 0)
bagsReference = {}
rootContainers = []

with Path(f'{currentPath}/input').open() as file:
  for line in map(lambda x: x.replace(' bags', '').replace(' bag', '').strip(' .\n'), file):
    container, bags = line.split(' contain ')
    bags = bags.split(', ')
    bagColors = dict((color, number) for color, number in list(map(
      lambda x: [x[2:], int(x[:2].strip())],
      [bag for bag in bags if bag[:2] != 'no']
    )))

    if container in bagsReference:
      bagsReference[container] = {**bagsReference[container], **bagColors}
    else:
      bagsReference[container] = bagColors

isRootBag = lambda container: sum(1 for bag in bagsReference if container in bagsReference[bag]) == 0
for container in bagsReference:
  if isRootBag(container):
    rootContainers.append(container)

print(rootContainers)

for container in rootContainers:
  createSubTree(tree, container, 1, bagsReference)

print(tree)
print('Shiny gold containers:', countContainers('shiny gold', tree))
print('Count children number:', countChildrenNumber(next(findNode('shiny gold', tree))))
