import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'radnaev.settings')

import django
django.setup()

from store.models import Category, Product

# Создаём категории
categories_data = [
    {'name': 'Ручки и карандаши', 'slug': 'pens'},
    {'name': 'Тетради и блокноты', 'slug': 'notebooks'},
    {'name': 'Офисная бумага', 'slug': 'paper'},
    {'name': 'Папки и органайзеры', 'slug': 'folders'},
    {'name': 'Клей и корректоры', 'slug': 'glue'},
    {'name': 'Степлеры и дыроколы', 'slug': 'staplers'},
]

categories = {}
print("Создаём категории...")
for cat_data in categories_data:
    category, created = Category.objects.get_or_create(
        slug=cat_data['slug'],
        defaults={'name': cat_data['name']}
    )
    categories[cat_data['slug']] = category
    if created:
        print(f"  ✓ Создана категория: {category.name}")
    else:
        print(f"  ✓ Категория уже существует: {category.name}")

# Создаём товары
products_data = [
    # Ручки и карандаши
    {'category': 'pens', 'name': 'Ручка шариковая синяя', 'slug': 'pen-blue', 'price': 25.00, 'stock': 150, 'description': 'Классическая шариковая ручка с синими чернилами. Мягкое письмо, не мажет.'},
    {'category': 'pens', 'name': 'Ручка гелевая чёрная', 'slug': 'gel-pen-black', 'price': 45.00, 'stock': 100, 'description': 'Гелевая ручка с быстросохнущими чернилами. Тонкая линия 0.5 мм.'},
    {'category': 'pens', 'name': 'Ручка капиллярная', 'slug': 'felt-pen', 'price': 55.00, 'stock': 80, 'description': 'Капиллярная ручка-линер для черчения и письма.'},
    {'category': 'pens', 'name': 'Карандаш простой HB', 'slug': 'pencil-hb', 'price': 15.00, 'stock': 200, 'description': 'Простой карандаш средней твёрдости. Идеален для письма и черчения.'},
    {'category': 'pens', 'name': 'Набор цветных карандашей 12 шт', 'slug': 'colored-pencils', 'price': 180.00, 'stock': 40, 'description': 'Набор цветных карандашей, 12 цветов. Яркие и мягкие.'},
    
    # Тетради и блокноты
    {'category': 'notebooks', 'name': 'Тетрадь 48 листов (клетка)', 'slug': 'notebook-48-cell', 'price': 35.00, 'stock': 80, 'description': 'Тетрадь в клетку, 48 листов. Обложка - плотный картон.'},
    {'category': 'notebooks', 'name': 'Тетрадь 96 листов (линейка)', 'slug': 'notebook-96-line', 'price': 65.00, 'stock': 60, 'description': 'Тетрадь в линейку, 96 листов. Качественная бумага.'},
    {'category': 'notebooks', 'name': 'Блокнот А5 на пружине', 'slug': 'notepad-a5', 'price': 120.00, 'stock': 40, 'description': 'Блокнот формата А5, 80 листов. Твёрдая обложка, удобная пружина.'},
    {'category': 'notebooks', 'name': 'Ежедневник датированный', 'slug': 'daily-planner', 'price': 350.00, 'stock': 25, 'description': 'Датированный ежедневник А5, 160 страниц. Искусственная кожа.'},
    
    # Офисная бумага
    {'category': 'paper', 'name': 'Бумага А4 500 листов', 'slug': 'paper-a4-500', 'price': 350.00, 'stock': 30, 'description': 'Офисная бумага А4, 80 г/м², 500 листов. Класс С.'},
    {'category': 'paper', 'name': 'Бумага цветная А4', 'slug': 'colored-paper', 'price': 180.00, 'stock': 25, 'description': 'Набор цветной бумаги, 100 листов. 10 разных цветов.'},
    {'category': 'paper', 'name': 'Бумага для заметок (стикеры)', 'slug': 'sticky-notes', 'price': 75.00, 'stock': 120, 'description': 'Блок стикеров 76x76 мм, 100 листов. Яркие цвета.'},
    
    # Папки и органайзеры
    {'category': 'folders', 'name': 'Папка-скоросшиватель', 'slug': 'folder-binder', 'price': 55.00, 'stock': 70, 'description': 'Папка-скоросшиватель пластиковая, формат А4.'},
    {'category': 'folders', 'name': 'Папка на кольцах', 'slug': 'ring-binder', 'price': 150.00, 'stock': 35, 'description': 'Папка на кольцах, формат А4. Вмещает до 200 листов.'},
    {'category': 'folders', 'name': 'Папка-конверт на кнопке', 'slug': 'envelope-folder', 'price': 35.00, 'stock': 90, 'description': 'Папка-конверт пластиковая, формат А4. Прозрачная.'},
    {'category': 'folders', 'name': 'Органайзер настольный', 'slug': 'desk-organizer', 'price': 420.00, 'stock': 15, 'description': 'Настольный органайзер с 5 отделениями. Чёрный пластик.'},
    
    # Клей и корректоры
    {'category': 'glue', 'name': 'Клей-карандаш 20г', 'slug': 'glue-stick', 'price': 40.00, 'stock': 90, 'description': 'Клей-карандаш для бумаги. Не токсичен, легко смывается.'},
    {'category': 'glue', 'name': 'Клей ПВА 100мл', 'slug': 'pva-glue', 'price': 65.00, 'stock': 55, 'description': 'Клей ПВА универсальный. Подходит для бумаги, картона, дерева.'},
    {'category': 'glue', 'name': 'Корректор-лента', 'slug': 'correction-tape', 'price': 85.00, 'stock': 45, 'description': 'Корректирующая лента 5 мм х 6 м. Мгновенное высыхание.'},
    {'category': 'glue', 'name': 'Корректор-жидкость', 'slug': 'correction-fluid', 'price': 60.00, 'stock': 50, 'description': 'Корректирующая жидкость с кисточкой, 20 мл.'},
    
    # Степлеры и дыроколы
    {'category': 'staplers', 'name': 'Степлер №10', 'slug': 'stapler-10', 'price': 220.00, 'stock': 20, 'description': 'Степлер для скоб №10. Металлический корпус.'},
    {'category': 'staplers', 'name': 'Скобы №10 (1000 шт)', 'slug': 'staples-10', 'price': 45.00, 'stock': 150, 'description': 'Скобы для степлера №10, 1000 штук в упаковке.'},
    {'category': 'staplers', 'name': 'Дырокол на 2 отверстия', 'slug': 'hole-punch', 'price': 190.00, 'stock': 15, 'description': 'Дырокол металлический до 10 листов.'},
    {'category': 'staplers', 'name': 'Антистеплер', 'slug': 'staple-remover', 'price': 35.00, 'stock': 100, 'description': 'Устройство для удаления скоб. Удобная ручка.'},
]

print("\nСоздаём товары...")
for prod_data in products_data:
    category = categories[prod_data['category']]
    product, created = Product.objects.get_or_create(
        slug=prod_data['slug'],
        defaults={
            'category': category,
            'name': prod_data['name'],
            'price': prod_data['price'],
            'stock': prod_data['stock'],
            'description': prod_data['description'],
            'available': True,
        }
    )
    if created:
        print(f"  ✓ {product.name} - {product.price} ₽")
    else:
        print(f"  ✓ Товар уже существует: {product.name}")

print(f"\n✅ Готово!")
print(f"📊 Статистика:")
print(f"  - Категорий: {Category.objects.count()}")
print(f"  - Товаров: {Product.objects.count()}")