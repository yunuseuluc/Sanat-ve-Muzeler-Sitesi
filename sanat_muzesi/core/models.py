from django.db import models

class Sehir(models.Model):
    ad = models.CharField(max_length=100)

    def __str__(self):
        return self.ad

class Muze(models.Model):
    ad = models.CharField(max_length=150)
    sehir = models.ForeignKey(Sehir, on_delete=models.CASCADE)
    aciklama = models.TextField()
    resim = models.ImageField(upload_to='muze_resimleri/')
    harita_linki = models.URLField()

    def __str__(self):
        return self.ad


class Sanatci(models.Model):
    ad = models.CharField(max_length=150)
    biyografi = models.TextField()
    resim = models.ImageField(upload_to='sanatci_resimleri/', blank=True, null=True)
    muze = models.ForeignKey(Muze, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.ad

class SanatciResim(models.Model):
    sanatci = models.ForeignKey(Sanatci, on_delete=models.CASCADE, related_name='ek_resimler')
    resim = models.ImageField(upload_to='sanatci_resimleri_ek/')

    def __str__(self):
        return f"{self.sanatci.ad} - Resim {self.id}"

class Eser(models.Model):
    ad = models.CharField(max_length=150)
    sanatci = models.ForeignKey(Sanatci, on_delete=models.SET_NULL, null=True, blank=True)
    muze = models.ForeignKey(Muze, on_delete=models.CASCADE)
    aciklama = models.TextField(null=True, blank=True)
    resim = models.ImageField(upload_to='eser_resimleri/', blank=True, null=True)

    def __str__(self):
        return self.ad

class EserResim(models.Model):
    eser = models.ForeignKey(Eser, on_delete=models.CASCADE, related_name='ek_resimler')
    resim = models.ImageField(upload_to='eser_resimleri_ek/')

    def __str__(self):
        return f"{self.eser.ad} - Resim {self.id}"

class Yorum(models.Model):
    isim = models.CharField(max_length=100)
    icerik = models.TextField()
    tarih = models.DateTimeField(auto_now_add=True)
    muze = models.ForeignKey(Muze, on_delete=models.CASCADE, null=True, blank=True)
    sehir = models.ForeignKey(Sehir, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.isim} - {self.tarih.strftime('%d/%m/%Y')}"
