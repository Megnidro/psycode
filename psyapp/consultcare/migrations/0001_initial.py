# Generated by Django 4.2.6 on 2023-10-23 11:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0003_rename_user_patient_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForfaitConsultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duree', models.IntegerField(help_text='Durée du forfait en jours')),
                ('nombre_consultations', models.IntegerField(help_text='Nombre de consultations incluses dans le forfait')),
                ('description', models.TextField(blank=True, null=True)),
                ('psy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forfaits', to='accounts.psy')),
            ],
        ),
        migrations.CreateModel(
            name='SpecialisationPsy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialist', models.CharField(choices=[('Psychologue', 'Psychologue'), ('Psychiatre', 'Psychiatre'), ('Psychotherapeute', 'Psychotherapeute'), ('Psychanalyste', 'Psychanalyste')], max_length=50)),
                ('psy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.psy')),
            ],
        ),
        migrations.CreateModel(
            name='SouscriptionForfait',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_souscription', models.DateTimeField(auto_now_add=True)),
                ('date_expiration', models.DateTimeField()),
                ('consultations_restantes', models.IntegerField()),
                ('forfait', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='souscriptions', to='consultcare.forfaitconsultation')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='souscriptions', to='accounts.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('communication_method', models.CharField(choices=[('SMS', 'Messagerie SMS'), ('AudioCall', 'Appel Audio'), ('VideoCall', 'Appel Vidéo'), ('Email', 'Email'), ('Office', 'Office')], max_length=10)),
                ('date_et_heure', models.DateTimeField()),
                ('duree', models.DurationField(default=datetime.timedelta(seconds=1800))),
                ('status', models.CharField(choices=[('planifiee', 'Planifiée'), ('en_cours', 'En cours'), ('terminee', 'Terminée'), ('annulee', 'Annulée')], default='planifiee', max_length=20)),
                ('note', models.TextField(blank=True, null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultations', to='accounts.patient')),
                ('psy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.psy')),
                ('souscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultations', to='consultcare.souscriptionforfait')),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('stripe_payment_intent_id', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(default='en_attente', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('consultation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultcare.consultation')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commandes', to='accounts.patient')),
                ('psy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.psy')),
            ],
        ),
    ]