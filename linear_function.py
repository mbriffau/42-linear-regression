import sys

def linear_function(x, theta0, theta1):
  return theta0 + theta1 * x

if __name__ == '__main__':
  if len(sys.argv) != 4:
    print "Error Params : x, theta0, theta1"
    exit(-1)
  x = float(sys.argv[1])
  theta0 = float(sys.argv[2])
  theta1 = float(sys.argv[3])
  print "y =", linear_function(x, theta0, theta1)
