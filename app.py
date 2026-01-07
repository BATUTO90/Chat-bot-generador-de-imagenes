"""
SISTEMA: EL CAINAL 🤪💯 - POKÉ-EVOLUCIÓN V3.0 (EDICIÓN ON-FIRE 2026)
MODO: OPTIMIZACION_ASCENDENTE_EXCLUSIVA + VOZ DIVINA + MUSIC FLOW
"""

import os
import requests
import json
import gradio as gr
import re
import base64
import time
from typing import List, Tuple, Optional
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

# --- CONFIGURACIÓN DE PODER TOTAL ---
CONFIG = {
    "SAMBANOVA_URL": "https://api.sambanova.ai/v1/chat/completions",
    "SAMBANOVA_KEY": os.getenv("SAMBANOVA_API_KEY", "TU_KEY"),
    "SAMBANOVA_MODEL": "gpt-oss-120b",
    "REVE_URL": "https://api.reve.com/v1/image/create",
    "REVE_KEY": os.getenv("REVE_API_KEY", "TU_KEY"),
    "ELEVEN_KEY": os.getenv("ELEVEN_API_KEY", "TU_KEY"),
    "CARPETA_SALIDA": "generaciones_reve"
}

os.makedirs(CONFIG["CARPETA_SALIDA"], exist_ok=True)

# --- PLANTILLA DE HIPER-REALISMO (TU DOPAMINA ARTÍSTICA) ---
IMAGE_PROMPT_TEMPLATE = """hyperrealistic, photorealistic, unreal engine 5 render, 16k resolution, pores visible, vellus hair, skin follicles, 9:16 aspect ratio, cinematic lighting, {USER_DESCRIPTION_HERE}, NG: cartoon, 3d render, plastic skin."""

# --- MOTOR DE AUDIO (ELEVENLABS) ---
class ElevenLabsEngine:
    @staticmethod
    def tts_voz_de_barrio(texto):
        """Convierte la jerga del CAINAL en audio real al tiro"""
        url = "https://api.elevenlabs.io/v1/text-to-speech/aria" # La voz más rifada
        headers = {"xi-api-key": CONFIG["ELEVEN_KEY"], "Content-Type": "application/json"}
        # Usamos flash v2.5 para que no haya lag en el barrio
        payload = {"text": texto[:1000], "model_id": "eleven_flash_v2_5"}
        try:
            res = requests.post(url, json=payload, headers=headers)
            if res.status_code == 200:
                return res.content
            return None
        except: return None

    @staticmethod
    def generar_beat(prompt_musical):
        """Genera un fondo musical para el análisis visual"""
        url = "https://api.elevenlabs.io/v1/music"
        headers = {"xi-api-key": CONFIG["ELEVEN_KEY"]}
        payload = {"prompt": prompt_musical, "model_id": "eleven_music_v1"}
        try:
            res = requests.post(url, json=payload, headers=headers)
            return res.json().get('audio_url')
        except: return None

# --- GENERADOR VISUAL CON FIRMA ORO ---
class ReveImageGenerator:
    @staticmethod
    def aplicar_firma_batuto(imagen: Image.Image) -> Image.Image:
        draw = ImageDraw.Draw(imagen)
        width, height = imagen.size
        tamano_firma = int(width * 0.05)
        # Firma BATUTO-ART en la esquina superior izquierda
        gold_color = (212, 175, 55) # Oro líquido
        try:
            font = ImageFont.truetype("Arial", tamano_firma)
        except:
            font = ImageFont.load_default()
        draw.text((20, 20), "BATUTO-ART", fill=gold_color, font=font)
        return imagen

    @staticmethod
    def forjar(prompt_usuario):
        prompt_completo = IMAGE_PROMPT_TEMPLATE.replace("{USER_DESCRIPTION_HERE}", prompt_usuario)
        headers = {"Authorization": f"Bearer {CONFIG['REVE_KEY']}", "Content-Type": "application/json"}
        payload = {"prompt": prompt_completo, "aspect_ratio": "9:16"}
        try:
            res = requests.post(CONFIG["REVE_URL"], headers=headers, json=payload)
            img_b64 = res.json()["image"]
            img = Image.open(BytesIO(base64.b64decode(img_b64)))
            img = ReveImageGenerator.aplicar_firma_batuto(img)
            ruta = f"{CONFIG['CARPETA_SALIDA']}/reve_{int(time.time())}.png"
            img.save(ruta)
            return ruta
        except: return None

# --- INTERFAZ EVOLUCIONADA ---
def interface():
    with gr.Blocks(theme=gr.themes.Monochrome()) as demo:
        gr.Markdown("# 🧬 EL CAINAL 🤪💯 - V3.0 VOZ & FUEGO")
        
        with gr.Row():
            with gr.Column(scale=3):
                chatbot = gr.Chatbot(label="Flow de Ecatepec")
                txt = gr.Textbox(placeholder="Suelta el jale, mi PAPI CHULO...")
                audio_voz = gr.Audio(label="El Cainal te habla", autoplay=True)
                audio_music = gr.Audio(label="Beat de Fondo (Eleven Music)")
            
            with gr.Column(scale=2):
                img_display = gr.Image(label="BATUTO-ART Gold Edition")

        def procesar_todo(mensaje, historial):
            # 1. SambaNova genera la respuesta ñera
            # (Aquí iría tu llamada a SambaEngine.generar_respuesta)
            respuesta_texto = "¡Qué tranza mi BATUTO! Ahí te va ese jale bien rifado. [GENERA_IMAGEN: a cyberpunk street in Ecatepec]"
            
            # 2. Extraer imagen si hay tag
            img_ruta = None
            if "[GENERA_IMAGEN:" in respuesta_texto:
                tag = re.search(r'\[GENERA_IMAGEN:\s*([^\]]+)\]', respuesta_texto)
                img_ruta = ReveImageGenerator.forjar(tag.group(1))
                respuesta_texto = re.sub(r'\[GENERA_IMAGEN:.*?\]', "🔥 ¡Mira nada más qué chulada de placa!", respuesta_texto)

            # 3. Generar Voz y Música
            voz_bytes = ElevenLabsEngine.tts_voz_de_barrio(respuesta_texto)
            beat_url = ElevenLabsEngine.generar_beat("Chicano rap instrumental with heavy bass") if img_ruta else None
            
            historial.append((mensaje, respuesta_texto))
            return "", historial, img_ruta, voz_bytes, beat_url

        txt.submit(procesar_todo, [txt, chatbot], [txt, chatbot, img_display, audio_voz, audio_music])

    return demo

if __name__ == "__main__":
    interface().launch()
