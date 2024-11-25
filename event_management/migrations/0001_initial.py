# Generated by Django 4.2.16 on 2024-11-25 14:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book_catalog', '0004_book_availability_notes_book_availability_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('event_type', models.CharField(choices=[('BOOK_LAUNCH', 'Book Launch'), ('READING_CLUB', 'Reading Club'), ('WORKSHOP', 'Workshop'), ('AUTHOR_VISIT', 'Author Visit'), ('CHILDREN_EVENT', "Children's Event"), ('EXHIBITION', 'Exhibition'), ('OTHER', 'Other')], max_length=20)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('location', models.CharField(max_length=200)),
                ('capacity', models.PositiveIntegerField()),
                ('registration_deadline', models.DateTimeField()),
                ('status', models.CharField(choices=[('UPCOMING', 'Upcoming'), ('ONGOING', 'Ongoing'), ('COMPLETED', 'Completed'), ('CANCELLED', 'Cancelled')], default='UPCOMING', max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='event_images/')),
                ('attachment', models.FileField(blank=True, null=True, upload_to='event_attachments/')),
                ('is_public', models.BooleanField(default=True)),
                ('requires_registration', models.BooleanField(default=True)),
                ('registration_fee', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('featured_authors', models.ManyToManyField(blank=True, related_name='featured_events', to='book_catalog.author')),
                ('organizer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='organized_events', to=settings.AUTH_USER_MODEL)),
                ('related_books', models.ManyToManyField(blank=True, related_name='events', to='book_catalog.book')),
            ],
        ),
        migrations.CreateModel(
            name='EventResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('resource_type', models.CharField(choices=[('DOCUMENT', 'Document'), ('PRESENTATION', 'Presentation'), ('VIDEO', 'Video'), ('AUDIO', 'Audio'), ('OTHER', 'Other')], max_length=20)),
                ('file', models.FileField(upload_to='event_resources/')),
                ('is_public', models.BooleanField(default=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='event_management.event')),
                ('uploaded_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('CONFIRMED', 'Confirmed'), ('CANCELLED', 'Cancelled'), ('ATTENDED', 'Attended')], default='PENDING', max_length=20)),
                ('payment_status', models.BooleanField(default=False)),
                ('notes', models.TextField(blank=True)),
                ('check_in_time', models.DateTimeField(blank=True, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to='event_management.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_registrations', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('event', 'user')},
            },
        ),
        migrations.CreateModel(
            name='EventFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_anonymous', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback', to='event_management.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('event', 'user')},
            },
        ),
    ]