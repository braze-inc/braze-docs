---
nav_title: Accesibilidad
article_title: Accesibilidad
platform: Web
page_order: 22
page_type: reference
description: "Este artículo describe cómo Braze soporta la accesibilidad."

---

# Accesibilidad

> Este artículo ofrece un resumen de cómo Braze admite la accesibilidad en tu integración.

Braze Web SDK es compatible con las normas establecidas por [las Directrices de Accesibilidad al Contenido en la Web (WCAG 2.1)](https://www.w3.org/TR/WCAG21/). Mantenemos una [puntuación Lighthouse de 100/100](https://developer.chrome.com/docs/lighthouse/accessibility/scoring) para las tarjetas de contenido y los mensajes dentro de la aplicación en todas nuestras nuevas versiones para mantener nuestro estándar de accesibilidad.

## Requisitos previos

La versión mínima del SDK que satisface las WCAG 2.1 está próxima a la v3.4.0. Sin embargo, te recomendamos que actualices al menos a la versión 6.0.0 para corregir las principales etiquetas de imagen.

### Correcciones notables de accesibilidad

| Versión | Tipo | Cambios clave |
|---------|------|-------------|
| **6.0.0** | **Mayor** | Imágenes como etiquetas `<img>`, campos `imageAltText` o `language`, mejoras generales de accesibilidad de la IU |
| **3.5.0** | Menor | Mejoras en la accesibilidad del texto desplazable |
| **3.4.0** | Arregla | Tarjetas de contenido `article` role fix |
| **3.2.0** | Menor | Objetivos táctiles mínimos de 45x45px para los botones |
| **3.1.2** | Menor | Texto alternativo predeterminado para las imágenes |
| **2.4.1** | **Mayor** | HTML semántico (`h1` o `button`), atributos ARIA, navegación por teclado, gestión del enfoque |
| **2.0.5** | Menor | Administrador de foco, navegación por teclado, etiquetas |
{: .reset-td-br-1, .reset-td-br-2 role="presentation" }

## Características de accesibilidad compatibles

Admitimos estas características para las tarjetas de contenido y los mensajes dentro de la aplicación:

- Roles y etiquetas ARIA
- Soporte de navegación por teclado
- Enfoque de gestión
- Anuncios para lectores de pantalla
- Soporte de texto alternativo para imágenes

## Pautas de accesibilidad para las integraciones de SDK

Consulta [Construir mensajes accesibles en Braze]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/accessibility) para conocer las pautas generales de accesibilidad. Esta guía proporciona consejos y buenas prácticas para conseguir la máxima accesibilidad al integrar el SDK Braze Web en tu aplicación web.

### Tarjetas de contenido

#### Configuración de una altura máxima

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

Para las tarjetas de contenido que se muestran en línea, ten en cuenta las restricciones de la ventana gráfica, como en este ejemplo.

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
No pongas información importante en los mensajes dentro de la aplicación, ya que no son accesibles para los lectores de pantalla.
{% endalert %}

### Consideraciones móviles

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

### Comprobar la accesibilidad

#### Lista de comprobación de pruebas manuales

Comprueba manualmente tu accesibilidad realizando estas tareas:

- Navega por las tarjetas de contenido y los mensajes dentro de la aplicación sólo con el teclado (pestaña, Intro, espacio)
- Prueba con lector de pantalla (NVDA, JAWS, VoiceOver)
- Comprueba que todas las imágenes tienen texto alternativo
- Comprueba la relación de contraste de los colores (utiliza herramientas como WebAIM Contrast Checker)
- Prueba en dispositivos móviles táctiles
- Comprueba que los indicadores de enfoque son visibles
- Prueba de captura de enfoque de mensaje modal
- Comprueba que todos los elementos interactivos son accesibles mediante un teclado

### Problemas comunes de accesibilidad

Para evitar problemas comunes de accesibilidad, haz lo siguiente:

1. **Mantén los estilos de enfoque:** Los indicadores de enfoque del SDK son esenciales para los usuarios de teclado.
2. **Utiliza `display: none` sólo en elementos no interactivos:** Utiliza `visibility: hidden` o `opacity: 0` para ocultar los elementos interactivos.
3. **No anules los atributos ARIA:** El SDK establece las funciones y etiquetas ARIA adecuadas.
4. **Utiliza los atributos de `tabindex`:** Controlan el orden de navegación del teclado.
5. **Proporciona un desplazamiento si configuras `overflow: hidden`:** Confirma que el contenido desplazable sigue siendo accesible.
6. **No interfieras con los controladores de teclado incorporados:** Confirma que funciona la navegación por teclado existente.