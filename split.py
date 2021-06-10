import pickle
import re
import numpy as np
if __name__ == '__main__':
    # file = open('C:/Users/80670/Desktop/sentences.pkl', 'rb')
    # info = pickle.load(file)
    # list2 = [',', '.', 'is', 'are', 'on', 'with', 'in', 'at', 'before', 'after', 'about', 'above', 'across', 'up',
    #          'along', 'as','behind', 'to', 'for', 'about', 'beyond',
    #          'as', 'but', 'by', 'between', 'of', 'over', 'below', 'under', 'among',
    #          'into', 'down', 'through', 'like', 'from', 'within']
    # list1 = []
    # savez_dict = dict()
    # count = 0
    # for i in info:
    #     tmp = []
    #     for k in i:
    #         is_select = True
    #         for j in list2:
    #             if k == j:
    #                 is_select = False
    #                 break
    #         if is_select:
    #             tmp.append(k)
    #     count = count + 1
    #     list1.append(tmp)
    #     savez_dict[str(count)] = tmp
    # np.savez('1', **savez_dict)
    # data = np.load('C:/Users/80670/PycharmProjects/software_test/1.npz', allow_pickle=True)
    # print(data['2'])
    f1 = [[1,2,3],[4,5,6]]
    np.savez('2', f1)
    data = np.load('C:/Users/80670/PycharmProjects/software_test/2.npz')
    print(data['arr_0'][0])
