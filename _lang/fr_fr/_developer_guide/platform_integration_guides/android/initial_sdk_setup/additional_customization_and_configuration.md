---
nav_title: Autres personnalisations du SDK
article_title: Autres personnalisations du SDK pour Android et FireOS
page_order: 3
platform: 
  - Android
  - FireOS
description: "Cet article de référence couvre des options de personnalisation et de configuration supplémentaires, telles que la journalisation verbeuse, la suppression de la journalisation et l’implémentation de plusieurs clés API."

---

# Autres personnalisations du SDK pour Android et FireOS

> Cet article de référence couvre des options de personnalisation et de configuration supplémentaires, telles que la journalisation verbeuse, la suppression de la journalisation et l’implémentation de plusieurs clés API.

## Utiliser R8 ou ProGuard avec Braze

La configuration de la [réduction du code](https://developer.android.com/studio/build/shrink-code) est automatiquement incluse dans votre intégration de Braze.

Les applications client qui obscurcissent le code Braze doivent stocker des fichiers de mappage de libération pour Braze afin d’interpréter les traces de pile. Si vous souhaitez continuer à conserver tous les codes Braze, ajoutez ce qui suit à votre fichier ProGuard :

```
-keep class bo.app.** { *; }
-keep class com.braze.** { *; }
```

## Journalisation

Par défaut, le niveau de journalisation du SDK Android de Braze est défini sur `INFO`. Vous pouvez [supprimer ces journaux](#suppressing-logs) ou [définir un niveau de journal différent](#enabling-logs), tel que `VERBOSE`, `DEBUG`, ou `WARN`.

### Activation des journaux {#enabling-logs}

Pour faciliter la résolution des problèmes dans votre application ou réduire les délais de résolution des problèmes avec le service d'assistance de Braze, vous devez activer les journaux détaillés pour le SDK. Lorsque vous envoyez des journaux verbeux à l'assistance Braze, veillez à ce qu'ils commencent dès le lancement de votre application et se terminent bien après l'apparition de votre problème.

Gardez à l'esprit que les journaux verbeux ne sont destinés qu'à votre environnement de développement, et que vous devez donc les désactiver avant de rendre votre application publique.

{% alert important %}
Activez l'option "verbose logs" avant tout autre appel dans `Application.onCreate()` pour vous assurer que vos logs sont aussi complets que possible.
{% endalert %}

{% tabs %}
{% tab Application %}
Pour activer les journaux directement dans votre application, ajoutez ce qui suit à la méthode `onCreate()` de votre application avant toute autre méthode.

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

Remplacez `MIN_LOG_LEVEL` par la **constante** du niveau de journalisation que vous souhaitez définir comme niveau de journalisation minimum. Tous les journaux d'un niveau `>=` au `MIN_LOG_LEVEL` que vous avez défini seront transmis à la méthode [`Log`](https://developer.android.com/reference/android/util/Log) par défaut d'Android. Tous les journaux `<` au `MIN_LOG_LEVEL` que vous avez défini seront rejetés.

| Constant    | Valeur          | Description                                                               |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | 2              | Enregistre les messages les plus détaillés pour le débogage et le développement.            |
| `DEBUG`     | 3              | Enregistre des messages descriptifs pour le débogage et le développement.                  |
| `INFO`      | 4              | Enregistre des messages d'information pour les faits marquants.                       |
| `WARN`      | 5              | Enregistre les messages d'avertissement pour identifier les situations potentiellement dangereuses.     |
| `ERROR`     | 6              | Enregistre les messages d'erreur pour indiquer les échecs de l'application ou les problèmes graves. |
| `ASSERT`    | 7              | Enregistre les messages d'assertion lorsque les conditions sont fausses pendant le développement.     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Par exemple, le code suivant transmettra les niveaux de journalisation `2`, `3`, `4`, `5`, `6` et `7` à la méthode `Log`.

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
Pour activer les journaux dans le `braze.xml`, ajoutez ce qui suit à votre fichier :

```xml
<integer name="com_braze_logger_initial_log_level">MIN_LOG_LEVEL</integer>
```

Remplacez `MIN_LOG_LEVEL` par la **valeur** du niveau de journalisation que vous souhaitez définir comme niveau de journalisation minimum. Tous les journaux d'un niveau `>=` au `MIN_LOG_LEVEL` que vous avez défini seront transmis à la méthode [`Log`](https://developer.android.com/reference/android/util/Log) par défaut d'Android. Tous les journaux `<` au `MIN_LOG_LEVEL` que vous avez défini seront rejetés.

| Constant    | Valeur          | Description                                                               |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | 2              | Enregistre les messages les plus détaillés pour le débogage et le développement.            |
| `DEBUG`     | 3              | Enregistre des messages descriptifs pour le débogage et le développement.                  |
| `INFO`      | 4              | Enregistre des messages d'information pour les faits marquants.                       |
| `WARN`      | 5              | Enregistre les messages d'avertissement pour identifier les situations potentiellement dangereuses.     |
| `ERROR`     | 6              | Enregistre les messages d'erreur pour indiquer les échecs de l'application ou les problèmes graves. |
| `ASSERT`    | 7              | Enregistre les messages d'assertion lorsque les conditions sont fausses pendant le développement.     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Par exemple, le code suivant transmettra les niveaux de journalisation `2`, `3`, `4`, `5`, `6` et `7` à la méthode `Log`.

```xml
<integer name="com_braze_logger_initial_log_level">2</integer>
```
{% endtab %}
{% endtabs %}

### Vérification des journaux de bord (verbose logs)

Pour vérifier que vos journaux sont définis sur `VERBOSE`, vérifiez si `V/Braze` apparaît quelque part dans vos journaux. Si c'est le cas, c'est que l'option de journalisation en mode verbeux a été activée avec succès. Par exemple :

```
2077-11-19 16:22:49.591 ? V/Braze v9.0.01 .bo.app.d3: Request started
```

### Suppression des journaux

Le niveau de journalisation par défaut du SDK Braze pour Android est `INFO`. Pour supprimer tous les journaux pour le SDK Android de Braze, appelez `BrazeLogger.SUPPRESS` dans la méthode `onCreate()` de votre application _avant_ toute autre méthode.

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

## Plusieurs clés API

Le cas d’usage le plus fréquent pour les clés API multiples est la séparation des clés API entre les variantes de version de débogage et de publication.

Pour basculer facilement entre plusieurs clés API dans vos versions, nous vous recommandons de créer un fichier `braze.xml` pour chaque [variante de version](https://developer.android.com/studio/build/build-variants.html) pertinente. Une variante de version est une combinaison du type de version et de la variété du produit. Remarquez que, par défaut, [un nouveau projet Android est configuré avec les types de version `debug` et `release`](http://tools.android.com/tech-docs/new-build-system/user-guide#TOC-Build-Types), et aucune variété de produit.

Pour chaque variante de version pertinente, créez un nouveau `braze.xml` pour elle dans `src/<build variant name>/res/values/` :

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">REPLACE_WITH_YOUR_BUILD_VARIANT_API_KEY</string>
</resources>
```

Lorsque la variante de version est compilée, elle utilisera la nouvelle clé API.

Consultez la documentation relative [à la configuration de l'exécution]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/) pour définir une clé API dans le code.
