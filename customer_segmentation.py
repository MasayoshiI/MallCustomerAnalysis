# Author: Masayoshi Iwasa
# Desc: to practice basic plt skills and k-mean clustering 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

class MallCustAnalyzer():
    """Mall Customer Data Analyze Class"""

    def __init__(self, filename):
        """Constructor for MallCustAnalyzer with param filename"""

        self.filename = filename
        self.df = self.get_df()
    
    def get_filename(self):
        """get file name """

        return self.filename
    
    def get_df(self):
        """creates df from file"""

        return pd.read_csv(self.filename)

    def get_summary(self):
        """get summary of df"""

        return self.df.describe()
    
    def plot_bar_graph(self, column):
        """plot a bar graph for given column"""

        d = self.df [column].value_counts().to_dict()
        plt.bar(range(len(d)), list(d.values()), align='center')
        plt.xticks(range(len(d)), list(d.keys()))
        plt.title(column)
        plt.show()
    
    def draw_pie_chart(self, column):
        """create pie chart for a given column"""

        d = self.df [column].value_counts().to_dict()
        plt.pie(list(d.values()), labels = list(d.keys()),autopct="%.1f%%")
        # plt.xticks(range(len(d)), list(d.keys()))
        plt.title(column)
        plt.show()

    # def plot_histogram(self, column, bins):
    #     """create hisogram for a given column"""
    #     d = self.df [column].value_counts().to_dict()
    #     # df = pd.DataFrame({"a": np.random.random_integers(0, high=100, size=100)})

    #     ranges = [0,10,20,30,40,50,60,70,80,90,100]
    #     df.groupby(pd.cut(df.a, ranges)).count()
    #     plt.hist(list(d.values()), range=[])
    #     # plt.xticks(range(len(d)), list(d.keys()))
    #     print(d)
    #     plt.title(column)
    #     plt.show()
    
    def draw_boxplot(self, column):
        """Draw boc plot for a given column"""
        d = self.df [column].value_counts().to_dict()
        plt.boxplot(list(d.keys()))
        # plt.xticks(range(len(d)), list(d.keys()))
        plt.title(column)
        plt.show()

    def k_mean(self):
        pass

def main():
    # Read/convert to df data using pd 
    cust_analyzer = MallCustAnalyzer("dataset/Mall_Customers.csv")
    df = cust_analyzer.df
    print(df)
    
    head = df.head()
    print("Head of cust_data:\n", head)
    print()
    
    summary = df.describe()
    print("Summary of cust_data:\n",summary)
    # print(summary['Spending Score (1-100)'].mean())
    # cust_analyzer.plot_bar_graph("Genre")
    # cust_analyzer.plot_pie_chart("Genre")
    # cust_analyzer.plot_histogram("Age")
    cust_analyzer.draw_boxplot("Age")
    
if __name__ == "__main__":  
    main()
