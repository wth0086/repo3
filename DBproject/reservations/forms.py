from django import forms
from django.utils import timezone
from . import models


class ReservationForm(forms.Form):
    Start_Date = forms.DateField(widget=forms.SelectDateWidget)
    End_Date = forms.DateField(widget=forms.SelectDateWidget)

    # def clean(self):
    #     Start_Date = self.cleaned_data.get("Start_Date")
    #     End_Date = self.cleaned_data.get("End_Date")


class Reservate(forms.ModelForm):
    class Meta:
        model = models.Reservation
        fields = (  # 기존의 위젯을 살릴 방법이 없을까? -> 노마드 20.10강 강의에서 나옴
            "user",
            "checkin",
            "checkout",
            "roomtype",
            "bedtype",
            "card",
            "cardNum",
            "cardExpYear",
            "cardExpMonth",
            "additionalService",
        )
        widgets = {
            "checkin": forms.SelectDateWidget,
            "checkout": forms.SelectDateWidget,
            "cardExpYear": forms.TextInput(attrs={"placeholder": "YYYY"}),
            "cardExpMonth": forms.TextInput(attrs={"placeholder": "MM"}),
            "additionalService": forms.CheckboxSelectMultiple,
        }

    def save(self, *args, **kwargs):
        reservation = super().save(commit=False)
        reservation.created = timezone.now()
        reservation.updated = timezone.now()
        reservation.user = self.cleaned_data.get("user")
        reservation.checkin = self.cleaned_data.get("checkin")
        reservation.checkout = self.cleaned_data.get("checkout")
        reservation.roomtype = self.cleaned_data.get("roomtype")
        reservation.bedtype = self.cleaned_data.get("bedtype")
        reservation.card = self.cleaned_data.get("card")
        reservation.cardExpYear = self.cleaned_data.get("cardExpYear")
        reservation.cardExpMonth = self.cleaned_data.get("cardExpMonth")
        reservation.save()
        reservation.additionalService.set(self.cleaned_data["additionalService"])
        super()._save_m2m()
