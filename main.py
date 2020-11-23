import json
import os.path

primera_entrada = str(input("""Ingrese acción a realizar:
-Ver estado usuario = a
-Ver cantidad de chocolates restantes = b
-Actualizar listado de usuario/s = c
"""))

chucherias = {"twix": 26,
              "milkyway": 26,
              "milknight": 26,
              "snickers": 26,
              "musketeers": 26,
              }

usuarios = {"Carlitos": {"twix": 0,
                         "milkyway": 0,
                         "milknight": 0,
                         "snickers": 0,
                         "musketeers": 0,
                         },
            "Betania": {"twix": 0,
                        "milkyway": 0,
                        "milknight": 0,
                        "snickers": 0,
                        "musketeers": 0,
                        },
            "Albert": {"twix": 0,
                       "milkyway": 0,
                       "milknight": 0,
                       "snickers": 0,
                       "musketeers": 0,
                       },
            "Papá": {"twix": 0,
                     "milkyway": 0,
                     "milknight": 0,
                     "snickers": 0,
                     "musketeers": 0,
                     },
            "Mamá": {"twix": 0,
                     "milkyway": 0,
                     "milknight": 0,
                     "snickers": 0,
                     "musketeers": 0,
                     },
            }


if not os.path.exists("datos.json"):
    with open("datos.json", "w") as write_file:
        json.dump(chucherias, write_file)

if not os.path.exists("usuarios.json"):
    with open("usuarios.json", "w") as write_file:
        json.dump(usuarios, write_file)


def modify(user, chuche, integer, file1, file2):
    file2[user][chuche] += integer
    file1[chuche] -= integer
    return "Acción completada"

while True:

    with open("datos.json", "r") as read_file:
        datos_chuches = json.load(read_file)

    if "a" in primera_entrada:
        try:
            with open("usuarios.json", "r") as read_file:
                datos_usuarios = json.load(read_file)
            for i, k in datos_usuarios[str(input("Ingrese usuario:\n"))].items():
                print(i, " = ", k)
        except (TypeError, KeyError, ValueError, IndexError):
            print("Entrada incorrecta, intente de nuevo")
            continue

    elif "b" in primera_entrada:
        print("Los chocolates restantes son: \n")
        for d, q in datos_chuches.items():
            if q == 0:
                print(d, " = ", "Vacio")
            else:
                print(d, " = ", q)
        print("\n" + "La cantidad total es: ", sum(datos_chuches.values()))

    elif "c" in primera_entrada:
        usuario = str(input("Ingrese usuario: "))
        nombre = str(input("Ingrese chucheria: "))
        num = input("Ingrese cantidad: ")

        try:
            with open("usuarios.json", "r+") as file:
                datos_usuarios = json.load(file)
                print(modify(usuario, nombre, num, datos_chuches, datos_usuarios))
                file.seek(0)
                file.write(json.dumps(datos_usuarios))
                file.truncate()

            with open("datos.json", "r+") as file:
                chucherias = json.load(file)
                modify(usuario, nombre, num, chucherias, datos_usuarios)
                file.seek(0)
                file.write(json.dumps(chucherias))
                file.truncate()
        except (IndexError, TypeError, KeyError, ValueError):
            print("Entrada incorrecta, intente de nuevo")
            continue

    break
