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

> Inbox Vision te permite ver tus correos electrónicos desde la perspectiva de varios clientes de correo electrónico y dispositivos móviles. Por ejemplo, puedes probar las diferencias entre el modo oscuro y el modo claro para confirmar que tus correos electrónicos se muestran según lo previsto.

{% alert important %}
Es posible que Inbox Vision no funcione si el contenido de tu correo electrónico se basa en información de plantillas, como los datos del perfil de usuario. Braze crea una plantilla de usuario vacía al enviar correos electrónicos para esta característica.<br><br>Añade valores predeterminados a cualquier Liquid en tu mensaje de correo electrónico. Sin valores predeterminados, es posible que recibas un falso positivo o que la prueba falle.
{% endalert %}

## Consideraciones

En general, tu correo electrónico no funcionará con Inbox Vision si su contenido depende de información de plantillas, como la información del perfil de usuario. Esto se debe a que Braze crea una plantilla de usuario vacía cuando enviamos correos electrónicos utilizando esta característica.

Puedes resolver esto añadiendo valores predeterminados o cualquier otro valor al Liquid de tu mensaje de correo electrónico antes de ejecutar Inbox Vision. Cuando termines la prueba en Inbox Vision, aparecerá el mensaje de correo electrónico original. Si no se proporcionan valores, es posible que la prueba no pueda generar las vistas previas correctamente.

Tu empresa tiene un límite en cuanto al número de correos electrónicos que puedes tener en vista previa con Inbox Vision. Puedes supervisar esto en la pestaña **«Vista previa de correos electrónicos»** de Inbox Vision.

Incluye una línea del asunto y un dominio de envío válido para ver las vistas previas. Ten en cuenta las diferencias entre la visualización en ordenadores de sobremesa y en dispositivos móviles. Utiliza las vistas previas para confirmar que el correo electrónico aparece como deseas.

Para probar tu mensaje de correo electrónico en Inbox Vision:

1. Vaya a su editor de arrastrar y soltar o a su editor de correo electrónico HTML.
2. En tu editor, selecciona **Vista previa&  Prueba**.
3. Selecciona **Visión de buzón de entrada**.
4. Selecciona **Ejecutar Visión de Buzón de Entrada**. Esto tarda hasta diez minutos.
5. A continuación, selecciona una baldosa para ver la vista previa con más detalle. Estas vistas previas están agrupadas en estas secciones: **Clientes Web**, **Clientes de Aplicación** y **Clientes Móviles**.

![La opción de seleccionar clientes de correo electrónico para obtener una vista previa.]({% image_buster /assets/img/select_email_preview_inbox_vision.png %}){: style="max-width:85%;"}

{:start="5"}
5\. Selecciona **Ejecutar Visión de Buzón de Entrada**. Esto puede llevar entre dos y diez minutos.

{% alert note %}
Inbox Vision no admite mensajes de correo electrónico que incluyan [lógica de aborto,]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages) ya que estos correos electrónicos se muestran como contenido estático.
{% endalert %}

### Vista previa como usuario

Cuando se realiza una vista previa como usuario aleatorio, Inbox Vision no guarda la configuración ni los atributos específicos del usuario (como el nombre o las preferencias). Cuando seleccionas un usuario personalizado, la vista previa de Inbox Vision puede diferir de otras vistas previas, ya que utiliza datos de usuario específicos.

## Análisis del código

El análisis del código destaca posibles problemas HTML, muestra el número de ocurrencias e indica los elementos HTML no compatibles.

### Visualización de la información de análisis de código

Encuentra esta información en la pestaña **Visión del buzón de entrada** seleccionando **Vista**<i class="fas fa-list"></i> **de lista**. La vista de lista solo está disponible para plantillas de correo electrónico HTML. Para las plantillas de arrastrar y soltar, utiliza las vistas previas para resolver los problemas.

![Ejemplo de análisis de código en la vista previa de Inbox Vision.]({% image_buster /assets/img_archive/inboxvision2.png %})

{% alert note %}
El análisis del código puede aparecer más rápido que la vista previa para un cliente en particular, ya que Braze espera a que llegue el correo electrónico antes de realizar la captura de pantalla.
{% endalert %}

## Pruebas de spam

Las pruebas de correo no deseado predicen si tu correo electrónico acabará en la bandeja de correo no deseado o en el buzón de entrada. Braze realiza pruebas en los principales filtros de correo no deseado (IronPort, SpamAssassin, Barracuda) y en los principales filtros de ISP (Gmail.com, Outlook.com).

### Ver los resultados de las pruebas de correo no deseado

Para comprobar los resultados de la prueba de correo no deseado:

1. Selecciona la pestaña **Pruebas de correo no deseado** en la sección **Visión de la bandeja de entrada**. La tabla de **resultados de la prueba de spam** muestra el nombre, el estado y el tipo del filtro de spam.
2. Revisa estos resultados y realiza los ajustes necesarios en tu campaña de envío por correo electrónico.
3. Selecciona **Reejecutar prueba** para volver a cargar los resultados de tus pruebas de correo no deseado.

## Pruebas de accesibilidad

Las pruebas de accesibilidad ponen de relieve los posibles problemas de accesibilidad en tu correo electrónico y muestran qué elementos no cumplen con los estándares. Braze analiza el contenido según las Pautas de Accesibilidad al Contenido en la Web ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)), un conjunto de normas reconocidas internacionalmente y desarrolladas por el W3C para hacer que el contenido web sea más accesible.

### Cómo funciona

Cuando ejecutas Inbox Vision, Braze comprueba automáticamente los problemas de accesibilidad más comunes del [conjunto de normas WCAG 2.2 AA](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.2&currentsidebar=%23col_customize&levels=aaa) (como la falta de texto alternativo, el contraste de colores insuficiente o la estructura de encabezados inadecuada) y clasifica su gravedad para ayudarte a priorizar las correcciones. 

{% alert important %}
Las pruebas de accesibilidad pueden utilizarse para respaldar los esfuerzos del Cliente por cumplir con normativas o leyes como la [Ley Europea de Accesibilidad](https://www.braze.com/resources/articles/european-accessibility-at-what-it-means-for-marketers); sin embargo, el Cliente reconoce que Braze no ofrece ninguna garantía con respecto a si el uso de las pruebas de accesibilidad satisface o no las obligaciones de cumplimiento del Cliente, y declina toda responsabilidad al respecto.
{% endalert %}

### Visualización de los resultados de las pruebas de accesibilidad

Las pruebas de accesibilidad generan resultados para cada regla como aprobada, fallida o que necesita revisión en la pestaña **Pruebas de accesibilidad**. Braze clasifica cada regla utilizando POUR (Perceptible, Operable, Comprensible, Robusto), los cuatro principios en los que se basan las WCAG.

#### Categorías POUR

El buzón de entrada clasifica los problemas según los cuatro [principios](https://www.w3.org/WAI/WCAG22/Understanding/intro#understanding-the-four-principles-of-accessibility) fundamentales [POUR](https://www.w3.org/WAI/WCAG22/Understanding/intro#understanding-the-four-principles-of-accessibility): Perceptible, operable, comprensible y robusto.

| Principio | Definición |
| --- | --- |
| Perceptible | La información y los componentes de la interfaz de usuario deben presentarse a los usuarios de forma que puedan percibirlos.<br><br>Los usuarios deben poder percibir la información que se presenta (no puede ser invisible para todos sus sentidos). |
| Operable | Los componentes de la interfaz de usuario y la navegación deben ser operables.<br><br>Los usuarios deben poder manejar la interfaz (la interfaz no puede requerir una interacción que el usuario no pueda realizar). |
| Comprensible | La información y el funcionamiento de la interfaz de usuario deben ser comprensibles.<br><br>Los usuarios deben poder comprender la información, así como el funcionamiento de la interfaz de usuario (el contenido o el funcionamiento no pueden exceder vuestra capacidad de comprensión). |
| Robusto | El contenido debe ser lo suficientemente sólido como para que pueda ser interpretado de forma fiable por una amplia variedad de agentes de usuario, incluidas las tecnologías de asistencia.<br><br>Los usuarios deben poder acceder al contenido a medida que avanza el avance tecnológico (a medida que evolucionan las tecnologías y los agentes de usuario, el contenido debe seguir siendo accesible). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Niveles de gravedad

Inbox Vision clasifica los problemas de accesibilidad según su gravedad para ayudarte a priorizar su solución.

| Estado | Definición |
| --- | --- |
| Crítico | Problemas que pueden bloquear el acceso al contenido o la funcionalidad para los usuarios con discapacidades. Estos son los más graves y deben ser priorizados para su reparación. |
| Serias | Problemas que pueden suponer obstáculos importantes, pero que no bloquean completamente el acceso. Estos deben abordarse con prontitud. |
| Moderado | Problemas que pueden causar algunas dificultades a los usuarios con discapacidades, pero que es menos probable que bloqueen el acceso por completo. |
| Menor | Cuestiones que tienen un impacto relativamente bajo en la accesibilidad y que solo pueden causar pequeñas molestias. |
| Necesita revisión | No se puede detectar si hay algún problema o no. Esto puede ocurrir cuando no podemos determinar la relación de contraste porque el texto está colocado sobre una imagen de fondo. Debes revisar manualmente porque no se puede determinar automáticamente. |
| Pasado correctamente | Cumplen con las normas WCAG A, AA o las mejores prácticas de accesibilidad. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
El editor de arrastrar y soltar no admite la configuración de un elemento de`<title>` documento, por lo que el escáner de accesibilidad siempre falla esta comprobación.<br><br>El seguimiento de esta limitación se realiza para futuras mejoras. Si esto afecta a tus flujos de trabajo o a tus usuarios, [comparte tus comentarios]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/#sharing-feedback) para que podamos dar prioridad a las soluciones más importantes.
{% endalert %}

### Comprender las pruebas de accesibilidad automatizadas

{% multi_lang_include accessibility/automated_testing.md %}

## Buenas prácticas

### Revisa tu lista de suscriptores de correo electrónico.

Consulta el [panel de información sobre correos electrónicos]({{site.baseurl}}/user_guide/analytics/dashboard/email_performance_dashboard#email-insights-dashboard) para determinar el tipo de dispositivo y los proveedores más populares entre tus suscriptores en cuanto a interacción. Si necesitas más granularidad, como el navegador, el modelo del dispositivo y más, puedes aprovechar tus datos [de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) o [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder) para recuperar este nivel de detalle sobre la interacción reciente de tus usuarios con el correo electrónico.

De lo contrario, Braze muestra por predeterminado las 20 vistas previas más importantes según datos generales del sector y de expertos, que abarcan la mayor parte de los casos en los que tus suscriptores realizan interacciones con tus correos electrónicos. Si tu análisis de datos apunta a otras vistas previas más populares, puedes definir un conjunto predeterminado de vistas previas cada vez que ejecutes Inbox Vision.

### Selecciona vistas previas significativas y vistas previas afectadas.

Si tu empresa tiene su sede principal en EE. UU., es posible que existan vistas previas específicas, como las vistas previas internacionales,GMX.de que solo utilizan un número reducido de usuarios. Recomendamos dar prioridad y optimizar los buzones de entrada con un impacto considerable en los suscriptores y reservar las vistas previas para los buzones de mayor impacto.

Cuando realices correcciones que afecten a vistas previas específicas, asegúrate de seleccionar solo las vistas previas afectadas para evitar consumir vistas previas que no se utilicen.

### Ejecuta Inbox Vision en la versión final del correo electrónico.

Recomendamos ejecutar Inbox Vision cuando el mensaje de correo electrónico esté listo para su producción o casi listo. Esto te permite reducir el número de vistas previas generadas, ya que el correo electrónico pasa por múltiples iteraciones antes de estar finalizado y listo para enviarse a los usuarios.

Ejecutar Inbox Vision cada vez que realizas una sola edición o cambio puede consumir rápidamente las vistas previas. Te recomendamos que primero realices todos los cambios necesarios en el correo electrónico y, a continuación, ejecutes Inbox Vision para obtener una vista previa de cómo todos tus cambios pueden afectar a la representación de tu correo electrónico en diferentes entornos.

Braze realiza pruebas a través de clientes de correo electrónico reales y se asegura de que las representaciones sean precisas. Si observas un problema recurrente con un cliente, abre un [ticket de soporte]({{site.baseurl}}/braze_support/).
