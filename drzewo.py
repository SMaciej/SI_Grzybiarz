"""		instances - zbior danych do nauki
		candidate_attribute_indexes - ['poisonous','color','shape','stipe']
		target_attribute_index - 'decision'
		choose_best_majority_value - liczy czy czesciej jest decY albo decN
		choose_best_attribute_index(instances,candidate_attribute_indexes,target_attribute_index):
			1. Policz DecY i DecN
			2. Licz information gain:
			
"""	
from collections import defaultdict
from collections import Counter		
import math
from math import log

def values(instance):
	vals=[]
	#print(instance.keys())
	for i in instance.keys():
		#print(i)
		#print(instance[i])
		vals.append(i)
		vals.append(instance[i])
	return vals


def sprawdz(dict,instance,candidates):
		#for instance in instances:
        #print('Zaczalem sie')
        for cand in candidates:
            #print(dict.keys())
            if cand in dict.keys():
               # print(dict[cand])
                if(dict[cand]=='y'):
                    return True
                elif(dict[cand]=='n'):
                    return False
                else:
                #    print(dict[cand])
                    return sprawdz(dict[cand],instance,candidates)
	
def entropy(data,target_attr):
 
	val_freqY = 0
	val_freqN = 0
	data_entropy = 0.0
 
	# Calculate the frequency of each of the values in the target attr
	for i in range(len(data)):
		if (data[i][target_attr]=='y'):
			val_freqY += 1.0
		else:
			val_freqN += 1.0
 
	# Calculate the entropy of the data for the target attribute
	#print(val_freqY)
	#print(len(data))
	if(val_freqY==0):
		data_entropy = (-val_freqN/len(data)) * math.log(val_freqN/len(data), 2)
	elif(val_freqN==0):
		data_entropy = (-val_freqY/len(data)) * math.log(val_freqY/len(data), 2)
	else:
		data_entropy = ((-val_freqY/len(data)) * math.log(val_freqY/len(data), 2))+((-val_freqN/len(data)) * math.log(val_freqN/len(data), 2))
	#print(data_entropy)
	return data_entropy

	#InformationGain	      -    liczy dla konkretnego attr
				
def gain(data, attr, target_attr):
 
	val_freq = {}
	subset_entropy = 0.0
	count = 0 

	# Calculate the frequency of each of the values in the target attribute
	for i in range(len(data)):
		#if (data[i][target_attr]=='y'):
			#print(attr)
			#print(val_freq[data[i][attr]])
		if data[i][attr] not in val_freq:
			#print(data[i][attr])
			val_freq[data[i][attr]] = 1.0
		else:
			val_freq[data[i][attr]] += 1.0			#Nie liczę dla tych co nie-
			
	#print(val_freq['y'])
	# Calculate the sum of the entropy for each subset of records weighted by their probability of occuring in the training set.
	for val in val_freq.keys():
		#print(val_freq.keys())
		val_prob = val_freq[val] / sum(val_freq.values())
		#print(val)
		#print(val_prob)
		#print(sum(val_freq.values()))
		#print(val_freq[val])
		#print(sum(val_freq.values()))
		data_subset = [record for record in data if record[attr] == val]
		#print(data_subset)
		#print(entropy(data_subset,target_attr))
		
		subset_entropy += val_prob * entropy(data_subset,target_attr)
 
	# Subtract the entropy of the chosen attribute from the entropy of the whole data set with respect to the target attribute (and return it)
	return (entropy(data,target_attr) - subset_entropy)
	
		# bedziemy chcieli splitowac drzewo


def split_instances(instances, attribute_index):

	partitions = defaultdict(list)
	for instance in instances:
		#print(instances[i][attribute_index])
		#print(partitions.keys())
		#print(instance[attribute_index])
		#if instance[attribute_index] not in partitions.keys():
		#	partitions.keys().append(instance[attribute_index])
		partitions[instance[attribute_index]].append(instance)
	return partitions
			
			
def majority_value(instances,target_attribute_index):
	DecY=0
	DecN=0
	for i in range(len(instances)):
		if (instances[i]['decision']=='y'):
			DecY+=1
		else:
			DecN+=1
	if(DecY>DecN):
		return 'y'
	else:
		return 'n'

def choose_best_attribute_index(instances,candidate_attribute_indexes,target_attribute_index):
	DecY=0
	DecN=0
	MaxGain=0
	currgain=0
	Attr=''
	for i in range(len(instances)):
		if (instances[i]['decision']=='y'):
			DecY+=1
		else:
			DecN+=1
	for j in candidate_attribute_indexes:
		for i in range(len(instances)):
			currgain = gain(instances,j,'decision')
			if(currgain>MaxGain):
				MaxGain=currgain
				Attr=j
	#print(MaxGain)
	#print(j)
	return j
	
def classify(tree, instance, default_class=None):
    '''Returns a classification label for instance, given a decision tree'''
    if not tree:  # if the node is empty, return the default class
        return default_class
    if not isinstance(tree, dict):  # if the node is a leaf, return its class label
        return tree
    attribute_index = list(tree.keys())[0]  # using list(dict.keys()) for Python 3 compatibility
    attribute_values = list(tree.values())[0]
    instance_attribute_value = instance[attribute_index]
    if instance_attribute_value not in attribute_values:  # this value was not in training data
        return default_class
    # recursively traverse the subtree (branch) associated with instance_attribute_value
    return classify(attribute_values[instance_attribute_value], instance, default_class)

	
class GrzybiarzDecisionTree:

    _tree = {}  # this instance variable becomes accessible to class methods via self._tree

    def __init__(self):
        # this is where we would initialize any parameters to the GrzybiarzDecisionTree
        pass
            
    def fit(self, 
            instances, 
            candidate_attribute_indexes=None,
            target_attribute_index=0,
            default_class=None):
        if not candidate_attribute_indexes:
            candidate_attribute_indexes = [i 
                                           for i in range(len(instances[0]))
                                           if i != target_attribute_index]
        self._tree = self._create_tree(instances,
                                       candidate_attribute_indexes,
                                       target_attribute_index,
                                       default_class)
 
    def _create_tree(self,
                     instances,
                     candidate_attribute_indexes,
                     target_attribute_index=0,
                     default_class=None):
        class_labels_and_counts = Counter([instance[target_attribute_index] 
                                          for instance in instances])
        if not instances or not candidate_attribute_indexes:
            return default_class
        elif len(class_labels_and_counts) == 1:
            class_label = class_labels_and_counts.most_common(1)[0][0]
            return class_label
        else:
            default_class = majority_value(instances, target_attribute_index)
            best_index = choose_best_attribute_index(instances,candidate_attribute_indexes,target_attribute_index)
            tree = {best_index:{}}
            partitions = split_instances(instances, best_index)
            remaining_candidate_attribute_indexes = [i 
                                                     for i in candidate_attribute_indexes 
                                                     if i != best_index]
            for attribute_value in partitions:
                subtree = self._create_tree(
                    partitions[attribute_value],
                    remaining_candidate_attribute_indexes,
                    target_attribute_index,
                    default_class)
                tree[best_index][attribute_value] = subtree
            return tree

    def pprint(self):
        print('drukowanie drzewa:')
        print(self._tree)
		
    def decide(self,instance,candidates):
		#for instance in instances:
        for cand in candidates:
            if cand in self._tree.keys():
             #   print(instance.keys())
                #print(self._tree[cand])
                if(self._tree[cand]=='y'):
                    return 'True'
                elif(self._tree[cand]=='n'):
                    return 'False'
                else:
                    return sprawdz(self._tree[cand],instance,values(instance))
                    #for i in self._tree.keys():
                    #    print(self._tree[i].keys())
           # if cand in instance.keys():
            #    print(self._tree[instance[cand]])
				

instances = []

instances.append({'poison': 'n', 'shape': 'cap', 'color': 'brown', 'stipe': 'plain', 'taste': 9})
instances.append({'poison': 'n', 'shape': 'cap', 'color': 'yellow', 'stipe': 'rugged', 'taste': 9})
instances.append({'poison': 'n', 'shape': 'cap', 'color': 'red', 'stipe': 'plain', 'taste': 38})
instances.append({'poison': 'n', 'shape': 'cone', 'color': 'brown', 'stipe': 'plain', 'taste': 49})
instances.append({'poison': 'n', 'shape': 'cap', 'color': 'brown', 'stipe': 'plain', 'taste': 5})
instances.append({'poison': 'y', 'shape': 'cap', 'color': 'red', 'stipe': 'dotted', 'taste': 11})
instances.append({'poison': 'y', 'shape': 'cap', 'color': 'yellow', 'stipe': 'plain', 'taste': 0})
instances.append({'poison': 'y', 'shape': 'cap', 'color': 'yellow', 'stipe': 'plain', 'taste': 0})
instances.append({'poison': 'y', 'shape': 'cap', 'color': 'red', 'stipe': 'dotted', 'taste': 19})
instances.append({'poison': 'y', 'shape': 'cap', 'color': 'yellow', 'stipe': 'plain', 'taste': 0})
instances.append({'poison': 'y', 'shape': 'cap', 'color': 'red', 'stipe': 'dotted', 'taste': 17})
instances.append({'poison': 'y', 'shape': 'cap', 'color': 'yellow', 'stipe': 'plain', 'taste': 0})
instances.append({'poison': 'n', 'shape': 'cap', 'color': 'brown', 'stipe': 'plain', 'taste': 8})
instances.append({'poison': 'n', 'shape': 'cap', 'color': 'brown', 'stipe': 'plain', 'taste': 7})
instances.append({'poison': 'y', 'shape': 'cap', 'color': 'yellow', 'stipe': 'plain', 'taste': 0})
instances.append({'poison': 'y', 'shape': 'cap', 'color': 'yellow', 'stipe': 'plain', 'taste': 0})
instances.append({'poison': 'n', 'shape': 'cone', 'color': 'brown', 'stipe': 'plain', 'taste': 48})
instances.append({'poison': 'y', 'shape': 'cap', 'color': 'red', 'stipe': 'dotted', 'taste': 11})
instances.append({'poison': 'y', 'shape': 'cap', 'color': 'yellow', 'stipe': 'plain', 'taste': 0})
instances.append({'poison': 'y', 'shape': 'cap', 'color': 'red', 'stipe': 'dotted', 'taste': 20})
instances.append({'poison': 'n', 'shape': 'cap', 'color': 'white', 'stipe': 'dotted', 'taste': 20})
instances.append({'poison': 'n', 'shape': 'cone', 'color': 'yellow', 'stipe': 'rugged', 'taste': 12})
instances.append({'poison': 'n', 'shape': 'cap', 'color': 'brown', 'stipe': 'plain', 'taste': 6})
instances.append({'poison': 'y', 'shape': 'cap', 'color': 'yellow', 'stipe': 'plain', 'taste': 0})
instances.append({'poison': 'y', 'shape': 'cap', 'color': 'yellow', 'stipe': 'plain', 'taste': 0})
instances.append({'poison': 'n', 'shape': 'cap', 'color': 'brown', 'stipe': 'plain', 'taste': 3})
instances.append({'poison': 'n', 'shape': 'cone', 'color': 'brown', 'stipe': 'plain', 'taste': 49})
instances.append({'poison': 'n', 'shape': 'cap', 'color': 'brown', 'stipe': 'plain', 'taste': 8})
instances.append({'poison': 'y', 'shape': 'cap', 'color': 'yellow', 'stipe': 'plain', 'taste': 0})
instances.append({'poison': 'n', 'shape': 'cap', 'color': 'brown', 'stipe': 'plain', 'taste': 1})
instances.append({'poison': 'n', 'shape': 'cone', 'color': 'brown', 'stipe': 'plain', 'taste': 52})
instances.append({'poison': 'y', 'shape': 'cap', 'color': 'yellow', 'stipe': 'plain', 'taste': 0})
instances.append({'poison': 'y', 'shape': 'cap', 'color': 'yellow', 'stipe': 'plain', 'taste': 0})
instances.append({'poison': 'n', 'shape': 'cone', 'color': 'brown', 'stipe': 'plain', 'taste': 49})
instances.append({'poison': 'y', 'shape': 'cap', 'color': 'red', 'stipe': 'dotted', 'taste': 17})
instances.append({'poison': 'y', 'shape': 'cap', 'color': 'yellow', 'stipe': 'plain', 'taste': 0})
instances.append({'poison': 'y', 'shape': 'cap', 'color': 'red', 'stipe': 'dotted', 'taste': 12})
instances.append({'poison': 'n', 'shape': 'cone', 'color': 'brown', 'stipe': 'plain', 'taste': 53})
instances.append({'poison': 'y', 'shape': 'cap', 'color': 'yellow', 'stipe': 'plain', 'taste': 0})
instances.append({'poison': 'y', 'shape': 'cap', 'color': 'yellow', 'stipe': 'plain', 'taste': 0})
instances.append({'poison': 'n', 'shape': 'cap', 'color': 'brown', 'stipe': 'plain', 'taste': 5})
instances.append({'poison': 'n', 'shape': 'cone', 'color': 'brown', 'stipe': 'plain', 'taste': 45})
instances.append({'poison': 'y', 'shape': 'cap', 'color': 'red', 'stipe': 'dotted', 'taste': 13})
instances.append({'poison': 'y', 'shape': 'cap', 'color': 'yellow', 'stipe': 'plain', 'taste': 0})
#print(instances)
'''
def decide(instance,candidates,tree):
	for cecha in candidates:
		if ((instance['cecha']=='y') or (instance['cecha']=='n')):
			return instance['cecha']
		else:
	'''		

#values = ['y','n','cap','cone','plain','rugged','dotted','yellow','red','brown','white','poison','shape','stipe','color']
candidates = ['poison','shape','stipe','color']
#print(candidates)
target = 'decision'
#print(target)
def konwertuj(instances):
	print(instances)
	dane_uczace = []
	for i in range(len(instances)):
		poison = instances[i]['poison']
		shape = instances[i]['shape']
		color = instances[i]['color']
		stipe = instances[i]['stipe']
		if ((instances[i]['taste']<10) or instances[i]['poison']=='y'):
			decision = 'n'
		else:
			decision='y'
		dane_uczace.append({'poison': poison, 'shape':shape,'color':color,'stipe':stipe,'decision':decision})
	return dane_uczace

#print(dane_uczace)
		
#drzewo_grzybiarza = GrzybiarzDecisionTree()
#drzewo_grzybiarza.fit(dane_uczace,candidates,target)
#drzewo_grzybiarza._create_tree(dane_uczace,candidates,target)
#drzewo_grzybiarza.pprint()
#vals=values({'poison': 'n', 'shape': 'cone', 'color': 'brown', 'stipe': 'plain', 'taste': 53})
#print(vals)
#for i in dane_uczace:
#	print(drzewo_grzybiarza.decide(i,candidates))

#print()
#entropy(dane_uczace,'decision')
#for j in candidates:
#	print(gain(dane_uczace,j,target))
#print(drzewo_grzybiarza._tree['color']['white'])
#print(drzewo_grzybiarza['color'])
#for i in range(len(dane_uczace)):
#	print(classify(drzewo_grzybiarza,dane_uczace[i]))
'''			
predicted_labels = drzewo_grzybiarza.predict(dane_uczace)
print(dane_uczace[0])
actual_labels = [instance[0] for instance in dane_uczace]
for predicted_label, actual_label in zip(predicted_labels, actual_labels):
    print('Model: {}; truth: {}'.format(predicted_label, actual_label))
print()
print('Classification accuracy:', drzewo_grzybiarza.classification_accuracy(test_instances))
'''