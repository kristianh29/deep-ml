import numpy as np
from numpy.linalg import norm

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	if v1.shape == v2.shape:
		return (np.dot(v1,v2))/(norm(v1)*norm(v2))
	else:
		raise ValueError("Shape of the vectors is not the same.")