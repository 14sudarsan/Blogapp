from typing import Any
from blog.models import Category
from django.core.management.base import BaseCommand



    
class Command(BaseCommand):
    
    help = "This command insert post data"
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        #delete existing data
        Category.objects.all().delete()
        
        categories = ['sports','Technology','Science','Art','Food']
        
        
        
        

        for category_name in categories:
            
            Category.objects.create(name = category_name)
        
        self.stdout.write(self.style.SUCCESS("completed inserting data"))    
                