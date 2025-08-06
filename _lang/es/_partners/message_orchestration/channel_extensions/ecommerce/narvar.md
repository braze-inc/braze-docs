---
nav_title: Narvar
article_title: Narvar
description: "Aprende a integrar Narvar con Braze."
alias: /partners/narvar/
page_type: partner
search_tag: Partner
---

# Narvar

> Narvar es una plataforma post-compra que mejora la fidelización de los clientes mediante el seguimiento de los pedidos, las actualizaciones de las entregas y la gestión de las devoluciones. La integración de Braze y Narvar habilita a las marcas a aprovechar los eventos de notificación de Narvar para desencadenar mensajes directamente desde Braze, manteniendo a los clientes informados con actualizaciones puntuales.

## Requisitos previos

| Requisito           | Descripción                                                                                   |
|-----------------------|-----------------------------------------------------------------------------------------------|
| Cuenta Narvar        | Se requiere una cuenta Narvar para beneficiarse de esta asociación.                           |
| Clave de API REST de Braze    | Una clave de API REST de Braze con permiso de `messages.send`. Puede crearse en el panel Braze desde **Configuración** > **Claves API**.                                            |
| Punto final REST Braze   | [La URL de tu punto final REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints), que depende de la URL de tu instancia de Braze.         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Características compatibles

|Tipo|Características compatibles|
|-------|----------|
| Notificaciones | \- Anticipación de la entrega<br>\- Retraso del operador<br>\- Entregado Estándar |
| Canales | Notificaciones push |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Si te interesan otros tipos o canales de notificación, ponte en contacto con tu CSM de Braze y Narvar.
{% endalert %}

## Detalles de la integración

Para cada evento de notificación, Narvar inicia una solicitud al punto final Braze [`/messaging/send`]({{site.baseurl}}/api/endpoints/messaging) para entregar un mensaje push a cada consumidor con adhesión voluntaria.

Narvar es responsable de configurar las cargas útiles de notificación push para cada mensaje. Actualmente, Narvar no tiene una interfaz de diseño integrada para notificaciones push, por lo que su equipo colaborará con el tuyo para determinar y definir los requisitos de la carga útil. Estas cargas útiles pueden personalizarse en la misma medida que las que se envían a través de tu propio sistema, incluida la compatibilidad con marcadores de posición de contenido variable, como datos de pedidos y detalles de consumidores.

## Introducción a la integración Braze-Narvar

1. **Ponte en contacto con tu CSM de Narvar** para expresar tu interés en la integración.
2. **Designa entornos Braze** para la puesta en escena y la producción.
3. **Genera la clave de API** en Braze para uso de Narvar.
4. **Genera Clave(s) de Campaña** en Braze según sea necesario.
5. **Proporciona claves de API y de campaña** a Narvar a través de un enlace seguro de un solo uso.
6. **Comparte los detalles de la carga útil de la notificación push** para finalizar la configuración.
