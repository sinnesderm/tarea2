# ST0270 - Asignación 2: Eliminación de Recursión Izquierda

## Información del Estudiante
- **Nombre completo**: Steven Granda Palencia
- **Número de clase**: ST0270
- **Sistema Operativo**: Ubuntu 22.04 LTS
- **Lenguaje de programación**: Python 3.10.12
- **Herramientas**: VS Code, Git

## Descripción
Implementación del algoritmo de eliminación de recursión izquierda basado en Aho et al. (2006), Sección 4.3.3, para gramáticas libres de contexto.

---

## 🚀 Instrucciones de Ejecución

### Requisitos
- Python 3.x instalado
- Terminal de línea de comandos

## Casos De Prueba
### 1)
1
1
S -> Sa b
salida:
S -> bZ 
Z -> aZ e

### 2)
1
2
S -> Aa b
A -> Ac Sd m
salida:
S -> Aa b 
A -> mZ SdZ 
Z -> cZ e

### Ejecución básica
```bash
# Ejecutar con entrada manual
python3 eliminar_recursion.py

# Ejecutar con archivo de entrada
python3 eliminar_recursion.py < input.txt# tarea2

# Ejecutar todos los casos de prueba
chmod +x test.sh
./test.sh

