from typing import Any
from blog.models import Post,Category
from django.core.management.base import BaseCommand

import random

    
class Command(BaseCommand):
    
    help = "This command insert post data"
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        #delete existing data
        Post.objects.all().delete()
        
        
        
        
        
        titles = [
            
            "A Beginner's Guide to JavaScript",
            "Top 5 Coding Tips for Beginners",
            "Understanding React Components: A Simple Breakdown",
            "How to Build a To-Do List App in JavaScript",
            "Why Learning HTML & CSS is Essential for Web Development",
            "Mastering Arrays in JavaScript: Common Methods Explained",
            "5 Projects Every Front-End Developer Should Try",
            "How to Create a Responsive Portfolio with React",
            "An Easy Approach to State Management in React",
            "How to Use Flexbox for Responsive Layouts",
        ]

        contents = [
            
           "Learn the basics of JavaScript, including key concepts like variables, loops, and functions.",

            "Practice coding daily and break down problems into smaller, more manageable tasks.",

            "Understand how React components work and how to build a UI using functional components.",

            "Create a simple to-do list app with JavaScript, allowing users to add, delete, and mark tasks as done.",

            "Learn how HTML structures a webpage and how CSS styles it for an attractive design.",

            "Explore JavaScript array methods like map() and filter() to manipulate data efficiently.",

            "Build essential front-end projects to practice your skills, like a portfolio or a weather app.",

            "Create a responsive portfolio with React, utilizing components and styling with CSS.",

            "Manage state in React using hooks like useState to handle data flow and updates.",

            "Learn Flexbox to easily create responsive web layouts with minimal CSS code.",
        ]

        img_urls = [
            
            "https://picsum.photos/id/1/800/400",
            
            "https://picsum.photos/id/2/800/400",
             
            "https://picsum.photos/id/3/800/400",
            
            "https://picsum.photos/id/4/800/400",
            
            "https://picsum.photos/id/5/800/400",
            
            "https://picsum.photos/id/6/800/400",
            
            "https://picsum.photos/id/7/800/400",
            "https://picsum.photos/id/8/800/400",
            "https://picsum.photos/id/9/800/400",
            "https://picsum.photos/id/10/800/400",
        ]

        categories = Category.objects.all()
        for title,content,img_url in zip(titles,contents,img_urls):
            
            category = random.choice(categories)
            
            Post.objects.create(title=title,content=content,img_url=img_url,category = category)
        
        self.stdout.write(self.style.SUCCESS("completed inserting data"))    
                
    