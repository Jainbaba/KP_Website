from django.db import models

MARUDHAR_ME = [
    ('Sojat Road', 'Sojat Road'),
]

BLOOD_GROUP = [
    ("A+", "A+"),
    ("A-", 'A-'),
    ("B+", 'B+'),
    ("B-", 'B-'),
    ("O+", 'O+'),
    ("O-", 'O-'),
    ("AB+", 'AB+'),
    ("AB-", 'AB-'),
]

GENDER = [
    ('Male', 'Male'),
    ('Female', 'Female')
]

OCCUPATION_TYPE = [
    ("Businessman", "Businessman"),
    ("Professional", "Professional"),
    ("Private Employee", 'Private Employee'),
    ("Govt Employee", "Govt Employee"),
    ("Self Employee", "Self Employee"),
    ("Student", "Student"),
]

MARTIAL_STATUS = [
    ("Unmarried", "Unmarried"),
    ("Engaged", 'Engaged'),
    ("Married", 'Married'),
    ("Divorced", 'Divorced'),
    ("Widowed", 'Widowed'),
]


class State(models.Model):
    stateId = models.AutoField(primary_key=True)
    stateName = models.CharField(max_length=256)

    def __str__(self):
        return self.stateName


# class City(models.Model):
#     cityId = models.AutoField(primary_key=True)
#     state = models.ForeignKey(State, on_delete=models.CASCADE)
#     cityName = models.CharField(max_length=256)
#
#     def __str__(self):
#         return self.cityName


# class Area(models.Model):
#     areaId = models.AutoField(primary_key=True)
#     state = models.ForeignKey(State, on_delete=models.CASCADE)
#     city = models.ForeignKey(City, on_delete=models.CASCADE)
#     areaName = models.CharField(max_length=256)
#
#     def __str__(self):
#         return self.areaName

class QualificationType(models.Model):
    typeId = models.AutoField(primary_key=True)
    typeName = models.CharField(max_length=52)

    def __str__(self):
        return self.typeName


class QualificationName(models.Model):
    nameId = models.AutoField(primary_key=True)
    typeName = models.ForeignKey(QualificationType, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class FamilyDetails(models.Model):
    familyId = models.BigAutoField(primary_key=True)
    familyName = models.CharField(max_length=256)
    familySurname = models.CharField(max_length=256)
    marudharMe = models.CharField(max_length=256, choices=MARUDHAR_ME)
    residenceAddress = models.TextField(max_length=512)
    residenceState = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    residenceCity = models.CharField(max_length=256)
    residenceArea = models.CharField(max_length=256)
    residencePincode = models.CharField(max_length=6)
    landlineNumber = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.familyName + '(' + self.marudharMe + ")"


class Person(models.Model):
    personId = models.BigAutoField(primary_key=True)
    personFamily = models.ForeignKey(FamilyDetails, on_delete=models.CASCADE)
    personName = models.CharField(max_length=256)
    personGender = models.CharField(max_length=256, choices=GENDER)
    personBloodGroup = models.CharField(max_length=5, choices=BLOOD_GROUP)
    personBOD = models.DateField()
    personAge = models.CharField(max_length=3)
    personPhoto = models.FileField()
    personPhoneNumber = models.CharField(max_length=10)
    personQualificationType = models.ForeignKey(QualificationType, on_delete=models.SET_NULL, null=True)
    personQualificationName = models.ForeignKey(QualificationName, on_delete=models.SET_NULL, null=True)
    personQualificationInstitutionName = models.CharField(max_length=256)
    personQualificationInstitutionCity = models.CharField(max_length=256)
    personQualificationInstitutionState = models.ForeignKey(State, on_delete=models.SET_NULL, null=True,
                                                            related_name="personQualificationInstitutionState")
    personQualificationYearOfPassing = models.CharField(max_length=4)
    personOccupationCategory = models.CharField(max_length=256, choices=OCCUPATION_TYPE)
    personOccupationType = models.CharField(max_length=256)
    personOccupationTypeDetail = models.CharField(max_length=256)
    personOccupationName = models.CharField(max_length=256)
    personOccupationPhoneNumber = models.CharField(max_length=10)
    personOccupationAddress = models.CharField(max_length=512)
    personOccupationAddressState = models.ForeignKey(State, on_delete=models.SET_NULL, null=True,
                                                     related_name="personOccupationAddressState")
    personOccupationAddressCity = models.CharField(max_length=256)
    personOccupationAddressArea = models.CharField(max_length=256)
    personOccupationAddressPincode = models.CharField(max_length=6)
    personOccupationFile = models.FileField()
    personMartialStatus = models.CharField(max_length=256, choices=MARTIAL_STATUS)
