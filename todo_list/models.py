from django.db import models

class Todo(models.Model):
    # null=True allows null in the field
    # blank=True allows not giving a value at creation
    # db_index=True creates an index on the field
    order_index = models.IntegerField(
        null=True, blank=True, db_index=True
    )
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.order_index is None:
            last = Todo.objects.order_by("-order_index").first()
            self.order_index = (last.order_index + 1) if last else 0

        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"({'X' if self.completed else ' '}) {self.description}"
    
    # This specifies the default ordering 
    # for queries of this model. 
    # notice the class definition is inside the Todo class
    class Meta:
        ordering = ["order_index"]
