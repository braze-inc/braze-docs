---
nav_title: Conciliación de usuarios de Shopify
article_title: Conciliación de usuarios de Shopify
permalink: "/shopify_user_reconciliation/"
description: "Este artículo de referencia explica cómo conciliar el ID del dispositivo de tu usuario y su información personal cuando llega al flujo de pago."
hidden: true
---

# Reconciliación de usuarios de Shopify fuera del flujo de pago 

> La integración de Shopify concilia el ID del dispositivo de tu usuario y su información personal cuando llega al flujo de pago y realiza allí cualquier evento webhook de Shopify.

{% alert note %}
Esta característica está actualmente en fase beta. Si estás interesado, ponte en contacto con tu administrador del éxito del cliente o director de cuentas.
{% endalert %}

Para apoyar la conciliación de usuarios a través de tu flujo de registro e inicio de sesión en Shopify, podemos implementar una función JavaScript automáticamente en tu tienda Shopify fuera del flujo de pago. Braze implementará automáticamente una función siempre que veamos un formulario con un `type="email"` en la tienda Shopify, como en el ejemplo siguiente.

![1]{:style="max-width:60%;"}

Una vez que se llama a esta función, el usuario anónimo de la Web queda asociado a la dirección de correo electrónico proporcionada. En adelante, cualquier evento de Shopify que haga referencia a cualquiera de los identificadores que utilizamos (por ejemplo, ID de cliente de Shopify, dirección de correo electrónico, número de teléfono) se asignará al mismo usuario de Braze si hay coincidencia.

## Consideraciones

{% alert important %}
Braze no está familiarizado con todos los formularios que contiene `type="email"` en el sitio Shopify de un cliente. Esto significa que existe la posibilidad de que la función pase por alto algunos campos de entrada que deberían utilizarse para la conciliación del usuario o que recoja campos incorrectos que establecerían una dirección de correo electrónico errónea (por ejemplo, formulario de referidos) en el perfil de usuario.
{% endalert %}

Te animamos a que explores todos los formularios admitidos en el sitio web de Shopify y evalúes cómo esta solución beta puede satisfacer tus necesidades de forma eficaz. Al optar por utilizar esta característica beta, entiendes que existe la posibilidad de que se produzca un comportamiento inesperado al realizar cambios manuales en tus formularios de Shopify.

[1]: {% image_buster /assets/img/shopify_type_email.png %}
