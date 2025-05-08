---
nav_title: Otras personalizaciones del SDK
article_title: Otras personalizaciones del SDK para Android y FireOS
page_order: 3
platform: 
  - Android
  - FireOS
description: "En este artículo de referencia se cubren opciones adicionales de personalización y configuración, como el registro detallado, la supresión del registro y cómo implementar varias claves de API."

---

# Otras personalizaciones del SDK para Android y FireOS

> En este artículo de referencia se cubren opciones adicionales de personalización y configuración, como el registro detallado, la supresión del registro y cómo implementar varias claves de API.

## Uso de R8/ProGuard con Braze

La configuración de [la reducción de código](https://developer.android.com/studio/build/shrink-code) se incluye automáticamente con tu integración Braze.

Las aplicaciones cliente que ofuscan el código Braze deben almacenar archivos de mapeado de liberación para que Braze pueda interpretar las trazas de pila. Si quieres seguir conservando todo el código Braze, añade lo siguiente a tu archivo ProGuard:

```
-keep class bo.app.** { *; }
-keep class com.braze.** { *; }
```

## Registro

De manera predeterminada, el nivel de registro del SDK de Braze para Android está predeterminado en `INFO`. Puedes [suprimir estos registros](#suppressing-logs) o [establecer un nivel de registro diferente](#enabling-logs), como `VERBOSE`, `DEBUG`, o `WARN`.

### Habilitación de registros {#enabling-logs}

Para ayudar a solucionar problemas en tu aplicación, o reducir los tiempos de respuesta con el soporte de Braze, querrás habilitar los registros detallados para el SDK. Cuando envíes registros detallados al soporte de Braze, asegúrate de que empiezan en cuanto inicias la aplicación y terminan mucho después de que se produzca el problema.

Ten en cuenta que los registros detallados sólo están pensados para tu entorno de desarrollo, por lo que deberás desactivarlos antes de publicar tu aplicación.

{% alert important %}
Habilita los registros detallados antes de cualquier otra llamada en `Application.onCreate()` para asegurarte de que tus registros son lo más completos posible.
{% endalert %}

{% tabs %}
{% tab Aplicación %}
Para habilitar los registros directamente en tu aplicación, añade lo siguiente al método `onCreate()` de tu aplicación antes de cualquier otro método.

{% subtabs %}
{% subtab JAVA %}
```java
BrazeLogger.setLogLevel(Log.MIN_LOG_LEVEL);
```
{% endsubtab %}

{% subtab KOTLIN %}
```kotlin
BrazeLogger.logLevel = Log.MIN_LOG_LEVEL
```
{% endsubtab %}
{% endsubtabs %}

Sustituye `MIN_LOG_LEVEL` por la **Constante** del nivel de registro que quieras establecer como nivel mínimo de registro. Cualquier registro en un nivel `>=` a tu configuración `MIN_LOG_LEVEL` se reenviará al método predeterminado de Android [`Log`](https://developer.android.com/reference/android/util/Log). Se descartará cualquier registro `<` de tu configuración `MIN_LOG_LEVEL`.

| Constante    | Valor          | Descripción                                                               |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | 2              | Registra los mensajes más detallados para depuración y desarrollo.            |
| `DEBUG`     | 3              | Registra mensajes descriptivos para depuración y desarrollo.                  |
| `INFO`      | 4              | Registra mensajes informativos para los destacados generales.                       |
| `WARN`      | 5              | Registra mensajes de advertencia para identificar situaciones potencialmente perjudiciales.     |
| `ERROR`     | 6              | Registra mensajes de error para indicar fallos de la aplicación o problemas graves. |
| `ASSERT`    | 7              | Registra mensajes de aserción cuando las condiciones son falsas durante el desarrollo.     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Por ejemplo, el siguiente código reenviará los niveles de registro `2`, `3`, `4`, `5`, `6` y `7` al método `Log`.

{% subtabs %}
{% subtab JAVA %}
```java
BrazeLogger.setLogLevel(Log.VERBOSE);
```
{% endsubtab %}

{% subtab KOTLIN %}
```kotlin
BrazeLogger.logLevel = Log.VERBOSE
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab braze.xml %}
Para habilitar los registros en `braze.xml`, añade lo siguiente a tu archivo:

```xml
<integer name="com_braze_logger_initial_log_level">MIN_LOG_LEVEL</integer>
```

Sustituye `MIN_LOG_LEVEL` por el **valor** del nivel de registro que quieras establecer como nivel de registro mínimo. Cualquier registro en un nivel `>=` a tu configuración `MIN_LOG_LEVEL` se reenviará al método predeterminado de Android [`Log`](https://developer.android.com/reference/android/util/Log). Se descartará cualquier registro `<` de tu configuración `MIN_LOG_LEVEL`.

| Constante    | Valor          | Descripción                                                               |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | 2              | Registra los mensajes más detallados para depuración y desarrollo.            |
| `DEBUG`     | 3              | Registra mensajes descriptivos para depuración y desarrollo.                  |
| `INFO`      | 4              | Registra mensajes informativos para los destacados generales.                       |
| `WARN`      | 5              | Registra mensajes de advertencia para identificar situaciones potencialmente perjudiciales.     |
| `ERROR`     | 6              | Registra mensajes de error para indicar fallos de la aplicación o problemas graves. |
| `ASSERT`    | 7              | Registra mensajes de aserción cuando las condiciones son falsas durante el desarrollo.     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Por ejemplo, el siguiente código reenviará los niveles de registro `2`, `3`, `4`, `5`, `6` y `7` al método `Log`.

```xml
<integer name="com_braze_logger_initial_log_level">2</integer>
```
{% endtab %}
{% endtabs %}

### Verificar registros detallados

Para verificar que tus registros están configurados en `VERBOSE`, comprueba si `V/Braze` aparece en algún lugar de tus registros. Si lo hace, es que se han habilitado correctamente los registros detallados. Por ejemplo:

```
2077-11-19 16:22:49.591 ? V/Braze v9.0.01 .bo.app.d3: Request started
```

### Suprimir registros

El nivel de registro predeterminado para el SDK de Braze para Android es `INFO`. Para suprimir todos los registros del SDK de Braze para Android, llama a `BrazeLogger.SUPPRESS` en el método `onCreate()` de tu aplicación _antes de_ cualquier otro método.

{% tabs local %}
{% tab JAVA %}
```java
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS);
```
{% endtab %}

{% tab KOTLIN %}
```kotlin
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS)
```
{% endtab %}
{% endtabs %}

## Múltiples claves de API

El caso de uso más común para múltiples claves de API es separar las claves de API para las variantes de compilación de depuración y de lanzamiento.

Para cambiar fácilmente entre varias claves de API en tus construcciones, te recomendamos que crees un archivo `braze.xml` distinto para cada [variante de construcción](https://developer.android.com/studio/build/build-variants.html) relevante. Una variante de fabricación es una combinación del tipo de fabricación y la variante de producto. Ten en cuenta que, de manera predeterminada, [un nuevo proyecto Android se configura con los tipos de compilación `debug` y `release` ](http://tools.android.com/tech-docs/new-build-system/user-guide#TOC-Build-Types) y sin tipos de producto.

Para cada variante de compilación relevante, crea un nuevo `braze.xml` para ella en `src/<build variant name>/res/values/`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">REPLACE_WITH_YOUR_BUILD_VARIANT_API_KEY</string>
</resources>
```

Cuando se compile la variante de compilación, utilizará la nueva clave de API.

Consulta la documentación de [configuración en tiempo de ejecución]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/) para establecer una clave de API en código.
