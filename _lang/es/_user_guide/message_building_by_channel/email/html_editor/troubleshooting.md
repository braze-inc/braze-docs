---
nav_title: Solución de problemas
article_title: Solución de problemas
page_order: 9
description: "Este artículo de ayuda te explica cómo solucionar problemas con los correos electrónicos HTML."
channel: email
---

# Solución de problemas 

## El HTML se muestra incorrectamente en los correos electrónicos de prueba

Si tu [correo electrónico de prueba]({{site.baseurl}}/developer_guide/platform_wide/sending_test_messages/#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa) no parece correcto, te recomendamos que compruebes primero tu configuración HTML. A continuación, puedes comprobar si existen estos problemas:
* [Conflictos de prórroga](#check-conflicts)
* [Representación del correo electrónico](#check-rendering)
* [Inserción de CSS](#switch-css-inlining)

### Conflictos de prórroga

Algunas extensiones de navegador pueden causar problemas con nuestro editor de correo electrónico. Un ejemplo es [Grammarly](https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en) cuando se utiliza con Google Chrome. Si utilizas una de estas extensiones, deberías 
- Editar correos electrónicos Braze en un navegador que no tenga Grammarly como extensión del navegador
- Ponte en contacto con tu director de cuentas Braze y pídele que cambie tus editores de correo electrónico a sólo HTML o a texto sin formato. 

La vista de texto sin formato elimina tu editor ```WYSIWYG``` (lo que ves es lo que obtienes), por lo que primero debes confirmar que todos los miembros del equipo se sienten cómodos con HTML antes de hacer esta petición.

### Representación del correo electrónico

Los correos electrónicos se muestran de forma diferente según los navegadores y los clientes de correo electrónico, así que toma nota de los navegadores y clientes de correo electrónico con los que tienes problemas.

- Obtén una vista previa de tus correos electrónicos con [Inbox Vision]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#inbox-vision/) para ver cómo se ven en distintos navegadores y clientes de correo electrónico.
- Una vez que hayas identificado los navegadores o clientes de correo electrónico que causan problemas, informa a tu equipo de desarrolladores de que tendrán que modificar su HTML y hacer cambios para adaptarse a esos navegadores o clientes de correo electrónico.

### Inserción de CSS

Hay veces en que las vistas previas de Inbox Vision siguen sin coincidir con lo que se envía con Braze. Esto puede deberse a la diferencia en el inlining de CSS realizado por Braze y por otras herramientas. Si sospechas que éste es el caso, desactiva la inserción de CSS.

¿Aún necesitas ayuda? Abre un [ticket de soporte]({{site.baseurl}}/braze_support/).
