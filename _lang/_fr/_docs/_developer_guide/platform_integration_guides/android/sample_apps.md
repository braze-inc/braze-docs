---
nav_title: Exemple d'applications
article_title: Exemple d'applications pour Android/FireOS
platform:
  - Android
  - Pare-feu
page_order: 10
description: "Cet article couvre les exemples d'applications Android."
---

# Exemple d'applications

Les SDK de Braze sont chacun fournis avec un exemple d'application dans le référentiel pour votre commodité. Chacune de ces applications est entièrement constructible pour que vous puissiez tester les fonctionnalités de Braze en plus de les implémenter dans vos propres applications. Tester le comportement dans votre propre application par rapport au comportement attendu et aux chemins de code dans les exemples d'applications est un excellent moyen de déboguer tous les problèmes que vous pouvez rencontrer.

## Construire l'application de test Droidboy
L'application de test de Braze dans le dépôt [Android SDK github][3] est appelée Droidboy. Suivez les instructions ci-dessous pour en construire une copie entièrement fonctionnelle à côté de votre projet.

- Créez un nouveau ["Groupe d'application"][25] et notez la clé API de Braze.
- Copiez votre identifiant FCM Sender ID et votre clé API Braze dans les endroits appropriés dans `/droidboy/res/values/braze. ml` (dans les balises pour les chaînes nommées "com_appboy_push_fcm_sender_id" et "com_appboy_api_key", respectivement).
- Copiez votre clé d'API FCM dans votre page **Paramètres**.
- Pour assembler l'APK Droidboy, exécutez la commande suivante dans le répertoire SDK :

```
Montage de ./gradlew
```
> Utilisez `gradlew.bat` sur Windows

- Pour installer automatiquement l'APK Droidboy sur un périphérique de test, exécutez la commande suivante dans le répertoire SDK :

```
./gradlew installDebug
```

## Construire l'application de test Bonjour Braze
L'application de test Hello Braze montre un cas d'utilisation minimal du Braze SDK, et montre également comment intégrer facilement le Braze SDK dans un projet de gradle.

1. Copiez votre clé API depuis votre page **Paramètres** dans votre fichier `braze.xml` dans le dossier `res/values`. !\[HelloBraze\]\[34\]

2. Pour installer l'application exemple sur un périphérique ou un émulateur, exécutez la commande suivante dans le répertoire SDK :

```
./gradlew installDebug
```

> Si vous n'avez pas votre variable `ANDROID_HOME` correctement définie ou si vous n'avez pas de variable `locale. roperties` dossier avec un dossier `sdk.dir` valide, ce plugin installera également le SDK de base pour vous. Voir le repo du plugin [][27] pour plus d'informations.

Pour plus d'informations sur le système de compilation d'Android SDK, consultez le [dépôt Github readme][26].
[34]: {% image_buster /assets/img_archive/hello_appboy.png %}

[25]: {{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#app-group-configuration
[26]: https://github.com/Appboy/appboy-android-sdk/blob/master/README.md
[27]: https://github.com/JakeWharton/sdk-manager-plugin
[27]: https://github.com/JakeWharton/sdk-manager-plugin
[3]: https://github.com/appboy/appboy-android-sdk "Appboy Android Github Repository"
