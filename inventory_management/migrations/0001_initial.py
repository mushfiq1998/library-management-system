# Generated by Django 4.2.16 on 2024-11-20 13:27

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book_catalog', '0004_book_availability_notes_book_availability_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_copies', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)])),
                ('available_copies', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)])),
                ('minimum_threshold', models.PositiveIntegerField(default=2, help_text='Minimum number of copies before reordering')),
                ('last_inventory_date', models.DateTimeField(auto_now=True)),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='inventory', to='book_catalog.book')),
            ],
        ),
        migrations.CreateModel(
            name='InventoryLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('ADD', 'Added copies'), ('REMOVE', 'Removed copies'), ('ADJUST', 'Adjusted inventory'), ('DAMAGE', 'Marked as damaged'), ('LOST', 'Marked as lost'), ('REPAIR', 'Sent for repair'), ('RETURN', 'Returned from repair')], max_length=10)),
                ('quantity', models.IntegerField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('notes', models.TextField(blank=True)),
                ('inventory_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='inventory_management.inventoryitem')),
                ('performed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DamagedBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('damage_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('damage_description', models.TextField()),
                ('status', models.CharField(choices=[('DAMAGED', 'Damaged'), ('REPAIRING', 'Under Repair'), ('REPAIRED', 'Repaired'), ('DISCARDED', 'Discarded')], default='DAMAGED', max_length=10)),
                ('repair_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('repair_notes', models.TextField(blank=True)),
                ('repaired_date', models.DateTimeField(blank=True, null=True)),
                ('inventory_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='damaged_copies', to='inventory_management.inventoryitem')),
            ],
        ),
    ]
