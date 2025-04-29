---
page_order: 10
nav_title: Gestión de versiones
article_title: Acerca del administrador de versiones del SDK de Braze
description: "Infórmate sobre la gestión de versiones del SDK de Braze."
---

# Acerca de la gestión de versiones

> Infórmate sobre la gestión de versiones del SDK de Braze, para que tu aplicación se mantenga actualizada con las últimas características y mejoras de calidad. Dado que las versiones más antiguas del SDK pueden no recibir el último parche, corrección de errores o soporte, te recomendamos que lo mantengas siempre actualizado como parte de tu ciclo de vida de desarrollo en curso.

## Recomendaciones sobre versiones

Todos los SDK de Braze se adhieren a la [Especificación Semántica de Versionado (SemVer)](https://semver.org/), por lo que dado un número de versión `MAJOR.MINOR.PATCH`, recomendamos lo siguiente:

|Versión|Acerca de esta versión|Recomendación|
|-------|------------------|--------------|
| `PATCH` | Las actualizaciones son siempre no rupturistas e incluyen importantes correcciones de errores. Siempre estarán a salvo. | Siempre debes intentar actualizar inmediatamente a la última versión del parche de tu versión mayor y menor actual. |
| `MINOR` | Las actualizaciones son siempre sin ruptura, e incluyen nuevas funcionalidades netas. Nunca requerirán cambios en el código de tu aplicación. | Aunque no es necesario que lo hagas inmediatamente, deberías actualizarte a la última versión menor de tu versión mayor actual lo antes posible. 
| `MAJOR` | Las actualizaciones son cambios de última hora, y pueden requerir cambios en el código de tu aplicación. | Como esto puede requerir cambios en el código, actualiza a la última versión principal en el plazo que mejor convenga a tu equipo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert note %}
A veces, las nuevas actualizaciones de los sistemas operativos Android o Apple requieren cambios en el SDK de Braze. Para asegurarte de que tu aplicación es compatible con los nuevos teléfonos, es importante que mantengas actualizado tu SDK.
{% endalert %}

## Acerca de los problemas conocidos

Para garantizar que nuestros cambios no rompan tus procesos de compilación, **nunca modificaremos ni eliminaremos una versión después de haberla publicado en un sistema de distribución,**aunque esa versión en concreto tenga problemas conocidos.

En estos casos, documentaremos el problema en [el registro de cambios del SDK de Braze]({{site.baseurl}}/developer_guide/changelogs/) y publicaremos un nuevo parche para las versiones mayores o menores afectadas lo antes posible.
