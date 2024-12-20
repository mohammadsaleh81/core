from taxonomy.models import Category, Brand, Tag


def get_root_categories(organization):
    return Category.get_root_nodes().filter(organ=organization).select_related('organ')


def get_child_categories(parent_category, organization):
    return parent_category.get_children().filter(organ=organization).select_related('organ')


def get_category_configurations(category, organization):
    return category.get_all_configurations().filter(organ=organization).select_related('organ')


def get_category(cat_id, organization):
    return Category.objects.filter(id=cat_id, organ=organization).first()


def get_child_categories_by_id(organization, parent_id=None):
    parent = get_category(parent_id, organization)
    return parent.get_children().filter(organ=organization).select_related('organ')


def get_brands(organization):
    return Brand.objects.filter(organ=organization).select_related('organ')



def get_brand_by_id(organization, brand_id):
    return Brand.objects.filter(organ=organization, id=brand_id).first()


def get_tags(organization):
    return Tag.objects.filter(organ=organization)
