import json
from taxonomy.models import Category, Brand
from product.models import Product, ProductVariant, ProductConfiguration


def import_laptop_data():
    # Load the JSON data
    with open("mobile.json", "r", encoding="utf-8") as file:
        laptop_data = json.load(file)

    # Step 1: Ensure the "Laptop" category exists
    print("Ensuring Laptop category exists...")
    laptop_category, _ = Category.objects.get_or_create(
        title="mobile",
        slug="mobile",
    )
    print(f"Category: {laptop_category.title}")

    # Step 2: Get all configurations for the "Laptop" category
    print("Fetching configurations for Laptop category...")
    configurations = laptop_category.get_configurations()
    configurations_map = {config.key: config for config in configurations}
    print(f"Configurations fetched: {[config.key for config in configurations]}")

    # Step 3: Import brands, products, and their configurations
    print("Importing products and their configurations...")
    for item in laptop_data:
        # Ensure the brand exists
        # brand, _ = Brand.objects.get_or_create(
        #     title=item["brand"],
        #     title_fa=item["brand"],
        #     slug=item["brand"].lower().replace(" ", "-")
        # )

        # Create the product
        product, created = Product.objects.get_or_create(
            title=item["title"],
            title_fa=item["title"],
            slug=item["title"].replace(" ", "-").lower(),
            category=laptop_category,
            # brand=brand,
            min_price=item["min"],
            max_price=item["max"],  # You can calculate based on configurations if needed
            is_configurable=True
        )
        if created:
            print(f"Created product: {product.title}")
        else:
            print(f"Updated product: {product.title}")

        # Create variants for the product
        for config in item["configs"]:
            # Generate SKU based on configurations
            sku = f"{product.slug}-{config['ram']}-{config['storage']}"
            variant = ProductVariant.objects.create(
                product=product,
                price=0,  # You can adjust the price for each configuration if needed
                sku=sku
            )
            print(f"  Created variant: {variant.sku}")

            # Add configurations to the variant
            for key, value in config.items():
                if key.upper() in configurations_map:  # Ensure key matches configuration key
                    ProductConfiguration.objects.create(
                        variant=variant,
                        configuration=configurations_map[key.upper()],
                        value=value
                    )

    print("Data import completed successfully!")


import_laptop_data()
