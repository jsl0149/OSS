#PLEASE WRITE THE GITHUB URL BELOW!
#https://github.com/jsl0149/OSS
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

def load_dataset(dataset_path):
	#To-Do: Implement this function
	df1 = pd.read_csv(dataset_path);
	return df1

def dataset_stat(dataset_df):	
	#To-Do: Implement this function
	n_feat = dataset_df.shape[1]

	data0 = dataset_df['target'] == 0
	data1 = dataset_df['target'] == 1
	zeroCount = dataset_df[data0].shape[0]
	oneCount = dataset_df[data1].shape[0]

	return n_feat, zeroCount, oneCount

def split_dataset(dataset_df, testset_size):
	#To-Do: Implement this function
	return train_test_split(dataset_df, dataset_df.target, test_size=testset_size)
def decision_tree_train_test(x_train, x_test, y_train, y_test):
	#To-Do: Implement this function
	dt_cls = DecisionTreeClassifier()
	dt_cls.fit(x_train, y_train)
	y_pred = dt_cls.predict(x_train)
	acc_score = accuracy_score(y_test, dt_cls.predict(x_test))
	pre_score = precision_score(y_train, y_pred)
	rec_score = recall_score(y_train, y_pred)
	return acc_score, pre_score, rec_score

	
def random_forest_train_test(x_train, x_test, y_train, y_test):
	#To-Do: Implement this function
	rf_cls = RandomForestClassifier()
	rf_cls.fit(x_train, y_train)
	y_pred = rf_cls.predict(x_train)
	acc_score = accuracy_score(rf_cls.predict(x_test),y_test)
	pre_score = precision_score(y_train, y_pred)
	rec_score = recall_score(y_train, y_pred)
	return acc_score, pre_score, rec_score

def svm_train_test(x_train, x_test, y_train, y_test):
	#To-Do: Implement this function
	svm_cls = SVC()
	svm_cls.fit(x_train, y_train)
	y_pred = svm_cls.predict(x_train)
	acc_score = accuracy_score(y_test, svm_cls.predict(x_test))
	pre_score = precision_score(y_train, y_pred)
	rec_score = recall_score(y_train, y_pred)
	return acc_score, pre_score, rec_score

def print_performances(acc, prec, recall):
	#Do not modify this function!
	print ("Accuracy: ", acc)
	print ("Precision: ", prec)
	print ("Recall: ", recall)

if __name__ == '__main__':
	#Do not modify the main script!
	data_path = sys.argv[1]
	data_df = load_dataset(data_path)

	n_feats, n_class0, n_class1 = dataset_stat(data_df)
	print ("Number of features: ", n_feats)
	print ("Number of class 0 data entries: ", n_class0)
	print ("Number of class 1 data entries: ", n_class1)

	print ("\nSplitting the dataset with the test size of ", float(sys.argv[2]))
	x_train, x_test, y_train, y_test = split_dataset(data_df, float(sys.argv[2]))

	acc, prec, recall = decision_tree_train_test(x_train, x_test, y_train, y_test)
	print ("\nDecision Tree Performances")
	print_performances(acc, prec, recall)

	acc, prec, recall = random_forest_train_test(x_train, x_test, y_train, y_test)
	print ("\nRandom Forest Performances")
	print_performances(acc, prec, recall)

	acc, prec, recall = svm_train_test(x_train, x_test, y_train, y_test)
	print ("\nSVM Performances")
	print_performances(acc, prec, recall)