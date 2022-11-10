from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey


class User(AbstractUser):
    email = models.EmailField(
        _('email address'),
        unique=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Category(models.Model):

    name = models.CharField(max_length=50)
    parent = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        null=True,
        blank=True,

    )
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', null=True)



    def get_absolute_url(self,):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return f'{self.name} | parent - {self.parent}' if self.parent else self.name

    def return_children(self):

        return self.category_set.all()

    @classmethod
    def get_default_pk(cls):
        obj, created = cls.objects.get_or_create(name="No category")
        return obj.pk

class Order(models.Model):

    class StatusChoices(models.TextChoices):
        NOT_PAID = 'not_paid', 'Не оплачено'
        PAID = 'paid', 'Оплачено'

    customer = models.ForeignKey(
        "main.Customer",
        on_delete=models.SET_NULL,
        null=True
    )
    status = models.CharField(
        max_length=10,
        default=StatusChoices.NOT_PAID,
        choices=StatusChoices.choices
    )
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("order")
        verbose_name_plural = _("orders")

    def __str__(self):
        return f'{self.id} - {self.customer} ({self.get_status_display()})'

class OrderItems(models.Model):

    product = models.ForeignKey(
        "main.Product",
        on_delete=models.PROTECT,
        related_name='order_items'
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        # limit_choices_to={'status': 'not_paid'},
        related_name='items'
    )
    quantity = models.PositiveSmallIntegerField(default=1)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("order item")
        verbose_name_plural = _("order items")
        unique_together = (('product', 'order'),)

    def __str__(self):
        return f'{self.order} - {self.product} {self.quantity}'


class Customer(models.Model):

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = _("customer")
        verbose_name_plural = _("customers")

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=150)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_DEFAULT,
        default=Category.get_default_pk,
        related_name='+'
    )
    photo = models.ImageField(upload_to="media/photos/%Y/%m/%d/", verbose_name='Фото', null=True)
    brand = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', null=True)
    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")

    def __str__(self):
        return f'{self.brand} | {self.name} ({self.price})'
