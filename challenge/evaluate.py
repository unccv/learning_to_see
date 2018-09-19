## ------------------------- ##
##
## evaluate.py
## Basic student evaluation code.
## 
##
## ------------------------- ##

import numpy as np
import pickle
import time

def evaluate(student_file = 'sample_student', data_file = 'data/training_data.p'):
  '''
  Evaluate performance on finger-counting challenge.
  '''

  #import student method:
  # from sample_student import count_fingers
  count_fingers = getattr(__import__(student_file, 'count_fingers'), 'count_fingers')


  with open(data_file, 'rb') as f:
    d = pickle.load(f)
  
  confusion_matrix = np.zeros((3,3), dtype = 'int')

  for i in range(len(d)):
      cropped_image = d[i]['image'][d[i]['boxEdges'][2]:d[i]['boxEdges'][3], \
                                     d[i]['boxEdges'][0]:d[i]['boxEdges'][1]] 
      label = count_fingers(cropped_image)
      
      confusion_matrix[d[i]['numFingers']-1, label-1] += 1
      
  accuracy = np.sum(np.diag(confusion_matrix))/np.sum(confusion_matrix)


  #print out performance numbers:

  print('                  Correct Labels  ')
  print('                  1      2      3')
  print('                 -----------------')
  print('Predicted     1 | ' + str(confusion_matrix[0, 0]) + '      ' + 
                         str(confusion_matrix[0, 1]) + '      ' + 
                         str(confusion_matrix[0, 2]) + '      ')

  print('Labels        2 | ' + str(confusion_matrix[1, 0]) + '      ' + 
                         str(confusion_matrix[1, 1]) + '      ' + 
                         str(confusion_matrix[1, 2]) + '      ')

  print('              3 | ' + str(confusion_matrix[2, 0]) + '      ' + 
                         str(confusion_matrix[2, 1]) + '      ' + 
                         str(confusion_matrix[2, 2]) + '      ')

  print('\n')
  print('Accuracy = ' + str(round(accuracy, 3)))

  return accuracy, confusion_matrix


def calculate_score(accuracy):
    score = 0
    if accuracy >= 0.8:
       score = 10
    elif accuracy >= 0.7:
       score = 9
    elif accuracy >= 0.6:
       score = 8
    elif accuracy >= 0.5:
       score = 7
    elif accuracy >= 0.4:
       score = 6
    elif accuracy >= 0.35:
       score = 5
    elif accuracy >= 0:
       score = 4
    return score


if __name__ == '__main__':
    program_start = time.time()
    accuracy, _ = evaluate()
    score = calculate_score(accuracy)
    program_end = time.time()
    total_time = round(program_end - program_start,2)
    
    print("Execution time (seconds) = ", total_time)
    print("Score = ", score)
    print()