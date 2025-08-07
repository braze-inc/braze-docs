---
nav_title: Platzierungen erstellen
article_title: Erstellen von Bannerkartenplatzierungen für das Braze SDK
hidden: true
description: "Dieser Referenzartikel behandelt Banner-Cards und die Integration dieses Features in das Braze SDK."
platform:
  - iOS
  - Android
  - Web
  
---

# Erstellen von Bannerkartenplatzierungen

> Bevor Sie eine Kampagne für eine Bannerkarte in Ihrer App starten, müssen Sie eine Platzierung im Braze-Dashboard erstellen. Standorte sind Standorte, die Sie in Ihrer App definieren und an denen Bannerkarten angezeigt werden können.

{% alert important %}
Banner-Cards befinden sich derzeit in der Early Access-Phase. Wenden Sie sich an Ihren Braze Account Manager, wenn Sie an der Early-Access-Phase teilnehmen möchten.
{% endalert %}

## Voraussetzungen

Das sind die Mindestversionen des SDK, um Banner Cards zu verwenden:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.6.0 %}

## Erstellen einer Platzierung

### Schritt 1: Eine neue Platzierung erstellen

Gehen Sie zu **Einstellungen** > **Bannerkarten-Platzierungen** und wählen Sie dann **Platzierung erstellen**.

![Abschnitt "Banner-Card-Platzierungen" zum Erstellen von Platzierungs-IDs.]({% image_buster /assets/img/banners/create_placement.png %})

### Schritt 2: Details ausfüllen

Benennen Sie Ihre Platzierung und geben Sie ihr eine **Platzierungs-ID**. Optional können Sie eine Beschreibung für Ihre Platzierung hinzufügen.

Arbeiten Sie mit Ihrem Marketing Team zusammen, um diese ID zu erstellen. Dies ist die ID, die Sie im Code Ihrer App referenzieren werden. Ihr Marketing Team wird die ID verwenden, um dem Standort in Ihrer App eine Kampagne zuzuweisen. 

{% alert important %}
Vermeiden Sie es, Ihre Platzierungs-ID nach dem Start zu bearbeiten, da dies die Integration mit Ihrer App oder Website unterbrechen kann.
{% endalert %}

![Platzierungsdetails, die eine Banner-Card bezeichnen, in der linken Seitenleiste für einen Frühjahrsabverkauf]({% image_buster /assets/img/banners/placement_details_example.png %})

Wie Sie eine Kampagne einführen können, erfahren Sie unter [Erstellen einer]({{site.baseurl}}/create_banner_card/) Bannerkarte.

## Nächste Schritte

Jetzt, wo Sie Ihre Bannerkartenplatzierungen erstellt haben, können Sie:

- [Banner-Cards integrieren]({{site.baseurl}}/developer_guide/banner_cards/integration/)
- [Banner-Cards erstellen]({{site.baseurl}}/create_banner_card/)
