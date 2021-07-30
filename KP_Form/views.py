from django.http import HttpResponse
from django.shortcuts import render, redirect

from .form import FamilyForm, PersonForm
from .models import QualificationName, FamilyDetails


def index(request):
    familyForm = FamilyForm()
    if request.method == 'POST':
        familyForm = FamilyForm(request.POST)
        if familyForm.is_valid():
            familydetails = familyForm.save()
            return redirect(addPerson,familydetails.familyId)
            #return render(request, 'html/personForm.html',{"family":familydetails,'personForm':personForm})
    return render(request, 'html/index.html', {"familyForm": familyForm})


# def load_cities(request):
#     state_id = request.GET.get('state_id')
#     state_Name = request.GET.get('stateName')
#     cities = City.objects.filter(state_id=state_id).all()
#     return render(request, 'html/qualificationload.html', {"cities": cities})


# def addCityandState():
#     df = pd.read_csv('/Users/hrithikjain/PycharmProjects/KP_Website/static/CityState.csv')
#     statelist = df['State'].to_list()
#     citylist = df['City'].to_list()
#     res = {}
#
#     for value in sorted(set(statelist)):
#         print(value)
#         state = State.objects.create(stateName=value)
#         state.save()
#
#     for value in citylist:
#         for value2 in statelist:
#             res[value] = value2
#             statelist.remove(value2)
#             break
#
#     for key, value in res.items():
#         stateId = State.objects.get(stateName=value)
#         city = City.objects.create(state=stateId, cityName=key)
#         city.save()


# def addQualification():
#     df = pandas.read_csv('/Users/hrithikjain/PycharmProjects/KP_Website/static/data.csv')
#     typelist = df['Type'].to_list()
#     namelist = df['Degree'].to_list()
#     res = {}
#     for value in namelist:
#         for value2 in typelist:
#             res[value] = value2
#             typelist.remove(value2)
#             break
#     for key, value in res.items():
#         type = QualificationType.objects.get(typeName=value.strip())
#         name = QualificationName.objects.create(typeName=type, name=key)
#         name.save()


def load_qualification(request):
    TypeId = request.GET.get('TypeId')
    namedata = QualificationName.objects.filter(typeName_id=TypeId)
    return render(request, 'html/qualificationload.html', {"namedata": namedata})


def family(request, FamilyID):
    family = FamilyDetails.objects.get(familyId=FamilyID)
    idFam = FamilyID
    return render(request, 'html/familyCard.html', {"family": family , 'id':idFam})


def addPerson(request,FamilyID):
    family = FamilyDetails.objects.get(familyId=FamilyID)
    personForm = PersonForm()
    print(request.method)
    if request.method == 'POST':
        personForm = PersonForm(request.POST)
        print(personForm.errors)
        if personForm.is_valid():
            personDetails = personForm.save(commit=False)
            print(personDetails)
            return HttpResponse("<h1>Form FIlled</h1>")
    return render(request,'html/personForm.html', {"personForm":personForm, 'family':family })
