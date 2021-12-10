---
nav_title: Cas d'utilisation avancés
article_title: Cas d'utilisation de SDK avancé pour l'unité
platform:
  - Unité
  - iOS
  - Android
page_order: 7
description: "Cet article de référence couvre les cas d'utilisation avancés du SDK pour la plate-forme Unity."
---

# Personnalisation du package Unity

Vous pouvez choisir de personnaliser et d'exporter le paquet Braze Unity en utilisant les scripts fournis.

1. Clonez le projet [Braze Unity SDK Github][1]:

    ```bash
    git clone git@github.com:Appboy/appboy-unity-sdk.git
    ```
2. From the `appboy-unity-sdk/scripts` directory, run `./generate_package.sh` to export the Unity packages.
    - L'unité doit être ouverte en exécutant `generate_package.sh`.
3. Les paquets seront exportés vers `appboy-unity-sdk/unity-package/`.
4. Dans l'éditeur Unity, importez le paquet souhaité dans votre projet Unity en naviguant vers `Assets > Import Package > Pack personnalisé`.
5. (Facultatif) Désélectionnez les fichiers que vous ne souhaitez pas importer.

Vous pouvez personnaliser le package Unity exporté en modifiant à la fois `generate_package.sh` et le script d'exportation situé à `Assets/Editor/Build.cs`.

## Compatibilité Prime 31

Afin d'utiliser le plugin Braze Unity avec les plug-ins Prime31, éditez `AndroidManifest.xml` de votre projet pour utiliser les classes Activités compatibles Prime31. Changer toutes les références de `com.appboy.unity.AppboyUnityPlayerActivity` en `com.appboy.unity.prime31compatible.AppboyUnityPlayerActivity`

## Push ADM Amazon

Braze prend en charge l'intégration de [Amazon ADM push][10] dans les applications Unity. Si vous souhaitez intégrer Amazon ADM push, créez un fichier appelé `api_key. xt` contenant votre clé API ADM et placez-la dans le dossier `Plugins/Android/assets/`.  Pour plus d'informations sur l'intégration de l'ADM Amazon avec le Brésil, veuillez visiter notre [instructions d'intégration ADM][11].

[1]: https://github.com/appboy/appboy-unity-sdk
[10]: https://developer.amazon.com/public/apis/engage/device-messaging
[11]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/adm_push_notifications/
