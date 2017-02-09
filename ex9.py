from sys import argv

script,first,second,third = argv

print "The script is called:",script
print "Your first variable is :",first
print "Your second variable is:",second
print "Your third variable is:",third

#argv 和 raw_input()的区别
#它们的不同之处在于要求用户输入的位置不同。
#如果你想让用户在命令行输入你的参数，
#你应该使用argv.，如果你希望用户在脚本执行的过程中输入参数，
#那就就要用到raw_input()。