---
nav_title: "Push-Storys"
article_title: Push-Storys
page_order: 2
page_type: reference
description: "In diesem Referenzartikel erfahren Sie, was Push Stories sind, wie Sie sie erstellen und welche Fragen häufig gestellt werden."
channel:
  - push

---

# Push-Storys

> Push-Storys sind eine neue Art von Push-Benachrichtigung, die von Braze eingeführt wurde. Diese Funktion ist eine Weiterentwicklung der von Instagram und Facebook bekannten Fotokarussell-Funktion und ermöglicht es Marketingfachleuten, innerhalb eines Push-Beitrags ein Karussell von Seiten zu erstellen, das eine umfassende, zusammenhängende Geschichte erzählt. Diese Seiten bestehen aus einem Bild, einer Klickaktion, einem Titel und einer Beschreibung. Ihre Nutzer können durch diese Seiten blättern und sich die Geschichte ansehen - so wie Sie sie erzählen.

| Android Beispiel (Erweitert) | IOS Beispiel (Erweitert) |
| :-----: | :----------: |
| ![]({% image_buster /assets/img_archive/pushstories_android_preview.png %}) | ![]({% image_buster /assets/img_archive/pushstories_ios_preview.png %}) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Bei iOS SDK-Versionen 3.13.0+ wird aufgrund einer Änderung in der Art und Weise, wie das SDK Bilder herunterlädt, in der komprimierten Ansicht des Push-Benachrichtigung keine Miniaturansicht des ersten Bildes angezeigt. Stellen Sie sicher, dass Ihre Nachricht Nutzer:innen dazu auffordert, den Push zu erweitern, um die Bilder zu sehen.
{% endalert %}

## Voraussetzungen

Die folgenden SDK-Versionen sind für den Empfang von Push Stories erforderlich:

{% sdk_min_versions swift:5.0.0 android:2.2.0 %}


## Wie Sie Push Stories verwenden

![]({% image_buster /assets/img_archive/pushstories_composer_dropdown2.png %}){: style="float:right;max-width:50%;margin-left:15px;margin-bottom:15px;"}

Um Push-Storys zu verwenden, gehen Sie wie folgt vor:

1. Erstellen Sie eine [Push-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/).
2. Wählen Sie für Ihren **Benachrichtigungstyp** **Push-Stories** aus.
3. Wählen Sie **iOS** oder **Android**. Beachten Sie, dass, wenn Sie beides für eine Push-Nachricht auswählen, die Option zum Erstellen einer Push-Story nicht angezeigt wird. 

### Push Story Komponist

Um eine Seite zu erstellen, führen Sie die folgenden Schritte aus:

1. Klicken Sie im Hauptcomposer auf **Seiten verwalten**.
    <br><br>![]({% image_buster /assets/img_archive/pushstories_add_pages.png %}){: style="max-width:70%"}<br><br>
2. Fügen Sie für jede Seite ein Bild ein, zusammen mit dem Klickverhalten für dieses Bild.
3. Falls gewünscht, fügen Sie einen **Titel** und eine **Beschreibung** für jede Seite hinzu. Wenn Sie einen Titel und eine Beschreibung für eine Seite verwenden, müssen diese für alle Seiten eingefügt werden.

Die Vorschauen werden reflektiert und sind interaktiv.

![]({% image_buster /assets/img_archive/pushstories_composer.png %}){: style="max-width:60%"}

{% alert important %}
Wenn Sie Bilder mit [Connected-Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content) einbinden, stellen Sie sicher, dass die URL Ihres Bildes mit `https://` beginnt. Die Verwendung von `http://` führt zum Absturz Ihrer App.
{% endalert %}

### Bild- und Textangaben

Die folgenden Bild- und Textspezifikationen gelten für den Foto-Karussell-Teil von Push Stories. Informationen über den grundlegenden Push, mit dem Benutzer interagieren, um die Push-Story zu aktivieren, finden Sie in den [Textrichtlinien für Push]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#native-mobile-push-notifications).

{% tabs %}
{% tab Images %}

- **Bildverhältnis:** 2:1 (erforderlich)
- **Empfohlene Bildgröße:** 500 KB
- **Maximale Bildgröße:** 5 MB
- **Dateitypen:** PNG, JPEG

{% endtab %}
{% tab Text %}

- **Titel:** 30 Zeichen (empfohlen)
- **Beschreibung:** 30 Zeichen (empfohlen)

{% alert note %}
Auch wenn die Zeichenlänge von Gerät zu Gerät variieren kann, sind der Titel und die Beschreibung für Push Stories auf jeweils eine Zeile begrenzt. Der restliche Teil Ihrer Nachricht wird abgeschnitten. Testen Sie Ihre Nachricht immer auf einem echten Gerät.
{% endalert %}

{% endtab %}
{% endtabs %}

### Push Story Segmentierung

Wenn Sie eine Kampagne oder ein Canvas erstellen, können Sie die Nutzer, die Sie ansprechen möchten, danach filtern, ob sie auf eine Push-Story-Seite geklickt haben. Wählen Sie dann die Kampagne und die Seite, mit der Sie Ihre Nutzer ansprechen möchten.

### Push Stories-Analysen

Die Analytik wird dem aktuellen Analysebereich für Push-Benachrichtigungen sehr ähnlich sein. Für die Analyse von Push Stories können Sie die Metrik **Direkte Öffnungen** öffnen, um die Klicks pro Seite zu sehen.

![iOS Push Performance-Tabelle mit Beispiel-Analytics und erweiterten Details für die Metrik Direkte Öffnungen.]({% image_buster /assets/img_archive/pushstories_analytics.png %})

## Fehlersuche

### iOS

#### Ich habe mir eine Push Story geschickt, aber keine Benachrichtigung erhalten

Apple verfügt über spezielle Regeln, die verhindern, dass bestimmte Arten von Benachrichtigungen an ein Gerät gesendet werden, basierend auf einer Reihe verschiedener Faktoren. Dazu gehört die Bewertung des Kunden-Datenplans, der Benachrichtigungsgröße und der Speicherkapazität der Kund:innen. Infolgedessen wird manchmal keine Benachrichtigung an Ihre Kunden gesendet.

Dies sind von Apple auferlegte Einschränkungen, die bei der Gestaltung Ihrer Push Story berücksichtigt werden sollten.

#### Ich habe mir selbst eine Push-Story geschickt, aber stattdessen die komprimierte Ansicht gesehen

In bestimmten Situationen, in denen nicht alle Seiten geladen werden können, z. B. bei einem Verlust der Datenverbindung, zeigt die Push Story nur die verkürzte Benachrichtigung an.

### Android

#### Push Story wird nach dem Anklicken des Bildes nicht beendet 

Standardmäßig werden Push Stories auf Android nicht beendet, nachdem ein Benutzer auf das Bild geklickt hat. Wenn Sie die Benachrichtigung ablehnen möchten, rufen Sie [`cancelNotification`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-notification-utils/index.html#-1466259649%2FFunctions%2F-1725759721) auf.  

