
class Voluntary(object):
	"""docstring for Voluntary"""

	def __init__(self):
		super(Voluntary, self).__init__()
		self.friendBond = []
		self.focusKnown = []
		self.nodeId = 0

#++++++++++ Method to add the focus to vertices+++++++++++++
	def addFocus(self, vertices, focus):
		"""adding all focus to all voluntaries"""
		vertices.focusKnown.append(focus)
