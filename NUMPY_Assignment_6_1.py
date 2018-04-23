##Write a function so that the columns of the output matrix are powers of the input vector.

import numpy as np

inp_arr=np.array([2,4,1,5])  # 1 dimensional Input vector.
N=input('Please enter no. of columns in the output: ')	## Default is length(array)
increase_value=input('Please enter increasing value(True/False): ')	## Default is False). If True, the each element will be calculated like x^0,x^1...x^N-1
																	## If False, then 	each element will be calculated like x^N-1,x^N-2...x^0


##Approach -1 - Using vander method			
def column_mtrx_1(arr,N,increase_value):
	if len(N)==0 and increase_value=='False':
		output_matrix=np.vander(arr) ## N is default i.e len(arr) and increasing is also default as False
	elif len(N)==0 and increase_value=='True':
		output_matrix=np.vander(arr,increasing=True) ## N is default i.e len(arr) and increasing=True
	elif len(N)>0 and increase_value=='False':
		output_matrix=np.vander(arr,N=int(N)) ## N is user input and increasing is default as False
	elif len(N)>0 and increase_value=='True':
		output_matrix=np.vander(arr,N=int(N),increasing=True) ## N is a user input and increasing is also a user input
	
	print('---------------- Using vandor method ----------------')
	print('Input Vector is :\n',inp_arr ,'\n And New matrix is :\n',output_matrix)
	

##Approach -2 - Using column_stack
def column_mtrx_2(arr,N,increase_value):
	if len(N)==0 and increase_value=='False':
		N=len(inp_arr)
		output_matrix=np.column_stack([inp_arr**(N-i-1) for i in range(N)]) ## N is default i.e len(arr) and increasing is also default as False
	elif len(N)==0 and increase_value=='True':
		N=len(inp_arr)
		output_matrix=np.column_stack([inp_arr**(N-i-1) for i in range(N-1,-1,-1)]) ## N is default i.e len(arr) and increasing=True
	elif len(N)>0 and increase_value=='False':
		N=int(N)
		output_matrix=np.column_stack([inp_arr**(N-i-1) for i in range(N)]) ## N is user input and increasing is default as False
	elif len(N)>0 and increase_value=='True':
		N=int(N)
		output_matrix=np.column_stack([inp_arr**(N-i-1) for i in range(N-1,-1,-1)]) ## N is a user input and increasing is also a user input
	
	print('---------------- Using column_stack  ----------------')
	print('Input Vector is :\n',inp_arr ,'\n And New matrix is :\n',output_matrix)

	
def main():
	
	# Vandor function Call 
	column_mtrx_1(inp_arr,N,increase_value)
	
	# column_stack function call
	column_mtrx_2(inp_arr,N,increase_value)

# start of script
# +++++++++++++++++
if __name__ == '__main__':
	main()
