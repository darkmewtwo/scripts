# import n


# print(dir(n))
# f=getattr(n, 'd')('we', 10, 'tyyttt')
# print(f)

import fire


def add(x, y):
    print(x,y)
    return x + y

def multiply(x, y):
    return x * y

def g(fun):
    print(__name__, 'in module f')
    return fun()

if __name__ == '__main__':
  fire.Fire({
      'add': add,
      'mul': multiply,
  })
    # fire.Fire()