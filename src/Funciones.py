
def mostrar_ranking_despues_de_ronda(ranking):
    
    print(f"{'Jugador':<8}{'Kills':<8}{'Asistencias':<14}{'Muertes':<12}{'MVPs':<8}{'Puntos':<10}")

    print("-" * 60)

    for nombre, stats in ranking:
        print(f"{nombre:<10}{stats['kills']:<12}{stats['assists']:<12}{stats['deaths']:<10}{stats['MVPs']:<8}{stats['points']:<8}")
    
    print("-" * 60)

def ordenar_rankings(ranking):
    return sorted(ranking, key=lambda x: x[1]['points'], reverse=True)



def procesar_actualizar_rankings(rounds, puntos_kill, puntos_assist, puntos_death):
    
    # Inicializar estructura de jugadores
    jugadores = {}

    # Procesar cada ronda
    for i, ronda in enumerate(rounds, start=1):
        mvp_actual = None
        max_puntos = float('-inf')

        for jugador, stats in ronda.items():
            kills = stats['kills']

            assists = stats['assists']

            if stats['deaths']:
                deaths = 1
            else:
                deaths = 0

            puntos = (kills * puntos_kill) + (assists * puntos_assist) + (deaths * puntos_death)

            #Inicializamos 
            if jugador not in jugadores:
                jugadores[jugador] = {'kills': 0, 'assists': 0, 'deaths': 0, 'MVPs': 0, 'points': 0}

            # Actualizar estadísticas del jugador
            jugadores[jugador]['kills'] += kills
            jugadores[jugador]['assists'] += assists
            jugadores[jugador]['deaths'] += deaths
            jugadores[jugador]['points'] += puntos

            # Determinar MVP de la ronda
            if puntos > max_puntos:
                max_puntos = puntos
                mvp_actual = jugador

        # Asignamos MVP
        jugadores[mvp_actual]['MVPs'] += 1

        # Ordenar ranking manualmente
        rankingg = list(jugadores.items())
        ranking = ordenar_rankings(rankingg)

        # Mostrar ranking después de la ronda
        if i < 5:
            print(f"\nRanking ronda {i}:")
            mostrar_ranking_despues_de_ronda(ranking)
    
    print(f"\nRanking ronda {i} y ranking final:")
    mostrar_ranking_despues_de_ronda(ranking)









    


