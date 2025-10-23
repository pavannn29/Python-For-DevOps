'''
'pip freeze' returns all the packege installed in a given python environment along with the version.

pip freeze > requirements.txt

The above command create a files name in the same direcory containing the output of 'pip freeze'.
we can distribute this file to other users. and they can recreates the same environment using:

pip install -r requirement.txt

'''

