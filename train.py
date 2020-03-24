import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('data/creditcard-sample10k.csv')

features_train = df.sample(frac=0.75, random_state=100)
features_test = df[~df.index.isin(features_train.index)]

drop_time_class = ['Time','Class','V1','V2','V5','V6','V7','V8','V9','V13','V15','V16','V18','V19','V20','V21','V22','V23','V24','V25','V26','V27','V28']
drop_class=['Class']

features_train = features_train.loc[:, ~features_train.columns.str.contains('^Unnamed')]
features_test = features_test.loc[:, ~features_test.columns.str.contains('^Unnamed')]
target_train = features_train['Class']
target_test = features_test['Class']
features_train = features_train.drop(drop_time_class, axis=1)
features_test = features_test.drop(drop_time_class, axis=1)

model = RandomForestClassifier(n_estimators=200, max_depth=6, n_jobs=10, class_weight='balanced')
                               
model.fit(features_train, target_train.values.ravel())

pred_train = model.predict(features_train)
pred_test = model.predict(features_test)

pred_train_prob = model.predict_proba(features_train)
pred_test_prob = model.predict_proba(features_test)

print("Number of features")
print(len(model.feature_importances_))
  
#save mode in filesystem
joblib.dump(model, 'model.pkl') 