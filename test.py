import numpy as np

from predict import make_prediction
import config

def test_2d_cnn_prediction():
	# Given 
	test_data = np.load(open(config.DATA_DIR + config.TEST_DATA_2D, 'rb'))
	y_test = np.load(open(config.DATA_DIR + config.Y_TEST, 'rb'))

	# When 
	y_pred = make_prediction(config.MODEL_DIR + config.MODEL_2D, test_data)

	# Then
	assert len(y_pred) == len(y_test)
	assert len(y_pred) == len(test_data)


def test_sequence_prediction():
	# Given
	test_data = np.load(open(config.DATA_DIR + config.TEST_DATA_1D, 'rb'))
	test_data = test_data.reshape(test_data.shape[0], test_data.shape[2], test_data.shape[1])
	y_test = np.load(open(config.DATA_DIR + config.Y_TEST, 'rb'))

	# When 
	y_pred = make_prediction(config.MODEL_DIR + config.MODEL_1D, test_data)

	# Then
	assert len(y_pred) == len(y_test)
	assert len(y_pred) == len(test_data)


