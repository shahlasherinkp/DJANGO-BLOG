import random
import string

from django.utils.text import slugify


def generate_unique_slug(instance,base_little, new_slug=False, update=False):
    slug = slugify(base_little)
    model = instance.__class__

    if new_slug:
        slug = new_slug

    if update:

        slug_exists = model.objects.filter(
        slug_icontains = slug

    ).exclude(pk=instance.pk)

    else:
        slug_exists = model.objects.filter(
        slug_icontains=slug
        ).exists()

    if slug_exists:
        random_string = "".join(random.choice(string.ascii_lowercase, k=4))
        new = slugify(base_little + '-' + random_string)
        return generate_unique_slug(
            instance,
            base_little,
            new_slug=new

        )

    return slug
        