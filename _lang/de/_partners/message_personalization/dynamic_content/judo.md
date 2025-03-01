---
nav_title: Judo
article_title: Judo
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Judo, einer servergesteuerten UI-Plattform ohne Code, mit der Sie Ihren iOS- und Android-Apps Standortkontext und -verfolgung hinzufügen können."
alias: /partners/judo/
page_type: partner
search_tag: Partner

---

# Judo

> [Judo](https://judo.app) ist eine serverbasierte UI-Plattform, die es Publishern ermöglicht, auf effiziente Weise reichhaltige, ansprechende In-App-Nutzererlebnisse ohne App-Updates zu liefern.

Die Integration von Braze und Judo bietet maßgeschneiderte Erlebnisse in Ihren Kampagnen und Canvases. Anstelle einer einfachen Landing Page mit Vorlagen kann eine Braze-Kampagne Inhalte mit mehreren Bildschirmen, Modals, Videos, benutzerdefinierten Schriftarten und Unterstützungseinstellungen wie Dark Mode und Barrierefreiheit enthalten, die ohne Code erstellt und ohne App-Updates bereitgestellt werden. Daten von Braze können auch verwendet werden, um personalisierte Inhalte in einem Judo-Erlebnis zu unterstützen. Benutzerereignisse und Daten aus dem Erlebnis können für Attribution und Targeting in Braze zurückgeführt werden.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Judo Konto | Um diese Partnerschaft zu nutzen, benötigen Sie ein [Judo-Konto](https://www.judo.app/). |
| Judo SDK | Das Judo SDK muss in Ihre [iOS-](https://github.com/judoapp/judo-ios/) und/oder [Android-Apps](https://github.com/judoapp/judo-android) integriert werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

**Onboarding**: App-Herausgeber, die Judo verwenden, erstellen und implementieren reichhaltige, native Onboarding-Erlebnisse. Diese Erlebnisse können nun ein Element in einem personalisierten, kanalübergreifenden Onboarding-Prozess sein, der über Braze koordiniert wird. Die Erlebnisse können personalisiert und schnell aktualisiert werden, ohne dass die App aktualisiert werden muss, um die Wirksamkeit verschiedener In-App-Flows zu testen.

**Umwandlung**: App-Publisher können die Daten von Braze nutzen, um ein personalisiertes In-App-Erlebnis zu schaffen, um In-App-Käufe, kostenpflichtige Abonnements oder kontextbezogenes Merchandising mit Hilfe von Integrationshaken in Judo zu fördern. Der Zugang zu diesen Erlebnissen kann über in Braze erstellte Engagement-Marketing-Kampagnen ausgelöst werden.

**Ereignisgesteuerte Inhalte**: Ein Hauptanwendungsbereich für Judo im Sport und in der Unterhaltung ist der Aufbau reichhaltiger Erlebnisse zur Vorschau, Werbung und Zusammenfassung von Veranstaltungen. Diese Fähigkeit kann auch in anderen Branchen für saisonale und nachrichtenorientierte Inhalte eingesetzt werden. Durch die Verknüpfung von Nachrichten, die Ereignisse ankündigen oder hervorheben, mit reichhaltigen In-App-Erlebnissen können Verlage das Engagement fördern, indem sie kontextabhängig sind.

## Nebeneinander liegende SDK-Integration

Judo bietet zusätzliche Bibliotheken, die einen Teil des Aufwands automatisieren, der notwendig ist, um die SDKs von Judo und Braze Seite an Seite in Ihre mobilen Anwendungen zu integrieren. 

### Schritt 1: Installieren Sie die Judo-Braze Integrationsbibliothek

Installieren und richten Sie die Judo-Braze Integrationsbibliothek in Ihren Anwendungen ein. Dadurch wird die Ereignisverfolgung automatisch aktiviert.

- [iOS-Installation
Anweisungen](https://github.com/judoapp/judo-braze-ios/wiki#installation)
- [Android-Installation
Anweisungen](https://github.com/judoapp/judo-braze-android/wiki#installation).

### Schritt 2: In-App-Nachrichten konfigurieren

Dieser Schritt umfasst die Erstellung benutzerdefinierter `ABKInAppMessageControllerDelegate` und `IInAppMessageManagerListener` Implementierungen für iOS und Android.

Sehen Sie sich die Dokumentation zur Einrichtung von In-App-Nachrichten an, die für jede der Integrationsbibliotheken mitgeliefert wird:

- [iOS In-App-Nachrichten
Einrichtung](https://github.com/judoapp/judo-braze-ios/wiki#in-app-messaging-setup)
- [Android In-App-Nachrichten
Einrichtung](https://github.com/judoapp/judo-braze-android/wiki#in-app-messaging-setup).

## Mit dieser Integration

Sobald Sie die app-seitige Integration abgeschlossen haben, können Sie sie testen, indem Sie eine Test-Braze In-App-Nachrichtenkampagne für ein Judo-Erlebnis durchführen, um zu überprüfen, ob sie wie erwartet funktioniert.

### Schritt 1: Erstellen Sie eine In-App Nachrichtenkampagne mit benutzerdefiniertem Code

Erstellen Sie auf der Braze-Plattform eine Braze-In-App-Nachrichtenkampagne mit einem Nachrichtentyp **Custom Code**. Als nächstes wählen Sie **HTML-Upload** als benutzerdefinierten Typ. Achten Sie darauf, den Inhalt der Nachricht mit den Basisfeldern für In-App-Nachrichten zu füllen; dieser Inhalt wird dem Benutzer nicht angezeigt.

![Ein Bild davon, wie das Dashboard aussieht, wenn Sie den Nachrichtentyp "Benutzerdefinierter Code" auswählen.][2]

Als nächstes verwenden Sie den folgenden minimalen HTML-Schnipsel, um die Formularvalidierung zu erfüllen: 
```
<a href="appboy://close">X</a>
```

Beachten Sie, dass dies in der Produktion auf Ihrem Gerät nicht angezeigt wird, da Judo es umschreibt und durch eine Judo Experience ersetzt.

![Ein Bild, das den Code für die Formularvalidierung zeigt, der dem Erstellungsschritt Ihrer Kampagne hinzugefügt wurde.][3]

### Schritt 2: Setzen Sie ein Schlüssel-Wert-Paar für Judo
![Dieses Bild zeigt das Schlüssel-Wert-Paar, das für diese Integration benötigt wird. Der "Schlüssel" ist "judo-experience" und der "Wert" ist Ihr Judo-Link.][4]{: style="float:right;max-width:50%;margin-left:15px;"}

Legen Sie ein [benutzerdefiniertes Schlüssel-Wert-Paar]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) für die Kampagne mit dem Schlüssel `judo-experience` fest. Geben Sie die URL der Judo-Erfahrung an, die Sie hier zeigen möchten. Die Judo-Braze-Integrationsbibliothek erkennt dann dieses Schlüssel-Wert-Paar im Handler und verwendet es, um Ihr Judo-Erlebnis anstelle der Standard-Braze-In-App-Nachrichten-UI einzubinden.
<br><br>
### Schritt 3: Beendigung der Kampagne

Zum Schluss vervollständigen Sie die Kampagne, indem Sie einen Auslöser für die Kampagne einrichten und Benutzer über Segmente in den Abschnitten **Lieferung** und **Zielbenutzer** auswählen. Lesen Sie unseren [Artikel]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/) über die verschiedenen Komponenten einer In-App-Nachricht von Braze.


[2]: {% image_buster /assets/img/judo/braze-campaign-select-custom-type.png %}
[3]: {% image_buster /assets/img/judo/braze-html-boilerplate.png %}
[4]: {% image_buster /assets/img/judo/braze-campaign-extras-judo-experience.png %}
