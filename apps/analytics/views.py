from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import random
import json

def get_stats(request):
    # Datos simulados de BigQuery
    stats = {
        'total_videos': 142,
        'total_clases': 36,  # 26 letras + 10 números
        'precision_promedio': round(random.uniform(0.85, 0.95), 3),
        'tiempo_entrenamiento': '2h 15m',
        'clases_mas_comunes': [
            {'letra': 'A', 'count': 12},
            {'letra': 'B', 'count': 11},
            {'letra': 'C', 'count': 10},
            {'letra': '5', 'count': 9},
        ]
    }
    return JsonResponse(stats)

def dashboard_analytics(request):
    return render(request, 'analytics/dashboard.html')