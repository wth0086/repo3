from django import forms
from .models import Employee

class EmployeesForm(forms.ModelForm):
    class Meta:
        model = Employee

        fields = (  # 기존의 위젯을 살릴 방법이 없을까?
            "ID",
            "name",
            "work_type",
            "birthdate",
            "address",
            "phone_number",
        )
    def save(self, *args, **kwargs):
        employee = super().save(commit=False)
        employee.ID = self.cleaned_data.get("ID")
        employee.name = self.cleaned_data.get("name")
        employee.work_type = self.cleaned_data.get("work_type")
        employee.birthdate = self.cleaned_data.get("birthdate")
        employee.address = self.cleaned_data.get("address")
        employee.phone_number = self.cleaned_data.get("phone_number")
        super()._save_m2m()