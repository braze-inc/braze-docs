---
nav_title: Erste SDK-Einrichtung mit Eclipse
page_order: 1

page_type: update
description: "Dieser archivierte Artikel beschreibt, wie Sie ein erstes SDK-Setup mit Eclipse durchführen. Braze hat die Unterstützung für die Eclipse IDE eingestellt."
---

# Erste SDK-Einrichtung mit Eclipse

{% alert update %}
Braze hat die Unterstützung für die Eclipse IDE entfernt, da [Google die Unterstützung für das Eclipse Android Developer Tools Plugin eingestellt hat](http://android-developers.blogspot.com/2015/06/an-update-on-eclipse-android-developer.html). Wenn Sie vor der Migration Hilfe bei der Eclipse-Integration benötigen, [wenden Sie sich bitte per E-Mail an den Support]({{site.baseurl}}/support_contact/).
{% endalert %}

## Schritt 1
Klonen Sie in Ihrer Befehlszeile das [Braze Android GitHub Repository][03].

```bash
$ git clone git@github.com:braze-inc/braze-android-sdk.git
```

## Schritt 2
Importieren Sie das Braze-Projekt in Ihren lokalen Arbeitsbereich

In Eclipse:

  - Navigieren Sie zu Datei > Importieren.

    ![Datei-Import][04]
  - Wählen Sie Android > Vorhandener Android-Code im Arbeitsbereich.

    ![Android Import][05]
  - Klicken Sie auf "Durchsuchen".

    ![Durchsuchen][06]
  - Markieren Sie den Braze UI-Projektordner sowie "Projekt in Arbeitsbereich kopieren" und klicken Sie auf "Fertig stellen".

    ![Wählen Sie Android UI Projekt][07]

## Schritt 3
Referenzieren Sie Braze in Ihrem eigenen Projekt.
In Eclipse:

  - Klicken Sie mit der rechten Maustaste auf Ihr Projekt und wählen Sie "Eigenschaften".

    ![Klicken Sie auf Eigenschaften][08]
  - Klicken Sie unter "Android" im Abschnitt "Bibliothek" auf "Hinzufügen..." und fügen Sie android-sdk-ui als Bibliothek zu Ihrer App hinzu.

    ![Hartlöten hinzufügen][09]

## Schritt 4
Beheben Sie Abhängigkeitsfehler und korrigieren Sie das Build-Ziel.

Es kann sein, dass Sie zu diesem Zeitpunkt Fehler im Braze-Code sehen. Das liegt daran, dass die Abhängigkeiten nicht ausgefüllt sind und das Build-Ziel möglicherweise falsch ist:

   - Klicken Sie mit der rechten Maustaste auf das Braze UI-Projekt und wählen Sie Eigenschaften->Android, um sicherzustellen, dass das Build-Ziel auf die aktuelle Version der Build-Tools von Braze eingestellt ist.

      ![Ziel bauen][10]
   - Klicken Sie mit der rechten Maustaste auf das Braze UI-Projekt und wählen Sie Eigenschaften->Java Build Path->Add JARs... und fügen Sie 'android-support-v4.jar' aus der Hauptanwendung als Bibliothek hinzu.

      ![Unterstützen Sie][11]

## Schritt 5

Fügen Sie die letzten Teile hinzu.

  - Für SDK Version 1.10.0 oder höher, müssen Sie Folgendes hinzufügen
  `<service android:name="com.appboy.services.AppboyDataSyncService" />`
  zu Ihrem AndroidManifest.xml, da Eclipse das Zusammenführen von Manifesten nicht unterstützt.

  - Für SDK Version 1.7.0 oder höher müssen Sie "assets/fontawesome-webfont.ttf" aus unserem Bibliotheksprojekt in Ihre Anwendung kopieren. Eclipse fügt nicht automatisch den Ordner Assets aus Bibliotheken ein.

[03]: https://github.com/braze-inc/braze-android-sdk "Appboy Android GitHub Repository"
[04]: {{site.baseurl}}/assets/img_archive/file_import.png
[05]: {{site.baseurl}}/assets/img_archive/android_import.png
[06]: {{site.baseurl}}/assets/img_archive/click_browse.png
[07]: {{site.baseurl}}/assets/img_archive/select_project_android.png
[08]: {{site.baseurl}}/assets/img_archive/click_properties.png
[09]: {{site.baseurl}}/assets/img_archive/add_appboy_ui.png
[10]: {{site.baseurl}}/assets/img_archive/build_target.png
[11]: {{site.baseurl}}/assets/img_archive/android_support_v4.png
