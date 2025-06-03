# import pprint

# data_compleja = {
#     "nombre": "Alice",
#     "edad": 30,
#     "ciudades_visitadas": [
#         {"nombre": "París", "pais": "Francia", "anos": [2018, 2022]},
#         {"nombre": "Tokio", "pais": "Japón", "anos": [2019]},
#         {"nombre": "Roma", "pais": "Italia", "anos": [2021, 2023, 2024]},
#     ],
#     "preferencias": {
#         "comida": ["italiana", "japonesa"],
#         "bebida": "café"
#     }
# }

# print("--- Salida con print() ---")
# print(data_compleja)
# print("\n--- Salida con pprint() ---")
# pprint.pprint(data_compleja)

import sqlite3
import pprint

# ... (código de base de datos idéntico al anterior) ...
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE usuarios (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        email TEXT,
        configuracion_perfil TEXT
    )
''')
cursor.execute("INSERT INTO usuarios VALUES (1, 'Ana', 'ana@email.com', '{\"tema\": \"oscuro\", \"notificaciones\": {\"email\": true, \"sms\": false}}')")
cursor.execute("INSERT INTO usuarios VALUES (2, 'Luis', 'luis@email.com', '{\"tema\": \"claro\", \"notificaciones\": {\"email\": false, \"sms\": true}, \"idioma\": \"es\"}')")
cursor.execute("INSERT INTO usuarios VALUES (3, 'Marta', 'marta@email.com', '{\"tema\": \"verde\", \"notificaciones\": {\"email\": true, \"sms\": true}, \"privacidad\": {\"compartir_datos\": false}}')")
conn.commit()
cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()

print("\n--- Salida con pprint() para resultados de DB ---")
pprint.pprint(usuarios)

conn.close()