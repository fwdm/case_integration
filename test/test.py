import numpy as np



from cases.case9 import case9 as Case




case = Case()




#demand of nodes
D_i = case['bus'][:,2]

#maximal generator capacities.
G_max = case['gen'][:,8]

#generator costs
k_alpha = case['gencost'][:,4]

# contains the node number, the generators are connected to. First entry in array corresponds to first generator and so on. Start to COUNT FROM ONE!
G_connections = case['gen'][:,0]

#line susceptances
B_l = case['branch'][:,3]
B_l = 1 / B_l

#transmission maxima for lines
F_max = case['branch'][:,5]

#the transmission lines go in this array
Node_connections = case['branch'][:, 0:2].astype(int)

#Node_connections = Node_connections.astype(int)

print Node_connections
















































































































