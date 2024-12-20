from taxonomy.models import Category, CategoryConfiguration
# from product.models import


mobile_category = Category.add_root(title="mobile", slug="mobile")
mobile_category = Category.objects.get(slug='mobile')


ram_config = CategoryConfiguration.objects.create(
    category=mobile_category,
    key="RAM",
    input_type="dropdown",
    options="4GB,8GB,16GB"
)


storage = CategoryConfiguration.objects.create(
    category=mobile_category,
    key="Storage",
    input_type="dropdown",
    options="64GB,128GB,256GB"
)



other = CategoryConfiguration.objects.create(
    category=mobile_category,
    key="Other",
    input_type="dropdown",
    options=""
)





# smartphones = mobile_category.add_child(title="", slug='ultra-book')
# tablets = mobile_category.add_child(title="Gaming", slug='gaming')

# مشاهده کانفیگ‌های ارث‌برده
# print(smartphones.configurations.all())  # RAM کانفیگ را نمایش می‌دهد
# print(tablets.configurations.all())      # RAM کانفیگ را نمایش می‌دهد



