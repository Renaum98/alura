import subprocess

def flush_dns():
    try:
        # Executa o comando ipconfig /flushdns
        subprocess.run(["ipconfig", "/flushdns"], check=True)
        print("Cache DNS limpo com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao tentar limpar o cache DNS: {e}")

# Chama a função para limpar o cache DNS
flush_dns()