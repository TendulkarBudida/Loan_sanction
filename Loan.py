import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

m = LogisticRegression()

class LoanInfo:
    def __init__(self) -> None:
        self.loan_id = None
        self.gender
        self.is_married
        self.dependents
        self.education
        self.is_self_employed
        self.applicant_income
        self.co_applicant_income
        self.loan_amount
        self.loan_amount_term
        self.credit_history
        self.property_area
        self.is_loan_status

def readXlsx():
    df = pd.read_excel('loan-predictionUC.xlsx')

    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    #print(X)
    #print(y)

    #print(df.info())#isna().sum())

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    m.fit(X_train, y_train)
    pred = m.predict(X_test)
    print(pred)

    print(m.score(X_test, y_test))
    print(m.score(X_train, y_train))

    #print(file[:10])


readXlsx()