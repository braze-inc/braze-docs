---
nav_title: Worthy
article_title: Worthy
description: "Este artículo de referencia describe la asociación entre Braze y Worthy, una plataforma de personalización de mensajes que permite crear experiencias ricas y personalizadas dentro de la aplicación y ofrecerlas a través de Braze."
alias: /partners/worthy/
page_type: partner
search_tag: Partner

---

# Worthy

> La integración de [Worthy](https://worthy.ai/) y Braze te permite crear fácilmente experiencias ricas y personalizadas dentro de la aplicación utilizando el editor de arrastrar y soltar de Worthy y entregarlas a través de Braze. Además, Worthy hará automáticamente lo siguiente:

_Esta integración está mantenida por Worthy._

## Sobre la integración

- Crea un servidor de contenido conectado y una API segura para tu mensajería.
- Construye tus mensajes in-app con análisis y seguimiento de clics que aparecerán directamente en Braze.
- Exporta automáticamente HTML a través del editor de arrastrar y soltar de Worthy para utilizarlo en campañas de mensajes in-app de **código personalizado** en Braze, junto con las conexiones API necesarias y el contenido dinámico que configure.

## Casos prácticos

- Experiencias de bienvenida personalizadas basadas en las selecciones de incorporación del usuario
- Experiencias dentro de la app para eventos especiales y promociones
- Recopilación de opiniones y valoraciones de los clientes basadas en el comportamiento de la aplicación
- Probar rápidamente posibles ideas de productos de aplicaciones
- Avisos, noticias y actualizaciones de la comunidad

## Requisitos previos

| Requisito | Descripción |
| --- | --- |
| Cuenta [Worthy](https://worthy.ai/)  | Se requiere una cuenta Worthy para beneficiarse de esta asociación. |
| SDK Braze | Tendrás que configurar el SDK Braze en tu aplicación móvil para enviar mensajes enriquecidos in-app. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Integración

### Paso 1: Crear mensajes personalizados en Worthy

Ve a tu aplicación en el panel de Worthy, selecciona el **Creador de mensajes** y crea un mensaje personalizado que quieras utilizar para interactuar con tus usuarios.

### Paso 2: Crear una campaña Braze

Crea una [campaña de mensajería dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/) en Braze y establece el **Tipo de mensaje** en **Código personalizado**.

### Paso 3: Copia tu mensaje personalizado en Braze

En el creador de mensajes dignos, haz clic en **Exportar** y selecciona **Braze** para exportar tu mensaje personalizado y utilizarlo en campañas Braze. Copia el contenido exportado en el cuadro de texto HTML en **HTML + Zip de activos** en el editor de campañas Braze.

Eso es todo. Puedes probar inmediatamente tu mensaje personalizado utilizando la pestaña **Prueba** del editor de campañas Braze. 

