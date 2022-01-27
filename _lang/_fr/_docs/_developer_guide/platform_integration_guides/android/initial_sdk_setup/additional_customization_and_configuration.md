---
nav_title: Autres personnalisations du SDK
article_title: Autres personnalisations SDK pour Android/FireOS
page_order: 3
platform:
  - Android
  - Pare-feu
description: "Cet article couvre des options supplémentaires de personnalisation et de configuration telles que l'enregistrement verbeux, la suppression de loggind, et comment implémenter plusieurs clés API."
---

# Personnalisation et configuration supplémentaires

## Utiliser R8/ProGuard avec Braze
La configuration de [Rétrécissement de code][50] est automatiquement incluse dans votre intégration à Braze.

Les applications clientes qui masquent le code Braze doivent stocker les fichiers de mappage de version pour que Braze interprète les traces de pile. Si vous souhaitez continuer à garder tout le code de Braze, ajoutez ce qui suit à votre fichier ProGuard :

```
-keep class bo.app.** { *; }
-keep class com.appboy.** { *; }
```

## Activation du journal verbeux {#android-verbose-logging}

Les logs détaillés du Braze SDK sont essentiels pour un retour en arrière rapide sur les problèmes de support. Ces logs ne doivent pas être modifiés pour des raisons de clarté; les longs fichiers journaux sont préférables! La journalisation détaillée est destinée uniquement à être utilisée dans les environnements de développement et ne devrait pas être activée dans une application publiée. Les journaux envoyés à notre équipe de support devraient commencer dès que la demande est lancée et devraient se terminer bien après que le problème observé se soit produit.

Pour activer la connexion détaillée sur le SDK Braze Android:

{% tabs %}
{% tab JAVA %}

```java
BrazeLogger.setLogLevel(Log.VERBOSE) ;
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
BrazeLogger.setLogLevel(Log.VERBOSE)
```

{% endtab %}
{% endtabs %}

{% alert important %}
Les journaux verbeux devraient être activés dès que possible dans votre application `. nCreate()`, avant tout autre appel au SDK, pour garantir autant de logs que possible.
{% endalert %}

Pour savoir si vos logs obtenus sont verbeux, cherchez `V/Braze` quelque part dans vos logs. Par exemple :

`2077-11-19 16:22:49.591 ? V/Braze v9.0.01 .bo.app.d3: Requête démarrée`

### Suppression des logs Braze SDK

Le niveau de log par défaut pour le SDK Android Braze est `INFO`.

Pour changer le niveau du journal de Braze, appelez [`BrazeLogger.setLogLevel()`][70] avec l'un des [`android. til.Log`][54] constantes ou `BrazeLogger.SUPPRESS`. Par exemple :

{% tabs %}
{% tab JAVA %}

```java
// Supprime tous les logs
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// Supprime tous les logs
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS)
```

{% endtab %}
{% endtabs %}

## Clés API multiples

Le cas d'utilisation le plus courant pour plusieurs clés API est la séparation des clés API pour le débogage et la publication des variantes de compilation.

Pour basculer facilement entre plusieurs clés API dans vos builds, nous vous recommandons de créer un frein `séparé. ml` fichier pour chaque [version pertinente][3]. Une variante de construction est une combinaison de type de construction et de saveur de produit. Notez que par défaut, [un nouveau projet Android est configuré avec `debug` et `version` types de build][8] et aucune saveur de produit.

Pour chaque variante de compilation pertinente, créez un nouveau `braze.xml` dans `src/<build variant name>/res/values/`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_appboy_api_key">REPLACE_WITH_YOUR_BUILD_VARIANT_API_KEY</string>
</resources>
```

Quand la variante de compilation est compilée, elle utilisera la nouvelle clé API.

Pour définir une clé API dans le code, veuillez consulter la documentation de la [configuration][69] d'exécution.

[3]: https://developer.android.com/studio/build/build-variants.html
[8]: http://tools.android.com/tech-docs/new-build-system/user-guide#TOC-Build-Types
[50]: https://developer.android.com/studio/build/shrink-code
[54]: https://developer.android.com/reference/android/util/Log.html
[69]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/
[70]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.support/-braze-logger/log-level.html
