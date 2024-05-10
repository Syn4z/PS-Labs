import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage import exposure
import numpy as np


figureCount = 1
xLabel = 'Time Index'
yLabel = 'Amplitude'

def drawPlot(c, title, blackAndWhite=False):
    plt.figure()
    if blackAndWhite:
        plt.hist(c.ravel(), bins=256, range=(0, 255), density=True, color='k', alpha=0.7)
        plt.title(title)
        plt.xlabel('Pixel Value')
        plt.ylabel('Frequency')
    elif not blackAndWhite:
        if title == 'Grayscale Image':
            plt.imshow(c, cmap='gray')
        else:
            plt.imshow(c)
        plt.title(title)
    savePlot() 

def savePlot():
    global figureCount
    plt.savefig(f'output/{figureCount}.png')
    plt.close()
    figureCount += 1

def scaleImage(path):
    c = mpimg.imread(path)
    cc = c[1:257, 1:257, :]
    drawPlot(c, 'Original Image')
    drawPlot(cc, 'Modified Image')
    return cc

def operationOnImage(c, operation):
    if operation == 'addition':
        c1 = np.clip(c.astype(np.int_) + 128, 0, 255).astype(np.uint8)
        drawPlot(c1, 'Addition Image')
    elif operation == 'subtraction':
        c1 = np.clip(c.astype(np.int_) - 128, 0, 255).astype(np.uint8)  
        drawPlot(c1, 'Substraction Image')  
    elif operation == 'division':
        c1 = np.clip(c.astype(np.float32) / 2, 0, 255).astype(np.uint8)
        drawPlot(c1, 'Division Image')
    elif operation == 'multiplication':
        c1 = np.clip(c.astype(np.float32) * 2, 0, 255).astype(np.uint8)
        drawPlot(c1, 'Multiplication Image')    
    elif operation == 'special':
        c1 = np.clip((c.astype(np.float32) * 0.5) + 128, 0, 255).astype(np.uint8)
        drawPlot(c1, 'Multiplication by 0.5 and Addition by 128 Image')    
    elif operation == 'black&white':
        c1 = np.mean(c, axis=2)
        drawPlot(c1, 'Grayscale Image')
        drawPlot(c1, 'Grayscale Image Histogram', blackAndWhite=True)  
    elif operation == 'rgb':
        R = np.histogram(c[:,:,0], bins=256, range=(0, 255), density=True)[0]
        G = np.histogram(c[:,:,1], bins=256, range=(0, 255), density=True)[0]
        B = np.histogram(c[:,:,2], bins=256, range=(0, 255), density=True)[0]    

        plt.figure()
        plt.plot(R, color='r')
        plt.plot(G, color='g')
        plt.plot(B, color='b')
        plt.title('Histogram for each color channel')
        plt.xlabel('Pixel Value')
        plt.ylabel('Frequency')
        plt.legend(['Red channel', 'Green channel', 'Blue channel'])   
        savePlot()

def equalizeImage(c, blackAndWhite=False):
    if blackAndWhite:
        cc_gray = np.mean(c, axis=2)

        # Perform histogram equalization
        h = exposure.equalize_hist(cc_gray)

        # Display the original and equalized images, and their histograms
        fig, axes = plt.subplots(1, 2, figsize=(12, 6))
        axes[0].imshow(cc_gray, cmap='gray')
        axes[0].set_title('Original Image')
        axes[0].axis('off')
        axes[1].imshow(h, cmap='gray')
        axes[1].set_title('Equalized Image')
        axes[1].axis('off')
        savePlot()

        plt.figure()
        plt.hist(cc_gray.ravel(), bins=256, range=(0, 1), color='b', alpha=0.5, label='Original')
        plt.hist(h.ravel(), bins=256, range=(0, 1), color='r', alpha=0.5, label='Equalized')
        plt.title('Histogram')
        plt.xlabel('Pixel Value')
        plt.ylabel('Frequency')
        plt.legend()       
        savePlot()
    else:
        I2 = cv2.convertScaleAbs(c, alpha=1, beta=0)
        I2 = cv2.cvtColor(I2, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB for matplotlib display

        # Calculate histograms for each color channel
        R = cv2.calcHist([I2], [0], None, [256], [0, 256])
        G = cv2.calcHist([I2], [1], None, [256], [0, 256])
        B = cv2.calcHist([I2], [2], None, [256], [0, 256])

        # Plot histograms
        plt.plot(R, color='r')
        plt.plot(G, color='g')
        plt.plot(B, color='b')
        plt.title('Histogram for each color channel')
        plt.xlabel('Pixel Value')
        plt.ylabel('Frequency')
        plt.legend(['Red channel', 'Green channel', 'Blue channel'])
        plt.show()    