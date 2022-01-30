
from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist



from .models import translation



# Create your views here.

#Home Page
def index(request):
    return render(request,'index.html')

# Function to query word exisiten


#search page 
def search(request):
    word = request.GET['word']

    # Query word in databse 
    # use english word to find twi word in database 
    # Querying word_english 
    try:
        query_translation = translation.objects.get(word_english__iexact=word)
    except ObjectDoesNotExist:
        return redirect('error')

    
    query_translation =translation.objects.filter(word_english__iexact=word)
    
    #print(query_translation)
    

   

#web scrapping to get translation from another site 
# previous idea  
# res = requests.get('https://glosbe.com/en/tw/'+word)
    # if res:
    #     #Convert result from res to lxml to be able to touch or access data
    #     soup = bs4.BeautifulSoup(res.text,'lxml')

    #     translationElement = soup.find_all('h3',{'class':'translation'})
    #     translation = translationElement[0].getText()
    # else:
    #     word = 'Sorry, '+word+'is not found in Our Database'
    #     translation='Not Found'


    return render(request,'search.html',{'translation': query_translation[0]})


# Add New Translation Page 
def addTranslation(request):

    if request.method=='POST':
  
        new_translation = translation(word_english=request.POST.get('word_english'),word_twi=request.POST.get('word_twi'),desc=request.POST.get('desc'),other_words=request.POST.get('other_words'))
        new_translation.save()
        return redirect('index')



    #messages.success(request,"Translation Saved.")

    return render(request,'add_translation.html')


#404 page 
def errorPage(request):
    return render(request,'404.html')


