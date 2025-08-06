---
nav_title: Monstruo del buzón de entrada
article_title: Monstruo del buzón de entrada
alias: /partners/inbox_monster/
description: "Este artículo de referencia describe la asociación entre Braze e Inbox Monster, una herramienta de marketing por correo electrónico en línea que permite a los clientes de Braze obtener información sobre la capacidad de entrega y análisis creativos para aumentar el rendimiento de la bandeja de entrada."
page_type: partner
search_tag: Partner

---

# Monstruo del buzón de entrada

> [Inbox Monster](https://inboxmonster.com/) es una plataforma de señales de buzón de entrada que ayuda a las marcas empresariales a aterrizar cada envío. Es una línea integrada de soluciones de capacidad de entrega, renderización creativa y monitorización de SMS, que capacita a los equipos modernos de administración de las relaciones con el cliente (CRM) y acaba con los sustos de los envíos.

La integración de Braze e Inbox Monster te permite eliminar las pruebas manuales de listas de semillas, automatizar la creación de señales potentes y procesables de colocación en la bandeja de entrada, simplificar el proceso de revisión y aprobación de activos creativos de correo electrónico y obtener valiosas informaciones de capacidad de entrega. También puedes importar fácilmente plantillas de correo electrónico para diagnósticos creativos y vistas previas de dispositivos.

## Requisitos previos

| Requisito                    | Descripción                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cuenta de la plataforma Inbox Monster | Se requiere una cuenta en la plataforma Inbox Monster para beneficiarse de esta asociación.                                                                                                                                                                                                                                                                                                                                                                 |
| Clave de API REST de Braze             | Una clave Braze REST API con los siguientes permisos:  <br> - `messages.send` <br>  - `templates.email.create`<br> - `templates.email.update` <br> - `templates.email.info`<br> - `templates.email.list` <br><br> Y con las siguientes IP de la lista blanca: <br> - `3.136.16.19` <br>  - `3.140.233.31`<br> - `18.220.127.138` <br><br> Se puede crear en el panel de Braze desde **Configuración** > **API e identificadores** en la pestaña **Claves de API**  |
| Identificador de la aplicación Braze           | Un identificador de aplicación Braze. <br><br>Puedes encontrarlo en el panel de Braze, en **Configuración** > **API e identificadores**, en la pestaña **Identificadores de aplicaciones**.                                                                                                                                                                                                                                                                                                |
| Punto final Braze                 | [Tu punto final Braze]({{site.baseurl}}/api/basics/#endpoints) se alinea con la URL de tu panel Braze.<br><br> Por ejemplo, si la URL de tu panel es `https://dashboard-03.braze.com`, tu punto final será `dashboard-03`.                                                                                                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Integración

Para integrar Inbox Monster, sigue los pasos de [Integración con Inbox Monster](https://intercom.help/inbox-monster/en/articles/9518204-scheduled-placement-tests-with-braze#h_80147afaf3).

## Uso

Para saber cómo enviar pruebas de nivel de buzón de entrada programadas a través de Inbox Monster, consulta [Pruebas de nivel de buzón de entrada programadas](https://intercom.help/inbox-monster/en/articles/9518204-scheduled-placement-tests-with-braze#h_7e74bc474e).
