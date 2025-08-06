---
nav_title: SDK-Ersteinrichtung mit Eclipse
page_order: 1

page_type: update
description: "Dieser archivierte Artikel beschreibt, wie Sie ein erstes SDK-Setup mit Eclipse durchführen. Braze hat die Unterstützung für die Eclipse IDE eingestellt."
---

# SDK-Ersteinrichtung mit Eclipse

{% alert update %}
Braze hat die Unterstützung für die Eclipse IDE entfernt, da [Google die Unterstützung für das Eclipse Android Developer Tools Plugin Sunsetting](http://android-developers.blogspot.com/2015/06/an-update-on-eclipse-android-developer.html). Wenn Sie vor der Migration Hilfe bei der Integration von Eclipse benötigen, [senden Sie eine E-Mail an den Support]({{site.baseurl}}/support_contact/).
{% endalert %}

## Schritt 1
Klonen Sie in Ihrer Befehlszeile das [Braze Android GitHub Repository](https://github.com/braze-inc/braze-android-sdk).

```bash
$ git clone git@github.com:braze-inc/braze-android-sdk.git
```

## Schritt 2
Importieren Sie das Braze-Projekt in Ihren lokalen Workspace

In Eclipse:

  - Navigieren Sie zu Datei > Importieren.

    ![Datei-Import]({{site.baseurl}}/assets/img_archive/file_import.png)
  - Wählen Sie Android > Vorhandener Android Code in Workspace.

    ![Android Import]({{site.baseurl}}/assets/img_archive/android_import.png)
  - Klicken Sie auf "Durchsuchen".

    ![Durchsuchen]({{site.baseurl}}/assets/img_archive/click_browse.png)
  - Markieren Sie den Braze UI Projektordner sowie "Projekt in Workspace kopieren" und klicken Sie auf "Fertig stellen".

    ![Android UI Projekt auswählen]({{site.baseurl}}/assets/img_archive/select_project_android.png)

## Schritt 3
Referenzieren Sie Braze in Ihrem eigenen Projekt.
In Eclipse:

  - Klicken Sie mit der rechten Maustaste auf Ihr Projekt und wählen Sie "Eigenschaften".

    ![Klicken Sie auf Eigenschaften]({{site.baseurl}}/assets/img_archive/click_properties.png)
  - Klicken Sie unter "Android" im Abschnitt "Bibliothek" auf "Hinzufügen..." und fügen Sie android-sdk-ui als Bibliothek zu Ihrer App hinzu.

    ![Braze Add]({{site.baseurl}}/assets/img_archive/add_appboy_ui.png)

## Schritt 4
Beheben Sie Abhängigkeitsfehler und korrigieren Sie das Build-Targeting.

Es kann sein, dass beim Code von Braze Fehler auftreten, weil die Abhängigkeiten nicht ausgefüllt sind und das Targeting für die Erstellung möglicherweise falsch ist:

   - Klicken Sie mit der rechten Maustaste auf das Braze UI-Projekt und wählen Sie Eigenschaften->Android, um sicherzustellen, dass das Build-Target auf die aktuelle Version der Braze-Build-Tools eingestellt ist.

      ![Ziel aufbauen]({{site.baseurl}}/assets/img_archive/build_target.png)
   - Klicken Sie mit der rechten Maustaste auf das Braze UI Projekt und wählen Sie Eigenschaften->Java Build Path->Add JARs... und fügen Sie 'android-support-v4.jar' aus der Hauptanwendung als Bibliothek hinzu.

      ![Support]({{site.baseurl}}/assets/img_archive/android_support_v4.png)

## Schritt 5

Fügen Sie die letzten Teile hinzu.

  - Für SDK Version 1.10.0 oder höher, müssen Sie Folgendes hinzufügen
  `<service android:name="com.appboy.services.AppboyDataSyncService" />`
  zu Ihrem AndroidManifest.xml, da Eclipse das Zusammenführen von Manifesten nicht unterstützt.

  - Für SDK Version 1.7.0 oder höher müssen Sie "assets/fontawesome-webfont.ttf" aus unserem Bibliothek-Projekt in Ihre Anwendung kopieren. Eclipse fügt den Assets-Ordner von Bibliotheken nicht automatisch ein.

