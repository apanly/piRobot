import jieba

class jiebaseg:
	def __init__(self,txt):
		self.txt=txt

	def cut(self,mode=False):
		return jieba.cut(self.txt,cut_all=mode)

