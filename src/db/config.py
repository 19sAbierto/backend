from django.db import models


class BaseModel(models.Model):
    """An abstract base class model that provides self-updating `created` and
    `modified` fields, along with some methods for uniquely identifying instances.
    """
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True
