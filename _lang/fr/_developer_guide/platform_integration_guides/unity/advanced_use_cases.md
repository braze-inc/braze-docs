---
nav_title: Cas d’utilisation avancés
article_title: Exemples d’utilisation de SDK avancés pour Unity
platform: 
  - Unity
  - iOS
  - Android
page_order: 7
description: "Cet article de référence couvre les cas d’utilisation avancés de SDK pour la plateforme Unity."
---

# Cas d’utilisation avancés

> Cet article de référence couvre les cas d’utilisation avancés de SDK pour la plateforme Unity.

## Personnaliser le package Unity

Vous pouvez choisir de personnaliser et d’exporter le package Unity de Braze en utilisant les scripts fournis.

1. Cloner le [Projet Braze Unity SDK GitHub][1] :

	```bash
	git clone git@github.com:Appboy/appboy-unity-sdk.git
	```
2. Dans le répertoire `appboy-unity-sdk/scripts`, exécutez `./generate_package.sh` pour exporter les packages Unity. Unity doit être ouvert pendant l’exécution de `generate_package.sh`.
3. Les packages seront exportés vers `appboy-unity-sdk/unity-package/`.
4. Dans Unity Editor, importez le package souhaité dans votre projet Unity en naviguant vers **Actifs > Importer un package > Personnaliser le package**.
5. (Facultatif) Désélectionnez les fichiers que vous ne souhaitez pas importer.

Vous pouvez personnaliser le package Unity exporté en modifiant à la fois `generate_package.sh` et le script d’exportation situé sur `Assets/Editor/Build.cs`.

## Compatibilité Prime 31

Pour utiliser le plug-in Unity de Braze avec les plug-ins Prime31, modifiez le `AndroidManifest.xml` de votre projet pour utiliser les classes d’activité compatibles Prime31. Modifier toutes les références de
`com.appboy.unity.AppboyUnityPlayerActivity` vers `com.appboy.unity.prime31compatible.AppboyUnityPlayerActivity`

## Notification push Amazon ADM

Braze prend en charge l’intégration des [notifications push Amazon ADM][10] dans les applications Unity. Si vous souhaitez intégrer les notifications push Amazon ADM, créez un fichier appelé `api_key.txt` contenant votre clé ADM API et placez-le dans le dossier `Plugins/Android/assets/`.  Pour plus d’informations sur l’intégration d’Amazon ADM avec Braze, consultez nos [Instructions d’intégration des notifications push ADM][11].

[1]: https://github.com/appboy/appboy-unity-sdk
[10]: https://developer.amazon.com/public/apis/engage/device-messaging
[11]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/adm_push_notifications/
