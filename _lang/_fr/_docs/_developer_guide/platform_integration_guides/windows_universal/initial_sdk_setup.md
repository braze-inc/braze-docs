---
nav_title: Configuration initiale du SDK
article_title: Configuration initiale du SDK pour Windows Universal
platform: Univers Windows
page_order: 0
description: "Cet article de référence couvre les étapes d'intégration du SDK initial pour l'intégration du Braze SDK sur votre plate-forme Windows Universelle."
---

# Intégration initiale du SDK

Le SDK Braze vous fournira une API pour rapporter les informations à utiliser dans l'analytique, la segmentation, et engagement, ainsi que la possibilité d'enregistrer des utilisateurs pour l'envoi et recevoir des notifications.

> Le SDK Windows Universal est également compatible avec les applications Windows Xamarin.

## Étape 1 : Installez le SDK via le gestionnaire de paquets NuGet

Le SDK Windows Universal est installé via [NuGet Package Manager][14]. Pour installer le Braze Windows SDK via NuGet:

1. Clic droit sur le fichier du projet
2. Cliquez sur "Gérer les paquets Nuget"
3. Cliquez sur "En ligne" dans le menu déroulant à gauche
4. Rechercher dans "NuGet.org" pour "Appboy"
5. Cliquez sur le paquet NuGet "AppboyPlatform.Universal.Release" et cliquez sur Installer

> La bibliothèque universelle Windows devrait être utilisée pour toutes les applications Windows 8.1, Windows Phone 8.1 et UWP.

## Étape 2 : Création et configuration de AppboyConfiguration.xml

Créez un fichier appelé `AppboyConfiguration.xml` à la racine de votre projet et ajoutez le code snippet suivant dans ce fichier :

```xml
    <?xml version="1.0" encoding="utf-8"?>
    <AppboyConfig>
        <ApiKey>VOTRE_API_KEY_ICI</ApiKey>
    </AppboyConfig>
```
> N'oubliez pas de mettre à jour `VOTRE_API_KEY_ICI` avec votre clé API qui se trouve sur la page [Paramètres][1] dans le tableau de bord de Braze.

Une fois que vous avez ajouté ce snippet, assurez-vous de modifier les propriétés de fichier suivantes pour `AppboyConfiguration.xml`

1. Définissez l'action `Build Action` à `Contenu`
2. Définir `Copier dans le répertoire de sortie` à `Copier toujours`

## Étape 3 : Configuration de package.appxmanifest

Dans l'onglet « Capacités », assurez-vous que `Internet (Client)` est vérifié. !\[Client Internet\]\[18\]

## Étape 4 : Modifier la classe de votre application

- Ajoutez ce qui suit aux `utilisations` de votre fichier `App.xaml.cs`:

```csharp
en utilisant AppboyPlatform.PCL.Managers;
en utilisant AppboyPlatform.Universal;
en utilisant AppboyPlatform.Universal.Managers.PushArgs;
```

- Appelez ce qui suit dans votre méthode de cycle de vie `OnLaunched`:

```csharp
Appboy.SharedInstance.OpenSession();
```

- Appelez ce qui suit dans votre méthode de cycle de vie `En suspendant`:

```csharp
Appboy.SharedInstance.CloseSession();
```

## Intégration de base du SDK terminée

Braze devrait maintenant collecter des données de votre application. Veuillez consulter les sections suivantes sur la façon d'enregistrer les attributs, les événements et les achats dans notre SDK et sur la façon d'instruire les messages push.

> Si vous utilisez le projet Braze Unity dans la même application, vous devrez peut-être qualifier entièrement les appels vers Braze en tant que « AppboyPlatform.Universal.Appboyboyboyboy »
[18]: {% image_buster /assets/img_archive/internet_client.png %}

[1]: https://dashboard-01.braze.com/app_settings/app_settings "Settings"
[14]: http://www.nuget.org/
