from django.shortcuts import render

def index(request):
    context_dict = {'tags':[
        "Cheddar",
        "Gouda",
        "Brie",
        "Swiss",
        "Mozzarella",
        "Provolone",
        "Blue",
        "Feta",
        "Havarti",
        "Gorgonzola",
        "Monterey Jack"
    ]}
    return render(request, 'CheeseBoardSite/index.html', context=context_dict)