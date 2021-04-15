import numpy as np



with open('input.txt', 'w') as file:
    for i in range(200):
        permutation = np.random.permutation(200)
        listToStr = ' '.join([str(elem) for elem in permutation])
        file.writelines(listToStr+'\n')



        
