---
nav_title: Autres personnalisations du SDK
article_title: Autres personnalisations du SDK pour Android et FireOS
page_order: 3
platform: 
  - Android
  - FireOS
description: "Cet article de référence couvre des options de personnalisation et de configuration supplémentaires, telles que la journalisation verbeuse, la suppression de la journalisation et l’implémentation de plusieurs clés API."

---

# Personnalisation et configuration supplémentaires

## Utiliser R8 ou ProGuard avec Braze
La configuration de [réduction du code][50] est automatiquement comprise dans votre intégration Braze.

Les applications client qui obscurcissent le code Braze doivent stocker des fichiers de mappage de libération pour Braze afin d’interpréter les traces de pile. Si vous souhaitez continuer à conserver tous les codes de Braze, ajoutez ce qui suit à votre fichier ProGuard :

```
-keep class bo.app.** { *; }
-keep class com.braze.** { *; }
```

## Activer la journalisation verbeuse {#android-verbose-logging}

La journalisation verbeuse du SDK Braze est essentielle à un traitement rapide des problèmes de support. Ces journaux ne doivent pas être modifiés pour plus de clarté. Nous préférons des fichiers de journalisation longs. La journalisation verbeuse est uniquement destinée aux environnements de développement et ne doit pas être activée dans une application publiée. Les journaux envoyés à notre équipe d’assistance doivent commencer dès que l’application est lancée et se terminer bien après le problème observé.

Pour activer la journalisation verbeuse sur le SDK Braze pour Android :

{% tabs %}
{% tab JAVA %}

```java
BrazeLogger.setLogLevel(Log.VERBOSE);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
BrazeLogger.setLogLevel(Log.VERBOSE)
```

{% endtab %}
{% endtabs %}

Pour activer la journalisation verbeuse dans le `braze.xml` :
```
<integer name="com_braze_logger_initial_log_level">2</integer>
```

{% alert important %}
La journalisation verbeuse doit être activée dès que possible dans votre `Application.onCreate()`, avant d’autres appels vers le SDK afin de garantir autant de journalisation que possible.
{% endalert %}

Pour savoir si les journaux obtenus sont verbeux, cherchez `V/Braze` quelque part à l’intérieur. Par exemple :

`2077-11-19 16:22:49.591 ? V/Braze v9.0.01 .bo.app.d3: Request started`

### Supprimer la journalisation du SDK Braze

Le niveau de journalisation par défaut du SDK Braze pour Android est `INFO`.

Pour modifier le niveau de journalisation de Braze, appelez [`BrazeLogger.setLogLevel()`][70] avec l’une des constantes [`android.util.Log`][54] ou `BrazeLogger.SUPPRESS`. Par exemple :

{% tabs %}
{% tab JAVA %}

```java
// Suppress all logs
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// Suppress all logs
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS)
```

{% endtab %}
{% endtabs %}

## Plusieurs clés API

Le cas d’usage le plus fréquent pour les clés API multiples est la séparation des clés API entre les variantes de version de débogage et de publication.

Pour basculer facilement entre plusieurs clés API dans vos versions, nous vous recommandons de créer un fichier `braze.xml` pour chaque [variante de version][3]. Une variante de version est une combinaison du type de version et de la variété du produit. Remarquez que par défaut, [un nouveau projet Android est configuré avec les types de versions `debug` et `release`][8] et aucune variété de produit.

Pour chaque variante de version pertinente, créez un nouveau `braze.xml` pour elle dans `src/<build variant name>/res/values/` :

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">REPLACE_WITH_YOUR_BUILD_VARIANT_API_KEY</string>
</resources>
```

Lorsque la variante de version est compilée, elle utilisera la nouvelle clé API.

Consultez la documentation de [configuration de temps d’exécution][69] pour définir une clé API dans le code.

[3]: https://developer.android.com/studio/build/build-variants.html
[8]: http://tools.android.com/tech-docs/new-build-system/user-guide#TOC-Build-Types
[50]: https://developer.android.com/studio/build/shrink-code
[54]: https://developer.android.com/reference/android/util/Log.html
[69]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/
[70]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.support/-braze-logger/log-level.html
