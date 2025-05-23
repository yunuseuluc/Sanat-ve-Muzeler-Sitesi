# Generated by Django 5.2 on 2025-05-04 18:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Muze',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=150)),
                ('aciklama', models.TextField()),
                ('resim', models.ImageField(upload_to='muze_resimleri/')),
                ('harita_linki', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Sehir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sanatci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=150)),
                ('biyografi', models.TextField()),
                ('resim', models.ImageField(upload_to='sanatci_resimleri/')),
                ('muze', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.muze')),
            ],
        ),
        migrations.CreateModel(
            name='Eser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=150)),
                ('aciklama', models.TextField()),
                ('resim', models.ImageField(upload_to='eser_resimleri/')),
                ('muze', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.muze')),
                ('sanatci', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.sanatci')),
            ],
        ),
        migrations.AddField(
            model_name='muze',
            name='sehir',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.sehir'),
        ),
        migrations.CreateModel(
            name='Yorum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=100)),
                ('icerik', models.TextField()),
                ('tarih', models.DateTimeField(auto_now_add=True)),
                ('muze', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.muze')),
                ('sehir', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.sehir')),
            ],
        ),
    ]
