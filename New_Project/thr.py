def three():
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd
    import seaborn as sns
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error,r2_score

    data = pd.read_csv("C:\\Users\\Mark\\Desktop\\Coaching\\flaskpro\\New\\Work\\wage.csv")
    data = data.drop('Unnamed: 0',1)

    data.columns

    y = data['wage']
    x = data.drop(y.name,1)

    sns.pairplot(x)
    plt.show()

    for i in x.columns:
        sns.scatterplot(x[i],y)
        plt.ylabel('wage')
        plt.show()

    X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.3)

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test,y_pred)
    r2 = r2_score(y_test,y_pred)
    return r2,model

