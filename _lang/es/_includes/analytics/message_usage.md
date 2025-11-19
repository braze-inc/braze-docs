# Panel de uso de mensajes

> El panel de uso de mensajes proporciona información de autoservicio sobre tu uso de crédito de SMS, RCS y WhatsApp para obtener una visión completa del uso histórico y actual comparado con las asignaciones del contrato. Esta información puede reducir tu confusión y ayudarte a hacer ajustes para evitar riesgos de excedente.

El panel de **Uso de Mensajes** está dividido en tres secciones:
- [Resumen del uso del crédito](#credit-usage-overview)
- [SMS/MMS](#smsmms) 
- [WhatsApp](#whatsapp)

Accede al panel yendo a **Configuración** > **Facturación** > **Uso de mensajes**.

## Resumen del uso de los créditos para mensajes

**El resumen de uso de créditos de mensajes** proporciona un resumen del uso en todos los canales que utilizan créditos. Puedes ver cómo vas con respecto a tu asignación total de crédito, y encontrar detalles sobre tu contrato activo y tu periodo de contrato.

Esta página se muestra si tienes un contrato de créditos por mensajes. Los canales que utilizan créditos de mensajes se muestran en el **resumen del contrato Créditos**.

{% alert note %}
Si has comprado WhatsApp pero no tienes un contrato de créditos de mensajes, seguirás viendo el consumo de créditos de WhatsApp porque así es como se facturan los contratos de WhatsApp antiguos. Esto difiere de los SMS tradicionales, que sólo consumen créditos cuando tienes un contrato de créditos de mensajes.
{% endalert %}

Los datos **generales de uso de los créditos de mensajes** se limitan al periodo del contrato, que se muestra en el **resumen del contrato de créditos**. No puedes filtrar por un intervalo de fechas fuera del **periodo de Créditos**.

### Uso de créditos de mensajes por contrato

El gráfico **Uso de créditos de mensajes durante el contrato** muestra tu uso durante el periodo de tiempo seleccionado. La granularidad de este gráfico depende del marco temporal que hayas seleccionado. Exporta las opciones de exportación seleccionando el menú de la esquina superior derecha del gráfico.

![Panel general de uso de créditos para mensajes con secciones para el uso de créditos, resumen del contrato de créditos y consumo de créditos sobre el contrato.]({% image_buster /assets/img/app_settings/credit_usage_over_contract1.png %}){: style="max-width:70%;"}

## SMS, MMS y RCS

**SMS/MMS/RCS Uso de créditos** muestra el desglose de uso del canal SMS, MMS y RCS. Las columnas de la tabla de datos generalmente requieren que hayas comprado Créditos para mensajes (aunque Braze aún admite temporalmente modelos de facturación más antiguos), y las columnas **Ratio de crédito** y **Créditos** indican la tasa del país respectivo y los créditos consumidos. Además, los mosaicos de alto nivel indicarán el consumo total de SMS y, si procede, de MMS en el intervalo de fechas seleccionado.

Hay filtros disponibles que te permiten filtrar por **País** o por tipo de SMS y RCS.

![SMS/MSS/RCS Utilización de créditos con mosaicos para los datos de alto nivel y una sección para el consumo por cuenta.]({% image_buster /assets/img/app_settings/sms_credit_consumption2.png %}){: style="max-width:70%;"}

A diferencia del **Resumen de uso de créditos para mensajes**, esta sección contiene datos históricos de periodos contractuales anteriores. 

{% alert note %}
Es posible seleccionar un intervalo de fechas que contenga tanto el uso sin créditos como el uso con créditos de los mensajes. En este caso, el consumo que se haya producido fuera de los créditos del mensaje mostrará `—` (nulo) en las columnas **Ratio de créditos** y **Créditos**.
{% endalert %}

![SMS/MMS/RCS Tabla de utilización de créditos con valores nulos.]({% image_buster /assets/img/app_settings/sms_table_null3.png %}){: style="max-width:70%;"}

## WhatsApp

**Uso de créditos de WhatsApp** muestra el desglose de uso del canal WhatsApp. Los mosaicos muestran el uso total de crédito de WhatsApp, que puede desglosarse en la sección **Uso por cuenta** aplicando filtros para limitar los resultados de la tabla de datos a un espacio de trabajo concreto.

### Filtros

Puedes filtrar tus datos por:
- País
- Cuenta de WhatsApp Business
- Espacio de trabajo de Braze
- Tipo de categoría de conversación
- Región

![Uso de créditos de WhatsApp con un mosaico para el total de créditos consumidos y una tabla de uso por cuenta.]({% image_buster /assets/img/app_settings/whatsapp_credit_consumption4.png %}){: style="max-width:70%;"}

## Lo que hay que saber

{% alert important %}
Los datos que se muestran en el panel de **Uso de mensajes** son a nivel de contrato y no se limitan a una empresa o espacio de trabajo individual del panel. Estos datos reflejan el uso de todos los espacios de trabajo de tu panel, y potencialmente de todos los paneles (si tienes varios).
{% endalert %}

- Los datos subyacentes se proporcionan en una cadencia diaria, con las tablas de datos actualizadas a las 3 am, 9 am, 12 pm y 6 pm EST. 
- Braze sigue la metodología estándar de redondeo: las cifras se redondean a la décima más próxima.