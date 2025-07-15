def call_center_calcular_eficiencia_tiempo(tiempo_promedio, tiempo_ideal = 300):
    # El tiempo promedio y tiempo ideal se iden en segundos
    eficiencia = (tiempo_ideal / tiempo_promedio) * 100
    return eficiencia

def call_center_calcular_eficiencia_volumen(volumen_llamadas, volumen_esperado = 100):
    # El volumen de llamdas y el volumen esperado se expresan sin su millar 
    # Ejemplo: volumen_esperado = 100000 (100 mil) ingresado como 100
    # Si el empleado atendio 80 mil llamadas: se ingresa 80
    eficiencia = (volumen_llamadas / volumen_esperado) * 100
    return eficiencia

def call_center_calcular_rendimiento(satisfaccion_cliente, tiempo_promedio, volumen_llamadas):
    # La satisfaccion del cliente es dato porcentual (0 - 100): se ingresa el valor numerico
    eficiencia_tiempo = call_center_calcular_eficiencia_tiempo(tiempo_promedio)
    eficiencia_volumen = call_center_calcular_eficiencia_volumen(volumen_llamadas)
    rendimiento = (0.4 * satisfaccion_cliente) + (0.3 * eficiencia_tiempo) + (0.3 * eficiencia_volumen)
    return rendimiento

def calcular_bono_rendimiento(rendimiento, salario_base):
    if rendimiento >= 90:
        return salario_base * 0.2
    elif rendimiento >= 75:
        return salario_base * 0.1
    elif rendimiento >= 60:
        return salario_base * 0.05
    else:
        return 0

def calcular_bono_antiguedad(tiempo_años, salario_base) :
    if tiempo_años >= 10:
        return salario_base * 0.15
    elif tiempo_años >= 5:
        return salario_base * 0.10
    elif tiempo_años >= 2:
        return salario_base * 0.05
    else:
        return 0

def calcular_bono_total(salario_base, rendimiento, tiempo_años):
    bono_r = calcular_bono_rendimiento(rendimiento, salario_base)
    bono_a = calcular_bono_antiguedad(tiempo_años, salario_base)
    total = bono_r + bono_a
    return total, bono_r, bono_a

def mostrar_resultado (nombre, area, salario_base, rendimiento, tiempo_años):
    total, bono_r, bono_a = calcular_bono_total(salario_base, rendimiento, tiempo_años)
    print('\n--- RESULTADO DEL CÁLCULO ---')
    print(f'Empleado: {nombre}')
    print(f'Área: {area}')
    print(f'Salario base: S/ {salario_base:.2f}')
    print(f'Rendimiento: {rendimiento:.2f}% -> Bono por rendimiento: S/{bono_r:.2f}')
    print(f'Antigüedad: {tiempo_años} años -> Bono por antigüedad: S/{bono_a:.2f}')
    print(f'TOTAL BONO A RECIBIR: S/ {total:.2f}')
    print('-----------------------------\n')

def verificar_si_bonifica (numero):
    # Base de datos entregada por el cliente para probar el programa. Los usuarios cuentan con la misma base. La cantidad de digitos en el código indica el area del trabajador: 
    # Contabilidad - 2 digitos, RR.HH - 3 digitos, Administración - 4 digitos, Operaciones - 5 digitos, Marketing - 5 digitos, Callcenter - 6 digitos
    Codigo_de_Trabajadores = [51,56,50,54,53,52,57,58,55,209,210,200
                          ,206,203,202,207,211,205,204,208,212,3476,3461,3468
                          ,3456,3484,44183,44184,44185,44188,44182,44186,44178,44180,555908,555906
                          ,555902,555910,555911,555907,555901,555905,555904,555909,555903,6666033,6666041,6666025
                          ,6666031,6666046,6666036,6666021,6666044,6666049,6666039,6666050,6666023,6666043,6666045,6666020
                          ,6666026,6666048,6666035,6666022,6666028,6666027,6666038,6666032,6666024]

    area_de_trabajo = ['Contabilidad', 'RR.HH', 'Administración',
                       'Operaciones', 'Marketing', 'Callcenter']
    contador = 0

    if numero in Codigo_de_Trabajadores:
        for _ in str(numero):
            contador += 1
        if contador == 2:
            area = area_de_trabajo[0]
            print(f'{area} NO aplica')
            return area
        elif contador == 3:
            area = area_de_trabajo[1]
            print(f'{area} NO aplica')
            return area
        elif contador == 4:
            area = area_de_trabajo[2]
            print(f'{area} NO aplica')
            return area
        elif contador == 5:
            area = area_de_trabajo[3]
            print(f'{area} SI aplica')
            return area
        elif contador == 6:
            area = area_de_trabajo[4]
            print(f'{area} SI aplica')
            return area
        elif contador == 7:
            area = area_de_trabajo[5]
            print(f'{area} SI aplica')
            return area
        else:
            print('Ingrese un número de entres 2 a 7 digitos\n')
    else:
        print('El código no pertenece a un trabajador de la empresa')
        return None

def main():
    while True:
        print("=== MENÚ DE CÁLCULO DE BONOS ===")
        print("1. Calcular bono para un empleado")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "cancelar":
            continue

        if opcion == "1":
            codigo_input = input("Ingrese el código del trabajador(2 a 7 digitos) o 'cancelar': ")
            if codigo_input == "cancelar":
                continue
            elif not codigo_input.isdigit():
                print("Código inválido.\n")
                continue
            codigo = int(codigo_input)

            area = verificar_si_bonifica(codigo)
            if area == 'Callcenter':
                nombre = input("Nombre del trabajador o 'cancelar': ")
                if nombre == "cancelar":
                    continue

                salario_input = input("Ingrese el salario base (S/) o 'cancelar': ")
                if salario_input == "cancelar":
                    continue
                salario = float(salario_input)

                tiempo_input = input("Ingrese el tiempo en la empresa (años) o 'cancelar': ")
                if tiempo_input == "cancelar":
                    continue
                tiempo = int(tiempo_input)

                satisfaccion_input = input("Satisfacción del cliente (0-100) o 'cancelar': ")
                if satisfaccion_input == "cancelar":
                    continue
                satisfaccion = float(satisfaccion_input)

                tiempo_promedio_input = input("Tiempo promedio de llamada (segundos) o 'cancelar': ")
                if tiempo_promedio_input == "cancelar":
                    continue
                tiempo_promedio = float(tiempo_promedio_input)

                volumen_input = input("Volumen de llamadas atendidas o 'cancelar': ")
                if volumen_input == "cancelar":
                    continue
                volumen = int(volumen_input)

                rendimiento = call_center_calcular_rendimiento(satisfaccion, tiempo_promedio, volumen)

            elif area == 'Operaciones' or area == 'Marketing':
                nombre = input("Nombre del trabajador o 'cancelar': ")
                if nombre == "cancelar":
                    continue

                salario_input = input("Ingrese el salario base (S/) o 'cancelar': ")
                if salario_input == "cancelar":
                    continue
                salario = float(salario_input)

                tiempo_input = input("Ingrese el tiempo en la empresa (años) o 'cancelar': ")
                if tiempo_input == "cancelar":
                    continue
                tiempo = int(tiempo_input)

                rendimiento_input = input("Ingrese el rendimiento ya calculado del trabajador (0-100) o 'cancelar': ")
                if rendimiento_input == "cancelar":
                    continue
                rendimiento = float(rendimiento_input)

            elif area in ['Contabilidad', 'Administración', 'RR.HH']:
                continue
            elif area is None:
                continue

            mostrar_resultado(nombre, area, salario, rendimiento, tiempo)

        elif opcion == "2":
            print("Gracias por usar el sistema de cálculo de bonos. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.\n")

main()
