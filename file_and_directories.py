from pathlib import Path

# Absolute path.
'''
c:\Program Files\Microsoft <- for windows path
/user/local/bin <- for mac path
'''
# Relative path

#       for check is any path exists
path = Path("ecommerce_pkg")
# print(path.exists())

#       for make a directory

path = Path("emails")
# print(path.mkdir())

#       for remove directory

path = Path("emails")
# print(path.rmdir())

#       for search in this directory any thing

path = Path()
# for file in path.glob('*.py'):
for file in path.glob('*'):
    print(file)