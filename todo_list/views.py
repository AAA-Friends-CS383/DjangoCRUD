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

@csrf_exempt
def todo_detail(request, id):
    try:
        todo = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        return JsonResponse({"error": "Not found"}, status=404)

    if request.method == "DELETE":
        todo.delete()
        return JsonResponse({"deleted": True})

    if request.method == "PATCH":
        data = json.loads(request.body)

        if "description" in data:
            todo.description = data["description"]
        if "completed" in data:
            todo.completed = data["completed"]

        todo.save()

        return JsonResponse({
            "id": todo.id,
            "description": todo.description,
            "completed": todo.completed,
            "order_index": todo.order_index,
        })

    return HttpResponseNotAllowed(["PATCH", "DELETE"])

@csrf_exempt
def toggle_todo(request, id):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    try:
        todo = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        return JsonResponse({"error": "Not found"}, status=404)

    todo.completed = not todo.completed
    todo.save()

    return JsonResponse({
        "id": todo.id,
        "completed": todo.completed
    })

@csrf_exempt
def reorder_todos(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    try:
        ordered_ids = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    if not isinstance(ordered_ids, list):
        return JsonResponse({"error": "Expected a list of IDs"}, status=400)

    # Optional: ensure no duplicates / invalid types
    if len(set(ordered_ids)) != len(ordered_ids):
        return JsonResponse({"error": "Duplicate IDs not allowed"}, status=400)

    # Fetch all todos in one query
    todos = Todo.objects.filter(id__in=ordered_ids)

    # Ensure all IDs exist
    existing_ids = set(t.id for t in todos)
    if existing_ids != set(ordered_ids):
        return JsonResponse({"error": "Some IDs do not exist"}, status=400)

    # dictionary comprehension for fast lookup (like a list comprehension)
    todo_map = {t.id: t for t in todos}

    # Reassign order_index based on frontend order
    for index, todo_id in enumerate(ordered_ids, start=1):
        todo_map[todo_id].order_index = index

    # Bulk update (efficient single database operation)
    Todo.objects.bulk_update(todo_map.values(), ["order_index"])

    return JsonResponse({"status": "ok", "updated": len(ordered_ids)})
