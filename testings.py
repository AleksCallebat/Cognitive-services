import matplotlib.pyplot as plt

def showResultOnImage( result, img,name ):
    print("printing the image")
    """Display the obtained results onto the input image"""
    img = img[:, :, (2, 1, 0)]
    fig, ax = plt.subplots(figsize=(12, 12))
    ax.imshow(img, aspect='equal')
    for i in range(len(result)):
        text=result[i]['text']
        bb=result[i]["boundingBox"].split(",")
        x = np.array([bb[0], bb[0], bb[2], bb[2], bb[0]],dtype=int)
        y = np.array([bb[1], bb[3], bb[3], bb[1], bb[1]],dtype=int)
        try :
            ax.text(int(bb[0]), int(bb[1]) - 2, '{:s}'.format(text),
            bbox=dict(facecolor='white', alpha=0.5),
            fontsize=22, color='black')
        except:
            print("exception",x,y)
                
    plt.axis('off')
    plt.tight_layout()

    plt.draw()
    plt.show()
