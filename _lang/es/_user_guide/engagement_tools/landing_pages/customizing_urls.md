---
nav_title: Personalizar la URL
article_title: Personalizar las URL de las páginas de destino
description: "Aprende a personalizar las URL de tus páginas de destino con la marca de tu empresa, conectando tu dominio a tu espacio de trabajo Braze."
page_order: 1
---

# Personalizar las URL de las páginas de destino

> Aprende a personalizar las URL de tus páginas de destino con la marca de tu empresa, conectando tu dominio a tu espacio de trabajo Braze.

## Cómo funciona

Cuando [conectes tu dominio a Braze](#connecting-your-domain-to-braze), se utilizará como dominio predeterminado para todas las páginas de destino. Por ejemplo, si conectas el subdominio `forms.example.com`, las URL de tu página de destino serían ahora `forms.example.com/holiday-sale`.

El número de dominios personalizados que puedes conectar a tu cuenta Braze depende [del nivel de]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/#plan-tiers) tu [plan]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/#plan-tiers). Para aumentar tu límite, ponte en contacto con tu director de cuentas Braze.

## Conectar tu dominio a Braze

Para conectar un dominio a tu cuenta Braze, haz que un administrador siga los pasos que se indican a continuación.

1. Ve a **Configuración** > **Configuración de la página de destino**.
2. Introduce el dominio al que quieres conectarte y selecciona **Enviar**. Por ejemplo, `forms.example.com`.
3. Copia y pega los registros **TXT** y **CNAME** en la configuración de DNS de tu proveedor de dominios.
4. Vuelve al panel de Braze para verificar la conexión.

\![Página de configuración de la página de destino con un registro TXT y dos CNAME listados con sus respectivos nombres y valores.]({% image_buster /assets/img/landing_pages/connect_subdomain.png %})

{% alert note %}
Dependiendo de tu proveedor de dominios, la conexión puede tardar hasta 48 horas. Una vez completado el proceso, empezaremos a utilizar tu dominio personalizado para tus páginas de destino en el panel de Braze.
{% endalert %}

## Eliminar tu dominio

Si eres administrador de Braze, puedes eliminar un dominio previamente configurado siguiendo los pasos siguientes:

1. Ve a **Configuración** > **Configuración de la página de destino**.
2. Selecciona **Eliminar dominio personalizado**
3. Confirma la eliminación del dominio.
4. Elimina los registros de DNS enumerados de la configuración de tu dominio.

{% alert important %}
Cuando elimines un dominio personalizado, esa URL dejará de ser válida. Todas las páginas de destino que estaban utilizando este dominio volverán automáticamente al dominio predeterminado establecido por Braze.
{% endalert %}


## Recursos DNS

A continuación encontrarás recursos para crear y administrar registros de DNS con los proveedores de dominios más utilizados. Si utilizas otro proveedor, consulta su documentación o ponte en contacto con su equipo de soporte para obtener información.

| Proveedor de dominios | Recursos |
| --- | --- |
| Bluehost | [Explicación de los registros de DNS](https://my.bluehost.com/hosting/help/508)<br> [Gestión de DNS Añadir Editar o Eliminar Entradas DNS](https://my.bluehost.com/hosting/help/559) |
| Dreamhost | [¿Cómo añado registros de DNS personalizados?](https://help.dreamhost.com/hc/en-us/articles/360035516812) |
| GoDaddy | [Añadir un registro CNAME](https://www.godaddy.com/help/add-a-cname-record-19236?) |
| Cloudflare | [Gestionar registros de DNS](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/) |
| Squarespace | [Añadir configuración DNS personalizada](https://support.squarespace.com/hc/en-us/articles/360002101888-Adding-custom-DNS-records-to-your-Squarespace-managed-domain) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Solución de problemas 

### Ha fallado la conexión a mi dominio

Comprueba que tu dominio se ha introducido correctamente y que coincide con el que enviaste a Braze desde tu cuenta de proveedor de dominios. Si es correcto y coincide, comprueba los registros TXT y CNAME proporcionados por Braze. Deben coincidir con los registros que introdujiste en tu cuenta de proveedor de dominios.

## Preguntas más frecuentes

### ¿Puedo conectar varios subdominios a mi espacio de trabajo o conectar un subdominio a varios espacios de trabajo?

No, actualmente sólo puedes conectar un subdominio a un espacio de trabajo.

### ¿Puedo utilizar el mismo subdominio que utilizo actualmente para mi sitio web principal o mi dominio de envío?

No, no puedes utilizar subdominios que ya estén en uso. Aunque estos subdominios son válidos, no pueden utilizarse para páginas de destino si ya están asignados a otros fines o tienen registros de DNS que entran en conflicto con los registros CNAME requeridos.

