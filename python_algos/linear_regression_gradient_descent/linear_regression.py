import numpy as np

def get_gradient(data, m_slope, b_intercept, learning_rate):
    slope_sum = 0
    intercept_sum = 0
    len_data = float(len(data))
    for i in range(len(data)):
        slope_sum += (-data[i][0]) * (data[i][1] - (m_slope * data[i][0] + b_intercept)) * (2/len_data)
        intercept_sum += (data[i][1] - (m_slope * data[i][0] + b_intercept)) * (-2/len_data)
    return [(m_slope - (learning_rate * slope_sum)), (b_intercept - (learning_rate * intercept_sum))]

def run_linear_regression(data, m_slope, b_intercept, learning_rate, num_iters):
    print "Initial values m - %f, b - %f" %(m_slope, b_intercept)
    for i in range(num_iters):
        print "Iteration %d, m - %f, b - %f" %(i, m_slope, b_intercept)
        m_slope, b_intercept = get_gradient(data, m_slope, b_intercept, learning_rate)
    print "Final values m - %f, b - %f" %(m_slope, b_intercept)

def main():
    data = np.genfromtxt("data.csv", delimiter=",")
    # Initializing hyperparameters
    m_slope = 0
    b_intercept = 0
    learning_rate = 0.0001
    num_iters = 200
    run_linear_regression(data, m_slope, b_intercept, learning_rate, num_iters)

if __name__ == "__main__":
    main()
