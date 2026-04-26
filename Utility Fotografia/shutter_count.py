# Restituisce il numero di scatti fatti con una macchina nikon
# a partire dai dati exif contenuti nell afoto.
#
# necessita pip install exifread
#
# Mauro De Filippis
# mauro.defilippis1978@gmail.com
# 26/04/2026

import exifread
import sys

def get_nikon_shutter_count(image_path):
    try:
        with open(image_path, 'rb') as f:
            # Estrae i tag EXIF dal file
            tags = exifread.process_file(f)
            
            # Nikon usa solitamente questi nomi per il conteggio scatti
            possible_tags = [
                'MakerNote TotalShutterReleases',
                'MakerNote ShutterCount',
                'Image ImageNumber'
            ]
            
            for tag_name in possible_tags:
                if tag_name in tags:
                    return tags[tag_name]
            
            return "Tag non trovato. Assicurati che sia un file originale Nikon."
            
    except FileNotFoundError:
        return "Errore: File non trovato."
    except Exception as e:
        return f"Errore imprevisto: {e}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Utilizzo: python shutter_count.py percorso/della/tua/foto.nef")
    else:
        path = sys.argv[1]
        scatti = get_nikon_shutter_count(path)
        print(f"--- Risultato per: {path} ---")
        print(f"Numero totale di scatti: {scatti}")
