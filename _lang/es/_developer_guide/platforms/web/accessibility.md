---
nav_title: Accesibilidad
article_title: Accesibilidad
platform: Web
page_order: 22
page_type: reference
description: "Este artículo describe cómo Braze favorece la accesibilidad."

---

# Accesibilidad

> Este artículo ofrece un resumen de cómo Braze favorece la accesibilidad dentro de tu integración.

Braze Web SDK es compatible con los estándares establecidos por las [Pautas de Accesibilidad al Contenido en la Web (WCAG 2.1)](https://www.w3.org/TR/WCAG21/). Mantenemos una [puntuación de 100/100 en Lighthouse](https://developer.chrome.com/docs/lighthouse/accessibility/scoring) para las tarjetas de contenido y los mensajes dentro de la aplicación en todas nuestras nuevas versiones, con el fin de mantener nuestro estándar de accesibilidad.

## Requisitos previos

La versión mínima del SDK que cumple con WCAG 2.1 es cercana a la v3.4.0. Sin embargo, recomendamos actualizar al menos a la versión 6.0.0 para obtener correcciones importantes en las etiquetas de imagen.

### Correcciones notables en materia de accesibilidad

| Versión | Tipo | Cambios clave |
|---------|------|-------------|
| **6.0.0** | **Mayor** | Imágenes como`<img>`etiquetas o`language`campos`imageAltText`, mejoras generales en la accesibilidad de la interfaz de usuario. |
| **3.5.0** | Menor | Mejoras en la accesibilidad del texto desplazable |
| **3.4.0** | Arregla | Tarjetas de contenido  `article`corrección de funciones |
| **3.2.0** | Menor | Objetivos táctiles mínimos de 45 x 45 píxeles para botones. |
| **3.1.2** | Menor | Texto alternativo predeterminado para imágenes |
| **2.4.1** | **Mayor** | HTML semántico (`h1` o `button`), atributos ARIA, navegación con el teclado, gestión del foco |
| **2.0.5** | Menor | Administración del foco, navegación con el teclado, etiquetas |
{: .reset-td-br-1, .reset-td-br-2 role="presentation" }

## Características de accesibilidad compatibles

Admitimos estas características para tarjetas de contenido y mensajes dentro de la aplicación:

- Funciones y etiquetas ARIA
- Compatibilidad con la navegación mediante teclado
- Gestión del enfoque
- Anuncios del lector de pantalla
- Compatibilidad con texto alternativo para imágenes

## Directrices de accesibilidad para integraciones de SDK

Consulta [Creación]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/accessibility) de [mensajes accesibles en Braze]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/accessibility) para obtener directrices generales sobre accesibilidad. Esta guía proporciona consejos y prácticas recomendadas para lograr la máxima accesibilidad al integrar el SDK web de Braze en tu aplicación web.

### Tarjetas de contenido

#### Establecer una altura máxima

Para evitar que las tarjetas de contenido ocupen demasiado espacio vertical y mejorar la accesibilidad, puedes establecer una altura máxima en el contenedor de la fuente, como en este ejemplo:

{% raw %}
```css
/* Limit the height of the Content Cards feed */
.ab-feed {
  max-height: 600px; /* Adjust to your needs */
  overflow-y: auto;
}

/* For inline feeds (non-sidebar), you may want to limit individual cards */
.ab-card {
  max-height: 400px; /* Optional: limit individual card height */
  overflow: hidden;
}
```
{% endraw %}

#### Consideraciones sobre la ventana gráfica

Para las tarjetas de contenido que se muestran en línea, ten en cuenta las restricciones del área de visualización, como en este ejemplo.

{% raw %}
```css
/* Limit feed height on mobile to prevent covering too much screen */
@media (max-width: 768px) {
  body > .ab-feed {
    max-height: 80vh; /* Leave space for other content */
  }
}
```
{% endraw %}

### Mensajes dentro de la aplicación

{% alert warning %}
No incluyas información importante en los mensajes dentro de la aplicación, ya que no son accesibles para los lectores de pantalla.
{% endalert %}

### Consideraciones sobre los dispositivos móviles

#### Diseño receptivo

El SDK incluye puntos de interrupción receptivos. Confirma que tus personalizaciones funcionan en todos los tamaños de pantalla, como en este ejemplo:

{% raw %}
```css
/* Mobile-specific accessibility considerations */
@media (max-width: 768px) {
  /* Ensure readable font sizes */
  .ab-feed {
    font-size: 14px; /* Minimum 14px for mobile readability */
  }
  
  /* Ensure sufficient touch targets */
  .ab-card {
    padding: 16px; /* Adequate padding for touch */
  }
}
```
{% endraw %}

### Prueba de accesibilidad

#### Lista de verificación de pruebas manuales

Comprueba manualmente tu accesibilidad completando estas tareas:

- Navega por las tarjetas de contenido y los mensajes dentro de la aplicación solo con el teclado (Tab, Intro, Espacio).
- Prueba con lector de pantalla (NVDA, JAWS, VoiceOver)
- Verifica que todas las imágenes tengan texto alternativo.
- Comprueba los ratios de contraste de color (utiliza herramientas como WebAIM Contrast Checker).
- Prueba en dispositivos móviles con pantalla táctil.
- Comprueba que los indicadores de enfoque sean visibles.
- Prueba de captura de enfoque de mensajes modales
- Verifica que se pueda acceder a todos los elementos interactivos mediante el teclado.

### Problemas comunes de accesibilidad

Para evitar problemas comunes de accesibilidad, haz lo siguiente:

1. **Mantén los estilos de enfoque:** Los indicadores de enfoque del SDK son esenciales para los usuarios de teclado.
2. **Úsalo solo`display: none` en elementos no interactivos:** Usa`visibility: hidden`  o`opacity: 0`  para ocultar elementos interactivos.
3. **No anules los atributos ARIA:** El SDK establece las funciones y etiquetas ARIA adecuadas.
4. **Utiliza`tabindex`los atributos:** Estos controlan el orden de navegación del teclado.
5. **Proporciona un desplazamiento si realizas la configuración`overflow: hidden`:** Confirma que el contenido desplazable sigue siendo accesible.
6. **No interfieras con los controladores de teclado integrados:** Confirma que la navegación con el teclado existente funciona correctamente.