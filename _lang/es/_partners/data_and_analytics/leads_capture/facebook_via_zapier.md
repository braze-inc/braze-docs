---
nav_title: Facebook Lead Ads a través de Zapier
article_title: Facebook Lead Ads a través de Zapier
description: "Este artículo de referencia describe la integración entre Braze y Facebook Lead Ads a través de Zapier para automatizar la transferencia de datos de clientes potenciales de Facebook a Braze, lo que permite el compromiso en tiempo real y las acciones de seguimiento personalizadas."
alias: /partners/facebook_via_zapier/
page_type: partner
search_tag: Partner

---

# Facebook Lead Ads a través de la integración de Zapier

> Con la integración de Facebook Lead Ads a través de <a href="https://zapier.com/" target="_blank">Zapier</a>, puede importar sus clientes potenciales de Facebook a Braze y realizar un seguimiento de un evento personalizado cuando se captan clientes potenciales. 

Facebook Lead Ads es un formato de anuncio que permite a las empresas recopilar información sobre clientes potenciales directamente en Facebook. Estos anuncios están diseñados para que el proceso de generación de clientes potenciales sea fácil y fluido. Al aprovechar una integración de Zapier y Braze, puedes automatizar la transferencia de datos de clientes potenciales de Facebook a Braze, lo que permite una participación en tiempo real y acciones de seguimiento personalizadas. 

## Requisitos previos

| Requisitos | Descripción |
|---|---|
| Cuenta Zapier | Se requiere una cuenta Zapier para aprovechar esta asociación. Esta integración requiere el uso de <a href="https://zapier.com/app/pricing/" target="_blank">aplicaciones Zapier</a> premium, así que comprueba que tu plan Zapier tiene acceso a aplicaciones premium. |
| <a href="https://www.facebook.com/business/help/540596413257598?id=735435806665862/" target="_blank">Acceso a Facebook Leads</a> | El acceso a Facebook Leads es necesario para cada cuenta de anuncios que planees utilizar con Braze. |
| <a href="https://www.facebook.com/business/help/1710077379203657?id=180505742745347" target="_blank">Facebook Business Manager</a> | Como parte de esta integración, utilizarás Facebook Business Manager, una herramienta centralizada para gestionar los activos de Facebook de tu marca (por ejemplo, cuentas de anuncios, páginas y aplicaciones). |
| <a href="https://www.facebook.com/business/help/195296697183682?id=829106167281625/" target="_blank">Cuenta publicitaria en Facebook</a> | Necesitarás una cuenta de anuncios de Facebook activa vinculada al administrador de negocios de tu marca. <br><br>Asegúrese de que dispone del permiso "Gestionar cuentas de anuncios" para cada cuenta de anuncios que tenga previsto utilizar con Braze, y de que ha aceptado los términos y condiciones de su cuenta de anuncios. |
| <a href="https://www.facebook.com/business/help/183277585892925?id=420299598837059/" target="_blank">Página de Facebook</a> | Necesitarás una página de Facebook activa vinculada al director comercial de tu marca. <br><br>Asegúrate de que tienes permisos para "Gestionar páginas" para cada página de Facebook que quieras utilizar con Braze. |
| Punto final REST Braze | Asegúrate de que conoces la [URL de tu punto final REST]({{site.baseurl}}/api/basics/#api-definitions). Tu punto final de API coincide con la URL del panel de tu instancia de Braze. <br><br> Por ejemplo, si la URL de tu panel es `https://dashboard-03.braze.com`, tu punto final será `dashboard-03`. |
| Clave REST API de Braze | Asegúrate de que tienes una clave de API REST Braze con permisos `users.track`. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1: Crea una campaña de Lead Ads con un formulario instantáneo

Desde el administrador de anuncios de Facebook, crea una <a href="https://www.facebook.com/business/help/397336587121938?id=735435806665862&helpref=uf_permalink" target="_blank">campaña de Facebook Leads y un formulario de Facebook Lead Ads</a>.

Puede utilizar una dirección de correo electrónico o un número de teléfono al realizar una solicitud al [punto final`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para actualizar o crear el perfil de usuario. Por este motivo, incluya un **campo de Contacto** para **correo electrónico** o **teléfono** en su formulario de anuncios de clientes potenciales. Si recopila nombres o apellidos, hágalo por separado en el formulario en lugar de utilizar los nombres completos.

### Paso 2: Conecta tu cuenta de Facebook a Zapier 

#### Paso 2a: Seleccione su método de conexión en Zapier

En Zapier, ve a **Aplicaciones** para buscar las aplicaciones de Facebook disponibles. Selecciona **Facebook Lead Ads** o **Facebook Lead Ads (para administradores de empresas)**.

Para obtener más información sobre estos dos métodos de conectar tu cuenta de Facebook a Zapier, consulta:

- <a href="https://help.zapier.com/hc/en-us/articles/8496123584781-How-to-get-started-with-Facebook-Lead-Ads-for-Business-Admins-on-Zapier#h_01HC9VZFZG0GR2KRYM5EQJN329" target="_blank">Facebook Lead Ads (para administradores de empresas)</a>
- <a href="https://help.zapier.com/hc/en-us/articles/8496061306253#h_01HC9VMZ2XP0017AR6SE7S30JG" target="_blank">Anuncios de clientes potenciales en Facebook</a>

![]({% image_buster /assets/img/fb_lead_ads_zapier/integration1.png %}){: style="max-width:80%;"}

#### Paso 2b: Añadir Zapier al acceso a clientes potenciales en el administrador de empresas de Facebook

En tu Facebook Business Manager, ve a **Integraciones** > **Acceso a clientes potenciales** en el menú de la izquierda. Selecciona tu página de Facebook y, a continuación, haz clic en **CRM**. En la pestaña CRM, selecciona **Asignar CRM** y añade **Zapier**.

![]({% image_buster /assets/img/fb_lead_ads_zapier/integration2.png %}){: style="max-width:80%;"}

Para conocer los pasos necesarios para asignar Zapier como integración de CRM, consulta la <a href="https://www.facebook.com/business/help/540596413257598?id=735435806665862" target="_blank">documentación</a> de Facebook.

### Paso 3: Crea tu Zap

#### Paso 3a: Crear el disparador 

Una vez que hayas conectado tu cuenta de Facebook, puedes proceder a crear un Zap. Para el **activador**, selecciona **Facebook Lead Ads** o **Facebook Lead Ads (para administradores de empresas)** según lo que hayas elegido en el paso 2. 

![]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap1.png %}){: style="max-width:80%;"}

Para el **evento**, seleccione **Nuevos clientes potenciales** > **Continuar**. 

![]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap2.png %}){: style="max-width:80%;"}

Selecciona tu cuenta de Facebook y, a continuación, **Continuar**. 

![]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap3.png %}){: style="max-width:80%;"}

Selecciona tu página de Facebook y el formulario instantáneo que creaste anteriormente y, a continuación, **Continuar**.

![]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap4.png %}){: style="max-width:80%;"}

A continuación, prueba este activador. Después de validar la salida del formulario, seleccione **Continuar con el registro seleccionado**.

#### Paso 3b: Crear una acción

Añade un nuevo paso y selecciona **Webhooks by Zapier**. A continuación, seleccione **Solicitud personalizada** para el campo **Evento** y haga clic en **Continuar**. 

![]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap5.png %}){: style="max-width:80%;"}

Por último, configure su solicitud personalizada insertando campos en su carga útil. El siguiente fragmento de código muestra un ejemplo de carga útil. 

```
{
    "attributes": [
        {
            "email": "<insert_email_field>",
            "first_name": "<insert_first_name_field>",
            "last_name": "<insert_last_name_field>",
            "lead_form": "<insert_form_name_field>",
            "fb_campaign": "<insert_campaign_id_field>",
            "fb_ad_set": "<insert_campaign_id_field>",
            "fb_ad": "<insert_campaign_id_field>",
            "email_subscribe": "subscribed",
            "subscription_groups" : [{
                "subscription_group_id": "<subscription_group_id>",
                "subscription_state": "subscribed"
                }
            ]
        }
    ],
    "events": [
        {
            "email": "<insert_email_field>",
            "name": "<insert_custom_event_name>",
            "time": "<insert_timestamp_field>",
            "_update_existing_only": false
        }
    ]
}`
```

Aquí tienes un ejemplo de cómo se ve esto en Zapier:

![]({% image_buster /assets/img/fb_lead_ads_zapier/configuration_example.png %}){: style="max-width:80%;"}

Después de configurar su webhook, seleccione **Continuar y probar**. Si la prueba tiene éxito, puedes publicar tu Zap.

### Paso 4: Prueba tu Facebook Lead Ads Zap

Para probarlo de extremo a extremo, utiliza la herramienta de prueba de anuncios Leads de Facebook en tu consola para desarrolladores de Facebook. Para más información, consulta <a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/testing-troubleshooting/" target="_blank">Pruebas y solución de problemas</a>.

## Gestión de la identidad de los usuarios

Esta integración le permite atribuir sus clientes potenciales de Facebook por correo electrónico a través del [punto final`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#example-request-for-updating-a-user-profile-by-phone-number).

* Si el correo electrónico coincide con un perfil de usuario existente, Braze actualizará el perfil con los datos de clientes potenciales de Facebook.
* Si hay varios perfiles de usuario con el mismo correo electrónico, Braze dará prioridad al perfil actualizado más recientemente con un ID externo para las actualizaciones.
* Si el ID externo no existe, Braze dará prioridad al perfil actualizado más recientemente con el correo electrónico coincidente.
* Si no existe ningún perfil con el correo electrónico proporcionado, Braze creará un nuevo perfil y se creará un nuevo perfil de usuario alias. Para identificar los perfiles de usuario alias recién creados, utiliza el [punto final `/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/). 

{% alert note %}
También puede utilizar un número de teléfono o un ID externo como parte de la solicitud a Braze si esos campos están disponibles y son el identificador principal que desea para la integración. Para ello, modifica la carga útil de tu solicitud como se indica en el [punto final`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).
{% endalert %}

## Solución de problemas

{% details He probado el desencadenante y la acción correctamente, así que ¿por qué no puedo publicar mi Zapier Zap? %}
Para utilizar esta integración, debes tener un <a href="https://zapier.com/app/pricing/" target="_blank">plan Zapier</a> que admita aplicaciones premium.
{% enddetails %}

{% details ¿Por qué los clientes potenciales de Facebook no se sincronizan con Braze? %}
1. Comprueba que tienes acceso de administrador a tu página de Facebook, cuenta publicitaria y acceso de clientes potenciales. A continuación, vuelve a conectar tu cuenta en Zapier.
2. Comprueba que el formulario instantáneo que has creado en Facebook coincide con el formulario seleccionado en el paso Activador. 
3. Comprueba que has asignado Zapier a Acceso a clientes potenciales yendo a **Administrador de empresas de Facebook** > **Integraciones** > **Acceso a clientes potenciales**.
{% enddetails %}

{% details ¿Por qué veo perfiles de usuario duplicados con el mismo correo electrónico? %}
Existen formas únicas de crear y gestionar perfiles de usuario en Braze en función de su [ciclo de vida]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-profile-lifecycle).

Dependiendo de sus procesos internos y de cuándo esté activando la creación de clientes dentro de Braze, puede encontrarse con perfiles de usuario duplicados debido a una condición de carrera del perfil de usuario que está siendo creado por la integración y cuando el usuario se crea desde su sistema. Puedes [fusionar perfiles de usuario]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) en Braze.
{% enddetails %}

{% details No tengo una cuenta Zapier. ¿Cómo puedo activar los webhooks de Facebook Lead Ads en Braze? %}
Si no utilizas Zapier ni tienes previsto hacerlo, puedes crear la integración directamente desde Facebook en Braze. Consulta la <a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/" target="_blank">documentación de Lead Ads</a> para obtener más información.

Para recuperar clientes potenciales de Facebook, utiliza <a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#webhooks" target="_blank">webhooks</a>. Consulta <a href="https://developers.facebook.com/docs/graph-api/webhooks/getting-started" target="_blank">la documentación de Webhooks</a> para empezar a utilizar webhooks en Facebook.

Después de establecer la URL de los webhooks en Facebook, trabaja con tu equipo para determinar la mejor ruta para reenviar los datos al [punto final`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Al igual que con Zapier, recomendamos realizar una [solicitud por correo electrónico]({{site.baseurl}}/api/endpoints/user_data/post_user_track#example-request-for-updating-a-user-profile-by-phone-number) a través del punto final `users/track`.
{% enddetails %}

{% alert tip %}
Para obtener más consejos sobre la solución de problemas, consulta la <a href="https://help.zapier.com/hc/en-us/articles/8495982030861-Common-Problems-with-Facebook-Lead-Ads#h_01HC9V6Y652KQYYY96YG99T423" target="_blank">guía de solución de problemas de clientes potenciales de Facebook</a> de Zapier.
{% endalert %}


