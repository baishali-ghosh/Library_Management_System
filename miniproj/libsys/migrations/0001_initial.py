# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bid', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('price', models.IntegerField(max_length=20)),
                ('noofcopies', models.IntegerField(default=0, max_length=20)),
                ('author', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('issuedate', models.DateField()),
                ('duedate', models.DateField()),
                ('bookid', models.ForeignKey(to='libsys.Book')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('mid', models.AutoField(serialize=False, primary_key=True)),
                ('bday', models.DateTimeField()),
                ('fname', models.CharField(max_length=50)),
                ('midname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('password', models.CharField(default=b'', max_length=100)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('age', models.IntegerField()),
                ('occupation', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('pid', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('paddress', models.CharField(max_length=200)),
                ('pphone', models.IntegerField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('sid', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('sname', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='borrow',
            name='memid',
            field=models.ForeignKey(to='libsys.Member'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='pubid',
            field=models.ForeignKey(to='libsys.Publisher'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='secid',
            field=models.ForeignKey(to='libsys.Section'),
            preserve_default=True,
        ),
    ]
