# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth2_provider', '0003_auto_20160316_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='access_token_expire_seconds',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
