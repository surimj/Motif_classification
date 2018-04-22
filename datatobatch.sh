
for dtype in 'train' 'valid' 'test'
do
	#paste -d' ' < example/$dtype.data - - > tmp.tsv
	python embedH5.py dcdata/$dtype.fa dcdata/$dtype.target dcexp/$dtype.h5
done