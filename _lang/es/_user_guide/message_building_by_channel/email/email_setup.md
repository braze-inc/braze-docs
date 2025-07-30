---
nav_title: Configuración de correo electrónico
article_title: Configuración del correo electrónico de incorporación
layout: dev_guide
page_order: 1
guide_top_header: "Configuración de correo electrónico"
guide_top_text: "Braze puede ayudarle a empezar a enviar campañas por correo electrónico. Sigue nuestras guías o consulta nuestro curso de Braze Learning sobre <a href='https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability' target='_blank'>Incorporación por correo electrónico</a>."
page_type: landing
description: "Esta página de destino incluye recursos sobre cómo empezar con las campañas de correo electrónico, incluida la configuración de sus IP y dominios, el calentamiento de IP, la validación de correo electrónico y mucho más."
channel: email

guide_featured_title: "Artículos de sección"
guide_featured_list:
- name: "Configuración de IP y dominios"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/
  image: /assets/img/braze_icons/target-05.svg
- name: "Calentamiento de IP"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/ip_warming/
  image: /assets/img/braze_icons/annotation-alert.svg
- name: "Validación de correo electrónico"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/email_validation/
  image: /assets/img/braze_icons/check-square-broken.svg
- name: "Autenticación del correo electrónico"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/authentication/
  image: /assets/img/braze_icons/user-square.svg
- name: "Importar su lista de correo electrónico"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/import_your_email_list/
  image: /assets/img/braze_icons/list.svg
- name: "Descripción general de SSL"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/ssl/
  image: /assets/img/braze_icons/navigation-pointer-01.svg
- name: "Consentimiento y recogida de direcciones"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/consent_and_address_collection/
  image: /assets/img/braze_icons/book-closed.svg
- name: "Trampas de capacidad de entrega y trampas de correo no deseado"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/deliverability_pitfalls_and_spam_traps/
  image: /assets/img/braze_icons/alert-triangle.svg
---

## Requisitos

Antes de empezar a enviar correos electrónicos, hay algunas cosas que necesitas. Consulta el siguiente cuadro para saber más sobre estos requisitos.

| Requisito | Descripción | Fuente |
|---|---|---|
| Una IP (Protocolo de Internet) dedicada| Una IP dedicada es una dirección de Internet única proporcionada exclusivamente a una sola cuenta de alojamiento. | Braze ofrece a sus clientes IP dedicadas, para garantizar el control de la reputación de su remitente de correo electrónico. La incorporación a Braze lo configurará por ti.|
| Dominios con etiqueta blanca | Consisten en un dominio y un subdominio. Al utilizar la etiqueta sin marca, puedes pasar las comprobaciones de autenticación de correo electrónico para DKIM y SPF. | El equipo de Braze Onboarding generará estos dominios para usted, pero deberá elegir sus nombres. |
| Subdominios | Se trata de una subdivisión de un dominio (como "@news.company.com") dentro de su dirección de correo electrónico. Tener un subdominio evitará cualquier error que pueda dañar la reputación del correo electrónico oficial de su empresa. | El equipo de Incorporación lo generará por ti, pero tú debes decidir el nombre del subdominio. No puede utilizar subdominios que se estén utilizando actualmente fuera de Braze. |
| Grupos de IP | Se trata de una configuración opcional que se utiliza para separar la reputación de los distintos tipos de correo electrónico (como "promocional" y "transaccional") para evitar que la reputación de uno afecte al otro y favorecer una mayor entregabilidad. | El equipo de Incorporación configurará los grupos por ti. A continuación, cuando redactes tu correo electrónico, selecciona el grupo de IP de tu correo electrónico en el desplegable **Grupo de IP** de la página **Audiencias objetivo**.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Calentamiento de IP

{% alert important %}
El calentamiento de IP es el **paso más importante** en el proceso de configuración del correo electrónico. Aunque no es el primer paso (de hecho es el último), lo señalamos aquí para que sepas que debes calentar tu dirección IP, o de lo contrario cualquier correo electrónico que envíes será enviado a spam o estará sujeto a otras barreras de envío.
{% endalert %}

[El calentamiento IP]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/) consiste en enviar un número relativamente pequeño de correos electrónicos en el primer lote y, con el tiempo, aumentar ligeramente el volumen en los lotes siguientes hasta alcanzar el volumen diario habitual. Esto se hace al final del proceso de configuración de tu correo electrónico.

Al empezar con volúmenes más pequeños de correo electrónico, está estableciendo un nivel de confianza con su proveedor de correo electrónico, demostrando que sólo envía correos electrónicos a usuarios relevantes. Si envía su primer lote de correos electrónicos a los usuarios más comprometidos, podrá ganarse más rápidamente la confianza de su proveedor.

Cuando hayas terminado de calentar tu IP, podrás [empezar a crear y enviar correos electrónicos]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/).

<br><br>