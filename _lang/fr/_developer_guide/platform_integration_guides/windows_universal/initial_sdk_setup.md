---
nav_title: Configuration initiale du SDK
article_title: Configuration initiale du SDK pour Windows Universal
platform: Windows Universal
page_order: 0
description: "Cet article de référence couvre les étapes initiales d’intégration SDK pour intégrer le SDK Braze sur votre plateforme Windows Universal."
search_rank: 1
---

# Intégration SDK initiale
{% multi_lang_include archive/windows_deprecation.md %}

Le SDK Braze vous fournira une API pour signaler les informations à utiliser pour l’analytique, la segmentation et l’engagement, ainsi que la possibilité d’enregistrer des utilisateurs pour les notifications push et reçues.

>  Le SDK pour Windows Universal est également compatible avec les applications Xamarin pour Windows.

## Étape 1 : Installer le SDK via le gestionnaire de package NuGet

Le SDK pour Windows Universal est installé à l’aide du [gestionnaire de package NuGet.][14]. Pour installer le SDK Braze pour Windows via NuGet :

1. Cliquez avec le bouton droit sur le fichier du projet
2. Cliquez sur « Gérer les package NuGet »"
3. Cliquez sur « En ligne » dans le menu déroulant de gauche
4. Rechercher « Appboy » dans « NuGet.org » "
5. Cliquez sur le package « AppboyPlatform.Universal.Release » de NuGet et cliquez sur Installer

>  La bibliothèque Windows Universal doit être utilisée pour toutes les applications Windows 8.1, Windows Phone 8.1 et UWP.

## Étape 2 : Créer et configurer AppboyConfiguration.xml

Créez un fichier appelé `AppboyConfiguration.xml` dans le répertoire racine de votre projet et ajoutez l’extrait de code suivant dans ce fichier :

```xml
    <?xml version="1.0" encoding="utf-8"?>
    <AppboyConfig>
        <ApiKey>YOUR_API_KEY_HERE</ApiKey>
    </AppboyConfig>
```
>  Assurez-vous de mettre à jour `YOUR_API_KEY_HERE` avec votre clé API qui se trouve sur la page **Console du développeur** du tableau de bord de Braze.

Une fois que vous avez ajouté cet extrait de code, assurez-vous de modifier les propriétés de fichier suivantes pour `AppboyConfiguration.xml`

1. Définir le `Build Action` à `Content`
2. Définir `Copy to Output Directory` à `Copy Always`

## Étape 3 : Configurer package.appxmanifest

Dans l’onglet « Capacités », assurez-vous que `Internet (Client)` est coché.
![][18]

## Étape 4 : Modifier la classe de votre application

- Ajouter les éléments suivants aux `usings` de votre fichier `App.xaml.cs` :

```csharp
using AppboyPlatform.PCL.Managers;
using AppboyPlatform.Universal;
using AppboyPlatform.Universal.Managers.PushArgs;
```

- Appelez les éléments suivants dans votre méthode de cycle de vie `OnLaunched` :

```csharp
Appboy.SharedInstance.OpenSession();
```

- Appelez les éléments suivants dans votre méthode de cycle de vie `OnSuspending` :

```csharp
Appboy.SharedInstance.CloseSession();
```

## Intégration SDK de base terminée

Braze devrait maintenant collecter des données depuis votre application. Consultez les articles suivants concernant la manière d’enregistrer des [attributs]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/setting_custom_attributes/), des [événements]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/logging_custom_events) et des [achats]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/logging_purchases) à notre SDK et l’implémentation de la messagerie des notifications push.

>  Si vous utilisez le projet Braze Unity au sein de la même application, vous devrez peut-être qualifier pleinement les appels vers Braze en tant que « AppboyPlatform.Universal.Appboy »

[14]: http://www.nuget.org/
[18]: {% image_buster /assets/img_archive/internet_client.png %}
