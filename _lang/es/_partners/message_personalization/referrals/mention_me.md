---
nav_title: Mencióname
article_title: Integración de Mention Me con Braze
description: Guía de configuración de la integración de Mention Me
alias: /partners/mention_me/
page_type: partner
search_tag: Partner
---

# Mencióname

> Juntos, [Mention Me](https://www.mention-me.com/) y Braze pueden ser tu puerta de entrada para atraer a clientes premium y fomentar una fidelización inquebrantable a la marca. Al integrar fácilmente datos propios de referidos en Braze, puedes entregar experiencias omnicanal altamente personalizadas dirigidas a los fans de tu marca.

_Esta integración está mantenida por Mention Me._

## Requisitos previos

Antes de empezar, necesitarás lo siguiente:

| Requisito previo          | Descripción                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Una cuenta Mencióname   | Es necesario tener una cuenta [Mencióname](https://mention-me.com/login) para beneficiarse de esta asociación.                                                                     |
| Una clave de API REST Braze  | Una clave de API REST Braze con permisos `users.track` y `templates.email.create`. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Un punto final REST Braze | [La URL de tu punto final REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto final dependerá de la URL Braze de tu instancia.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Ejemplos

* Envía datos de contacto y adhesiones voluntarias de clientes referidos de Mention Me a Braze en tiempo real.
* Utiliza los datos de los referidos para crear recordatorios de cupones por correo electrónico
* Mejora el rendimiento de otros canales de marketing utilizando datos de referidos para segmentar y dirigirte a clientes de alto valor.

## ¿Qué datos se envían desde Mencióname a Braze?

Cuando configures esta integración, Mention Me creará automáticamente tus atributos y eventos del cliente, por lo que no tendrás que hacerlo de antemano.

Las direcciones de correo electrónico de tus clientes en Braze se utilizarán para vincular eventos y atributos personalizados relevantes. Mention Me enviará eventos y atributos del perfil de contacto de cualquier cliente potencial o existente que desencadene este evento a través de Mention Me, independientemente de su estado de adhesión voluntaria.

Para más detalles, consulta [Atributos y eventos del perfil de contacto](https://help.mention-me.com/hc/en-gb/articles/26677937177501-What-Mention-Me-data-is-sent-to-Braze).

## Integración de Mention Me

{% alert tip %}
Para una guía completa paso a paso, consulta [la documentación de configuración de Braze de Mention Me](https://help.mention-me.com/hc/en-gb/articles/26151773368221-How-to-setup-Braze-with-Mention-Me).
{% endalert %}

Para integrar Mention Me con Braze:

1. En Mencióname, ve a la página de [integración de Braze](https://mention-me.com/merchant/~/integrations/braze) y, a continuación, selecciona **Conectar**.
2. Selecciona **Crear nueva autorización**, luego añade la [clave de API que creaste anteriormente](#prerequisites) y selecciona tu instancia de Braze.
3. Elige uno o varios países con los que quieras sincronizarte.
4. Cuando hayas terminado, selecciona **Conectar**.
