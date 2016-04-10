#!/bin/bash

# Basic thing
curl localhost:5000

# File test
curl 	-o test1.jpg \
	-F hat_type=red \
	-F image=@img/bern1.jpg \
	localhost:5000/api/
