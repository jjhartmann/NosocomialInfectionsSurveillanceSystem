from django.shortcuts import render

# Create your views here.


# Main function to call the index for the main front page.
def indexview(request):
    return render(request, 'index/index.html')
