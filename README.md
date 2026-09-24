# App DADM Personalizada 🎨🧛‍♂️

Bienvenido a la evolución definitiva de la aplicación: **App DADM Personalizada**. En este nuevo repositorio hemos llevado el desarrollo a un nivel más avanzado integrando una arquitectura de **Temáticas Dinámicas (Theme Switching)** usando Custom Views y Sound Management.

## 🚀 ¿Qué se agregó en esta versión personalizada?

### 1. Sistema de Temáticas Dual (Classic vs. Halloween)
Ahora el usuario puede cambiar toda la experiencia gráfica y auditiva en tiempo real a través del menú de opciones.
*   **Tema Clásico:** El tradicional juego de 'X' (Azul) contra 'O' (Rojo), con sonidos estándar (Sword & Swish).
*   **Tema Halloween:** Un diseño escalofriante con un **Murciélago 🦇** (Morado oscuro) y una **Calabaza 🎃** (Naranja/Verde) acompañados por nuevos efectos de sonido de ambiente espectral.

### 2. Actualización Dinámica del `BoardView` (Custom Views)
Hemos implementado un método `setTheme(int)` dentro de nuestra vista personalizada.
*   En lugar de cargar estáticamente el `Bitmap` en la creación de la clase, el `BoardView` ahora vuelve a inyectar las gráficas XML vectoriales correctas y ejecuta un `invalidate()` forzando a la GPU a redibujar el tablero con el nuevo arte **sin necesidad de reiniciar el juego o la pantalla actual**.

### 3. Recarga Inteligente de Memoria Multimedia (`MediaPlayer`)
La clase principal `MainActivity` ahora administra activamente los recursos de audio en tiempo de ejecución.
*   Al seleccionar una nueva temática, el método personalizado `loadSounds()` se asegura de llamar a `release()` en las instancias actuales de MediaPlayer (para evitar fugas de memoria, o "Memory Leaks") y las sobre-escribe con los nuevos audios `bat_sound` y `ghost_sound` encolándolas a la memoria de nuevo de manera asíncrona.

### 4. Integración Perfecta de la Interfaz (UI)
*   Se agregó la opción de "Temática" tanto al **Overflow Menu** (los 3 puntos en la esquina superior derecha) como en la **Bottom Navigation Bar** inferior, proporcionando la máxima accesibilidad para el usuario.
*   Ambos menús levantan un nuevo `AlertDialog.Builder` optimizado con SingleChoiceItems, preservando el patrón de diseño ya estructurado.

---
Este proyecto es una muestra sólida de buenas prácticas para manejar múltiples recursos de diseño y audio optimizando el rendimiento de memoria en el ciclo de vida (Lifecycle) de una app Android.

### 📲 Descarga de la Aplicación
El APK con las últimas funciones ya ha sido generado y se llama **`TresEnRaya_Personalizado.apk`**. Puedes encontrarlo directamente en la carpeta **APK/** de este repositorio para instalar en cualquier móvil Android (Versión 7.0 o superior).