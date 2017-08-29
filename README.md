# TextCatHTM
Text categorization using Hierarchical Temporal Memory (HTM)

Pre processing
Uses gensim to generate TFIDFs and subsequently WORDIDS. These are generated using the Wikipedia corpus by running make_wiki.py file. These TFIDFs and WORDIDs are used by LSA encoder. 
1. Create bag of words of each sentence.(stopwords and punctuations  are removed)
2. Generate weights of the words in the bag of words.(using tfidf)
3. Pass these weights to Singular Value Decomposition.
4. The indices of the top weights of the right singular matrix of the SVD are used to generate bit arrays.  

Training and testing the model 
Change the training and testing file names in train_test.py file. Populate the category names and ids in category_list.csv file.  The predictions will be received in result_output.csv file. 

Files details
Filename: a.py
Input: text corpus (similar to wiki corpus)
Output: mm corpus

Filename: category_list.py
Input: training_set.csv
Output: category_list with labels category_count with its counts refined_training_set.csv

Filename: split_final.py
Input: refined_trainig_set.csv
Output: splitted the training set into number of categories having equal records in it. Created train_set.csv.created test_set.csv

Filename: driver_function.py 
Input: test_set.csv, train_set.csv
Function: starts the categorization


Filename: lsa_encoder.py
Input: mm corpus from a.py word_ids.txt from a.py
Output: tfidf_model model
Returns: bit arrays

Filename: language_encoder.py
Function: parent of lsa_encoder.py

Filename: sdr_classifier.py
Input: active indices
Output: probability distribution

Filename: make_wiki.py
Input: wiki corpus 
Output: tfidf and wordIds for LSA
Execution Steps
Step1:
Create mm corpus using a.py file. Input is the corpus which is going to then be splitted into the train and the test set.
Step 2:
Run the category_list.py file. It takes the corpus which has to be splitted into the train and the test set.
This file gives three files as mentioned above.
Step 3:
The output files in the above step are then given to the split_final.py file. Removes the stop words and single character words. The code in split_final.py splits refined_corpus.csv into train_set.csv and test_set.csv with ratio 90 - 10 respectively. 
Step 4:
Run the driver_function.py. This file takes input from the output of the previous step. This file uses lsa_encoder.py file to convert text into bit arrays by creating bow and tfidf model. These bit arrays are then passed to the spatial_pooler.py in the nupic library to get converted into Sparse Distributed Representations (SDRs). These sdrs are then passed on to the sdr_classifier.py to get trained and classify into pre-defined categories.
