from pathlib import Path

nombreFichero = "don_quijote_cap1.txt"

### SIEMPRE IGUAL ####
BASE_DIR = Path(__file__).resolve().parent
fichero = BASE_DIR / f"data/{nombreFichero}"
### SIEMPRE IGUAL ####

with open(fichero, "r", encoding="utf-8") as f:
    contenido = f.read()

print(contenido)

