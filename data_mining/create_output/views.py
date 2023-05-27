from django.shortcuts import render  
from django.http import HttpResponse  
 
from .forms import StudentForm
from .models import Student
import pandas
import numpy as np
#from sklearn.linear_model import LogisticRegression
#from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
from django.template.loader import get_template
from .utils import get_plot,get_sns_plot,get_dataset
#from sklearn.linear_model import LinearRegression
#from sklearn.metrics import mean_squared_error, r2_score
from pathlib import Path
#import  csv
from django.views import View


class Index_View(View): 
    def get(self,request):
        return render(request,'index.html')  
    def post(self,request): 
        #if request.method == 'POST': 
         student = StudentForm(request.POST, request.FILES) 
         file = request.FILES['file'] 
         #request.session['file']=current
         ah=pandas.read_csv(file)
         current=ah
         print(current)
         get_dataset(ah)
         head_data=ah.head(10)
         head_data_con=head_data.to_html()
         shape=ah.shape
         info=ah.describe().to_html()
         type_of_dataset=ah.ndim
         data_types=pandas.DataFrame(ah.dtypes).to_html()
         info_of_dataset=(ah.info())
         x=[1,2,3,4,5,6]
         y=[2,4,6,8,9,10]
         a=get_plot(x,y)
         b=get_sns_plot(ah)
         print(ah.columns.values)
         ah1=ah.to_html()
         context={'ah1':ah1,'ah':head_data_con,'shape':shape,'info':info,'type':type_of_dataset,'types':data_types,'info':info_of_dataset,'a':a,'b':b}
         if student.is_valid(): 
             student.save()
             return render(request,"file.html",context)
         else:
             student = StudentForm()
             return render(request,"index.html",{'form':student})
             
			  
		
		
		
		
		
		
		
		
		
		
		
		
		#plt.figure(figsize=(10,8))
		#print(sns.heatmap(ah.corr(), cmap="RdBu"))
		#a=plt.show()
		#x=ah[[ 'bedrooms','bathrooms','sqft_living','sqft_lot','sqft_above','sqft_basement','yr_built','yr_renovated','floors','waterfront','view','condition','grade']]

		#y = ah['price']
		
		  
		
		
		
		#regression_model = LinearRegression()
		#regression_model.fit(x, y)
		

		#X=[ah.drop([])]
		#X_train, X_val, y_train, y_val = train_test_split(X, y, test_size = 0.2)

class show_file(View):
    def get(self,request,pk):
        ahs=Student.objects.get(id=pk)
        context={'ahs':ahs}
        return render(request,'show.html',context)
	    
	    

	

def calculate_X_Y(request):
	x=Student.objects.all().last()
	a=(x.file)
	b=str(a)
	#ahsan()
	#file1 = open("test.txt")
	#print(file1)
	#ah=pandas.read_csv(b)
	#print(ah)
	#path = Path(r'D:/django_projects/data_mining/media/')

	#for filename in path.iterdir():
	#   with filename.open() as f:
	
	
	#print(file)
	context={'x':x,'b':b}
	return render(request,'calculation.html',context)
	
