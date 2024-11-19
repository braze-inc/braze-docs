---
nav_title: Conectar tu dominio
article_title: Conectar tu dominio
description: "Este artículo explica cómo conectar tu propio dominio personalizado a las páginas de destino de Braze."
page_order: 1
alias: /landing_pages/connect_domain/
---

# Conectar tu dominio

> Conecta tu propio dominio a tu espacio de trabajo Braze para personalizar las URL de tus páginas de destino con tu marca.

Para conectar un dominio o subdominio a tu cuenta Braze, haz que un administrador siga los pasos que se indican a continuación.

1. Ve a **Configuración** > **Configuración de la página de destino**.
2. Introduce el dominio o subdominio al que quieres conectarte y selecciona **Enviar**. Por ejemplo, `forms.example.com`.
3. Copia y pega los registros **TXT** y **CNAME** en la configuración de DNS de tu proveedor de dominios.
4. Vuelve al panel de Braze para verificar la conexión.

![Página de configuración de la página de destino con un registro TXT y dos CNAME listados con sus respectivos nombres y valores.][1]

{% alert note %}
Dependiendo de tu proveedor de dominios, la conexión puede tardar hasta 48 horas. Una vez completado el proceso, empezaremos a utilizar tu dominio personalizado para tus páginas de destino en el panel de Braze.
{% endalert %}

## Utilizar tu dominio en Braze

Una vez completada la verificación de tu dominio, se utilizará por predeterminado en Braze. Por ejemplo, si conectas el subdominio `forms.example.com`, las URL de tu página de destino se actualizarán para que parezcan `forms.example.com/holiday-sale`.

{% alert note %}
Pronto se eliminará el dominio personalizado. Ponte en contacto con tu administrador del éxito del cliente si necesitas eliminar tu subdominio.
{% endalert %}

## Recursos de proveedores de dominios

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

[1]: {% image_buster /assets/img/landing_pages/connect_subdomain.png %}
