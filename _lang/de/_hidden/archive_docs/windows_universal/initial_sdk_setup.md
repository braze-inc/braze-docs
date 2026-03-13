---
nav_title: SDK-Ersteinrichtung
article_title: Erste SDK-Einrichtung für Windows Universal
platform: Windows Universal
page_order: 0
description: "Dieser referenzierte Artikel beschreibt die ersten Schritte der SDK-Integration, um das Braze SDK auf Ihrer Windows Universal Plattform zu integrieren."
search_rank: 1
hidden: true
---

# Erste SDK-Integration
{% multi_lang_include archive/windows_deprecation.md %}

Das Braze SDK stellt Ihnen eine API zur Verfügung, mit der Sie Informationen für Analytics, Segmentierung und Engagement melden können, sowie die Möglichkeit, Nutzer:innen für Push-Benachrichtigungen zu registrieren und diese zu empfangen.

>  Das Windows Universal SDK ist auch mit .NET MAUI Windows Apps kompatibel.

## Schritt 1: Installieren Sie das SDK über die NuGet Paketverwaltung

Das Windows Universal SDK wird über den [NuGet Package Manager:](http://www.nuget.org/)in installiert. So installieren Sie das Braze Windows SDK über NuGet:

1. Klicken Sie mit der rechten Maustaste auf die Projektdatei
2. Klicken Sie auf "NuGet Pakete verwalten".
3. Klicken Sie auf "Online" im Dropdown-Menü auf der linken Seite
4. Suchen Sie in "NuGet.org" nach "Appboy".
5. Klicken Sie auf das NuGet-Paket "AppboyPlatform.Universal.Release" und klicken Sie auf Installieren

>  Die Windows Universal Library sollte für alle Windows 8.1-, Windows Phone 8.1- und UWP-Anwendungen verwendet werden.

## Schritt 2: Erstellung und Konfiguration von AppboyConfiguration.xml

Erstellen Sie eine Datei namens `AppboyConfiguration.xml` im Stammverzeichnis Ihres Projekts und fügen Sie den folgenden Code Snippet in diese Datei ein:

```xml
    <?xml version="1.0" encoding="utf-8"?>
    <AppboyConfig>
        <ApiKey>YOUR_API_KEY_HERE</ApiKey>
    </AppboyConfig>
```

>  Stellen Sie sicher, dass Sie `YOUR_API_KEY_HERE` mit Ihrem API-Schlüssel aktualisieren, den Sie auf der Seite [API-Schlüssel]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) finden.

Sobald Sie dieses Snippet hinzugefügt haben, müssen Sie die folgenden Eigenschaften der Datei für `AppboyConfiguration.xml`

1. Stellen Sie die `Build Action` auf `Content`
2. Setzen Sie `Copy to Output Directory` auf `Copy Always`

## Schritt 3: Konfigurieren von package.appxmanifest

Vergewissern Sie sich auf dem Tab "Fähigkeiten", dass `Internet (Client)` markiert ist.
![]({% image_buster /assets/img_archive/internet_client.png %})

## Schritt 4: Bearbeiten Ihrer App-Klasse

- Fügen Sie Folgendes in die `usings` Ihrer `App.xaml.cs` Datei ein:

```csharp
using AppboyPlatform.PCL.Managers;
using AppboyPlatform.Universal;
using AppboyPlatform.Universal.Managers.PushArgs;
```

- Rufen Sie innerhalb Ihrer Methode `OnLaunched` lifecycle folgendes auf:

```csharp
Appboy.SharedInstance.OpenSession();
```

- Rufen Sie innerhalb Ihrer Methode `OnSuspending` lifecycle folgendes auf:

```csharp
Appboy.SharedInstance.CloseSession();
```

## Grundlegende SDK-Integration abgeschlossen

Braze sollte nun Daten von Ihrer Anwendung sammeln. In den folgenden Artikeln erfahren Sie, wie Sie [Attribute]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/), [Ereignisse]({{site.baseurl}}/developer_guide/analytics/logging_events/) und [Käufe]({{site.baseurl}}/developer_guide/analytics/logging_purchases/) in unserem SDK protokollieren und wie Sie Push Messaging einsetzen können.

>  Wenn Sie das Unity-Projekt von Braze in der gleichen App verwenden, müssen Sie Aufrufe an Braze möglicherweise vollständig als "AppboyPlatform.Universal.Appboy" qualifizieren.

