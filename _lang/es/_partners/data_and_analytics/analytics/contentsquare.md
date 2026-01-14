---
nav_title: Contentsquare
article_title: Contentsquare
description: "Este artículo de referencia describe la asociación entre Braze y Contentsquare, una plataforma de análisis de la experiencia digital que le permite mejorar la relevancia y las tasas de conversión de sus campañas mediante la orientación de los mensajes en función de la experiencia digital de sus clientes."
alias: /partners/contentsquare/
page_type: partner
search_tag: Partner

---

# Contentsquare

> [Contentsquare](https://contentsquare.com/) es una plataforma de análisis de la experiencia digital que permite una comprensión sin precedentes de la experiencia del cliente.

_Esta integración es mantenida por Contentsquare._

## Sobre la integración

La integración de Braze y Contentsquare le permite enviar señales en directo (fraude, señales de frustración, etc.) como eventos personalizados en Braze. Aproveche la información sobre la experiencia de Contentsquare para mejorar la relevancia y las tasas de conversión de sus campañas dirigiendo los mensajes en función de la experiencia digital y el lenguaje corporal de sus clientes.

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Contentsquare | Se requiere una cuenta Contentsquare para beneficiarse de esta asociación. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos `users.track`. Para crear una nueva clave en el panel de Braze, ve a **Configuración** > **Claves de API**. |
| Punto final REST Braze | [Tu URL del punto final REST]({% image_buster /assets/img/contentsquare_custom_events.png %}). Tu punto final dependerá de la URL Braze de tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos prácticos

Algunos casos habituales de uso de Braze y Contentsquare son:
- Mensajes hiperpersonalizados basados en la intención del cliente haciendo aflorar los datos de la experiencia del cliente en Braze.
- Reorienta a los clientes en función de su comportamiento digital, sus dudas, su frustración y su intención.
- Identifique las malas experiencias dentro de Contentsquare y recupere a los clientes con mensajes específicos y ofertas de retención.
- Recupere a los clientes en riesgo enviándoles mensajes más pertinentes y empáticos en el momento y lugar adecuados.

## Integración

Para integrar Contentsquare en Braze, debe solicitar la instalación de una integración "Live Signals" desde el catálogo de integraciones de Contentsquare:

1. En Contentsquare, haz clic en **Consola** en el menú **Configuración**. Esto le redirigirá al proyecto en el que está trabajando actualmente. 
2. En la página **Proyectos**, vaya a la pestaña **Integraciones** y haga clic en el botón **\+ Añadir integración**.
3. En el catálogo de integraciones, localice la integración **Señales en directo** y haga clic en **Añadir**. El equipo de Contentsquare se pondrá en contacto con usted para configurar el fragmento de código y enviar señales en directo a Braze.
4. Contentsquare procesará ahora su integración. El texto del indicador se actualizará una vez finalizada la integración.

Para más información, consulta [Solicitar una integración de Contentsquare](https://uxanalyser.zendesk.com/hc/en-gb/articles/4405613239186).

## Mediante esta integración

Una vez completada la integración, los eventos personalizados de Contentsquare estarán disponibles para ser utilizados en tus campañas y Canvases. Puedes comprobar qué eventos se envían a Braze desde **Configuración de datos** > **Eventos personalizados**.

![Datos de señales en vivo de Contentsquare en la pestaña de eventos personalizados de Braze]({% image_buster /assets/img/contentsquare_custom_events.png %})


