'''
def isnumber():
 while(True):
    try:
      answer = input("Enter a no:  ")
      n = int(answer)
          #if error any statement after that, it will search for next except statement
      return n
    except ValueError:
      print('ValueError')
    except:
      print(n)


a  = isnumber()
#print(isnumber())
print(a)
'''
'''
import os

def filename():
 while(True):
    file = input('Enter file name you wish to open : ')
    try:
      path = os.path.join(os.getcwd(), file)
      o = open(path)
      no_oflines = 0
      if o:
        while True:
          r = o.readline()
          if not r:
            break
          else:
            no_oflines += int(r)
      return no_oflines
    except ValueError:
      print('Sorry!! Unable to convert to integer.')
    except FileNotFoundError:
      print('File not found!')
    except:
      print(o)
      o.close()   
a  = filename()
#print(isnumber())
print(a)
'''
'''
import os

def filename():
 while(True):
    file = input('Enter file name you wish to open : ')
    try:
      path = os.path.join(os.getcwd(), file)
      o = open(path)
      no_oflines = 0
      if o:
        while True:
          r = o.readline()
          if not r:
            break
          else:
            no_oflines += int(r)
      return no_oflines
    except ValueError:
      print('Sorry!! Unable to convert to integer.')
    except FileNotFoundError:
      print('File Name : '+str(file)+' ---with specified path--- '+str(path)+' ---File not found!')
    except Exception as e:
      #print('unexpected error!!!')
      e.args
      print(type(e))
      #o.close()
    finally:
      try:
        o.close()
      except:
        print(str(o)+' was never created')
a  = filename()

#print(isnumber())
print(a)

'''
'''
import os

def filename():
 while(True):
    file = input('Enter file name you wish to open : ')
    try:
      path = os.path.join(os.getcwd(), file)
      o = open(path)
      no_oflines = 0
      if o:
        while True:
          r = o.readline()
          if not r:
            break
          else:
            no_oflines += int(r)
      return no_oflines
    except ValueError:
      print('Sorry!! Unable to convert to integer.')
    except FileNotFoundError:
      print('File not found!')
    except:
      print(o)
      o.close()
    else:
      print('Success')
filename()
#print(isnumber())
print(a)
'''
'''
try:
  raise SyntaxError('add error')
  s = 1 + x
  print(s)
except Exception as e:
  print(e.args)
  '''
'''
#stack trace error across fun

def fun3():
  raise SyntaxError('Error')
def fun2():
  fun3()
def fun1():
  fun2()

fun1()

'''

'''

def function3():
  raise SyntaxError('Error')
  print('function 3')
def function2():
  try:
    function3()
  except:
     print('Function 2')
def function1():
  function2()
  print('Function 1')

function1()

'''
'''

class circle():
  def __init__(self):
    self.radius = 3
c = circle()
print(c.radius)
'''

class Robot():
  def __init__(self,name):
    self.name = name
    #print('I am Robot :'+ name)
  def say.name(self):
    print('I am Robot :'+ self.name)
    
R1 = Robot('Optimus Prime')
R1.say.name():
  #print('I am Robot :'+ name)
  
    
