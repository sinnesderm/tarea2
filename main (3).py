def eliminar_recursion_izquierda(gramatica):
    no_terminales = list(gramatica.keys())
    nueva_gramatica = {}

    for i, A in enumerate(no_terminales):
        # Paso 1: Eliminar recursión directa para A
        producciones_A = gramatica[A]
        alfa, beta = [], []
        
        for prod in producciones_A:
            if prod.startswith(A):
                alfa.append(prod[len(A):])  # Producciones recursivas (A -> Aα)
            else:
                beta.append(prod)           # Producciones no recursivas (A -> β)
        
        if alfa:  # Hay recursión por la izquierda
            nuevo_nt = chr(ord('Z') - i)  # Nuevo no-terminal (ej: Z, Y...)
            nueva_gramatica[A] = [f"{b}{nuevo_nt}" for b in beta]
            nueva_gramatica[nuevo_nt] = [f"{a}{nuevo_nt}" for a in alfa] + ["e"]
        else:
            nueva_gramatica[A] = producciones_A
    
    return nueva_gramatica

def main():
    import sys
    input = sys.stdin.read().splitlines()
    idx = 0
    casos = int(input[idx])
    idx += 1
    
    for _ in range(casos):
        k = int(input[idx])
        idx += 1
        gramatica = {}
        
        for _ in range(k):
            partes = input[idx].split('->')
            nt = partes[0].strip()
            producciones = [p.strip() for p in partes[1].split() if p.strip()]
            gramatica[nt] = producciones
            idx += 1
        
        nueva_gramatica = eliminar_recursion_izquierda(gramatica)
        
        # Imprimir resultados
        for nt in sorted(nueva_gramatica.keys()):
            producciones = " ".join(nueva_gramatica[nt])
            print(f"{nt} -> {producciones}")
        print()  # Separador entre casos

if __name__ == "__main__":
    main()