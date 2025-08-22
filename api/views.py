from django.http import JsonResponse
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_json(filename):
    path = os.path.join(BASE_DIR, filename)
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        return data, None
    except FileNotFoundError:
        return None, f"File not found: {path}"
    except json.JSONDecodeError as e:
        return None, f"Invalid JSON in {path}: {str(e)}"

def get_free_medicines(request):
    data, err = load_json("medicines.json")
    if err:
        return JsonResponse({"error": err}, status=404)
    return JsonResponse(data, safe=not isinstance(data, list))

def get_disease_medicines(request):
    data, err = load_json("disease_medicines.json")
    if err:
        return JsonResponse({"error": err}, status=404)
    return JsonResponse(data, safe=not isinstance(data, list))

def get_health_centers(request):
    data, err = load_json("list_of_health_centers.json")
    if err:
        return JsonResponse({"error": err}, status=404)
    return JsonResponse(data, safe=not isinstance(data, list))
