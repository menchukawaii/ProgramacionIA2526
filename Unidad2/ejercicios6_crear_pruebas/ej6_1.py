def clasificar_persona(edad, estado_civil):
    if edad < 18:
        return "Menor de edad"
    elif edad >= 18 and edad <= 65:
        if estado_civil == "soltero":
            return "Adulto soltero"
        elif estado_civil == "casado":
            return "Adulto casado"
        else:
            return "Estado civil desconocido"
    else:
        return "Persona mayor"


personas = [[17, "soltero"], [15, "casado"], [15, ""],
            [25, "soltero"], [45, "casado"], [65, "adfghjhk"],
            [66, "soltero"], [88, "casado"], [100, "12347"],
            [0, "casado"], [-5, "casado"], [275, "casado"]]
resultados = ["Menor de edad", "Menor de edad", "Menor de edad",
              "Adulto soltero", "Adulto casado", "Estado civil desconocido",
              "Persona mayor", "Persona mayor", "Persona mayor",
              "Menor de edad", "ERROR: EDAD NEGATIVA", "ERRROR: PERSONA MUY MAYOR"]

for i in range(len(personas)):
    edad = personas[i][0]
    estado_civil = personas[i][1]
    if clasificar_persona(edad, estado_civil) == resultados[i]:
        print("CORRECTO")
    else:
        print(f"edad: {edad} estado civil: {estado_civil} {resultados[i]}")
