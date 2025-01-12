# Generated by Django 4.2 on 2024-12-15 00:09

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import mobo.storage
import tools.uploader
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0001_initial'),
        ('taxonomy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100)),
                ('input_type', models.CharField(choices=[('text', 'Text'), ('number', 'Number'), ('boolean', 'Boolean'), ('dropdown', 'Dropdown')], max_length=50)),
                ('options', models.TextField(blank=True, help_text='Comma-separated options for dropdown (e.g., 4GB,8GB,16GB)', null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='configurations', to='taxonomy.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('status', models.CharField(choices=[('cancelled', 'توقف تولید'), ('avail', 'موجود در ایران'), ('tobeavail', 'به زودی موجود'), ('notavail', 'ناموجود در ایران')], default='avail', max_length=15)),
                ('title', models.CharField(max_length=128)),
                ('title_fa', models.CharField(max_length=256)),
                ('thumbnail', models.ImageField(blank=True, null=True, storage=mobo.storage.PublicMediaStorage(), upload_to=tools.uploader.upload_to_product)),
                ('slug', models.SlugField(max_length=128, unique=True)),
                ('min_price', models.DecimalField(decimal_places=4, default=0.0, max_digits=19)),
                ('max_price', models.DecimalField(decimal_places=4, default=0.0, max_digits=19)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('summery', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('upc', models.CharField(blank=True, max_length=120, null=True)),
                ('has_wp_page', models.BooleanField(default=False)),
                ('extra', models.TextField(blank=True, null=True)),
                ('nickname', models.CharField(blank=True, max_length=600, null=True)),
                ('generate_content_ai', models.BooleanField(default=False)),
                ('wp_post_id', models.CharField(max_length=10, null=True)),
                ('mobo_offer', models.BooleanField(default=False)),
                ('edit_upc_access', models.BooleanField(default=True)),
                ('crawler_status', models.BooleanField(default=True)),
                ('is_configurable', models.BooleanField(default=False)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='taxonomy.brand')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accessories', to='taxonomy.category')),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='organization.organization')),
                ('tags', models.ManyToManyField(blank=True, null=True, to='taxonomy.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
                ('configuration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_values', to='product.categoryconfiguration')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='configurations', to='product.product')),
            ],
        ),
    ]
