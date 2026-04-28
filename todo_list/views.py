import json
from django.http import JsonResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Todo

def index(request):
    return render(request, "todo_list/index.html")

# In a production app, you should not use @csrf_exempt.
# It disables Django's CSRF (Cross-Site Request Forgery) 
# protection and makes POST/PUT/PATCH/DELETE requests
# not require a CSRF token. Without @csrf_exempt, you'd
# need to add a `"X-CSRFToken": token` to your fetches
@csrf_exempt
def todos_collection(request):
    if request.method == "GET":
        todos = list(Todo.objects.values())
        return JsonResponse(todos, safe=False)

    if request.method == "POST":
        data = json.loads(request.body)

        todo = Todo.objects.create(
            description=data.get("description", ""),
        )

        return JsonResponse({
            "id": todo.id,
            "description": todo.description,
            "completed": todo.completed,
            "order_index": todo.order_index,
        })

    return HttpResponseNotAllowed(["GET", "POST"])
