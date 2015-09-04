# lldb-scripts
Scripts to make debugging a tiny bit easier.

## Usage
Easiest way to use these is to add a .lldbinit to your home directory and use the `command script import` command to add them.

Example:
```command script import /path/to/lldb-scripts/ch.py```

## Included Scripts

__ch__ — The ch (superClass Hierarchy) will print the superclass hierarchy of a given class name or memory address pointing to an ObjC object.

Example:

	(lldb) ch NSString
	NSString > NSObject

	(lldb) ch 0x000000000000 // Memory address pointing to an NSString
	NSString > NSObject
