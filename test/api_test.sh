#!/bin/bash

# Basic thing
curl localhost:5000

# File test
curl -o test1.jpg -d "hat_id=1" --data-binary @"img/bern1.jpg" localhost:5000/api/
