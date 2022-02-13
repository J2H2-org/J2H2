<<<<<<< HEAD
# Generated by Django 3.1.14 on 2022-02-13 04:33
=======
# Generated by Django 3.1.14 on 2022-02-12 07:07
>>>>>>> elasticsearch

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
            name='user_col',
            fields=[
                ('user_Id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='신규 회원', max_length=64)),
                ('major', models.CharField(blank=True, max_length=128)),
                ('degree', models.CharField(blank=True, max_length=16)),
                ('contact_email', models.CharField(blank=True, max_length=32)),
                ('belong', models.CharField(blank=True, max_length=64)),
                ('career', models.CharField(blank=True, max_length=128)),
                ('img_link', models.SlugField(blank=True, max_length=128)),
=======
            name='answer_col',
            fields=[
                ('answer_Id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('answer_text', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='c_answer_col',
            fields=[
                ('c_answer_Id', models.AutoField(primary_key=True, serialize=False)),
                ('c_ans', models.TextField()),
                ('c_question_Id', models.IntegerField()),
>>>>>>> elasticsearch
            ],
        ),
        migrations.CreateModel(
            name='c_question_col',
            fields=[
<<<<<<< HEAD
                ('thesis_plan_Id', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=128)),
                ('schedule', models.IntegerField()),
                ('on_domestic', models.BooleanField()),
                ('journal_tier', models.BooleanField()),
                ('purpose', models.CharField(max_length=32)),
                ('user_Id', models.ForeignKey(db_column='user_Id', on_delete=django.db.models.deletion.CASCADE, related_name='TP_user_Id', to='chat_teesis.user_col')),
=======
                ('c_question_Id', models.AutoField(primary_key=True, serialize=False)),
                ('c_que', models.TextField()),
                ('que_classification_Id', models.IntegerField()),
>>>>>>> elasticsearch
            ],
        ),
        migrations.CreateModel(
            name='mentor_answer_col',
            fields=[
                ('mentor_answer_Id', models.AutoField(primary_key=True, serialize=False)),
                ('mentor_answer', models.TextField()),
                ('mentee_question_Id', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('title', models.TextField()),
                ('user_Id', models.ForeignKey(db_column='user_Id', on_delete=django.db.models.deletion.CASCADE, related_name='MA_user_Id', to='chat_teesis.user_col')),
            ],
        ),
        migrations.CreateModel(
            name='mentee_question_col',
            fields=[
                ('mentee_question_Id', models.AutoField(primary_key=True, serialize=False)),
                ('thesis_plan_Id', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('title', models.TextField()),
                ('mentee_question', models.TextField()),
                ('user_Id', models.ForeignKey(db_column='user_Id', on_delete=django.db.models.deletion.CASCADE, related_name='MQ_user_Id', to='chat_teesis.user_col')),
            ],
        ),
        migrations.CreateModel(
            name='thesis_plan_col',
            fields=[
                ('thesis_plan_Id', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=128)),
                ('schedule', models.IntegerField()),
                ('on_domestic', models.BooleanField()),
                ('journal_tier', models.BooleanField()),
                ('purpose', models.CharField(max_length=32)),
                ('user_Id', models.ForeignKey(db_column='user_Id', on_delete=django.db.models.deletion.CASCADE, related_name='TP_user_Id', to='chat_teesis.user_col')),
            ],
        ),
        migrations.CreateModel(
            name='mentor_answer_col',
            fields=[
                ('mentor_answer_Id', models.AutoField(primary_key=True, serialize=False)),
                ('mentor_answer', models.TextField()),
                ('mentee_question_Id', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('title', models.TextField()),
                ('user_Id', models.ForeignKey(db_column='user_Id', on_delete=django.db.models.deletion.CASCADE, related_name='MA_user_Id', to='chat_teesis.user_col')),
            ],
        ),
        migrations.CreateModel(
            name='mentee_question_col',
            fields=[
                ('mentee_question_Id', models.AutoField(primary_key=True, serialize=False)),
                ('thesis_plan_Id', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('title', models.TextField()),
                ('mentee_question', models.TextField()),
                ('user_Id', models.ForeignKey(db_column='user_Id', on_delete=django.db.models.deletion.CASCADE, related_name='MQ_user_Id', to='chat_teesis.user_col')),
            ],
        ),
    ]
