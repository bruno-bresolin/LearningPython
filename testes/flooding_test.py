import time
import threading
from scapy.all import IP, UDP, TCP, ICMP, send
import argparse

# Configurações globais
PACOTES_ENVIADOS = 0
TAXA_ENVIO = 1000  # Pacotes por segundo
TESTE_ATIVO = True

# Função para enviar pacotes UDP
def enviar_pacotes_udp(alvo_ip, alvo_porta):
    global PACOTES_ENVIADOS
    while TESTE_ATIVO:
        pacote = IP(dst=alvo_ip) / UDP(dport=alvo_porta)
        send(pacote, verbose=False)
        PACOTES_ENVIADOS += 1

# Função para enviar pacotes TCP
def enviar_pacotes_tcp(alvo_ip, alvo_porta):
    global PACOTES_ENVIADOS
    while TESTE_ATIVO:
        pacote = IP(dst=alvo_ip) / TCP(dport=alvo_porta)
        send(pacote, verbose=False)
        PACOTES_ENVIADOS += 1

# Função para enviar pacotes ICMP (ping)
def enviar_pacotes_icmp(alvo_ip):
    global PACOTES_ENVIADOS
    while TESTE_ATIVO:
        pacote = IP(dst=alvo_ip) / ICMP()
        send(pacote, verbose=False)
        PACOTES_ENVIADOS += 1

# Função para exibir estatísticas
def exibir_estatisticas():
    global PACOTES_ENVIADOS
    while TESTE_ATIVO:
        time.sleep(1)
        print(f"Pacotes enviados: {PACOTES_ENVIADOS}")
        PACOTES_ENVIADOS = 0  # Reseta o contador a cada segundo

# Função principal
def main():
    global TESTE_ATIVO, TAXA_ENVIO

    # Configura o parser de argumentos
    parser = argparse.ArgumentParser(description="Teste de sobrecarga de rede")
    parser.add_argument("--alvo", required=True, help="Endereço IP do alvo")
    parser.add_argument("--porta", type=int, default=80, help="Porta do alvo (para UDP/TCP)")
    parser.add_argument("--protocolo", choices=["udp", "tcp", "icmp"], required=True, help="Protocolo a ser usado")
    parser.add_argument("--taxa", type=int, default=1000, help="Taxa de envio (pacotes por segundo)")
    parser.add_argument("--threads", type=int, default=10, help="Número de threads para envio")
    args = parser.parse_args()

    # Define a taxa de envio
    TAXA_ENVIO = args.taxa

    # Inicia as threads de envio
    threads = []
    for i in range(args.threads):
        if args.protocolo == "udp":
            thread = threading.Thread(target=enviar_pacotes_udp, args=(args.alvo, args.porta))
        elif args.protocolo == "tcp":
            thread = threading.Thread(target=enviar_pacotes_tcp, args=(args.alvo, args.porta))
        elif args.protocolo == "icmp":
            thread = threading.Thread(target=enviar_pacotes_icmp, args=(args.alvo,))
        threads.append(thread)
        thread.start()

    # Inicia a thread de estatísticas
    thread_estatisticas = threading.Thread(target=exibir_estatisticas)
    thread_estatisticas.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nTeste interrompido pelo usuário.")
        TESTE_ATIVO = False

    # Aguarda as threads terminarem
    for thread in threads:
        thread.join()
    thread_estatisticas.join()

if __name__ == "__main__":
    main()