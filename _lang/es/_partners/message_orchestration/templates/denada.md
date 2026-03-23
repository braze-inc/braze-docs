---
nav_title: Denada
article_title: Denada
alias: /partners/denada/
description: "Este artículo de referencia describe la asociación entre Braze y Denada, una plataforma creativa de marketing impulsada por IA que te permite crear plantillas de correo electrónico alineadas con tu marca a través de conversación natural y exportarlas directamente a Braze."
page_type: partner
search_tag: Partner
---

# Denada

> [Denada](https://heydenada.com) es una plataforma creativa de marketing impulsada por IA que permite a los expertos en la materia crear materiales de marketing alineados con su marca a través de conversación natural. Con Denada, los equipos pueden pasar de la ideación al contenido de correo electrónico terminado sin necesidad de experiencia en diseño.

_Esta integración es mantenida por Denada._

## Acerca de la integración

La integración de Braze y Denada te permite exportar plantillas de correo electrónico creadas en Denada directamente a Braze, incluyendo la carga automática de imágenes a la biblioteca de medios de Braze. Esto agiliza el proceso de pasar de la ideación creativa a la ejecución de campañas.

## Requisitos previos

Se requiere lo siguiente para usar esta integración:

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de Denada | Se requiere una [cuenta de Denada](https://app.heydenada.com) para usar esta integración. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos completos de **Plantillas**. <br><br>Se puede crear en el panel de Braze desde **Configuración** > **Claves de API**. |
| Punto de conexión REST de Braze | [La URL de tu punto de conexión REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto de conexión depende de la URL de Braze para tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso

Denada está diseñado para especialistas en marketing y expertos en la materia que desean crear contenido de correo electrónico alineado con su marca sin habilidades de diseño o programación. Es ideal para quienes:
- Quieren usar IA conversacional para generar rápidamente plantillas de correo electrónico y enviarlas directamente a Braze
- Necesitan iterar sobre plantillas de correo electrónico existentes en Braze reexportando desde Denada con detección de conflictos y soporte de sobrescritura
- Quieren carga y gestión automática de imágenes en la biblioteca de medios de Braze durante la exportación

## Integración

### Paso 1: Configura tu integración

En Denada, selecciona el nombre de tu empresa en la esquina inferior izquierda y luego selecciona **Team settings** > **Add integration**.

Selecciona **Braze** como la integración, luego introduce tu **clave de API** de Braze y selecciona tu **punto de conexión de la API REST** de la lista de regiones disponibles.

{% alert note %}
Esta es una configuración única. Cuando tus credenciales sean validadas, tu configuración se guardará para todas las exportaciones futuras.
{% endalert %}

### Paso 2: Exporta una plantilla a Braze

En Denada, abre una plantilla de correo electrónico en el editor y selecciona **Export** > **Braze**.

Introduce un nombre de plantilla y una línea del asunto para el correo electrónico. Elige tu preferencia de manejo de imágenes:
- **Upload new:** Carga todas las imágenes a la biblioteca de medios de Braze.
- **Use existing:** Reutiliza imágenes cargadas previamente cuando estén disponibles.

Si ya existe una plantilla con el mismo nombre en Braze, Denada detecta el conflicto y te solicita confirmar si deseas sobrescribir la plantilla existente o crear una nueva.

Selecciona **Export**. Denada renderiza la plantilla a HTML, carga las imágenes a Braze y crea o actualiza la plantilla de correo electrónico en tu cuenta de Braze.

## Uso de la integración

Puedes encontrar tus correos electrónicos de Denada cargados en Braze en **Plantillas y medios** > **Plantillas de correo electrónico**. Están listos para usar en cualquier campaña o Canvas de Braze.

Denada hace seguimiento de las exportaciones anteriores, por lo que las exportaciones posteriores de la misma plantilla pueden actualizar la plantilla existente en Braze en lugar de crear duplicados.