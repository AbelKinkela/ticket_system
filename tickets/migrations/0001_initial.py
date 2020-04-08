# Generated by Django 3.0.5 on 2020-04-07 16:22

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_name', models.CharField(max_length=344)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_type', models.CharField(max_length=14)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('item_collection_date', models.DateTimeField()),
                ('item_collected', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=3)),
                ('status', models.CharField(choices=[('AVAILABE', 'AVAILABLE'), ('NOT AVAILABLE', 'NOT AVAILABLE'), ('CLOSED', 'CLOSED')], max_length=13)),
                ('priority', models.CharField(choices=[('LOW', 'LOW'), ('MEDIUM', 'MEDIUM'), ('HIGH', 'HIGH')], max_length=7)),
                ('assigned_To', models.CharField(max_length=344)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tickets.User')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.Request')),
            ],
            managers=[
                ('number', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='request',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.User'),
        ),
        migrations.CreateModel(
            name='Password',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=30)),
                ('is_active', models.CharField(max_length=3)),
                ('created_date', models.DateField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tickets.User')),
            ],
        ),
        migrations.CreateModel(
            name='Event_Logs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(choices=[('LOGIN', 'LOGIN'), ('LOGOUT', 'LOGOUT'), ('REGISTER', 'REGISTER')], max_length=15)),
                ('start_date', models.DateField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tickets.User')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.Ticket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tickets.User')),
            ],
        ),
    ]
