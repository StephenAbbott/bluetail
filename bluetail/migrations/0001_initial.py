# Generated by Django 2.2.10 on 2020-06-03 09:43

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BODSEntityStatement',
            fields=[
                ('statement_id', models.TextField(primary_key=True, serialize=False)),
                ('statement_json', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('statement_type', models.TextField()),
                ('entity_name', models.TextField()),
                ('entity_type', models.TextField()),
                ('entity_id_scheme', models.TextField()),
                ('entity_id', models.TextField()),
                ('incorporatedInJurisdiction', models.TextField()),
            ],
            options={
                'db_table': 'bluetail_bods_entitystatement_view',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BODSOwnershipStatement',
            fields=[
                ('statement_id', models.TextField(primary_key=True, serialize=False)),
                ('statement_json', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('statement_type', models.TextField()),
                ('subject_entity_statement', models.TextField()),
                ('interested_person_statement_id', models.TextField()),
                ('interested_entity_statement_id', models.TextField()),
            ],
            options={
                'db_table': 'bluetail_bods_ownershipstatement_view',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BODSPersonStatement',
            fields=[
                ('statement_id', models.TextField(primary_key=True, serialize=False)),
                ('statement_json', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('identifiers_json', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('fullName', models.TextField()),
                ('personType', models.TextField()),
                ('identifiers_0_id', models.TextField()),
                ('identifiers_0_schemaName', models.TextField()),
            ],
            options={
                'db_table': 'bluetail_bods_personstatement_view',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OCDSParty',
            fields=[
                ('ocid', models.TextField(primary_key=True, serialize=False)),
                ('release_json', django.contrib.postgres.fields.jsonb.JSONField()),
                ('party_json', django.contrib.postgres.fields.jsonb.JSONField()),
                ('party_id', models.TextField()),
                ('party_role', models.TextField()),
                ('party_identifier_scheme', models.TextField()),
                ('party_identifier_id', models.TextField()),
                ('party_legalname', models.TextField()),
                ('party_name', models.TextField()),
                ('party_countryname', models.TextField()),
                ('contact_name', models.TextField()),
            ],
            options={
                'db_table': 'bluetail_ocds_parties_view',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OCDSTender',
            fields=[
                ('ocid', models.TextField(primary_key=True, serialize=False)),
                ('release_id', models.TextField()),
                ('release_json', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('value', models.FloatField()),
                ('currency', models.TextField()),
                ('release_date', models.DateTimeField()),
                ('tender_startdate', models.DateTimeField()),
                ('tender_enddate', models.DateTimeField()),
                ('buyer', models.TextField()),
                ('buyer_id', models.TextField()),
            ],
            options={
                'db_table': 'bluetail_ocds_tender_view',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BODSEntityStatementJSON',
            fields=[
                ('statement_id', models.TextField(primary_key=True, serialize=False)),
                ('statement_json', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
            ],
            options={
                'db_table': 'bluetail_bods_entitystatement_json',
            },
        ),
        migrations.CreateModel(
            name='BODSOwnershipStatementJSON',
            fields=[
                ('statement_id', models.TextField(primary_key=True, serialize=False)),
                ('statement_json', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
            ],
            options={
                'db_table': 'bluetail_bods_ownershipstatement_json',
            },
        ),
        migrations.CreateModel(
            name='BODSPersonStatementJSON',
            fields=[
                ('statement_id', models.TextField(primary_key=True, serialize=False)),
                ('statement_json', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
            ],
            options={
                'db_table': 'bluetail_bods_personstatement_json',
            },
        ),
        migrations.CreateModel(
            name='OCDSReleaseJSON',
            fields=[
                ('ocid', models.TextField(primary_key=True, serialize=False)),
                ('release_id', models.TextField()),
                ('release_json', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
            options={
                'db_table': 'bluetail_ocds_release_json',
            },
        ),
    ]
