#coding:utf-8

import os
import shutil


def isDir(path):

	return os.path.isdir(path)


def isFile(path):

	return os.path.isfile(path)


def convertSlashToBackslash(path):

	path = path.replace("/", "\\")
	return path


def convertBackslashToSlash(path):

	path = path.replace("\\", "/")
	return path


def addExtension(path, ext):

	path = path + ext
	return path


def deleteExtension(path):

	ext = "." + path.split(".")[-1]

	path = path.replace(ext, "")
	return path