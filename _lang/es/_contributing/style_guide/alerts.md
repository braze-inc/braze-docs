---
nav_title: Alertas
article_title: Buenas prácticas para alertas
description: "Información, directrices y ejemplos para los tipos de alertas utilizados en la documentación de Braze."
page_order: 2
noindex: true
---

# Buenas prácticas para alertas

> Este documento contiene información, directrices generales y ejemplos para los tipos de alertas utilizados en la documentación de Braze.

## Tipos de alertas {#alert-types}

Las alertas categorizan información que el lector debería conocer. Hay cuatro tipos de alertas que se pueden utilizar en nuestra documentación:

* Importante  
* Nota  
* Consejo  
* Advertencia

## Cuándo usar una alerta {#when-to-use-an-alert}

Usa alertas para llamar la atención del lector sobre información importante. Mantén el contenido breve y directo. Queremos asegurarnos de que la información quede grabada en el lector.

Consulta la siguiente tabla para ver las definiciones de cada alerta:

<style>
.style-guide-table td {
  overflow-wrap: break-word;
  word-break: break-word;
  min-width: 0;
}
</style>

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<colgroup><col style="width: 20%;"><col style="width: 80%;"></colgroup>
<thead>
<tr><th>Tipo de alerta</th><th>Definición</th></tr>
</thead>
<tbody>
<tr><td>Importante</td><td>Incluye información esencial que el lector <strong>debería</strong> tener en cuenta, como: <ul><li>Características obsoletas</li><li>Impactos en la facturación</li><li>Información relacionada con actualizaciones relevantes</li><li>Advertencias urgentes sobre características (ej.: características en fase beta)</li><li>Otros datos importantes</li></ul></td></tr>
<tr><td>Nota</td><td>Incluye información puntual que el lector debería conocer, como: <ul><li>Advertencias sobre características</li><li>Orientación sobre formato</li><li>Llamadas de atención útiles</li><li>Información que se ha degradado desde una alerta Importante debido a que la gravedad del contenido ha disminuido (ej.: una alerta importante de larga data que pasa a ser una nota estándar)</li></ul></td></tr>
<tr><td>Consejo</td><td>Incluye conocimiento complementario y recomendaciones que el lector debería tener en cuenta, como: <ul><li>Artículos adicionales de solución de problemas</li><li>Pasos y atajos que ayudan a mejorar la usabilidad (ej.: personalización adicional para mensajes dentro de la aplicación)</li></ul></td></tr>
<tr><td>Advertencia</td><td>Incluye información esencial que el lector debe abordar y puede incluir: <ul><li>Consecuencias irreversibles (ej.: eliminación de campañas y Canvas)</li><li>Comportamiento que rompe la funcionalidad</li><li>Pérdida de datos</li><li>Otras advertencias cruciales</li></ul></td></tr>
</tbody>
</table>
{:/}

**Buenas prácticas para alertas**  
Aquí tienes directrices generales y buenas prácticas para las alertas.

Como regla general, evita usar alertas para contenido que sea esencial para la estructura del artículo (como introducciones de características, instrucciones de configuración y pasos para usar una característica). En caso de duda, consulta con el equipo durante la revisión entre pares.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<colgroup><col style="width: 50%;"><col style="width: 50%;"></colgroup>
<thead>
<tr><th>Directriz</th><th>Ejemplo</th></tr>
</thead>
<tbody>
<tr><td>Explica la información de la alerta en una declaración clara y concisa.</td><td>{% multi_lang_include alerts/note_alerts.md alert='Segment profiles first app use' %}<br><br> <a href="{{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment">Alerta de nota en el paso 4: sección Añadir filtros a tu segmento</a></td></tr>
<tr><td>Para alertas que aplican a diferentes secciones del mismo artículo, considera crear una nueva sección que capture estos detalles para evitar contenido repetitivo.</td><td>{% multi_lang_include currents/property_details_dispatch_state_source.md %}<br><br> <a href="{{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#subscription-group-state-change-events">Detalles de propiedades en eventos de interacción con mensajes</a></td></tr>
<tr><td>Separa la información en párrafos cortos o listas dentro de la alerta.</td><td>{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}<br><br> <a href="{{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/import_your_email_list/">Alerta importante en Importar tu lista de correo electrónico</a></td></tr>
<tr><td>Considera cualquier formato adicional que pueda afectar cómo se muestra la alerta (fragmentos de código, pasos, imágenes circundantes y más).</td><td>{% multi_lang_include alerts/tip_alerts.md alert='catalog data images' %}<br><br> <a href="{{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications/#considerations">Alerta de consejo con fragmento de código en Notificaciones de bajada de precio</a></td></tr>
<tr><td>Incluye un salto de línea para las alertas que comienzan un artículo.</td><td><img src="{% image_buster /assets/img/contributing/style_guide/alert_5.png %}" alt="Ejemplo de una alerta al inicio de un artículo."><br><br> <a href="{{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/implementation_guide/">Guía de implementación de tarjetas de contenido</a></td></tr>
<tr><td>Al escribir sobre características en fase beta, incluye una alerta Importante que destaque el estado beta y la información de contacto de Braze correspondiente. Coloca esta alerta beta después del texto de resumen y antes del primer encabezado principal.</td><td><img src="{% image_buster /assets/img/contributing/style_guide/alert_6.png %}" alt="Ejemplo de una alerta importante para una característica en fase beta."></td></tr>
<tr><td>Evita usar dos o más alertas seguidas si es posible. En su lugar, reorganiza o incluye la información como parte del texto.</td><td><img src="{% image_buster /assets/img/contributing/style_guide/alert_7.png %}" alt="Un ejemplo de dos alertas juntas, lo cual deberías evitar."></td></tr>
<tr><td>Si tu alerta es extensa, considera crear una nueva sección que incluya la información como una lista. Por ejemplo, en lugar de incluir pasos de solución de problemas en una alerta, considera crear una sección de solución de problemas o proporcionar un enlace a un artículo relacionado.</td><td><img src="{% image_buster /assets/img/contributing/style_guide/alert_8.png %}" alt="Ejemplo de una nueva sección de contenido."></td></tr>
</tbody>
</table>
{:/}

## Ejemplos de alertas {#alert-examples}

Consulta los siguientes ejemplos para ver cómo y por qué se usa cada tipo de alerta en nuestra documentación.

### Alerta importante {#important-alert}

{% multi_lang_include alerts/important_alerts.md alert='Web push private browsing' %}

* **Artículo:** [Push para Web]({{site.baseurl}}/user_guide/message_building_by_channel/push/web/)
* **Caso de uso:** Incluye una advertencia esencial sobre la característica que el lector debería conocer al configurar su notificación push web.
* **Razonamiento de la alerta:** Usa una alerta Importante en lugar de una alerta de Nota porque la importancia del contenido es mayor para que el lector lo conozca al configurar su notificación push web.

{% multi_lang_include alerts/important_alerts.md alert='BCC address billable emails' %}

* **Artículo:** [Configuración de correo electrónico]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/)
* **Caso de uso:**
  - Proporciona una advertencia importante sobre la posibilidad de duplicar los correos electrónicos facturables
  - Redirige al lector para que se ponga en contacto con su administrador del éxito del cliente según sea necesario
* **Razonamiento de la alerta:** La alerta Importante se usa aquí para comunicar detalles sobre las direcciones BCC en la configuración de correo electrónico. Esta información se presenta mejor usando una alerta Importante en lugar de una alerta de Advertencia porque omitir esta información no afecta la característica de forma irreversible (como romper la funcionalidad o pérdida permanente de datos).

{% multi_lang_include alerts/important_alerts.md alert='Android notification priority' %}

* **Artículo:** [Configuración avanzada de campaña]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/advanced_campaign_settings/#notification-display-priority)
* **Caso de uso:** Incluye una advertencia urgente sobre la prioridad de notificación. Redirige al lector a nueva información disponible.
* **Razonamiento de la alerta:** La alerta Importante es la mejor opción aquí para redirigir al lector a información actualizada y para destacar que la sección aplica solo a ciertos usuarios. También se coloca después del encabezado de la sección, lo que obliga al usuario a abordar la alerta importante antes de leer el resto de la sección.

### Alerta de nota {#note-alert}

{% multi_lang_include alerts/note_alerts.md alert='Content Cards frequency capping' %}

* **Artículo:** [Crear una tarjeta de contenido]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/)
* **Caso de uso:** Incluye información adicional que el lector debería conocer a medida que aprende más sobre las Tarjetas de contenido.
* **Razonamiento de la alerta:** Esta alerta de Nota proporciona información de contexto sobre cómo Braze rota las Tarjetas de contenido más antiguas para los usuarios. Esta es información complementaria útil para que el lector la tenga en cuenta y no requiere el uso de una alerta Importante o de Consejo.

{% multi_lang_include alerts/note_alerts.md alert='Custom Attributes time attribute' %}

* **Artículo:** [Atributos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/)
* **Caso de uso:** Incluye información general que el lector debería conocer. Proporciona un artículo para aprender más sobre contenido relacionado (atributos de tiempo).
* **Razonamiento de la alerta:** Esta información se transmite mejor usando una alerta de Nota en lugar de una alerta Importante porque el contenido está dirigido a proporcionar información general. Ignorar esta información no afectaría la facilidad de uso de esta característica.

{% multi_lang_include alerts/note_alerts.md alert='Manage custom data storage' %}

* **Artículo:** [Administrar datos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data/#managing-properties)
* **Caso de uso:** Incluye información general que el lector debería conocer. Redirige al contacto de Braze para obtener más información.
* **Razonamiento de la alerta:** Esta alerta de Nota proporciona información adicional sobre el almacenamiento de datos que sería útil para que el lector la conozca al administrar sus atributos personalizados. Sin embargo, el contenido no requiere una indicación más fuerte de importancia para el lector, por lo que una alerta de Nota es aceptable aquí.

### Alerta de consejo {#tip-alert}

{% multi_lang_include alerts/tip_alerts.md alert='SMS segment calculator' %}

* **Artículo:** [Calculadoras de facturación de SMS y RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/)
* **Caso de uso:** Incluye una herramienta para que el lector comprenda la longitud de su mensaje y el recuento de segmentos SMS. Proporciona información que puede ser útil para que el lector entienda los límites de texto.
* **Razonamiento de la alerta:** Esta es una alerta de Consejo extensa porque proporciona un espacio para ingresar el texto y ver cuántos segmentos envía un mensaje. La alerta de Consejo es la mejor opción aquí porque es un generador útil para que el lector lo use en el proceso de configuración de sus mensajes SMS.

{% multi_lang_include alerts/tip_alerts.md alert='Export troubleshooting' %}

* **Artículo:** [Exportar KPIs de desinstalaciones diarias de la aplicación por fecha]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/)
* **Caso de uso:** Proporciona consejos de solución de problemas al usar este punto de conexión.
* **Razonamiento de la alerta:** La alerta de Consejo proporciona soporte adicional para el lector. Usa una alerta de Consejo en lugar de una alerta de Nota porque el enfoque del contenido es ayudar al lector proporcionando el artículo de solución de problemas.

### Alerta de advertencia {#warning-alert}

{% multi_lang_include alerts/warning_alerts.md alert='User profile external_id' %}

* **Artículo:** [Ciclo de vida del perfil de usuario]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/)
* **Caso de uso:** Indica algo que el lector no debería hacer al crear sus perfiles de usuario en Braze.
* **Razonamiento de la alerta:** La alerta de Advertencia se usa para prevenir al lector de asignar un external_id antes de identificarlos de forma única. Esta información se transmite mejor usando una alerta de Advertencia en lugar de una alerta Importante porque incluye consecuencias irreversibles para el perfil de usuario.

{% multi_lang_include alerts/warning_alerts.md alert='Segment Currents multiple connectors' %}

* **Artículo:** [Segment para Currents]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_for_currents/)
* **Caso de uso:** Advierte al lector al crear conectores de Currents. Incluye la consecuencia de crear estos conectores incorrectamente.
* **Razonamiento de la alerta:** La alerta de Advertencia es la mejor opción aquí para describir las limitaciones de la integración de Braze Segment Currents. Usa una alerta de Advertencia en lugar de una alerta Importante porque crear más de un conector de Currents del mismo tipo incorrectamente puede resultar en pérdida de datos.

{% multi_lang_include alerts/warning_alerts.md alert='Canvas race condition audience trigger' %}

* **Artículo:** [Crear un Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)
* **Caso de uso:** Enumera la información que puede causar que la característica no funcione. Detalla cómo la audiencia prevista puede no recibir la campaña o entrar en el Canvas.
* **Razonamiento de la alerta:** La alerta de Advertencia se usa aquí para señalar cómo la característica puede funcionar incorrectamente. Esta información se transmite mejor usando una alerta de Advertencia en lugar de una alerta Importante porque la información es crítica y puede resultar en la interrupción de la entrega del Canvas.