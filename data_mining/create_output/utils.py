import matplotlib.pyplot as plt
import base64
from io import BytesIO
import seaborn as sns
import pandas as pd


def get_graph():
    buffer=BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png=buffer.getvalue()
    graph=base64.b64encode(image_png)
    graph=graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title('Helo_diagram is')
    plt.plot(x,y)
    plt.xticks(rotation=45)
    plt.xlabel('khotha')
    plt.ylabel('kameena')
    plt.tight_layout()

    graph=get_graph()
    return graph

def get_sns_plot(ah):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title('Helo_diagram is')
    
    sns.countplot(data=ah)
    
    
    plt.show()
    
    graph=get_graph()
    return graph

def get_dataset(x):
    print(x)

