from django.shortcuts import render, get_object_or_404, redirect
from .models import Sehir, Muze, Sanatci, Eser, Yorum
from .forms import YorumForm

def anasayfa(request):
    sehir_id = request.GET.get("sehir")
    sehirler = Sehir.objects.all().order_by("ad")
    secilen_sehir = None
    muze_listesi = []

    if sehir_id:
        secilen_sehir = Sehir.objects.get(id=sehir_id)
        muze_listesi = Muze.objects.filter(sehir=secilen_sehir)

    return render(request, "core/anasayfa.html", {
        "sehirler": sehirler,
        "secilen_sehir": secilen_sehir,
        "muze_listesi": muze_listesi
    })

def muze_detay(request, muze_id):
    muze = get_object_or_404(Muze, id=muze_id)

    sanatcilar = Sanatci.objects.filter(muze=muze).prefetch_related('ek_resimler')
    eserler = Eser.objects.filter(muze=muze).prefetch_related('ek_resimler')  # GÜNCELLENDİ
    yorumlar = Yorum.objects.filter(muze=muze).order_by('-tarih')

    if request.method == "POST":
        form = YorumForm(request.POST)
        if form.is_valid():
            yorum = form.save(commit=False)
            yorum.muze = muze
            yorum.save()
            return redirect('muze_detay', muze_id=muze.id)
    else:
        form = YorumForm()

    return render(request, "core/muze_detay.html", {
        "muze": muze,
        "sanatcilar": sanatcilar,
        "eserler": eserler,
        "yorumlar": yorumlar,
        "form": form
    })

