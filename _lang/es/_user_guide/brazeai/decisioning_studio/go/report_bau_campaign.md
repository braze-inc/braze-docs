---
nav_title: Informe sobre la campaña BAU
article_title: Informar sobre la campaña BAU
page_order: 10
description: "Este artículo ofrece respuestas a las preguntas más frecuentes sobre la elaboración de informes de una campaña Business as Usual (BAU) en el portal BrazeAI Decisioning Studio Go."
---

# Reportaje sobre la campaña Business as Usual

> Este artículo ofrece respuestas a las preguntas más frecuentes sobre la elaboración de informes de una campaña Business as Usual (BAU) en el portal BrazeAI Decisioning Studio™ Go.

## Acerca de informar sobre la campaña BAU

De forma predeterminada, el informe del portal BrazeAI Decisioning Studio™ Go comparará los grupos BrazeAI Decisioning Studio™ Go y de control aleatorio. Además de comparar estos dos grupos, puede que tengas un grupo Business as Usual (también conocido como BAU) con el que te gustaría comparar el rendimiento de BrazeAI Decisioning Studio™ Go. Al configurar los informes BAU, puedes ver el rendimiento de los tres grupos en un único lugar en el portal BrazeAI Decisioning Studio™ Go.

La principal ventaja de configurar los informes BAU es la aplicación del filtrado de clics no válidos de BrazeAI Decisioning Studio™ Go, que, cuando se aplica a los tres grupos del experimento, permite la comparación más precisa y justa (o "manzanas con manzanas") del rendimiento de los clics, al eliminar cualquier ruido adicional de los clics sospechosos de la máquina y los clics al enlace de cancelar suscripción.

## Requisitos

Antes de configurar los informes BAU, asegúrate primero de que existe una comparación equitativa entre el grupo de tratamiento BAU, el BrazeAI Decisioning Studio™ Go y el grupo de control aleatorio. Esto incluye comprobar que:

- Ningún destinatario puede pertenecer a más de un grupo (durante toda la duración del experimento).
- Los destinatarios se asignan aleatoriamente a los grupos, de forma que no haya sesgos en las asignaciones de los grupos.
- Cualquier opción disponible para el grupo BAU (creativa, frecuencia, tiempo, incentivo u oferta) está disponible para el grupo BrazeAI Decisioning Studio™ Go y el grupo de control aleatorio

Sin un diseño experimental "manzanas con manzanas", los informes BAU pueden ser confusos o engañosos.

Una vez que hayas validado el diseño de tu experimento, se necesitan los siguientes datos para configurar los informes BAU:
- Uno o varios ID de campaña de tu plataforma de activación integrada (Braze, Salesforce Marketing Cloud o Klaviyo) en la que todas las comunicaciones de la campaña sean comunicaciones BAU.
    - Para Braze, se aceptan campañas y lonas
    - Para Salesforce Marketing Cloud, sólo se aceptan Journeys
    - Para Klaviyo, sólo se aceptan Flujos
- Un ID de audiencia de tu plataforma de activación integrada que hace un seguimiento diario de los destinatarios que forman parte de la audiencia BAU
    - Para Braze, sólo se aceptan segmentos
    - Para Salesforce Marketing Cloud, sólo se aceptan extensiones de datos
    - Para Klaviyo, sólo se aceptan segmentos

Si no tienes una audiencia existente que haga un seguimiento de tu audiencia BAU, debes crear una.

{% alert note %}
**Sólo para clientes de Braze:** Asegúrate de que tu exportación de Braze Currents a BrazeAI Decisioning Studio™ Go incluye datos de tus campañas BAU.
{% endalert %}

## Consideraciones

De forma similar a BrazeAI Decisioning Studio™ Go más general, los informes BAU sólo cubren los KPI de clics, no los de conversión.

En este momento, no podemos filtrar por ID de pasos en Canvas específicos. Los eventos de todos los pasos en Canvas se incluirán en los datos BAU. Ten en cuenta que esto puede invalidar las comparaciones con BAU si sólo se incluyen determinados pasos en Canvas.

## Configurar una campaña BAU 

Sigue las instrucciones de tu portal BrazeAI Decisioning Studio™ Go. Debes tener uno o varios [ID de campaña y un ID de audiencia](#what-are-the-requirements-to-use-in-portal-bau-reporting).