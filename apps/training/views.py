from django.shortcuts import render
from django.http import JsonResponse
import numpy as np
import pandas as pd
import random
import time
import json

# Datos simulados de entrenamiento (pérdida y precisión)
def simular_entrenamiento(epochs=50):
    history = {
        'loss': [],
        'accuracy': [],
        'val_loss': [],
        'val_accuracy': []
    }
    # Simular mejora gradual
    for epoch in range(1, epochs + 1):
        loss = 2.0 / (epoch + 1) + random.uniform(-0.1, 0.1)
        acc = 0.95 * (1 - np.exp(-epoch / 20)) + random.uniform(-0.02, 0.02)
        val_loss = loss * (1 + random.uniform(-0.1, 0.1))
        val_acc = acc * (1 + random.uniform(-0.05, 0.05))
        
        history['loss'].append(max(0.1, loss))
        history['accuracy'].append(min(0.99, acc))
        history['val_loss'].append(max(0.1, val_loss))
        history['val_accuracy'].append(min(0.99, val_acc))
    
    return history

def iniciar_entrenamiento(request):
    if request.method == 'POST':
        epochs = int(request.POST.get('epochs', 50))
        history = simular_entrenamiento(epochs)
        
        # Guardar en sesión para mostrar después
        request.session['training_history'] = history
        
        return JsonResponse({
            'status': 'completado',
            'history': history
        })
    return JsonResponse({'error': 'Método no permitido'}, status=405)

def dashboard_entrenamiento(request):
    history = request.session.get('training_history', None)
    return render(request, 'training/dashboard.html', {'history': history})