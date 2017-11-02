# FSI_Conecta4
Práctica de Heurísticas.

Heurística v.1 --> Se ha modificado el archivo games.py para que, en la poda alfa-beta, "eval_fn" acepte los dos parámetros de la función heurística. Esta versión de la heurística falla a veces, permitiendo el triunfo del jugador humano.

run.py --> Se han implementado los apartados obligatorios de selección de la dificultad (profundidad de búsqueda) y del jugador inicial. Ambas selecciones son posibles mediante dos variables globales creadas.

Versión final (corregida) --> Heurística basada en las posibilidades de cada jugador en hacer 4 en raya. Para ello se aplica la función vista en teoría, h = posibilidad_jugador1 - posibilidad_jugador2. Se añade una sección de código capaz de detectar la victoria o derrota, de forma que se incrementa (o decrementa) la heurística de manera "inifinita". Interfaz de usuario a través de prompt, en la que se puede seleccionar 3 niveles diferentes de dificultad (profundidades 2, 4 y 6) en forma de ajuste global para todas las partidas; al iniciar una partida se da a elegir el jugador inicial.
