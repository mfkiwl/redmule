# Copyright (C) 2022-2023 ETH Zurich and University of Bologna
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Author: Yvan Tortorella (yvan.tortorella@unibo.it)
#

import torch 

def tensor_to_string(tensor):
	tensor_string = ''
	ndim = len(tensor.size())
	if ndim == 1:
		sz0 = tensor.size()[0]
		for i in range(sz0):
			tensor_string += str(tensor[i].item()) 
			tensor_string += 'f, ' if i < sz0-1 else 'f'

	elif ndim == 2:
		sz0 = tensor.size()[0]
		sz1 = tensor.size()[1]
		print('Sizes: ',sz0,sz1)
		for i in range(sz0):
			for j in range(sz1):
				tensor_string += str(tensor[i][j].item()) 
				tensor_string += 'f, ' if (i*sz1+j) < (sz0*sz1-1) else 'f'

	else:

		pass # FIXME to be implemented


	return tensor_string


    
def main():
	import argparse
	parser = argparse.ArgumentParser("FCN Layer Test")
	parser.add_argument( '--in_size', type=int, default=2,
	    help="An integer will be increased by 1 and printed." )
	parser.add_argument( '--out_size', type=int, default=2,
	    help="An integer will be increased by 1 and printed." )
	args = parser.parse_args()

	dim0_sz = args.in_size
	dim1_sz = args.out_size
	t = torch.rand(dim0_sz)
	print(t)
	print(tensor_to_string(t))

	t = torch.rand(dim1_sz, dim0_sz)
	print(t)
	print(tensor_to_string(t))


if __name__ == '__main__':
    main()
