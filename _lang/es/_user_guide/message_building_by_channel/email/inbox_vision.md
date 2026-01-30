---
nav_title: Inbox Vision
article_title: Inbox Vision
page_order: 9
description: "Esta página explica cómo configurar Inbox Vision, una característica que permite a los especialistas en marketing ver sus correos electrónicos desde la perspectiva de varios clientes de correo electrónico y dispositivos móviles."
tool:
  - Dashboard
channel:
  - email

---

# Inbox Vision

> Inbox Vision te permite ver tus correos electrónicos desde la perspectiva de varios clientes de correo electrónico y dispositivos móviles. Por ejemplo, puedes probar las diferencias entre los modos oscuro y claro para confirmar que tus correos electrónicos se reproducen como es debido.

{% alert important %}
La Visión de buzón de entrada puede no funcionar si el contenido de tu correo electrónico depende de la información de la plantilla, como los datos de perfil de usuario. Braze plantillas un usuario vacío al enviar correos electrónicos para esta característica.<br><br>Añade valores predeterminados a cualquier Liquid de tu mensaje de correo electrónico. Sin los predeterminados puedes recibir un falso positivo o la prueba puede fallar.
{% endalert %}

## Consideraciones

En general, tu correo electrónico no funcionará con Inbox Vision si el contenido de tu correo electrónico depende de la información de la plantilla, como la información del perfil de usuario. Esto se debe a que Braze crea una plantilla de usuario vacía cuando enviamos correos electrónicos utilizando esta característica.

Puedes solucionarlo añadiendo valores predeterminados o cualquier valor al Liquid de tu mensaje de correo electrónico antes de ejecutar Inbox Vision. Cuando termines la prueba en Visión de la Bandeja de Entrada, aparecerá el mensaje de correo electrónico original. Si no se proporcionan valores, puede que la prueba no renderice correctamente las vistas previas.

Tu empresa tiene un límite en el número de correos electrónicos que puedes previsualizar con Visión de Bandeja de Entrada. Puedes controlar esto en la pestaña **Vistas previas de correo electrónico** de Visión de la bandeja de entrada.

Incluye una línea del asunto y un dominio de envío válido para ver las vistas previas. Ten en cuenta las diferencias de representación entre ordenadores de sobremesa y móviles. Utiliza la vista previa para confirmar que el correo electrónico es correcto.

Para probar tu mensaje de correo electrónico en Inbox Vision:

1. Vaya a su editor de arrastrar y soltar o a su editor de correo electrónico HTML.
2. En tu editor, selecciona **Vista previa & Test**.
3. Selecciona **Visión de buzón de entrada**.
4. Selecciona **Ejecutar Visión de Buzón de Entrada**. Esto lleva hasta diez minutos.
5. A continuación, selecciona una baldosa para ver la vista previa con más detalle. Estas vistas previas están agrupadas en estas secciones: **Clientes Web**, **Clientes de Aplicación** y **Clientes Móviles**.

![La opción de seleccionar clientes de correo electrónico para la vista previa.]({% image_buster /assets/img/select_email_preview_inbox_vision.png %}){: style="max-width:85%;"}

{:start="5"}
5\. Selecciona **Ejecutar Visión de Buzón de Entrada**. Esto puede llevar entre dos y diez minutos.

{% alert note %}
La Visión de Bandeja de Entrada no admite mensajes de correo electrónico que incluyan [una lógica de cancelación]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages), ya que estos mensajes se muestran como contenido estático.
{% endalert %}

### Vista previa como usuario

Cuando realizas una vista previa como usuario aleatorio, Inbox Vision no guarda la configuración ni los atributos específicos del usuario (como el nombre o las preferencias). Cuando seleccionas un usuario personalizado, la vista previa de Visión de bandeja de entrada puede diferir de otras vistas previas porque utiliza datos de usuario específicos.

## Análisis del código

El análisis del código destaca los posibles problemas de HTML, muestra el número de ocurrencias e indica los elementos HTML no compatibles.

### Visualización de la información de análisis de código

Encuentra esta información en la pestaña **Visión de la bandeja de entrada** seleccionando <i class="fas fa-list"></i> **Vista de lista**. La vista de lista sólo está disponible para plantillas de correo electrónico HTML. Para las plantillas de arrastrar y soltar, utiliza en su lugar vistas previas para resolver los problemas.

![Ejemplo de análisis de código en la vista previa de Inbox Vision.]({% image_buster /assets/img_archive/inboxvision2.png %})

{% alert note %}
El análisis del código puede aparecer más rápido que la vista previa para un cliente concreto, porque Braze espera a que llegue el correo electrónico antes de hacer la captura de pantalla.
{% endalert %}

## Pruebas de spam

Las pruebas de correo no deseado predicen si tu correo electrónico llega a las carpetas de correo no deseado o a los buzones de entrada. Braze ejecuta pruebas en los principales filtros de correo no deseado (IronPort, SpamAssassin, Barracuda) y en los principales filtros ISP (Gmail.com, Outlook.com).

### Ver los resultados de las pruebas de correo no deseado

Para comprobar los resultados de tus pruebas de correo no deseado:

1. Selecciona la pestaña **Pruebas de correo no deseado** en la sección **Visión de la bandeja de entrada**. La tabla de **resultados de la prueba de spam** muestra el nombre, el estado y el tipo del filtro de spam.
2. Revisa estos resultados y haz los ajustes necesarios en tu campaña de correo electrónico.
3. Selecciona **Reejecutar prueba** para volver a cargar los resultados de tus pruebas de correo no deseado.

## Pruebas de accesibilidad

Las pruebas de accesibilidad ponen de manifiesto posibles problemas de accesibilidad en tu correo electrónico y muestran qué elementos no cumplen las normas. Braze analiza el contenido según las Pautas de Accesibilidad al Contenido en la Web[(WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)) seleccionadas, un conjunto de normas reconocidas internacionalmente y desarrolladas por el W3C para hacer que el contenido web sea más accesible.

### Cómo funciona

Cuando ejecutas Inbox Vision, Braze comprueba automáticamente los problemas de accesibilidad comunes en el [conjunto de reglas WCAG 2.2 AA](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.2&currentsidebar=%23col_customize&levels=aaa) (como la falta de texto alternativo, el contraste de color insuficiente o la estructura inadecuada de los encabezamientos) y clasifica la gravedad para ayudarte a priorizar las correcciones. 

{% alert important %}
Las Pruebas de accesibilidad pueden utilizarse para respaldar los esfuerzos de cumplimiento de normativas o leyes del Cliente, como [la Ley europea de accesibilidad](https://www.braze.com/resources/articles/european-accessibility-at-what-it-means-for-marketers); sin embargo, el Cliente reconoce que Braze no hace declaraciones ni ofrece garantías con respecto a si el uso de las Pruebas de accesibilidad satisface o no las obligaciones de cumplimiento del Cliente, y declina toda responsabilidad al respecto.
{% endalert %}

### Ver los resultados de las pruebas de accesibilidad

Las pruebas **de accesibilidad** generan resultados para cada regla como aprobada, fallida o necesita revisión en la pestaña **Pruebas de accesibilidad**. Braze clasifica cada regla utilizando POUR (Perceptible, Operable, Comprensible, Robusto), los cuatro principios en los que se basan las WCAG.

#### Categorías POUR

Inbox Vision clasifica los problemas según los cuatro [principios fundamentales del POUR](https://www.w3.org/WAI/WCAG22/Understanding/intro#understanding-the-four-principles-of-accessibility): Perceptible, Operable, Comprensible y Robusto.

| Principio | Definición |
| --- | --- |
| Perceptible | La información y los componentes de la interfaz de usuario deben ser presentables a los usuarios de forma que puedan percibirlos.<br><br>Los usuarios deben poder percibir la información que se les presenta (no puede ser invisible a todos sus sentidos). |
| Operable | Los componentes de la interfaz de usuario y la navegación deben ser operables.<br><br>Los usuarios deben ser capaces de manejar la interfaz (la interfaz no puede requerir una interacción que un usuario no pueda realizar). |
| Comprensible | La información y el funcionamiento de la interfaz de usuario deben ser comprensibles.<br><br>Los usuarios deben ser capaces de comprender la información, así como el funcionamiento de la interfaz de usuario (el contenido o el funcionamiento no pueden estar más allá de su comprensión). |
| Robusto | El contenido debe ser lo suficientemente sólido como para que pueda ser interpretado de forma fiable por una amplia variedad de agentes de usuario, incluidas las tecnologías de asistencia.<br><br>Los usuarios deben poder acceder al contenido a medida que avanzan las tecnologías (a medida que evolucionan las tecnologías y los agentes de usuario, el contenido debe seguir siendo accesible). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Niveles de gravedad

Inbox Vision clasifica los problemas de accesibilidad por gravedad para ayudarte a priorizar la corrección.

| Estado | Definición |
| --- | --- |
| Crítico | Cuestiones que pueden bloquear el acceso a contenidos o funcionalidades para usuarios con discapacidad. Éstas son las más graves y debe darse prioridad a su reparación. |
| Serias | Cuestiones que pueden causar obstáculos importantes, pero que pueden no bloquear completamente el acceso. Deben abordarse con prontitud. |
| Moderado | Cuestiones que pueden causar alguna dificultad a los usuarios con discapacidad, pero que es menos probable que bloqueen totalmente el acceso. |
| Menor | Cuestiones que tienen un impacto relativamente bajo en la accesibilidad y que solo pueden causar pequeñas molestias. |
| Necesita revisión | Incapaz de detectar si puede haber un problema o no. Esto puede ocurrir cuando no somos capaces de determinar la relación de contraste al colocar el texto sobre una imagen de fondo. Debes revisarlo manualmente porque no se puede determinar automáticamente. |
| Pasado correctamente | Ha superado las pruebas WCAG A, AA o las mejores prácticas de accesibilidad. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
El editor de arrastrar y soltar no admite la configuración de un elemento del documento `<title>`, por lo que el escáner de accesibilidad siempre falla esta comprobación.<br><br>Esta limitación es objeto de seguimiento para futuras mejoras. Si esto afecta a tus flujos de trabajo o a tus usuarios, [comparte tus comentarios]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/#sharing-feedback) para que podamos priorizar las correcciones de impacto.
{% endalert %}

### Comprender las pruebas de accesibilidad automatizadas

{% multi_lang_include accessibility/automated_testing.md %}

## Buenas prácticas

### Revisa tu lista de suscriptores de correo electrónico

Consulta el [panel de información del correo electrónico]({{site.baseurl}}/user_guide/analytics/dashboard/email_performance_dashboard#email-insights-dashboard) para determinar el tipo de dispositivo y los proveedores más populares con los que interactúan tus suscriptores. Si necesitas más granularidad, como el navegador, el modelo de dispositivo, etc., puedes aprovechar tus datos [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) o [el Creador de consultas]({{site.baseurl}}/user_guide/analytics/query_builder) para recuperar este nivel de detalle sobre la interacción reciente de tus usuarios con el correo electrónico.

De lo contrario, Braze predeterminará las 20 mejores vistas previas basándose en datos generales del sector y de expertos, que cubren la mayoría de los lugares en los que tus suscriptores interactúan con tus correos electrónicos. Si tu análisis de datos apunta a otras vistas previas más populares, puedes definir un conjunto predeterminado de vistas previas cada vez que ejecutes Inbox Vision.

### Selecciona vistas previas significativas y vistas previas impactadas

Si tu empresa tiene su sede principal en EE.UU., puede que haya vistas previas específicas, como las vistas previas internacionales como GMX.de, que sólo utiliza un número nominal de usuarios. Recomendamos priorizar y optimizar los buzones de entrada con un impacto considerable en los suscriptores y reservar tus vistas previas para los buzones de entrada de mayor impacto.

Cuando realices correcciones que afecten a vistas previas concretas, asegúrate de seleccionar sólo las vistas previas afectadas para evitar consumir vistas previas no utilizadas.

### Ejecuta Inbox Vision en la versión final del correo electrónico

Sugerimos ejecutar Inbox Vision cuando el mensaje de correo electrónico esté listo para la producción o casi. Esto te permite reducir el número de vistas previas generadas, ya que el correo electrónico pasa por múltiples iteraciones antes de estar finalizado y listo para ser enviado a los usuarios.

Ejecutar Visión de Bandeja de Entrada cada vez que hagas una edición o cambio puede consumir rápidamente las vistas previas. Te sugerimos que primero hagas todos los cambios necesarios en el correo electrónico y luego ejecutes Visión de Bandeja de Entrada para ver cómo pueden afectar todos tus cambios a la representación de tu correo electrónico en todos los entornos.

Braze realiza pruebas a través de clientes de correo electrónico reales y trabaja para garantizar que las representaciones sean precisas. Si ves constantemente un problema con un cliente, abre un [ticket de soporte]({{site.baseurl}}/braze_support/).
