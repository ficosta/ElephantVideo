# Generated by Django 2.0.5 on 2018-08-20 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='block',
            name='channel',
        ),
        migrations.RemoveField(
            model_name='block',
            name='clip',
        ),
        migrations.RemoveField(
            model_name='favorite',
            name='block',
        ),
        migrations.AddField(
            model_name='clip',
            name='hiresURL',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='clip',
            name='lowresURL',
            field=models.URLField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='clip',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Indisponivel'), (1, 'Hires disponivel'), (2, 'Lowres disponivel'), (3, 'Hires e Lowres disponivel')], default=1),
        ),
        migrations.AddField(
            model_name='favorite',
            name='clip',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='video.Clip'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='channel',
            name='logo',
            field=models.ImageField(blank=True, upload_to='logo/'),
        ),
        migrations.DeleteModel(
            name='Block',
        ),
    ]
