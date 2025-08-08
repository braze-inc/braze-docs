---
nav_title: Judo
article_title: Judo
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Judo, einer no-code Server-gesteuerten UI-Plattform, die es Ihnen erlaubt, Standort-Kontext und Tracking zu Ihren iOS- und Android-Apps hinzuzufügen."
alias: /partners/judo/
page_type: partner
search_tag: Partner

---

# Judo

> [Judo](https://judo.app) ist eine Server-gesteuerte UI-Plattform, die es Publishern ermöglicht, ohne App-Updates ein reichhaltiges, ansprechendes Nutzer:in-Erlebnis zu liefern.

_Diese Integration wird von Judo gepflegt._

## Über die Integration

Die Integration von Braze und Judo bietet maßgeschneiderte Erlebnisse in Ihren Kampagnen und Canvase. Anstelle einer einfachen, mit Templates versehenen Landing Page kann eine Kampagne von Braze Inhalte enthalten, die mehrere Bildschirme, Modals, Videos, angepasste Schriftarten und Unterstützungseinstellungen wie Dark Mode und Barrierefreiheit umfassen, die ohne Code entwickelt und ohne App-Updates bereitgestellt werden. Daten von Braze können auch verwendet werden, um personalisierte Inhalte in einem Judo-Erlebnis zu unterstützen. Nutzer:innen-Ereignisse und Daten aus dem Erlebnis können für Attribution und Targeting in Braze zurückgeführt werden.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Judo Konto | Um diese Partnerschaft zu nutzen, benötigen Sie ein [Judo-Konto](https://www.judo.app/). |
| Judo SDK | Das Judo SDK muss in Ihre [iOS-](https://github.com/judoapp/judo-ios/) und/oder [Android-Apps](https://github.com/judoapp/judo-android) integriert werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

**Onboarding**: App-Herausgeber, die Judo verwenden, erstellen und implementieren reichhaltige, native Onboarding-Erlebnisse. Diese Erlebnisse können nun ein Element einer kanalübergreifenden, personalisierten Onboarding-Reise sein, die über Braze koordiniert wird. Die Erlebnisse können personalisiert und ohne App-Updates schnell aktualisiert werden, um die Wirksamkeit verschiedener In-App-Flows zu testen.

**Konversion**: App-Publisher können die Daten von Braze nutzen, um ein personalisiertes App-Erlebnis zu schaffen, um In-App-Käufe, bezahlte Abos oder kontextuelles Merchandising mit Hilfe von Integrations-Hooks in Judo zu fördern. Der Zugriff auf diese Erlebnisse kann über Engagement Marketing Kampagnen in Braze getriggert werden.

**Ereignisgesteuerte Inhalte**: Judo wird in erster Linie im Sport und in der Unterhaltung eingesetzt, um eine Vorschau auf Veranstaltungen zu geben, sie zu bewerben und zu rekapitulieren. Diese Fähigkeit lässt sich auch in anderen Branchen für saisonale und nachrichtenorientierte Inhalte einsetzen. Durch die Verknüpfung von Messaging zur Förderung oder Hervorhebung von Ereignissen mit reichhaltigen In-App-Erlebnissen können Verlage das Engagement steigern, indem sie kontextuell relevant sind.

## Side-by-side-Integration von SDKs

Judo bietet zusätzliche Bibliotheken, die einen Teil des Aufwands automatisieren, der für die Integration der SDKs von Judo und Braze in Ihre mobilen Apps erforderlich ist. 

### Schritt 1: Installieren Sie die Judo-Braze Integration Bibliothek

Installieren und richten Sie die Judo-Braze Integration Bibliothek in Ihren Apps ein. Dadurch wird das Tracking von Ereignissen automatisch aktiviert.

- [iOS-Installation
Anweisungen](https://github.com/judoapp/judo-braze-ios/wiki#installation)
- [Android-Installation
Anweisungen](https://github.com/judoapp/judo-braze-android/wiki#installation).

### Schritt 2: In-App-Nachrichten konfigurieren

In diesem Schritt werden angepasste `ABKInAppMessageControllerDelegate` und `IInAppMessageManagerListener` Implementierungen für iOS und Android erstellt.

Sehen Sie sich die Dokumentation zur Einrichtung von In-App-Nachrichten an, die für jede der Integrations-Bibliotheken mitgeliefert wird:

- [iOS In-App Messaging
Einrichtung](https://github.com/judoapp/judo-braze-ios/wiki#in-app-messaging-setup)
- [Android In-App Messaging
Einrichtung](https://github.com/judoapp/judo-braze-android/wiki#in-app-messaging-setup).

## Verwendung dieser Integration

Sobald Sie die App-seitige Integration abgeschlossen haben, können Sie sie testen, indem Sie eine In-App-Nachricht-Kampagne von Braze für ein Judo-Erlebnis ausführen, um zu überprüfen, ob sie wie erwartet funktioniert.

### Schritt 1: Erstellen Sie eine In-App-Nachricht-Kampagne mit angepasstem Code

Erstellen Sie auf der Braze-Plattform eine In-App-Nachricht-Kampagne mit einem Nachrichtentyp **mit angepasstem Code**. Als nächstes wählen Sie **HTML Upload** als angepassten Typ aus. Stellen Sie sicher, dass Sie den Inhalt der Nachricht mit den Basisfeldern für In-App-Nachricht ausfüllen; dieser Inhalt wird dem Nutzer:innen nicht angezeigt.

![Ein Bild davon, wie das Dashboard aussieht, wenn Sie den Nachrichtentyp "Custom Code" auswählen.]({% image_buster /assets/img/judo/braze-campaign-select-custom-type.png %})

Als nächstes verwenden Sie das folgende minimale HTML Snippet, um die Formularvalidierung zu erfüllen: 
```
<a href="appboy://close">X</a>
```

Beachten Sie, dass dies in der Produktion auf Ihrem Gerät nicht angezeigt wird, da Judo es umschreiben und durch eine Judo Experience ersetzen wird.

![Ein Bild, das den Code für die Formularvalidierung zeigt, der dem Erstellungsschritt Ihrer Kampagne hinzugefügt wurde.]({% image_buster /assets/img/judo/braze-html-boilerplate.png %})

### Schritt 2: Setzen Sie ein Schlüssel-Wert-Paar für Judo
![Dieses Bild zeigt das Schlüssel-Wert-Paar, das für diese Integration benötigt wird. Der "Schlüssel" ist "judo-experience" und der "Wert" ist Ihr Judo-Link.]({% image_buster /assets/img/judo/braze-campaign-extras-judo-experience.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Legen Sie ein [angepasstes Schlüssel-Wert-Paar]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) für die Kampagne mit einem Schlüssel von `judo-experience` fest. Geben Sie die URL des Judo-Erlebnisses an, das Sie hier zeigen möchten. Die Bibliothek zur Integration von Judo-Braze erkennt dann dieses Schlüssel-Wert-Paar im Handler und verwendet es, um Ihr Judo-Erlebnis anstelle der standardmäßigen In-App-Nachricht UI von Braze einzuspeisen.
<br><br>
### Schritt 3: Beendigung der Kampagne

Schließlich schließen Sie die Kampagne ab, indem Sie einen Trigger für die Kampagne einrichten und Nutzer:innen über Segmente in den Abschnitten **Zustellung** und **Targeting** auswählen. Besuchen Sie unseren [Artikel]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/) über In-App-Nachrichten, in dem wir die verschiedenen Komponenten einer In-App-Nachricht von Braze erläutern.


