import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn import preprocessing
import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv("key_stats.csv")
data = data[:300]
features = ['DE Ratio',
             'Trailing P/E',
             'Price/Sales',
             'Price/Book',
             'Profit Margin',
             'Operating Margin',
             'Return on Assets',
             'Return on Equity',
             'Revenue Per Share',
             'Market Cap',
             'Enterprise Value',
             'Forward P/E',
             'PEG Ratio',
             'Enterprise Value/Revenue',
             'Enterprise Value/EBITDA',
             'Revenue',
             'Gross Profit',
             'EBITDA',
             'Net Income Avl to Common ',
             'Diluted EPS',
             'Earnings Growth',
             'Revenue Growth',
             'Total Cash',
             'Total Cash Per Share',
             'Total Debt',
             'Current Ratio',
             'Book Value Per Share',
             'Cash Flow',
             'Beta',
             'Held by Insiders',
             'Held by Institutions',
             'Shares Short (as of',
             'Short Ratio',
             'Short % of Float',
             'Shares Short (prior ']

X = np.array(data[features].values)

y = (data["Status"]
         .replace("underperform",0)
         .replace("outperform",1)
         .values.tolist())

X = preprocessing.scale(X)

model = SVC(kernel="linear", C=1.0)

x_train,x_test,y_train,y_test = train_test_split(X, y, test_size=0.1, random_state=4)

model.fit(x_train, y_train)
print(model.score(x_test,y_test))
