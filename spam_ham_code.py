import numpy as np
import pickle
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
#load the dataset
df  = pd.read_csv('https://raw.githubusercontent.com/laxmimerit/All-CSV-ML-Data-Files-Download/master/spam.tsv', sep='\t')
#dataframe seperate ham and spam
ham = df[df['label']=='ham']
spam = df[df['label']=='spam']
ham = ham.sample(spam.shape[0])
data = pd.concat([ham, spam], axis=0, ignore_index=True)
#visualize the message length compare ham,spam length
plt.rcParams['figure.dpi'] = 200
plt.rcParams['figure.figsize'] = (10, 4)
plt.style.use('ggplot')
plt.hist(ham['length'], bins=100, alpha=0.7, label='HAM')
plt.hist(spam['length'], bins=100, alpha=0.7, label='SPAM')
plt.title('Message Length for HAM and SPAM')
plt.legend()
plt.show()
#graph for punctuation
plt.hist(ham['punct'], bins=100, alpha=0.7, label='HAM')
plt.hist(spam['punct'], bins=100, alpha=0.7, label='SPAM')
plt.title('Number of Punctuation in HAM and SPAM')
plt.legend()
plt.show()
#spliting data for training and testing
X_train, X_test, y_train, y_test = train_test_split(data['message'], data['label'],
                                                test_size=0.2, random_state=0,
                                                   shuffle=True, stratify=data['label'])
#term frequency inverse document frequency 
clf = Pipeline([('tfidf', TfidfVectorizer()), 
                ('rfc', RandomForestClassifier(n_estimators=100, n_jobs=-1))])#combine multiple decision trees to produce an accurate one

clf.fit(X_train, y_train)#training
y_pred = clf.predict(X_test)#predicting the result
print(classification_report(y_test, y_pred))#evaluating
pickle.dump(clf, open('model.pkl', 'wb'))#saving the model
model = pickle.load(open('model.pkl', 'rb'))
