import random
import json
import gradio as gr

# ===============================
# 🔹 Base de Datos de Personajes
# ===============================

characters = [
    {
        "id": 1,
        "name": "León-O",
        "universe": "ThunderCats",
        "type": "Felino-humanoide",
        "special_attack": "Espada del Augurio – 'Ho!'",
        "prompt": {
            "description": "Cuerpo felino de 2.15m, musculatura potente, pelaje naranja con manchas.",
            "styles": ["hiperrealista", "cinemático", "iluminación dramática"],
            "materials": ["piel", "armadura metálica"],
            "colors": ["anaranjado", "negro"],
            "lighting": "3-point lights con contrastes fuertes",
            "background": "ruinas post-apocalípticas con neblina volumétrica",
            "technical_specs": {
                "camera": "ARRI Alexa 65, 50mm, f/1.4, ISO-800",
                "render": "Unreal Engine 5.3, Lumen GI, ray-tracing"
            }
        }
    },
    {
        "id": 2,
        "name": "Sailor Moon (Usagi Tsukino)",
        "universe": "Sailor Moon",
        "type": "humana cosplay",
        "special_attack": "Moon Tiara Action",
        "prompt": {
            "description": "Cosplay hiperdetallado con coletas largas.",
            "styles": ["hiperrealista", "cosplay fotográfico", "HDR 8K"],
            "materials": ["cuero", "tela", "metal"],
            "colors": ["blanco", "azul", "rojo"],
            "lighting": "iluminación lunar + neón",
            "background": "paisaje urbano en ruinas con chispas eléctricas",
            "technical_specs": {
                "camera": "Hasselblad X1D, 45mm, f/2.0",
                "render": "UE5.3, texturas 32-bit"
            }
        }
    },
    {
        "id": 3,
        "name": "Ryu",
        "universe": "Street Fighter",
        "type": "humano cosplay",
        "special_attack": "Hadouken",
        "prompt": {
            "description": "Karateka musculoso en pose de Hadouken.",
            "styles": ["hiperrealista", "acción dinámica", "HDR"],
            "materials": ["gi de tela blanca"],
            "colors": ["blanco", "rojo"],
            "lighting": "luz dramática contrastante",
            "background": "ruinas urbanas con humo",
            "technical_specs": {
                "camera": "Canon EOS R5 Cine RAW 85mm",
                "render": "UE5 Ray-tracing, partículas dinámicas"
            }
        }
    }
    # 👉 Aquí agregas los demás personajes de KOF, Metal Slug, Darkstalkers, etc.
]

# ===============================
# 🔹 Funciones
# ===============================

def random_character_prompt():
    """
    Retorna un prompt aleatorio basado en la lista de personajes.
    """
    chara = random.choice(characters)
    prompt = f"""
### 🎭 {chara['name']} ({chara['universe']})
**Tipo:** {chara['type']}
**Ataque Especial:** {chara['special_attack']}

**Descripción:** {chara['prompt']['description']}
**Estilos:** {", ".join(chara['prompt']['styles'])}
**Materiales:** {", ".join(chara['prompt']['materials'])}
**Colores:** {", ".join(chara['prompt']['colors'])}
**Iluminación:** {chara['prompt']['lighting']}
**Fondo:** {chara['prompt']['background']}

🔧 **Specs Técnicos**
- Cámara: {chara['prompt']['technical_specs']['camera']}
- Render: {chara['prompt']['technical_specs']['render']}
"""
    return prompt.strip()

def catalog_view(universe):
    """
    Retorna la ficha de todos los personajes de un universo.
    """
    filtered = [ch for ch in characters if ch["universe"] == universe] if universe != "Todos" else characters
    if not filtered:
        return "No hay personajes en este universo."

    out = "## 📖 Catálogo de Personajes\n\n"
    for ch in filtered:
        out += f"""
---
### 🎭 {ch['name']} ({ch['universe']})
- **Tipo:** {ch['type']}
- **Ataque Especial:** {ch['special_attack']}
- **Descripción:** {ch['prompt']['description']}
- **Estilos:** {", ".join(ch['prompt']['styles'])}
- **Escenario:** {ch['prompt']['background']}
"""
    return out

# ===============================
# 🔹 Interfaz en Gradio
# ===============================
def launch_app():
    with gr.Blocks() as demo:
        gr.Markdown("# 🦾 BATUTO-VERSE Prompt Generator")
        gr.Markdown("Genera prompts hiperrealistas de personajes icónicos 🎲")

        with gr.Row():
            random_btn = gr.Button("🎲 Generar Aleatorio", variant="primary")
            universe_dropdown = gr.Dropdown(choices=["Todos", "ThunderCats", "Sailor Moon", "Street Fighter"],
                                            label="📚 Filtrar por Universo", value="Todos")
            catalog_btn = gr.Button("📖 Ver Catálogo")

        output = gr.Markdown("")

        random_btn.click(fn=random_character_prompt, inputs=None, outputs=output)
        catalog_btn.click(fn=catalog_view, inputs=universe_dropdown, outputs=output)

    demo.launch(share=True)

# Ejecutar en Colab/HF
if __name__ == "__main__":
    launch_app()
