---
nav_title: Configuración del correo electrónico
article_title: Configuración del correo electrónico de incorporación
layout: dev_guide
page_order: 1
guide_top_header: "Configuración del correo electrónico"
guide_top_text: "Braze puede ayudarte a empezar a enviar campañas por correo electrónico. Sigue nuestras guías o consulta nuestro curso de Braze Learning <a href='https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability' target='_blank'>sobre incorporación por correo electrónico</a>."
page_type: landing
description: "Esta página de destino incluye recursos sobre cómo empezar con las campañas de correo electrónico, incluida la configuración de tus IP y dominios, el calentamiento de IP, la validación del correo electrónico y mucho más."
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
- name: "Autenticación de correo electrónico"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/authentication/
  image: /assets/img/braze_icons/user-square.svg
- name: "Importar tu lista de correo electrónico"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/import_your_email_list/
  image: /assets/img/braze_icons/list.svg
- name: "Resumen de SSL"
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

Antes de empezar a enviar correos electrónicos, necesitas algunas cosas. Consulta el siguiente cuadro para saber más sobre estos requisitos.

| Requisito | Descripción | Fuente |
|---|---|---|
| Una IP (Protocolo de Internet) dedicada| Una IP dedicada es una dirección de Internet única proporcionada exclusivamente a una sola cuenta de alojamiento. | Braze te proporciona IP dedicadas para garantizar el control de la reputación del remitente de tu correo electrónico. La incorporación a Braze lo configurará por ti.|
| Dominios con etiqueta sin marca | Constan de un dominio y un subdominio. Al utilizar la etiqueta sin marca, puedes pasar las comprobaciones de autenticación de correo electrónico para DKIM y SPF. | El equipo de incorporación de Braze generará estos dominios por ti, pero tú debes elegir sus nombres. |
| Subdominios | Es una subdivisión de un dominio (como "@news.company.com") dentro de tu dirección de correo electrónico. Tener un subdominio evitará cualquier error que pueda dañar la reputación del correo electrónico oficial de tu empresa. | El equipo de Incorporación lo generará por ti, pero tú debes decidir el nombre del subdominio. No puedes utilizar subdominios que se estén utilizando actualmente fuera de Braze. |
| Grupos de IP | Se trata de una configuración opcional que se utiliza para separar la reputación de distintos tipos de correo electrónico (como "promocional" y "transaccional") para evitar que la reputación de uno afecte al otro y favorecer una mayor capacidad de entrega. | El equipo de Incorporación configurará los grupos por ti. Después, al redactar tu correo electrónico, puedes ver el grupo de IP de tu correo electrónico en el paso **Audiencias objetivo**.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Calentamiento de IP

{% alert important %}
El calentamiento de IP es el **paso más importante** en el proceso de configuración del correo electrónico. Aunque no es el primer paso (en realidad es el último), lo señalamos aquí para que sepas que debes calentar tu dirección IP, o de lo contrario cualquier correo electrónico que envíes se enviará a correo no deseado o estará sujeto a otras barreras de envío.
{% endalert %}

[El calentamiento de IP]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/) es cuando envías un número relativamente pequeño de correos electrónicos en tu primer lote, y luego, con el tiempo, aumentas ligeramente el volumen en los lotes siguientes hasta que alcanzas tu volumen diario típico. Esto se hace al final del proceso de configuración de tu correo electrónico.

Al empezar con volúmenes más pequeños de correo electrónico, estás estableciendo un nivel de confianza con tu proveedor de correo electrónico, demostrando que sólo envías correos electrónicos a usuarios relevantes. Enviar tu primer lote de envíos por correo electrónico a tus usuarios más comprometidos puede ayudarte a ganar confianza más rápidamente con tu proveedor.

Cuando hayas terminado de calentar tu IP, ¡podrás [empezar a crear y enviar correos electrónicos]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/)!

<br><br>
