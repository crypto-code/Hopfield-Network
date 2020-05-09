import numpy as np
np.random.seed(1)
from matplotlib import pyplot as plt
import skimage.data
from skimage.color import rgb2gray
from skimage.filters import threshold_mean
from skimage.transform import resize
import network
import os

# Helper Functions
def get_corrupted_input(input, corruption_level):
    corrupted = np.copy(input)
    inv = np.random.binomial(n=1, p=corruption_level, size=len(input))
    for i, v in enumerate(input):
        if inv[i]:
            corrupted[i] = -1 * v
    return corrupted

def reshape(data):
    dim = int(np.sqrt(len(data)))
    data = np.reshape(data, (dim, dim))
    return data
def split(l, n):
    for i in range(0,len(l), n):
        yield l[i:i+n]
    
def plot(data, test, predicted):
    data = [reshape(d) for d in data]
    test = [reshape(d) for d in test]
    predicted = [reshape(d) for d in predicted]
    if not os.path.exists('results_custom'):
        os.mkdir('results_custom')
    count=0
    file_count=0
    for d in split(data, 4):
        if not len(d)is 1: 
            fig, axarr = plt.subplots(len(d), 3)
            for i in range(len(d)):
                if i==0:
                    axarr[i, 0].set_title('Train data')
                    axarr[i, 1].set_title("Input data")
                    axarr[i, 2].set_title('Output data')

                axarr[i, 0].imshow(data[count])
                axarr[i, 0].axis('off')
                axarr[i, 1].imshow(test[count])
                axarr[i, 1].axis('off')
                axarr[i, 2].imshow(predicted[count])
                axarr[i, 2].axis('off')
                count = count+1

            plt.tight_layout()
            plt.savefig("results_custom/result_"+str(file_count)+".png")
            file_count=file_count+1
            plt.show()
        else:
            fig, axarr = plt.subplots(1, 3)
            axarr[0].set_title('Train data')
            axarr[1].set_title("Input data")
            axarr[2].set_title('Output data')

            axarr[0].imshow(data[count])
            axarr[0].axis('off')
            axarr[1].imshow(test[count])
            axarr[1].axis('off')
            axarr[2].imshow(predicted[count])
            axarr[2].axis('off')
            count = count+1
            plt.tight_layout()
            plt.savefig("results_custom/result_"+str(file_count)+".png")
            file_count=file_count+1
            plt.show()

def preprocessing(img, w=128, h=128):
    # Resize image
    img = resize(img, (w,h), mode='reflect')

    # Thresholding
    thresh = threshold_mean(img)
    binary = img > thresh
    shift = 2*(binary*1)-1 # Boolian to int

    # Reshape
    flatten = np.reshape(shift, (w*h))
    return flatten

def main():
    # Load data

    import cv2
    import glob
    img_dir = "train_custom/" # Enter Directory of all images 
    data_path = os.path.join(img_dir,'*g')
    files = glob.glob(data_path)
    data = []
    for f1 in files:
        img = rgb2gray(cv2.imread(f1))
        data.append(img)
        
    # Preprocessing
    print("Start to data preprocessing...")
    data = [preprocessing(d) for d in data]

    # Create Hopfield Network Model
    model = network.HopfieldNetwork()
    model.train_weights(data)

    # Generate testset
    img_dir = "test_custom/" # Enter Directory of all images 
    data_path = os.path.join(img_dir,'*g')
    files = glob.glob(data_path)
    test = []
    # Since same name order will be the same
    for f1 in files:
        img = rgb2gray(cv2.imread(f1))
        test.append(img)
    test = [preprocessing(d) for d in test]

    predicted = model.predict(test, threshold=0, asyn=False)
    print("Show prediction results...")
    plot(data, test, predicted)
    #print("Show network weights matrix...")
    #model.plot_weights("results_custom/")

if __name__ == '__main__':
    main()
