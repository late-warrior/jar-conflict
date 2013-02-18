#!/usr/bin/python
import optparse
import subprocess

def find_class_in_jar(jar):
    ja = ["jar","tf",jar]
    class_list = subprocess.check_output(ja).split("\n")
    class_list.pop()
    return [class_name for class_name in class_list if class_name.endswith(".class")]

def find_jars_in_directory(directory):
    find = ["find",directory,"-name","*.jar"]
    jar_list = subprocess.check_output(find).split("\n")
    jar_list.pop()
    return jar_list

def find_class(jar_name,class_):
    class_list = find_class_in_jar(jar_name)
    complete_class_name = class_ + ".class"
    try:
        class_list.index(complete_class_name)
    except ValueError:
        return False
    return True

def main(class_,directory):
    #Change format of the class
    class_ = class_.replace(".","/")
    jar_list = find_jars_in_directory(directory)
    found_jars = [jar for jar in jar_list if find_class(jar,class_)]
    print found_jars

def find_duplicate_classes(directory):
    #dict of class name to list of jars that contain them,
    #finally print out those entries in the dict whose list values
    #are greater than 1
    return_dict = {}
    jar_list = find_jars_in_directory(directory)
    jar_class_dict = {jar:tuple(find_class_in_jar(jar)) for jar in jar_list}
    for jar_name,class_tuple in jar_class_dict.iteritems():
        for class_name in class_tuple:
            if return_dict.has_key(class_name):
                return_dict[class_name].append(jar_name)
            else:
                return_dict[class_name] = []
                return_dict[class_name].append(jar_name)
    #Print only those classes that are found in more than 2 jars
    duplicate_dict =  {claz: jars for claz,jars in return_dict.iteritems() if len(jars) > 1}
    print duplicate_dict
        
if __name__== "__main__":
    parser = optparse.OptionParser()
    parser.add_option("-c","--classs",help="name of the class that you want \
    to search")
    parser.add_option("-d","--directory",help="directory that you want to \
    search")
    (options,args) = parser.parse_args()
    if options.classs == None:
        #If it is run without the class argument
        find_duplicate_classes(options.directory)
    else:
        main(options.classs,options.directory)
