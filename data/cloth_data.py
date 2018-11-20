with open('train_cloth.txt','w') as f:
    for i in range(2000):
        f.write('../cloth/clothes/train/images/' + str(i) + '.jpg\n')
