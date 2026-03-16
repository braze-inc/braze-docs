---
page_order: 10
nav_title: Gestión de versiones
article_title: Acerca de la gestión de versiones para el SDK de Braze
description: "Más información sobre la gestión de versiones para el SDK de Braze."
---

# Acerca de la gestión de versiones

> Obtén información sobre la gestión de versiones del SDK de Braze para que tu aplicación esté siempre actualizada con las últimas características y mejoras de calidad. Dado que es posible que las versiones anteriores del SDK no reciban los últimos parches, correcciones de errores o asistencia técnica, te recomendamos que lo mantengas siempre actualizado como parte de tu ciclo de desarrollo continuo.

## Recomendaciones sobre versiones

Todos los SDK de Braze cumplen con la [especificación de versionado semántico (SemVer)](https://semver.org/), por lo que, `MAJOR.MINOR.PATCH`dado un número de versión, recomendamos lo siguiente:

|Versión|Acerca de esta versión|Recomendación|
|-------|------------------|--------------|
| `PATCH` | Las actualizaciones nunca interrumpen el servicio e incluyen correcciones de errores importantes. Siempre estarán a salvo. | Siempre debes intentar actualizar inmediatamente a la última versión del parche de tu versión principal y secundaria actual. |
| `MINOR` | Las actualizaciones nunca interrumpen el servicio e incluyen nuevas funciones. Nunca requerirán cambios en el código de tu aplicación. | Aunque no es necesario que lo hagas inmediatamente, debes actualizar a la última versión menor de tu versión principal actual lo antes posible. 
| `MAJOR` | Las actualizaciones son cambios importantes y pueden requerir modificaciones en el código de tu aplicación. | Dado que esto puede requerir cambios en el código, actualiza a la última versión principal en el plazo que mejor se adapte a tu equipo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert note %}
A veces, las nuevas actualizaciones del sistema operativo Android o Apple requieren cambios en el SDK de Braze. Para garantizar que tu aplicación sea compatible con los teléfonos más nuevos, es importante que mantengas tu SDK actualizado.
{% endalert %}

## Acerca de los problemas conocidos

Para garantizar que nuestros cambios no afecten a tus procesos de compilación, **nunca modificaremos ni eliminaremos una versión después de que se haya publicado en un sistema de distribución**, incluso si esa versión en concreto tiene problemas conocidos.

En estos casos, documentaremos el problema en el [registro de cambios del SDK de Braze]({{site.baseurl}}/developer_guide/changelogs/) y, a continuación, lanzaremos un nuevo parche para las versiones principales o secundarias afectadas lo antes posible.
