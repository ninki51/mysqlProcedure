rom numpy import exp,array,random,dot
import math

PI = 3.14159
inputs = array([[0.1],[0.2],[0.3],[0.4],[0.5],[0.6],[0.7],[0.8]])
outputs = array([[math.sin(0.1),math.sin(0.2),math.sin(0.3),math.sin(0.4),math.sin(0.5),math.sin(0.6),math.sin(0.7),math.sin(0.8)]]).T
random.seed(1)
weights = 2 * random.random((1,1)) -1
for i in range(10000):
    output = 1 / (1 + exp(-(dot(inputs,weights))))
    weights += dot(inputs.T,(outputs - output) * output * (1 - output))
print(1/(1+exp(-(dot(array([math.sin(1.0)]),weights)))))