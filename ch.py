#!/usr/bin/python

import lldb

def pof(debugger, command, result, internal_dict):
	usage = "usage: %prog <instance|class>"
	'''Prints the class hirarchy for a given className or instance via memeory address. (Ex. 'ch NSString|<memory_address_to_an_NSString>' will output 'NSString > NSObject')
	'''
	print >>result, internal_dict
	return
	
	ci = debugger.GetCommandInterpreter()
	ro = lldb.SBCommandReturnObject()

	command = command.strip()
	if len(command) < 1:
		print >>result, "Empty argument."
		return

	ci.HandleCommand('expr -O -- [%(command)s class]' % {"command" : command}, ro)
	className = ro.GetOutput().strip()

	acc = []

	while className != "nil":
		acc.append(className)
		ci.HandleCommand('expr -O -- [%(className)s superclass]' % {"className" : className}, ro)
		className = ro.GetOutput().strip()

	print >>result, " > ".join(acc)

def __lldb_init_module(debugger, internal_dict):
	debugger.HandleCommand('command script add -f ch.pof ch')
	print 'The "ch" python command has been installed and is ready for use.'
