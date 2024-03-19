# always a good idea to set variable type while creating a variable

number = 10

# some reason people can change number type
# as by default it was meant to be int but if some one
# change it with float like 10.0 then it can create bug
# all the operation on number was used for int

number = 10.0  # shows no warning or anything, disable mypy for this case to as mypy will automatically catch it
# but if set type then giving float value will show error from code editor
new_number: int = 110.0
# let now try to change value format
new_number = 10.12
