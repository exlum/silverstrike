# Generated by Django 2.1.2 on 2019-01-05 11:47

from django.db import migrations, models
import django.db.models.deletion


def updateTransactions(apps, schema_editor):
    Transaction = apps.get_model('silverstrike', 'Transaction')
    db_alias = schema_editor.connection.alias
    for t in Transaction.objects.using(db_alias).all():
        for s in t.splits.filter(amount__gt=0):
            t.amount += s.amount
            t.src = s.opposing_account
            t.dst = s.account
        t.save()

class Migration(migrations.Migration):

    dependencies = [
        ('silverstrike', '0007_auto_20181230_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='transaction',
            name='dst',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='credits', to='silverstrike.Account'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='src',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='debits', to='silverstrike.Account'),
            preserve_default=False,
        ),
        migrations.RunPython(
            updateTransactions
        )
    ]
