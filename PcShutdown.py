# Shutdown Pc Temporizzato
# Mauro De Filippis
# mauro.defilippis1978@gmail.com
# 10/11/2025

import os
import time

# ─── CONFIGURAZIONE ──────────────────────────────────────────────
RITARDO_MINUTI = 1  # Minuti di attesa prima dello spegnimento
# ─────────────────────────────────────────────────────────────────


def spegni_pc():
    """
    Esegue lo spegnimento del sistema operativo dopo un ritardo configurabile.
    """
    ritardo_secondi = RITARDO_MINUTI * 60
    
    print(f"🕐 Spegnimento programmato tra {RITARDO_MINUTI} minuti ({ritardo_secondi} secondi)...")
    print(f"⏳ Countdown avviato...\n")
    
    # Countdown con visualizzazione dei secondi rimanenti
    for secondi_rimanenti in range(ritardo_secondi, 0, -1):
        minuti = secondi_rimanenti // 60
        secondi = secondi_rimanenti % 60
        print(f"\r⏱️  Spegnimento tra: {minuti:02d}:{secondi:02d}  ", end="", flush=True)
        time.sleep(1)
    
    print("\n")  # Vai a capo dopo il countdown
    
    # Determina il sistema operativo in uso
    if os.name == 'nt':
        # Per Windows (NT = New Technology)
        # /s = shutdown, /t 0 = tempo di attesa 0 secondi
        comando = 'shutdown /s /t 0'
    elif os.name == 'posix':
        # Per Linux o macOS (POSIX = Portable Operating System Interface)
        # 'now' spegne immediatamente. Richiede permessi di superutente.
        comando = 'sudo shutdown now'
    else:
        print("❌ Sistema operativo non supportato per lo spegnimento automatico.")
        return
    
    # Esegue il comando di spegnimento
    print(f"🔌 Esecuzione del comando: {comando}")
    try:
        os.system(comando)
    except Exception as e:
        print(f"❌ Errore durante l'esecuzione del comando: {e}")


if __name__ == "__main__":
    spegni_pc()