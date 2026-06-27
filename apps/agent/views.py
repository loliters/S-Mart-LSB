from django.shortcuts import render
from django.http import JsonResponse
import random
import json

def consultar_agente(request):
    if request.method == 'POST':
        pregunta = request.POST.get('pregunta', '')
        
        # Simular respuesta de Gemini
        respuestas_posibles = [
            f"La seña para '{pregunta.upper()}' se realiza con la mano derecha en posición vertical...",
            f"Para la letra '{pregunta.upper()}', debes colocar los dedos índice y medio en forma de V...",
            f"El número '{pregunta}' se representa cerrando el puño y extendiendo el pulgar...",
        ]
        respuesta = random.choice(respuestas_posibles)
        
        return JsonResponse({
            'pregunta': pregunta,
            'respuesta': respuesta,
            'confianza': round(random.uniform(0.8, 0.98), 3)
        })
    
    return render(request, 'agent/chat.html')