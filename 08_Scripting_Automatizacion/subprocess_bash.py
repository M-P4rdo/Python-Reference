#---------- Automatización de Terminal ----------
import subprocess
import os

#(Comando en Terminal):
comando = "dir" if os.name == "nt" else "ls"
resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
print("Salida del comando:", resultado.stdout)

#(Script Bash):
proceso = subprocess.run(["bash", "script.sh"], capture_output=True, text=True)
print(f"Salida del script: {proceso.stdout}")

#(Capturar Salida):
salida = subprocess.check_output("pwd", shell=True, text=True)
print(f"Directorio actual: {salida.strip()}")

#(Segundo Plano):
proceso = subprocess.Popen(["ping", "-c", "4", "google.com"], stdout=subprocess.PIPE, text=True)
for linea in proceso.stdout:
    print(linea.strip())

#(Errores):
try:
    subprocess.run(["python3", "--version"], check=True)
except subprocess.CalledProcessError:
    print("Error al ejecutar el comando")