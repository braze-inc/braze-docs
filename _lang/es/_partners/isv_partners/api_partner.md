---
nav_title: Integración de socios de API
alias: /api_partner_integration/
hidden: true
---

# Integración de socios de API

> Infórmate sobre los requisitos para las integraciones de API de socios, como la sintaxis de las cabeceras `User-Agent`.

{% alert important %}
Antes, los socios debían añadir su nombre al campo de socio en sus Solicitudes API. Este formato ya no se admite y ahora se requiere una cabecera `User-Agent`.
{% endalert %}

## Agentes de usuario

Debes incluir una cabecera `User-Agent` que identifique claramente el origen del tráfico. Esto habilita a nuestros clientes compartidos a ver el tráfico de socios en los informes de uso de la API de Braze, y permite a los ingenieros de Braze identificar las integraciones que no siguen las mejores prácticas. En general, sólo debes utilizar un único agente de usuario para todo tu tráfico.

### Sintaxis

Tu cabecera `User-Agent` debe ajustarse al siguiente formato (que es similar a la norma [RFC 7231](https://datatracker.ietf.org/doc/html/rfc7231#page-46) ):

```bash
User-Agent: partner-OrganizationName-ProductName/ProductVersion
```

Sustituye lo siguiente:

| Marcador de posición | Descripción |
|-------------|-------------|
| `OrganizationName` | El nombre de tu organización formateado en mayúsculas y minúsculas. |
| `ProductName` | El nombre de tu producto en formato Pascal. |
| `ProductVersion` | El número de versión de tu producto. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Ejemplos

Por ejemplo, el siguiente sería un agente de usuario correcto para la ingesta de datos en la nube de Snowflake:

```bash
User-Agent: partner-Snowflake-CloudDataIngestion/179
```

Mientras que esto sería incorrecto porque no identifica claramente la fuente del tráfico:

```bash
User-Agent: axios/1.4.0
``` 
