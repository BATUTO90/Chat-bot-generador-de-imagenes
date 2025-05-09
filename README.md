# Chat-bot-generador-de-imagenes

Este proyecto es un chatbot que genera imágenes automáticamente usando **Stable Diffusion**.  
El bot responde a cualquier petición del usuario generando una imagen en un estilo **ultra realista**, con iluminación cinematográfica, render tipo **Unreal Engine 5** y alto nivel de detalle.

## ¿Cómo funciona?

1. El usuario escribe cualquier texto al chatbot.
2. El bot toma ese texto y lo convierte en una imagen usando la API de Stable Diffusion.
3. Todas las imágenes generadas tendrán el siguiente estilo fijo:
   - ultra-realistic
   - cinematic lighting
   - Unreal Engine 5 render
   - high detail
4. **Las imágenes se generan en formato 9:16** (vertical), ideales para usarlas como fondos de pantalla de celular.

## ¿Cómo usarlo?

1. Clona este repositorio o descárgalo.
2. Instala las dependencias necesarias (por ejemplo, `requests` si usas Python).
3. Coloca tu **API key** de Stable Diffusion en un archivo llamado `.env` o `sai_platform_key.txt` (según cómo lo uses).
4. Ejecuta el bot y escribe cualquier texto para recibir una imagen generada.

## Ejemplo de prompt usado

El bot siempre añade el estilo al prompt del usuario.  
Por ejemplo, si el usuario escribe:  
> Un perro en la nieve

El prompt enviado a Stable Diffusion será:  
> Un perro en la nieve, ultra-realistic, cinematic lighting, Unreal Engine 5 render, high detail

## Configuración de la API Key

Crea un archivo `.env` o `sai_platform_key.txt` y coloca tu API key de Stable Diffusion así:

