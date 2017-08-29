from lsa_encoder import LSAEncoder
from SDRClassifierRegion import SDRClassifierRegion
from nupic.research.spatial_pooler import SpatialPooler
import numpy
import csv
from sdr_classifier import SDRClassifier
#from CLAClassifier import CLAClassifier

column_dimensions = 20000
number_of_active_columns = 100 
lsa_e = LSAEncoder()
#lsa_e = CLAClassifier()
sp = SpatialPooler(inputDimensions=(5000,), columnDimensions=(column_dimensions,), potentialRadius=5000, numActiveColumnsPerInhArea=number_of_active_columns, globalInhibition=True, synPermActiveInc=0.01, synPermInactiveDec=0.008, potentialPct=0.5, synPermConnected=0.1, stimulusThreshold=0, minPctOverlapDutyCycle=0.01, spVerbosity = 3, seed=1)
c = SDRClassifier(steps=(0,), alpha = 0.01, verbosity = 3, actValueAlpha=0.0001)
#c = CLAClassifier(steps=(0,), alpha = 0.01, verbosity = 3, actValueAlpha=0.0001)
row_count = 1
#cat_list = [1, 1, 2, 2, 3, 3, 3, 4, 4]
#cat_list = ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '4', '4', '4', '4', '4', '4', '4', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '6', '6', '6', '6', '6', '6', '6', '6', '6', '7', '7', '7', '7', '7', '7', '7', '7', '7', '7', '7', '7', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '9', '9', '9', '10', '10', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '12', '12', '12', '12', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '14', '14', '15', '15', '15', '16', '17', '17', '17']

#cat_list = ['1', '1', '1', '1', '1', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '11', '11', '11', '11', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '13', '13', '14', '14', '14', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '16', '16', '16', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '2', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '4', '4', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '7', '7', '7', '7', '7', '7', '7', '7', '7', '8', '8', '8', '8', '8', '8', '8', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9']

#cat_list = ['1', '1', '1', '1', '1', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '11', '11', '11', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '13', '13', '14', '14', '14', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '15', '16', '16', '16', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '17', '2', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '4', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '6', '7', '7', '7', '7', '7', '7', '7', '7', '7', '8', '8', '8', '8', '8', '8', '8', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9']

for m in range(30):
#	with open('dataset_to_train.csv') as csvfile:
#	with open('training_data_yash_proper.csv') as csvfile:
#	with open('5_6_8_train.csv') as csvfile:
#	with open('3_4_9_11_17_train_proper.csv') as csvfile:
#	with open('20_news_group_to_train.csv') as csvfile:
#	with open('dataset_after_spliting.csv') as csvfile:
#	with open('test_data_refined_2_proper.csv') as csvfile:
#	with open('train_proper.csv') as csvfile:
	with open('train_set_sorted_movie.csv') as csvfile:
		complete_file = csv.reader(csvfile)
		for row in complete_file:
			#print row[1]
			#print "---------------------------"
			abc = lsa_e.encode(row[1])
			#output = lsa_e.encode(row[1])
			output = numpy.zeros((column_dimensions,), dtype="int")
			sp.compute(abc.astype(int), learn=True, activeArray=output)
			#print output
			#print abc.astype(int)

			j = 0
			indices = [0] * number_of_active_columns

			for i in range(len(output)):
				if output[i] == 1:
					indices[j] = i
					j += 1
			#classification code
			#print indices
			result = c.compute(recordNum=row_count, patternNZ=indices, classification={"bucketIdx": int(row[0]), "actValue": None}, learn=True, infer=True)
			row_count += 1
	csvfile.close()

'''

row[0] = ['about the bible quiz answers in article healta saturn wwc edu healta saturn wwc edu tammy r healy writes the cheribums are on the ark of the covenant when god said make no graven image he was refering to idols which were created to be worshipped the ark of the covenant wasn t wrodhipped and only the high priest could enter the holy of holies where it was kept once a year on the day of atonement i am not familiar with or knowledgeable about the original language but i believe there is a word for idol and that the translator would have used the word idol instead of graven image had the original said idol so i think you re wrong here but then again i could be too i just suggesting a way to determine whether the interpretation you offer is correct dean kaflowitz']

abc = lsa_e.encode(row[0])

output = numpy.zeros((400,), dtype="int")
sp.compute(abc.astype(int), learn=False, activeArray=output)
j = 0
indices = [0] * 10

for i in range(len(output)):
	if output[i] == 1:
        	indices[j] = i
                j += 1
                #classification code
result = c.compute(recordNum=1, patternNZ=indices, classification=None, learn=False, infer=True)
print result
'''

row_count = 1
#with open('dataset_to_test.csv') as csvfile:
#with open('test_data_yash_proper.csv') as csvfile:
#with open('5_6_8_test.csv') as csvfile:
#with open('3_4_9_11_17_test_proper.csv') as csvfile:
#with open('20_news_group_to_test.csv') as csvfile:
#with open('dataset_after_spliting.csv') as csvfile:
#with open('test_data_refined_2_proper.csv') as csvfile:
#with open('test.csv') as csvfile:
#with open('train_sorted.csv') as csvfile:
with open('test_set_movie.csv') as csvfile:
        complete_file = csv.reader(csvfile)
	cnt = 0
        for row in complete_file:
                #print row[1]
                #print "---------------------------"
                abc = lsa_e.encode(row[1])
                #output = lsa_e.encode(row[1])
                output = numpy.zeros((column_dimensions,), dtype="int")
                sp.compute(abc.astype(int), learn=False, activeArray=output)
                #print output
                #print abc.astype(int)

                j = 0
                indices = [0] * number_of_active_columns

                for i in range(len(output)):
                        if output[i] == 1:
                                indices[j] = i
                                j += 1
                #classification code
                #print indices
                result = c.compute(recordNum = row_count, patternNZ=indices, classification=None, learn=False, infer=True)
		#print "stepssss : ", len(result[1])	
		print "result is : ", result
		max_value = result[0][1]
		#print "max_value : ", max_value
		max_index = 1
               	for a in range(2, len(result[0])):
			 if max_value < result[0][a]:
				max_value = result[0][a]
				max_index = a
		#print "max_index if not same : ", cat_list[int(max_index) - 1], " ", int(row[0])
		print "max_index if not same : ", max_index, " ", int(row[0])
		#if cat_list[max_index] != cat_list[int(row[0])]:
		#if int(cat_list[int(max_index) - 1]) != int(row[0]): for train_proper and train_sorted
		if max_index != int(row[0]): # for dataset_to_train dataset_to_test
			cnt += 1
			print "learning : "
			#result = c.compute(recordNum=row_count, patternNZ=indices, classification={"bucketIdx": int(row[0]), "actValue": None}, learn=True, infer=True)
		row_count += 1
		print row_count
		print "accuracy : ", ((row_count - float(cnt) - 1) / (row_count - 1)) * 100
