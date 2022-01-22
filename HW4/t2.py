from numpy import dot
from numpy.linalg import norm
a = [1,2,3,4,5,6,7,8,9,0,11,12,13,14,15,16,17,18,19]
b = [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
cos_sim = dot(a, b)/(norm(a)*norm(b))
print(cos_sim)

from numpy import dot
from numpy.linalg import norm
a = [1, 2]
b = [2.5, 4]
cos_sim = dot(a, b)/(norm(a)*norm(b))

import numpy as np
import matplotlib.pyplot as plt
# consider two vectors A and B in 2-D
A=np.array([1,2])
B=np.array([1,1])
ax = plt.axes()
ax.arrow(0.0, 0.0, A[0], A[1], head_width=0.4, head_length=0.5)
plt.annotate(f"A({A[0]},{A[1]})", xy=(A[0], A[1]),xytext=(A[0]+0.5, A[1]))
ax.arrow(0.0, 0.0, B[0], B[1], head_width=0.4, head_length=0.5)
plt.annotate(f"B({B[0]},{B[1]})", xy=(B[0], B[1]),xytext=(B[0]+0.5, B[1]))
plt.xlim(0,10)
plt.ylim(0,10)
plt.show()
plt.close()
# cosine similarity between A and B
cos_sim=np.dot(A,B)/(np.linalg.norm(A)*np.linalg.norm(B))
print (f"Cosine Similarity between A and B:{cos_sim}")
print (f"Cosine Distance between A and B:{1-cos_sim}")

a = [1, 2]
b = [2, 4]
c = [2.5, 4]
d = [4.5, 5]
from scipy import spatial
spatial.distance.cosine(c,a)

vector1 = [1, 2, 3]
vector2 = [3, 2, 1]

cosine_similarity = 1 - spatial.distance.cosine(vector1, vector2)
import sklearn
sklearn.metrics.pairwise.cosine_similarity(X, Y=None, dense_output=True)