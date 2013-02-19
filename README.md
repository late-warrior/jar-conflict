jar-conflict
============

Tries to list out similarly named classes across multiple jars

The script version is taken from the comments section of the post in 
http://alvinalexander.com/blog/post/java/shell-script-search-search-multiple-jar-files-class-pattern.

All credit to the original author (Dellaran)

> search-jars com.class.name this/is/the/directory/where/jars/are/present

The python script has a bit of additional functionality.

> search-jars.py -c com.class.name -d this/is/the/directory/where/jars/are/present

If you omit the -c key, the script will print the list of classes that are present in two or more jars
and also the jars in which they are present.


This has been tested in Python 2.7.  I will include a script that works with 2.6.6 as well.
