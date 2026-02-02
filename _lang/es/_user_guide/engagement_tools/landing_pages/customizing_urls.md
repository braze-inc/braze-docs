---
nav_title: Personaliza la URL
article_title: Personaliza las URL de las páginas de destino
description: "Aprende a personalizar las URL de tus páginas de destino con la marca de tu empresa, conectando tu dominio a tu espacio de trabajo Braze."
page_order: 1
---

# Personaliza las URL de las páginas de destino

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

![Página de configuración de la página de destino con un registro TXT y dos CNAME listados con sus respectivos nombres y valores.]({% image_buster /assets/img/landing_pages/connect_subdomain.png %})

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

{% multi_lang_include dns_records.md %}

## Solución de problemas 

### Ha fallado la conexión a mi dominio

Comprueba que tu dominio se ha introducido correctamente y que coincide con el que enviaste a Braze desde tu cuenta de proveedor de dominios. Si es correcto y coincide, comprueba los registros TXT y CNAME proporcionados por Braze. Deben coincidir con los registros que introdujiste en tu cuenta de proveedor de dominios.

## Preguntas más frecuentes

### ¿Puedo conectar varios subdominios a mi espacio de trabajo o conectar un subdominio a varios espacios de trabajo?

No, actualmente sólo puedes conectar un subdominio a un espacio de trabajo.

### ¿Puedo utilizar el mismo subdominio que utilizo actualmente para mi sitio web principal o mi dominio de envío?

No, no puedes utilizar subdominios que ya estén en uso. Aunque estos subdominios son válidos, no pueden utilizarse para páginas de destino si ya están asignados a otros fines o tienen registros de DNS que entran en conflicto con los registros CNAME requeridos.

### ¿Por qué mi dominio personalizado está atascado en "Conectando" a pesar de que los registros de DNS son válidos?

Si tu dominio personalizado muestra todos los registros de DNS como "Conectado", pero el estado del dominio permanece en "Conectando" durante más de cuatro horas, es posible que tu organización esté utilizando registros CAA (Autorización de Autoridad de Certificación) o retenciones de zona de Cloudflare que impiden que Braze proteja tu página.

#### Registros CAA

Los registros CAA restringen qué autoridades de certificación pueden emitir certificados SSL para tu dominio. Si tus registros CAA no incluyen LetsEncrypt, Braze (a través de Cloudflare) no puede emitir el certificado SSL necesario.

Para solucionarlo, pide a tu equipo de TI que añada un registro CAA a tu subdominio con los siguientes valores:
- **Tipo de registro:** CAA
- **Valor:** `0 issue "letsencrypt.org"`

Para más información, consulta [la documentación sobre CAA de LetsEncrypt](https://letsencrypt.org/docs/caa/).

#### La zona Cloudflare retiene

Si tu organización utiliza Cloudflare, una característica de seguridad de retención de zona puede estar impidiendo que Braze cree tu dominio personalizado.

Para solucionarlo, pide a tu equipo de TI que libere temporalmente la zona retenida. Para más información, consulta [la documentación sobre la retención de zonas de Cloudflare](https://developers.cloudflare.com/fundamentals/account/account-security/zone-holds/#release-zone-holds).

#### Reiniciar el proceso de validación

Después de resolver cualquiera de los dos problemas, elimina y vuelve a crear tu dominio personalizado en el panel de Braze para reiniciar el proceso de validación.

