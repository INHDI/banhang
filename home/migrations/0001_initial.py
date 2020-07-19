# Generated by Django 3.0.8 on 2020-07-19 13:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LoaiSPModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ma_loai', models.CharField(blank=True, max_length=10, verbose_name='Mã Loại Sản Phẩn')),
                ('Loai_sp', models.CharField(blank=True, max_length=50, verbose_name='Tên Loại Sản Phẩn')),
                ('Mo_ta', models.TextField(verbose_name='Mô Tả')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngay_tao', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False, null=True)),
                ('transaction_id', models.CharField(max_length=100, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hoten', models.CharField(max_length=200)),
                ('diachi', models.CharField(max_length=200)),
                ('sdt', models.CharField(max_length=200)),
                ('Email', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Customer')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Order')),
            ],
        ),
        migrations.CreateModel(
            name='SanPhamModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ma_sp', models.CharField(max_length=10, verbose_name='Mã Sản Phẩm')),
                ('Ten_sp', models.CharField(blank=True, max_length=50, verbose_name='Tên Sản Phẩm')),
                ('Mo_ta', models.TextField(verbose_name='Mô Tả')),
                ('Gia_nhap', models.IntegerField(blank=True, default=0, verbose_name='Giá Nhập')),
                ('Sale', models.PositiveIntegerField(blank=True, default=0)),
                ('Gia_ban', models.IntegerField(blank=True, default=200000, verbose_name='Giá Bán')),
                ('Gia_sale', models.IntegerField(default=150000, verbose_name='Giá Sale')),
                ('Hang_ton', models.IntegerField(default=100, verbose_name='Hàng Tồn')),
                ('Anh', models.ImageField(upload_to='images')),
                ('Loai_sp', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.LoaiSPModel', verbose_name='Loại Sản Phẩm')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.SanPhamModel')),
            ],
        ),
    ]
