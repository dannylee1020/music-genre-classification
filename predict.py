import numpy as np
from keras.models import load_model
from sklearn.metrics import classification_report
import inquirer

import config



def make_prediction(model,data):
	model = load_model(model)
	y_pred = model.predict(data)

	return y_pred



if __name__ == '__main__':

	questions = [
		inquirer.List('models',
					  message = 'What model do you want to use to use to make prediction?',
					  choices = ['2D CNN', '1D CNN - LSTM'],
					  ),
	]

	answers = inquirer.prompt(questions)
	answers = answers['models']


	if answers == '2D CNN':
		data = np.load(open(config.DATA_DIR + config.TEST_DATA_2D, 'rb'))

		y_pred = make_prediction(config.MODEL_DIR + config.MODEL_2D, data)
		y_pred = np.argmax(y_pred, axis = 1)

		y_test = np.load(open(config.DATA_DIR + config.Y_TEST, 'rb'))
		y_test = np.argmax(y_test, axis = 1)

		clr = classification_report(y_test, y_pred)

		print(clr)

	elif answers == '1D CNN - LSTM':
		data = np.load(open(config.DATA_DIR + config.TEST_DATA_1D, 'rb'))
		data = data.reshape(data.shape[0], data.shape[2], data.shape[1])

		y_pred = make_prediction(config.MODEL_DIR + config.MODEL_1D, data)
		y_pred = np.argmax(y_pred, axis = 1)

		y_test = np.load(open(config.DATA_DIR + config.Y_TEST, 'rb'))
		y_test = np.argmax(y_test, axis = 1)

		clr = classification_report(y_test, y_pred)

		print(clr)

	else:
		print('Wrong input. Please try again')




