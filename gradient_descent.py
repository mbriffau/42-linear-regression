import sys
import pandas as pd

# def average(var):
#   size = len(var)
#   sum = 0.0
#   for index in range(size):
#     sum += var[index]
#   return sum / size
#
# def ordinary_least_squares(x, y):
#   xMean = average(x)
#   yMean = average(y)
#   numerator = 0.0
#   for index in range(len(x)):
#     numerator += (y[index] - yMean) * (x[index] - xMean)
#   denominator = 0.0
#   for index in range(len(x)):
#     denominator += (x[index] - xMean)**2
#   theta1 = numerator / denominator
#   theta0 = yMean - theta1 * xMean
#   return theta0, theta1

################################################################################

def loss_function(x, y, theta0, theta1):
  size = len(x)
  sum = 0.0
  for index in range(size):
    sum += (theta0 + theta1 * x[index] - y[index])**2
  return sum / size

def gradient_theta_0(x, y, theta0, theta1):
  size = len(x)
  sum = 0.0
  for index in range(size):
    sum += theta0 + theta1 * x[index] - y[index]
  return sum / size

def gradient_theta_1(x, y, theta0, theta1):
  size = len(x)
  sum = 0.0
  for index in range(size):
    sum += x[index] * (theta0 + theta1 * x[index] - y[index])
  return sum / size

def gradient_descent(x, y, alpha):
  theta0 = 0
  theta1 = 0
  for _ in range(100000):
    loss = loss_function(x, y, theta0, theta1)
    gradientTheta0 = gradient_theta_0(x, y, theta0, theta1)
    gradientTheta1 = gradient_theta_1(x, y, theta0, theta1)
    theta0 -= alpha * loss/gradientTheta0
    theta1 -= alpha * loss/gradientTheta1
  return theta0, theta1

if __name__ == '__main__':
  if len(sys.argv) != 2:
    print "Error"
    exit(-1)
  data = pd.read_csv(sys.argv[1])
  x = [_ for _ in data["km"]]
  y = [_ for _ in data["price"]]
  # theta0, theta1 = ordinary_least_squares(x, y)
  # print "theta0", theta0
  # print "theta1", theta1
  theta0, theta1 = gradient_descent(x, y, 0.1)
  print "theta0", theta0
  print "theta1", theta1
