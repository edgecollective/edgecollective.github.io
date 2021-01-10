#!/bin/bash

for file in $1/*  
basename "$file"
do convert $file +dither -colors 5 -normalize "$2/${file%.*}_c.gif" 
done
