import logging
import os
logging.basicConfig(level=logging.INFO)
print(os.name)
print(os.environ.get('PATH'))
print(os.path.abspath('.'))
print(os.path.join('/Users/jitang/Documents/ugly-python3-webapp/www','mkdir'))
os.mkdir('/Users/jitang/Documents/ugly-python3-webapp/www/mkdir')
os.rmdir('/Users/jitang/Documents/ugly-python3-webapp/www/mkdir')
try:
    print('try...')
    r = 10 / 2
    print('result:', r)
except Exception as e:
    logging.exception(e)
finally:
    print('finally...')
print('END')

# the following can be used as dir -l
[print(x) for x in os.listdir('.')]


[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']


def p_decorate(func):
    def func_wrapper(*args, **kwargs):
        return "<p>{0}</p>".format(func(*args, **kwargs))
    return func_wrapper


class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorate
    def get_fullname(self):
        return self.name+" "+self.family

my_person = Person()

print(my_person.get_fullname())

import functools

def log(name='log'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            print('%s: before call %s()' % (name,func.__name__))
            print('{0}'.format(func(*args,**kwargs)))
            print('%s: after call %s()' % (name,func.__name__))
            return func(*args,**kwargs)
        return wrapper()
    return decorator
@log('execute')
def now():
    print('2016-10-21')
now()

@log('execute')
def now():
    print('2016-10-21')
now()
