---
nav_title: Redacción publicitaria
article_title: Asistente de redacción con inteligencia artificial
page_order: 2.1
description: "Este artículo de referencia cubre el asistente de redacción con inteligencia artificial, una característica que envía un breve nombre o descripción del producto a la herramienta de generación de textos GPT de OpenAI para generar textos de marketing con estilo natural para usar en tus mensajes."
---

# Genera textos con BrazeAI

> El asistente de redacción con inteligencia artificial envía un breve nombre o descripción del producto a una herramienta de generación de textos GPT de un proveedor externo (OpenAI) para generar textos de marketing con estilo natural para usar en tus mensajes. Esta funcionalidad está disponible de forma predeterminada en la mayoría de los creadores de mensajes del panel de Braze.

## Creación de contenido

### Paso 1: Lanza el redactor de inteligencia artificial

En el creador de mensajes, selecciona <i class="fa-solid fa-wand-magic-sparkles"></i> **Lanzar el redactor de inteligencia artificial**.

En el editor de arrastrar y soltar para mensajes dentro de la aplicación, selecciona un bloque de texto y elige <i class="fa-solid fa-wand-magic-sparkles" title="Redactor de inteligencia artificial"></i> en la barra de herramientas del bloque.

### Paso 2: Introduce los detalles

Introduce el nombre o la descripción del producto en el campo de entrada y, a continuación, selecciona una longitud aproximada para el resultado.

Puedes elegir un canal específico para una longitud de salida basada en las mejores prácticas específicas del canal o seleccionar entre corto (1 frase), medio (2-3 frases) o largo (1 párrafo).

### Paso 3: Personalízalo aún más (opcional)

Para personalizar tu texto aún más, puedes:

- **Aplicar las directrices de marca:** Después de [generar las directrices de marca con BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/generative_ai/brand_guidelines), puedes utilizarlas para ayudarte a crear tu texto.
- **Elegir un tono:** Cada tono generará un texto con un estilo diferente. Elige el tono que mejor se adapte a la voz de tu marca.
  
  Seleccionar un tono añade una instrucción de estilo al prompt enviado a OpenAI, por lo que el resultado exacto puede variar según la entrada, la longitud del canal, las directrices de marca y el modelo. 
  
  Esto es lo que cada tono pretende hacer de forma predeterminada:
  - **Formal:** Redacción más profesional y pulida. Frases completas, lenguaje más cortés, mínimo uso de jerga.
  - **Directo:** Más directo y conciso. Menos adjetivos, menos "relleno de marketing", llamadas a la acción más claras.
  - **Casual:** Más relajado y conversacional. Frases más amigables, palabras más sencillas, energía más ligera.
  - **Personal:** Más cercano y empático. Usa más el "tú", puede sentirse más personalizado, especialmente si añades personalización como {% raw %}`{{${first_name}}}`{% endraw %} al mensaje que estás creando.
  - **Llamativo:** Más atractivo y captador de atención. Frases más impactantes, mayor energía, ganchos y CTAs más fuertes (a menudo suena más "promocional" que los otros tonos).
  - **Sofisticado:** Lenguaje más elevado y refinado. Menos casual, posicionamiento más "premium".
  - **Profesional:** Empresarial y claro. Más moderno y accesible que Formal, pero manteniendo autoridad.
  - **Pasivo:** Lenguaje más suave y menos insistente. Menos órdenes directas, frases más sugerentes.
  - **Urgente:** Enfatiza la inmediatez y la sensibilidad temporal. CTAs más fuertes, plazos, señales de escasez.
  - **Emocionante:** Más enérgico y entusiasta. Enfatiza la emoción positiva y la celebración (a menudo más centrado en el entusiasmo que en el enfoque de gancho del tono Llamativo).
 
  
- **Consultar los datos de campañas anteriores**: Cuando esta opción está habilitada, las notificaciones push móviles anteriores enviadas a través de tus campañas o pasos en Canvas se utilizan como referencia estilística para generar tu nuevo texto. Para obtener más información, consulta [Uso de datos de campañas anteriores](#past-campaign-data).
- **Traducir automáticamente el texto:** Puedes elegir un idioma de salida diferente para tu texto. El contenido generado se mostrará en ese idioma.

### Paso 4: Genera tu texto

Cuando hayas terminado, selecciona **Generar**. Utilizaremos la información que nos proporciones para que GPT redacte un texto para ti. La respuesta se obtendrá de OpenAI y se te proporcionará. Para obtener más información, consulta [¿Cómo se utilizan y envían tus datos a OpenAI?](#ai-policy).

![Modal del asistente de redacción con inteligencia artificial con varias opciones disponibles.]({% image_buster /assets/img/ai_copywriter/gpt3.png %} "GPT3"){: style="max-width:70%;"}

{% alert important %}
Filtramos las respuestas de contenido ofensivo que infringe la [política de contenidos](https://beta.openai.com/docs/usage-guidelines/content-policy) de OpenAI.
{% endalert %}

## Acerca de los datos de campañas anteriores {#past-campaign-data}

Cuando utilices push como longitud de salida, si seleccionas **Consultar datos de campañas anteriores**, se enviarán a OpenAI campañas push móviles anteriores seleccionadas aleatoriamente para que GPT pueda utilizarlas como base para la generación de tu texto. Actualmente, el asistente de redacción con inteligencia artificial enviará a OpenAI campañas push que no contienen sintaxis Liquid. Deja esta casilla sin marcar si no quieres aprovechar esta capacidad. Consulta las secciones siguientes para obtener más información sobre cómo utilizan tus datos Braze y OpenAI. 

Si se utiliza junto con una [directriz de marca]({{site.baseurl}}/user_guide/brazeai/generative_ai//brand_guidelines/), tanto la directriz de marca como los datos de la campaña anterior se incorporarán al resultado final.

{% multi_lang_include brazeai/generative_ai/policy.md %}