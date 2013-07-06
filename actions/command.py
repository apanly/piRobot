#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

class InstructionSet:

	def __init__(self,txt):
		self.txt=txt
		self.browser()
		self.terminal()

	def browser(self):
		if self.txt.find("谷歌") > -1:
			os.system("firefox www.google.com.hk")
		if self.txt.find("百度") > -1:
			os.system("firefox www.baidu.com")
		if self.txt.find("新浪") > -1:
			os.system("firefox www.sina.com.cn")
		if self.txt.find("火狐") > -1:
			os.system("firefox www.echocool.net")


	def terminal(self):
		if self.txt.find("终端") > -1 :
			os.system("gnome-terminal")