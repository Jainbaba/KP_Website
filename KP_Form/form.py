from django import forms

from . import models


class FamilyForm(forms.ModelForm):
    class Meta:
        model = models.FamilyDetails
        exclude = ['familyId']
        widgets = {
            'familyName': forms.TextInput(attrs={
                "class": "form-control float-left mr-sm-2",
                "type": "text",
                "id": "familyName",
                "required": "",
                "placeholder": "Family Name",
                "autofocus": "",
            }),
            'familySurname': forms.TextInput(attrs={
                "class": "form-control float-left mr-sm-2",
                "type": "text",
                "id": "surname",
                "required": "",
                "placeholder": "Surname",
            }),
            'residenceAddress': forms.Textarea(attrs={
                "class": "form-control",
                "type": "text",
                "id": "residenceAddress",
                "required": "",
                "placeholder": "Residence Address",
                "rows": "3",
                'autocomplete': 'off'
            }),
            'residencePincode': forms.TextInput(attrs={
                "class": "form-control",
                "type": "text",
                "id": "pincode",
                "required": "",
                "placeholder": "Pincode",
                "pattern": "[0-9]{6}"
            }),
            'landlineNumber': forms.TextInput(attrs={
                "class": "form-control float-left mr-sm-2",
                "type": "tel",
                "id": "landline",
                "placeholder": "Landline",
                "pattern": "[0-9]{10}"
            }),
            'residenceState': forms.Select(attrs={
                'class': 'form-control State',
                'id': 'homeState',
            }),
            'residenceCity': forms.TextInput(attrs={
                'class': 'form-control City',
                'id': 'homeCity',
                "type": "text",
                "placeholder": "City",
            }),
            'residenceArea': forms.TextInput(attrs={
                'class': 'form-control Area',
                'id': 'homeArea',
                "type": "text",
                "placeholder": "Area",
                # 'class': 'form-control',
                # "type": "text",
                # 'id': 'homeArea',
                # "required": "",
                # "placeholder": "Area",
            }),
            'marudharMe': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'marudharMe',
                }),
        }


class PersonForm(forms.ModelForm):
    class Meta:
        model = models.Person
        exclude = ['personId', 'personFamily', "personAge",'personOccupationTypeDetail']
        widgets = {
            'personName': forms.TextInput(attrs={
                "class": "form-control float-left mr-sm-2",
                "type": "text",
                "id": "personName",
                "required": "",
                "placeholder": "Person Name",
                "autofocus": "",
            }),
            'personGender': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'personGender',
                }),
            'personBloodGroup': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'personBloodGroup',
                }),
            'personBOD': forms.TextInput(attrs={
                "class": "form-control",
                "type": "text",
                "id": "bod",
                "required": "",
                "placeholder": "Date Of Birth",
            }),
            'personPhoto': forms.FileInput(attrs={
                "required": "",
                "class": "custom-file-input",
                "type": "file",
            }),
            'personPhoneNumber': forms.TextInput(attrs={
                "class": "form-control  float-left mr-sm-2",
                "type": "tel",
                "id": "personePhoneNumber",
                "required": "",
                "placeholder": "Phone Number",
                "pattern": "[0-9]{10}"
            }),
            'personQualificationType': forms.Select(attrs={
                    "required": "",
                    "class": "form-control",
                    "id": "qualificationType",
            }),
            'personQualificationName': forms.Select(attrs={
                "class": "form-control",
                "id": "qualificationClass",
            }),
            'personQualificationYearOfPassing': forms.TextInput(attrs={
                "class": "form-control",
                "type": "text",
                "id": "qualificationYear",
                "placeholder": "Year Of Passing",
                "pattern": "[0-9]{4}"
            }),
            'personQualificationInstitutionName': forms.TextInput(attrs={
                "class": "form-control",
                "type": "text",
                "id": "qualificationName",
                "placeholder": "Institution Name",
            }),
            'personQualificationInstitutionState': forms.Select(attrs={
                'class': 'form-control State',
                'id': 'qualificationState',
            }),
            'personQualificationInstitutionCity': forms.TextInput(attrs={
                'class': 'form-control City',
                'id': 'qualificationCity',
                "type": "text",
                "placeholder": "City",
            }),
            'personOccupationCategory': forms.Select(attrs={
                "class": "form-control float-left mr-sm-2",
                "id": "occupation",
            }),
            'personOccupationName': forms.TextInput(attrs={
                "class": "form-control",
                "type": "text",
                "id": "occupationName",
                "required": "",
                "placeholder": "Office's Name",

            }),
            'personOccupationAddress': forms.Textarea(attrs={
                "class": "form-control",
                "type": "text",
                "id": "occupationAddress",
                "required": "",
                "placeholder": "Office's Address",
                "rows": "3",
                'autocomplete': 'off'
            }),
            'personOccupationAddressPincode': forms.TextInput(attrs={
                "class": "form-control",
                "type": "text",
                "id": "officePincode",
                "required": "",
                "placeholder": "Pincode",
                "pattern": "[0-9]{6}"
            }),
            'personOccupationPhoneNumber': forms.TextInput(attrs={
                "class": "form-control",
                "type": "tel",
                "id": "occupationPhoneNumber",
                "placeholder": "Office's Phone Number",
                "pattern": "[0-9]{10}"
            }),
            'personOccupationAddressState': forms.Select(attrs={
                'class': 'form-control State',
                'id': 'officeState',
            }),
            'personOccupationAddressCity': forms.TextInput(attrs={
                'class': 'form-control City',
                'id': 'officeCity',
                "type": "text",
                "placeholder": "City",
            }),
            'personOccupationAddressArea': forms.TextInput(attrs={
                'class': 'form-control Area',
                'id': 'officeArea',
                "type": "text",
                "placeholder": "Area",
                # 'class': 'form-control',
                # "type": "text",
                # 'id': 'homeArea',
                # "required": "",
                # "placeholder": "Area",
            }),
            'personOccupationFile': forms.FileInput(attrs={
                "required": "",
                "class": "custom-file-input",
                "type": "file",
            }),
            'personOccupationType': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'occupationType',
                "type": "text",
                "placeholder": "Type",
            }),
            'personMartialStatus': forms.Select(attrs={
                'class': 'form-control',
                'id': 'maritalStatus',
            }),



        }
