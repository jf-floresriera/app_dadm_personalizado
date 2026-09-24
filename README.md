# App DADM Personalizada 🎨🦦🐎

Bienvenido a la evolución definitiva de la aplicación: **App DADM Personalizada**. En este nuevo repositorio hemos llevado el desarrollo a un nivel más avanzado integrando una arquitectura de **Temáticas Dinámicas (Theme Switching)** usando Custom Views y Sound Management.

## 🚀 ¿Qué se agregó en esta versión personalizada?

### 1. Sistema Multi-Temáticas (4 en 1)
Ahora el usuario puede cambiar toda la experiencia gráfica y auditiva en tiempo real a través del menú de opciones.
*   🔵 **Tema Clásico:** El tradicional juego de 'X' contra 'O' con sonidos de espada y deslizamiento (Sword & Swish).
*   🏖️ **Tema Costa:** Relájate en la playa con **Conchas Marinas (🐚)** vs **Estrellas de Mar (⭐)**.
*   🇻🇪 **Tema Llanos:** Una experiencia con mucho joropo y tradición: **Chigüire (🦦)** vs **Maracas (🪇)**.
*   🤠 **Tema Vaquero (Country):** Un duelo en el viejo oeste usando **Sombreros Vaqueros (🤠)** y **Herraduras (🐎)**.

### 2. Actualización Dinámica del Menú
* Renombramos la opción "Temática" a **"Tema"** y diseñamos un nuevo Icono personalizado de **Paleta de Colores (`ic_theme_palette.xml`)** más profesional. 

---
## 🔊 Explicación Técnica: ¿Por qué no suenan los Audios? (Guía de Estudio)

Si descargas el proyecto, te darás cuenta de que **los audios no suenan (están en silencio)**. No es un error en el código, es una limitación técnica de red y una excelente oportunidad de aprendizaje sobre los "Placeholders".

### El Problema de Red (Bloqueos)
Al desarrollar este proyecto usando comandos automáticos para descargar música o efectos (.wav o .mp3) directamente desde repositorios crudos en internet hacia tu proyecto de Android Studio, las terminales devolvieron errores de servidor como **"404 Not Found"** o **"400 Bad Request"** (Android y PowerShell bloquean descargas no autorizadas).
Si una app en Android no encuentra un archivo declarado en la carpeta `res/raw`, ¡el código falla y no compila!

### La Solución y lo que debes hacer
Para asegurar que tu aplicación se pueda compilar, instalé pequeños archivos `.wav` de 0 segundos de duración, generados mediante Base64. Es decir, los archivos "físicos" sí existen en tu carpeta (para engañar al compilador y permitir que funcione el `MediaPlayer`), pero **están en blanco**.

**Para escuchar los sonidos en tu proyecto local y celular**, debes hacer lo siguiente manualmente:
1.  Busca y descarga en tu computadora 6 sonidos muy cortos (menos de 2 segundos) en formato `.mp3` o `.wav`.
2.  Renómbralos exactamente así:
    *   `sword.wav` y `swish.wav` (Para clásico).
    *   `wave_sound.wav` y `seagull_sound.wav` (Para Costa).
    *   `harp_sound.wav` y `cuatro_sound.wav` (Para los Llanos).
    *   `whip_sound.wav` y `banjo_sound.wav` (Para Vaquero Country).
3.  Abre tu proyecto en Android Studio.
4.  Arrastra y suelta tus archivos de audio reales dentro de la carpeta: `app/src/main/res/raw/`. Reemplaza ("Overwrite") los archivos silenciosos existentes.
5.  ¡Re-compila la aplicación (`Run app`) y ahora todo tu juego tendrá un sonido espectacular!

El manejo asíncrono y la gestión de memoria (`release()`) ya está perfectamente programada en el archivo `MainActivity.java`.

---
### 📲 Descarga de la Aplicación
El APK con las últimas funciones ya ha sido generado y se llama **`TresEnRaya_Personalizado.apk`**. Puedes encontrarlo directamente en la carpeta **APK/** de este repositorio para instalar en cualquier móvil Android (Versión 7.0 o superior).