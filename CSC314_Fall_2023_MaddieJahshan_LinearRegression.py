import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import turtle

'''Applies the data (The decrease in marathon times from 1920 to 2023)'''
def load_data():
    data = {
        'Year': list(range(1920, 2023)),
        'Time(mins)': [
            167.5, 166.433333, 160.783333, 156.166667, 155.983333, 154.416667, 155.356667, 152.95, 150.96, 156.55,
        153.316667, 151.516667, 151.166667, 152.933333, 146.233333, 148.533333, 150.633333, 150.46, 151.433333,
        153.7, 151.45, 151.633333, 158.588333, 160.81, 156.626667, 151.616667, 150.966667, 151.033333, 148.656667,
        149.156667, 148.123333, 140.703333, 138.58, 137.656667, 141.36, 138.08, 139.833333, 135.293333, 137.753333,
        135.27, 138.9, 136.16, 134.466667, 132.186667, 132, 134.08, 129.606667, 130.796667, 128.56, 129.48, 131.146667,
        130.5, 131.21, 129.2, 129.916667, 129.916667, 130.921667, 129.093333, 129.45, 129.016667, 128.3, 128.866667,
        128.616667, 128.083333, 127.2, 127.85, 128.3, 126.833333, 128.016667, 128.266667, 128.883333, 128.116667,
        128.85, 127.25, 127.033333, 128.416667, 127.166667, 126.083333, 125.7, 126.6, 126.833333, 125.63, 124.916667,
        126.233333, 126.325, 125.933333, 124.433333, 123.97, 124.438333, 124.8, 123.633333, 124.25, 123.383333, 122.95,
        124, 123.05, 123.533333, 121.65, 121.683333, 123, 122.95, 121.15, 120.58333333
        ]
    }

    df = pd.DataFrame(data)
    df = df.rename(columns={'Time(mins)': 'mins'})
    df.insert(2, 'x-xbar', 0)
    df.insert(3, 'y-ybar', 0)
    df['Year'] = df['Year'] - 1920
    return df

'''Finds the Regression Parameters'''
def calculate_regression(df):
    #numerator
    sumx = df['Year'].sum()
    sumy = df['mins'].sum()
    xbar = sumx / len(df)
    ybar = sumy / len(df)
    df['x-xbar'] = df['Year'] - xbar
    df['y-ybar'] = df['mins'] - ybar

    df.insert(4, 'z', 0)
    df['z'] = df['x-xbar'] * df['y-ybar']
    numerator = df['z'].sum()

    #denominator
    df.insert(5, '(x-xbar)^2', 0)
    df['(x-xbar)^2'] = df['x-xbar']**2
    denominator = df['(x-xbar)^2'].sum()

    m = numerator / denominator
    b = ybar - (m * xbar)

    return m, b

''' Plotting the Regression Line'''
def calculate_and_plot_regression(df):
    m, b = calculate_regression(df)
    #plot_data(df, m, b)
    plt.figure(figsize=(10, 5))
    plt.title("Improvement in Marathon Times over the Years", fontsize=16, pad=15)
    plt.xlabel("Years Since 1920", labelpad=15, fontsize=14)
    plt.ylabel("Time in Minutes", labelpad=15, fontsize=14)

    xplot = df['Year']
    yplot = df['mins']
    plt.scatter(xplot, yplot, color='mediumturquoise', label='Data Points')
    plt.scatter(xplot, yplot, color='mediumturquoise', marker='*', alpha=0.4)

    xvalues = range(df['Year'].min(), df['Year'].max() + 1)
    yvalues = [m * x + b for x in xvalues]
    plt.plot(xvalues, yvalues, color='mediumseagreen', label='Regression line')
    plt.legend()
    plt.show()
    print(m)

#    ''' Plotting the Turtle Line'''
#def plot_data(df, m, b):
    #plt.figure(figsize=(10, 5))
    #plt.title("Improvement in Marathon Times over the Years", fontsize=16, pad=15)
    #plt.xlabel("Years Since 1920", labelpad=15, fontsize=14)
    #plt.ylabel("Time in Minutes", labelpad=15, fontsize=14)

    #xplot = df['Year']
    #yplot = df['mins']
    #plt.scatter(xplot, yplot, color='mediumturquoise', label='Data Points')
    #plt.scatter(xplot, yplot, color='mediumturquoise', marker='*', alpha=0.4)

    #x1 = 1
    #x2 = 103
    #y1 = m*x1 + b
    #y2 = m*x2 + b
    #plt.plot([x1, x2], [y1, y2], color='lightpink', label='Turtle Line')

    #plt.legend()
    
    #plt.show()

if __name__ == "__main__":
    df = load_data()
    calculate_and_plot_regression(df)
 
  
