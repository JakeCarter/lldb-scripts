#!/usr/bin/python

import lldb

def ch(debugger, command, result, internal_dict):
	"""Prints the class hirarchy for a given className or instance via memeory address. (Ex. 'ch NSString|<memory_address_to_an_NSString>' will output 'NSString > NSObject')"""
	
	ci = debugger.GetCommandInterpreter()
	ro = lldb.SBCommandReturnObject()

	command = command.strip()
	
	if len(command) < 1:
		print >>result, "Empty argument. Try 'ch NSString' or 'ch <memory_address_to_an_NSString>'"
		return
	
	ci.HandleCommand("expr -l objc++ -O -- [{} class]".format(command), ro)	
	className = ro.GetOutput().strip()
	if len(className) == 0:
		print >>result, "Could not get class from {}".format(command)
		return
	
	acc = []

	while className != "nil":
		acc.append(className)
		ci.HandleCommand("expr -l objc++ -O -- [{} superclass]".format(className), ro)
		className = ro.GetOutput().strip()

	print >>result, " > ".join(acc)

def __lldb_init_module(debugger, internal_dict):
	debugger.HandleCommand('command script add -f ch.ch ch')
	print 'The "ch" python command has been installed and is ready for use.'
