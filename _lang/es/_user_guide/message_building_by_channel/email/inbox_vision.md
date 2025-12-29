---
nav_title: Visión del buzón de entrada
article_title: Visión del buzón de entrada
page_order: 9
description: "Esta página explica cómo configurar Inbox Vision, una característica que permite a los especialistas en marketing ver sus correos electrónicos desde la perspectiva de varios clientes de correo electrónico y dispositivos móviles."
tool:
  - Dashboard
channel:
  - email

---

# Visión del buzón de entrada

> Inbox Vision te permite ver tus correos electrónicos desde la perspectiva de varios clientes de correo electrónico y dispositivos móviles. Por ejemplo, puedes utilizar Visión de la Bandeja de Entrada para comprobar las diferencias entre los modos oscuro y claro y confirmar así que tus correos electrónicos son correctos.

{% alert important %}
En general, tu correo electrónico no funcionará con Inbox Vision si el contenido de tu correo electrónico depende de la información de la plantilla, como la información del perfil de usuario. Esto se debe a que las plantillas de Braze en un usuario vacío cuando enviamos correos electrónicos utilizando esta característica.<br><br>Asegúrate de haber añadido valores predeterminados a cualquier Liquid de tu mensaje de correo electrónico. Si no se proporcionan valores predeterminados, es posible que obtengas un falso positivo o que no se ejecute la prueba.
{% endalert %}

## Prueba tu correo electrónico en Inbox Vision

Tu correo electrónico debe incluir una línea del asunto y un dominio de envío válido para poder ver estas vistas previas. Ten en cuenta que tu correo electrónico puede tener un aspecto diferente en el escritorio que en los dispositivos móviles. Mientras ves estas vistas previas, puedes revisar tu contenido y asegurarte de que tu correo electrónico se muestra como es debido.

Para probar tu mensaje de correo electrónico en Inbox Vision, haz lo siguiente:

1. Ve a tu editor de arrastrar y soltar o a tu editor de correo electrónico HTML.
2. En tu editor, selecciona **Vista previa & Test**.
3. Selecciona **Visión de buzón de entrada**.
4. Selecciona **Ejecutar Visión de Buzón de Entrada**. Esto puede llevar entre dos y diez minutos.
5. A continuación, selecciona una baldosa para ver la vista previa con más detalle. Estas vistas previas están agrupadas en estas secciones: **Clientes Web**, **Clientes de Aplicación** y **Clientes Móviles**.

\![Resumen de Inbox Vision para el editor HTML.]({% image_buster /assets/img_archive/inboxvision1.png %})

{: start="6"}
6\. Haz cambios en una plantilla, si es necesario.
7\. Selecciona **Volver a ejecutar la prueba** para ver las vistas previas actualizadas.

{% alert note %}
La Visión de la bandeja de entrada no es compatible si tu mensaje de correo electrónico incluye [una lógica de cancelación]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages), ya que estos mensajes se muestran como contenido estático.
{% endalert %}

### Vista previa como usuario

Cuando previsualizas el correo electrónico como un usuario aleatorio, cualquier configuración o atributo específico asociado a un usuario, como su nombre o preferencias, no se guarda para las previsualizaciones actuales o futuras. Cuando seleccionas un usuario personalizado, la vista previa mostrada en la Visión de la Bandeja de Entrada puede diferir de la vista previa del mensaje en otro lugar, ya que esta opción utiliza datos de usuario específicos para crear la vista previa.

## Análisis del código

El análisis de código es una forma de que Braze resalte los problemas que puedan existir con tu HTML, mostrando el número de ocurrencias de cada problema y proporcionando información sobre qué elementos HTML no son compatibles.

### Ver la información del análisis del código

Puedes encontrar esta información en la pestaña **Visión de buzón de entrada** seleccionando <i class="fas fa-list"></i> **Vista de lista**. Esta vista de lista sólo está disponible para plantillas de correo electrónico HTML. Si utilizas plantillas de correo electrónico de arrastrar y soltar, comprueba en su lugar las vistas previas para resolver cualquier posible problema.

\![Ejemplo de análisis de código en la vista previa de Inbox Vision.]({% image_buster /assets/img_archive/inboxvision2.png %})

{% alert note %}
A veces, el análisis del código se mostrará más rápido que la vista previa para un cliente de correo electrónico concreto. Esto se debe a que Braze espera hasta que el correo electrónico llega al buzón de entrada antes de hacer la captura de pantalla.
{% endalert %}

## Pruebas de correo no deseado

Las pruebas de correo no deseado intentan predecir si tu correo electrónico llegará a las carpetas de correo no deseado o a los buzones de entrada de tus clientes. Las pruebas de correo no deseado se ejecutan en los principales filtros de correo no deseado, como IronPort, SpamAssassin y Barracuda, así como en los principales filtros de proveedores de servicios de Internet (ISP), como Gmail.com y Outlook.com.

### Ver los resultados de las pruebas de correo no deseado

Para comprobar los resultados de tus pruebas de correo no deseado, haz lo siguiente:

1. Selecciona la pestaña **Pruebas de correo no deseado** en la sección **Visión de la bandeja de entrada**. La tabla de **resultados de las pruebas de correo no deseado** muestra el nombre, estado y tipo del filtro de correo no deseado.

\![Tabla de resultados de pruebas de correo no deseado con tres columnas: Nombre, estado y tipo. Hay una lista de filtros de correo no deseado y filtros ISP que han superado las pruebas de correo no deseado, lo que indica que la campaña de correo electrónico no caerá en la carpeta de correo no deseado.]({% image_buster /assets/img_archive/email_spam_testing.png %})

{: start="2"}
2\. Revisa estos resultados y haz los ajustes necesarios en tu campaña de correo electrónico.
3\. Selecciona **Reejecutar prueba** para volver a cargar los resultados de tus pruebas de correo no deseado.

## Pruebas de accesibilidad

Las pruebas de accesibilidad de Inbox Vision ponen de manifiesto los problemas de accesibilidad que pueden existir en tu correo electrónico para proporcionar información sobre qué elementos no cumplen las normas de accesibilidad. Analiza el contenido de tu correo electrónico según algunas Pautas de Accesibilidad al Contenido en la Web[(WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)). Las WCAG son un conjunto de normas técnicas reconocidas internacionalmente y desarrolladas por el Consorcio de la World Wide Web (W3C) para que los contenidos Web sean más accesibles a las personas con discapacidad. 

### Cómo funciona

Cuando ejecutas una prueba de Inbox Vision, la herramienta comprueba automáticamente los problemas comunes de accesibilidad del correo electrónico en el [conjunto de reglas WCAG 2.2 AA](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.2&currentsidebar=%23col_customize&levels=aaa), como la falta de texto alternativo, el contraste insuficiente de colores y la estructura inadecuada de los encabezamientos, y luego clasifica la gravedad de cada problema para ayudarte a priorizar las correcciones. 

{% alert important %}
Las Pruebas de Accesibilidad pueden utilizarse para respaldar los esfuerzos del Cliente por cumplir normativas o leyes como [la Ley Europea de Accesibilidad](https://www.braze.com/resources/articles/european-accessibility-at-what-it-means-for-marketers); sin embargo, el Cliente reconoce que Braze no representa ni garantiza si el uso de las Pruebas de Accesibilidad satisface o no las obligaciones de cumplimiento del Cliente, y declina toda responsabilidad al respecto.
{% endalert %}

### Ver los resultados de las pruebas de accesibilidad

Las **pruebas de accesibilidad** generarán resultados para cada regla como aprobada, fallida o necesita revisión en la pestaña **Pruebas de accesibilidad**. Cada regla se clasifica utilizando POUR (Perceptible, Operable, Comprensible, Robusto), que son los cuatro principios fundamentales en los que se basan las WCAG.

#### Categorías POUR

Los temas se clasifican según los cuatro [principios fundamentales del POUR](https://www.w3.org/WAI/WCAG22/Understanding/intro#understanding-the-four-principles-of-accessibility): Perceptible, Operable, Comprensible y Robusto. Cada principio aborda un aspecto diferente del diseño accesible.

| Principio | Definición |
| --- | --- |
| Perceptible | La información y los componentes de la interfaz de usuario deben ser presentables a los usuarios de forma que puedan percibirlos.<br><br>Los usuarios deben poder percibir la información que se les presenta (no puede ser invisible a todos sus sentidos). |
| Operable | Los componentes de la interfaz de usuario y la navegación deben ser operables.<br><br>Los usuarios deben ser capaces de manejar la interfaz (la interfaz no puede requerir una interacción que un usuario no pueda realizar). |
| Comprensible | La información y el funcionamiento de la interfaz de usuario deben ser comprensibles.<br><br>Los usuarios deben ser capaces de comprender tanto la información como el funcionamiento de la interfaz de usuario (el contenido o el funcionamiento no pueden estar más allá de su comprensión). |
| Robusto | El contenido debe ser lo suficientemente sólido como para que pueda ser interpretado de forma fiable por una amplia variedad de agentes de usuario, incluidas las tecnologías de asistencia.<br><br>Los usuarios deben poder acceder al contenido a medida que avanzan las tecnologías (a medida que evolucionan las tecnologías y los agentes de usuario, el contenido debe seguir siendo accesible). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Niveles de gravedad

Inbox Vision clasifica los problemas de accesibilidad por gravedad para ayudarte a priorizar los esfuerzos de corrección.

| Estado | Definición |
| --- | --- |
| Crítica | Cuestiones que pueden bloquear el acceso a contenidos o funcionalidades para usuarios con discapacidad. Éstas son las más graves y debe darse prioridad a su reparación. |
| En serio | Cuestiones que pueden causar obstáculos importantes, pero que pueden no bloquear completamente el acceso. Deben abordarse con prontitud. |
| Moderado | Problemas que pueden causar alguna dificultad a los usuarios con discapacidad, pero es menos probable que bloqueen el acceso por completo. |
| Menor | Cuestiones que tienen un impacto relativamente bajo en la accesibilidad y que sólo pueden causar pequeñas molestias. |
| Necesita revisión | Incapaz de detectar si puede haber un problema o no. Esto puede ocurrir cuando no somos capaces de determinar la relación de contraste al colocar el texto sobre una imagen de fondo. Esto tendrá que revisarse manualmente porque no puede determinarse automáticamente. |
| Aprobado | Ha superado las pruebas WCAG A, AA o las mejores prácticas de accesibilidad. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
El editor de arrastrar y soltar de correo electrónico no admite actualmente la configuración de un elemento del documento `<title>`. Como resultado, el escáner de accesibilidad siempre fallará esta comprobación.<br><br>
Estamos haciendo un seguimiento de esta limitación para futuras mejoras. Si esto afecta a tus flujos de trabajo o a tus usuarios, [comparte tus comentarios]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/#sharing-feedback) para que podamos priorizar las correcciones más impactantes.
{% endalert %}

### Comprender las pruebas de accesibilidad automatizadas

{% multi_lang_include accessibility/automated_testing.md %}

## Precisión de la prueba

Todas nuestras pruebas se realizan con clientes de correo electrónico reales. Braze se esfuerza por comprobar que todas las representaciones sean lo más exactas posible. Si ves constantemente un problema con un cliente de correo electrónico, abre un [ticket de soporte]({{site.baseurl}}/braze_support/).
