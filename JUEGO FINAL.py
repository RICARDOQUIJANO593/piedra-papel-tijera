# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 07:50:05 2025

@author: Ricardo.Quijano
"""

import random

def eleccion_pc():
    opciones = ["piedra", "papel", "tijera"]
    return random.choice(opciones)

def determinar_resultado(eleccion_jugador, eleccion_oponente):
    if eleccion_jugador == eleccion_oponente:
        return "Empate"
    elif (eleccion_jugador == "piedra" and eleccion_oponente == "tijera") or \
         (eleccion_jugador == "papel" and eleccion_oponente == "piedra") or \
         (eleccion_jugador == "tijera" and eleccion_oponente == "papel"):
        return "Ganaste"
    else:
        return "Perdiste"

def jugar():
    print("¡Bienvenido al juego de Piedra, Papel o Tijera!")
    
    print("\nInstrucciones:")
    print("1. Piedra vence a Tijera.")
    print("2. Tijera vence a Papel.")
    print("3. Papel vence a Piedra.")
    print("4. Si ambos jugadores eligen la misma opción, es un empate.")
    print("5. Puedes jugar contra otro jugador o contra la computadora.")
    
    modo = input("\n¿Quieres jugar 1 vs 1 o 1 vs PC? (Escribe '1 vs 1' o '1 vs PC'): ").lower()
    
    if modo == "1 vs 1":
        nombre_jugador1 = input("Ingresa el nombre del Jugador 1: ")
        nombre_jugador2 = input("Ingresa el nombre del Jugador 2: ")
        
        jugadas_jugador1 = 0
        jugadas_jugador2 = 0
        empates = 0
        partidas = int(input("¿Cuántas rondas quieres jugar? "))
        
        for ronda in range(partidas):
            print(f"\nRonda {ronda + 1}:")
            eleccion1 = input(f"{nombre_jugador1}, elige entre piedra, papel o tijera: ").lower()
            eleccion2 = input(f"{nombre_jugador2}, elige entre piedra, papel o tijera: ").lower()
            
            resultado = determinar_resultado(eleccion1, eleccion2)
            
            if resultado == "Ganaste":
                print(f"{nombre_jugador1} ganó esta ronda!")
                jugadas_jugador1 += 1
            elif resultado == "Perdiste":
                print(f"{nombre_jugador2} ganó esta ronda!")
                jugadas_jugador2 += 1
            else:
                print("Esta ronda fue un empate!")
                empates += 1
        
        print(f"\nEstadísticas finales:")
        print(f"{nombre_jugador1} ganó {jugadas_jugador1} veces.")
        print(f"{nombre_jugador2} ganó {jugadas_jugador2} veces.")
        print(f"Hubo {empates} empates.")
    
    elif modo == "1 vs pc":
        nombre_jugador = input("Ingresa tu nombre: ")
        jugadas_ganadas = 0
        jugadas_perdidas = 0
        empates = 0
        partidas = int(input("¿Cuántas rondas quieres jugar? "))
        
        for ronda in range(partidas):
            print(f"\nRonda {ronda + 1}:")
            eleccion_jugador = input(f"{nombre_jugador}, elige entre piedra, papel o tijera: ").lower()
            eleccion_pc_oponente = eleccion_pc()
            
            print(f"La PC eligió: {eleccion_pc_oponente}")
            resultado = determinar_resultado(eleccion_jugador, eleccion_pc_oponente)
            
            if resultado == "Ganaste":
                print("¡Ganaste esta ronda!")
                jugadas_ganadas += 1
            elif resultado == "Perdiste":
                print("La PC ganó esta ronda!")
                jugadas_perdidas += 1
            else:
                print("Esta ronda fue un empate!")
                empates += 1
        
        print(f"\nEstadísticas finales:")
        print(f"{nombre_jugador} ganó {jugadas_ganadas} veces.")
        print(f"La PC ganó {jugadas_perdidas} veces.")
        print(f"Hubo {empates} empates.")
    
    else:
        print("Modo no válido, por favor elige '1 vs 1' o '1 vs PC'.")

jugar()

