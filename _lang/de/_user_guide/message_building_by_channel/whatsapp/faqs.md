---
nav_title: FAQ
article_title: WhatsApp FAQ
page_order: 10
description: "Dieser Artikel behandelt einige der am häufigsten gestellten Fragen, die bei der Einrichtung von WhatsApp-Kampagnen auftreten."
page_type: FAQ
channel:
  - WhatsApp

---

# Häufig gestellte Fragen

> Auf dieser Seite werden wir versuchen, Ihre wichtigsten Fragen zu WhatsApp zu beantworten!<br><br>Diese FAQ sind nicht als Rechtsberatung gedacht und dürfen auch nicht als solche angesehen werden. Die Nutzung des WhatsApp-Kanals unterliegt bestimmten Anforderungen von Meta Platforms, Inc. Um sicherzustellen, dass Sie den WhatsApp-Kanal in Übereinstimmung mit allen geltenden Anforderungen und Gesetzen nutzen, denen Sie möglicherweise unterliegen, sollten Sie sich von Ihrem Rechtsbeistand beraten lassen.

## FAQ-Themen
- [WhatsApp Geschäftskonten](#whatsapp-business-accounts)
- [Telefonnummer des WhatsApp-Geschäftskontos](#whatsapp-business-account-phone-numbers)
- [Opt-in und Abo-Management](#opt-in-and-subscription-management) 
- [Messaging-Limits](#messaging-limits) 
- [WhatsApp-Templates](#whatsapp-templates)
- [Zustellbarkeit](#deliverability) 
- [Verschiedenes](#miscellaneous)

### WhatsApp Geschäftskonten 

#### Wie erstelle ich ein WhatsApp-Geschäftskonto? 
Wir empfehlen Ihnen, Ihr WhatsApp-Geschäftskonto (WABA) über den eingebetteten Anmeldevorgang im Braze-Dashboard zu erstellen. 

#### Ich habe bereits ein Meta-Geschäftskonto. Brauche ich noch ein WhatsApp-Geschäftskonto? 
Ja, Sie müssen immer noch ein WhatsApp-Geschäftskonto erstellen. Wir empfehlen Ihnen, [Ihr WABA-Konto unter Ihrem Meta-Hauptgeschäftskonto anzulegen]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/). 

#### Wie kann ich auf mein WhatsApp-Geschäftskonto zugreifen? 
Nachdem Sie den eingebetteten Anmeldevorgang abgeschlossen haben, können Sie auf Ihr Konto unter business.facebook.com zugreifen, indem Sie zum [Bereich WhatsApp](https://business.facebook.com/wa/manage/home) navigieren. 

#### Kann ich mehrere WABAs mit Braze verbinden? 
Ja, Sie können bis zu 10 WhatsApp Business-Konten pro Workspace hinzufügen, und jedes Business-Konto kann unter einem anderen Meta Business Manager:in verschachtelt werden.

![Diagramm des Braze- und WhatsApp-Ökosystems, das zeigt, wie Workspaces und WhatsApp Business-Konten miteinander verbunden sind: Sie können eine Abo-Gruppe mit einer Telefonnummer, mehrere WhatsApp Business-Konten mit einem Workspace und einen Workspace mit mehreren Meta Business-Portfolios verbinden.]({% image_buster /assets/img/whatsapp/whatsapp_braze_ecosystem.png %}) 

### WhatsApp Geschäftskonto Telefonnummern 

#### Brauche ich eine Telefonnummer für mein WhatsApp-Geschäftskonto? 
Ja, Sie benötigen eine Nummer, zu der Sie Zugang haben. Sie werden aufgefordert, Ihre Telefonnummer mit der 2-Faktor-Authentifizierung zu verifizieren, wenn Sie den eingebetteten Anmeldevorgang durchlaufen. Die Rufnummer kann nicht für andere WhatsApp-Konten (geschäftlich oder privat) verwendet werden.

#### Welche Arten von Telefonnummern werden von WhatsApp unterstützt? 
Weitere Informationen finden Sie in den Anforderungen von Meta für [Telefonnummern](https://developers.facebook.com/docs/whatsapp/phone-numbers). 

#### Kann ich eine Rufnummer für mehrere WABAs verwenden? 
Nein. Eine Telefonnummer kann nicht von mehreren WABAs gemeinsam genutzt werden. 

#### Benötige ich eine bestimmte Art von Telefonnummer, um Nachrichten in bestimmte Länder zu senden? 
Nein. Mit WhatsApp können Sie von jeder unterstützten Telefonnummer in jedem Land Nachrichten an Endbenutzer senden. Weitere Informationen finden Sie in den Anforderungen von Meta für [Telefonnummern](https://developers.facebook.com/docs/whatsapp/phone-numbers). 

#### Muss ich eine länderspezifische Rufnummer verwenden, um in bestimmte Länder zu senden?
Nein. Mit WhatsApp kann jede unterstützte Telefonnummer an Endbenutzer in jedem unterstützten Land senden.

### Opt-in und Abo-Management 

#### Muss ich eine Einwilligung einholen, um Marketingnachrichten an Endnutzer:innen auf WhatsApp zu senden? 
Ja, WhatsApp verlangt von Unternehmen, dass sie [die Zustimmung](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) zum Versand von Marketing-Nachrichten an Endbenutzer [einholen](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/).

#### Kann ich Endnutzer proaktiv per WhatsApp benachrichtigen, um ihre Zustimmung einzuholen? 
Wenn Sie sich dafür entscheiden, Endbenutzer proaktiv zu benachrichtigen, sollte Ihre erste vom Unternehmen initiierte Nachricht den Benutzer fragen, ob er Marketingnachrichten von Ihrem Unternehmen erhalten möchte, und die Anforderungen von Meta für die [Einverständniserklärung](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) erfüllen. Denken Sie daran, dass WhatsApp den Ruf Ihres Unternehmens auf dem Kanal überwacht. Daher sollten Sie den Endbenutzern gegenüber explizit sein und nur Nachrichten senden, die sie auch erhalten möchten.
 
#### Muss ich die Telefonnummer des Endnutzers oder der Endnutzerin erfassen, wenn ich die Zustimmung einhole? 
Sie benötigen die Telefonnummer des Endbenutzers oder der Endnutzerin im Braze-Profil, um ihm oder ihr eine Nachricht zu senden. 
- Wenn Sie die Nummer bereits haben, müssen Sie sie bei der Anmeldung nicht erfassen. 
- Wenn Sie die Nummer des Endbenutzers oder der Endnutzerin nicht haben, sollte Ihre Opt-in-Methode die Erfassung der Telefonnummer beinhalten. 

#### Wie aktualisiere ich den Abonnementstatus von Endnutzer:innen, die sich angemeldet haben? 
Die Abonnementverwaltung des WhatsApp-Kanals funktioniert ähnlich wie bei den anderen Braze-Kanälen. Weitere Informationen finden Sie unter [Verwalten von Benutzerabonnements]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/).  

#### Wenn ich bereits eine Liste von Nutzern habe, die sich für den Erhalt von Marketingnachrichten auf WhatsApp entschieden haben, wie aktualisiere ich dann ihren Abonnementstatus in Braze? 
Sie können ihren Abonnementstatus über den [Benutzerimport]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#importing-custom-data) aktualisieren. 

#### Welche Methoden sollte ich verwenden, um Opt-ins zu erfassen? 
Braze empfiehlt, die [Meta-Richtlinien für Opt-in-Methoden](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) heranzuziehen, um die Einhaltung der Vorschriften zu gewährleisten. In der folgenden Quelle finden Sie [Ideen und Vorschläge für Braze-Kanäle und Opt-Ins](https://docs.google.com/document/d/1rNKnKN2oIn-e9bXdYEvnwdlzlCsEOKs-xREcdVvPBE8/edit).

#### Ist die doppelte Zustimmung für WhatsApp erforderlich? 
Nein, doppeltes Opt-in ist nicht erforderlich. 

#### Wie können meine Benutzer WhatsApp-Nachrichten abbestellen? 
Ihre Benutzer können sich auf zwei Arten abmelden:
1. Richten Sie eine eingehende WhatsApp-Nachricht mit einem bestimmten Abmeldewort ein und verwenden Sie einen Webhook, um den Abonnementstatus des Nutzers oder der Nutzerin zu aktualisieren.
2. Fügen Sie eine Opt-out-Schnellantwort in die WhatsApp-Template ein, mit einem entsprechenden Webhook zur Aktualisierung. 

### Messaging-Limits 

#### Was sind Messaging-Limits? 
Nachrichtenlimits sind ein Konzept zum Aufbau von WhatsApp-Integrität. Sie bestimmen die maximale Anzahl der geschäftlich initiierten Gespräche, die jede Telefonnummer innerhalb eines 24-Stunden-Zeitraums führen darf. Es gibt vier Messaging-Limits: 1k, 10k, 100k, und unbegrenzt.

#### Wie kann ich mein Nachrichtenlimit erhöhen? 
WhatsApp erhöht Ihr Messaging-Limit, wenn Sie die folgenden Bedingungen erfüllen:
1. Der [Status der Telefonnummer](https://www.facebook.com/business/help/896873687365001) ist **Verbunden** 
2. Die [Qualität der Telefonnummer wird](https://www.facebook.com/business/help/896873687365001) als **mittel** oder **hoch**[eingestuft](https://www.facebook.com/business/help/896873687365001).
3. In den letzten sieben Tagen haben Sie X oder mehr Unterhaltungen mit einzelnen Nutzern begonnen, wobei X Ihr aktuelles Nachrichtenlimit geteilt durch 2 ist. 

Um von 100.000 auf unbegrenzt zu kommen, müssen Sie also innerhalb von 7 Tagen mindestens 50.000 von Unternehmen initiierte Konversationen senden. 

#### Wie lange dauert es, meine Messaging-Limits zu erhöhen? 
Wenn alle oben genannten Bedingungen erfüllt sind, können Sie Ihr Messaging-Limit innerhalb von 4 Tagen von 1.000 auf unbegrenzt erhöhen. 

#### Wo kann ich mein aktuelles Nachrichtenlimit sehen? 
Sie können Ihre aktuellen Messaging-Limits im **WhatsApp Manager > Übersicht Dashboard >** Registerkarte **Einblicke** überprüfen. 

#### Was passiert, wenn ich versuche, Nachrichten zu senden, obwohl ich mein Nachrichtenlimit bereits erreicht habe?
Wenn Sie versuchen, eine Kampagne oder Canvas an mehr einzelne Benutzer zu senden, als Ihr aktuelles Limit erlaubt, werden die Nachrichten nicht gesendet. Braze wird weiterhin versuchen, die Nachrichten erneut zu senden, wenn Ihr Nachrichtenlimit für bis zu einem Tag erhöht wird. 

#### Kann mein Nachrichtenlimit verringert werden?
Ja, wenn die Qualitätsbewertung Ihrer Telefonnummer zu niedrig ausfällt, besteht die Gefahr, dass WhatsApp Ihr Messaging-Limit senkt. Braze empfiehlt Ihnen, sich anzumelden und sich über qualitätsbezogene Updates von WhatsApp benachrichtigen zu lassen, einschließlich Updates zu Ihrem Telefonnummernstatus und der Höhe Ihres Nachrichtenlimits. Sie können die Benachrichtigungen direkt im Dashboard des WhatsApp Managers abonnieren. 

#### Wie lautet das Meta-Durchsatzlimit?
Meta hat sein eigenes Durchsatzlimit, das vom WABA-Messaging-Limit getrennt ist. Das Standardlimit, das die Cloud-API unterstützt, liegt bei 80 Nachrichten pro Sekunde. Wenn Sie glauben, dass Ihre Kampagnen dieses Limit überschreiten werden, können Sie eine Erhöhung Ihres Limits [beantragen](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/#throughput). Meta empfiehlt, dass Sie diesen Antrag mindestens drei Tage vor dem Versand der Kampagne stellen.

### WhatsApp-Vorlagen 

#### Was ist eine WhatsApp-Vorlage? 
WhatsApp verlangt, dass alle geschäftlich initiierten Nachrichten mit einer genehmigten Template beginnen. Die Template enthält den Text der Nachricht sowie optionalen Rich-Media-Content wie Bilder, Handlungsaufforderungen und Schnellantwortschaltflächen. Nachdem WhatsApp die Vorlagen genehmigt hat, können Sie diese zum Verfassen einer WhatsApp-Nachricht in Braze verwenden. 

#### Wo kann ich meine WhatsApp-Vorlagen erstellen, bearbeiten und verwalten? 
Sie werden Vorlagen direkt im WhatsApp Manager erstellen, bearbeiten, verwalten und zur Genehmigung einreichen. Nachdem Ihr WABA-Konto mit Braze verbunden ist, sehen Sie alle Ihre Templates im Dashboard mit einer Statusanzeige. Wenn eine Vorlage abgelehnt wird, können Sie sie direkt über den WhatsApp-Manager erneut einreichen. **Templates können nicht direkt in Braze erstellt oder bearbeitet werden.**

#### Wie lange dauert es, bis WhatsApp eine Template überprüft? 
Der Genehmigungsprozess kann bis zu 24 Stunden dauern, aber oft werden die Templates in wenigen Stunden oder Minuten bearbeitet. 

#### Wie viele Vorlagen kann ich zu einem bestimmten Zeitpunkt haben? 
Das Limit für Ihre Nachrichtenvorlage hängt vom Status Ihrer Geschäftsverifizierung ab. Sie können Ihr Limit auf der Seite **WhatsApp Manager > Nachrichtenvorlagen** überprüfen. 

#### Wie kann ich Templates und Rich Media in Braze personalisieren? 
WhatsApp ermöglicht das Einfügen von variablen Parametern in Nachrichtenvorlagen. Nachrichten können nicht mit einem variablen Parameter beginnen oder enden. Variable Parameter können in der Braze-Plattform mit Liquid-Logik gefüllt werden. Unter [Verfassen einer WhatsApp-Nachricht in Braze]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#step-2-compose-your-whatsapp-message) erfahren Sie mehr über variable Parameter. 

#### Meine Vorlage wurde abgelehnt. Kann Braze mir bei der Genehmigung helfen? 
Das Braze-Team hat keinen Einblick in die Ablehnung von Vorlagen. Sie sollten direkt mit Ihrem WhatsApp Business Manager zusammenarbeiten, um die Vorlage zu bearbeiten und erneut einzureichen. Stellen Sie sicher, dass Sie bei Bedarf eine Beispiel-Template zur Verfügung stellen. Vergewissern Sie sich, dass Ihre Template den [Unternehmens-](https://www.whatsapp.com/legal/business-policy/?fbclid=IwAR2qWg6yFKdyjDMxJkbNSM38FLGsxXxffC1qStY2gaHOyp-gl_8g72rZNIw) oder [Handelsrichtlinien](https://www.whatsapp.com/legal/commerce-policy/?fbclid=IwAR3bzN3LTZ-7kO-wnO7X3smtPKGy0asxaFod-U1Ub8B9JUpnrfy1_y7LpAQ) von Meta entspricht.

#### Können die Rich Media in Braze zielgerichtet oder personalisiert werden? 
Bilder können aus der Mediathek hochgeladen werden, aber sie können nicht dynamisch ausgerichtet werden. Bei URLs kann der letzte Teil des Links mit Liquid dynamisch ausgefüllt werden. 

### Zustellbarkeit 

#### Warum sollte eine Nachricht nicht zugestellt werden? 
Es gibt verschiedene Gründe, warum eine Nachricht nicht zugestellt werden kann, z. B. Netzwerkprobleme oder das Ausschalten des Geräts. 

#### Wenn eine Nachricht nicht zugestellt wird, wird sie mir in Rechnung gestellt? 
Nein. Wenn eine Nachricht nicht zugestellt wird, wird sie Ihnen nicht in Rechnung gestellt. 

#### Was passiert, wenn ein Endbenutzer mein Geschäft blockiert? 
Wenn ein Endbenutzer Ihr Unternehmen blockiert, werden nachfolgende Nachrichten, die Sie zu senden versuchen, nicht zugestellt und Ihnen nicht in Rechnung gestellt. 

#### Was passiert, wenn ein Endbenutzer eine Nachricht meldet? 
Wenn ein:e Endnutzer:in eine Nachricht meldet, können Sie dennoch weitere Nachrichten an diesen Nutzer oder diese Nutzerin senden. Allerdings kann die Berichterstattung Ihre Qualitätsbewertung auf dem Kanal beeinträchtigen. 

#### Wenn ein Endbenutzer mein Unternehmen sperrt oder meldet, wird dann sein Abonnementstatus in Braze aktualisiert? 
Nein. Ihr Braze-Abonnementstatus wird nicht aktualisiert. 

### Verschiedenes

#### Unterstützt Braze Anwendungsfälle des Kundensupports wie Chatbots und menschlich unterstützte Chats für WhatsApp? 
Wir unterstützen keine Chatbots oder menschengestützte Chats innerhalb von Braze oder durch direkte Integrationen. 

Wenn Sie WhatsApp bereits als Kundensupport-Kanal verwenden, empfehlen wir Ihnen, Ihre aktuelle Einrichtung beizubehalten und über Braze eine neue WABA für Marketingnachrichten zu erstellen. Für dieses WABA-Konto benötigen Sie eine neue Rufnummer. 

#### Wie kann ich die Lücke zwischen den Nachrichten meines Kundensupports und meinen Marketingnachrichten über Braze schließen? 
Sie können die WhatsApp Liquid-Eigenschaften verwenden, um den Inhalt eingehender WhatsApp-Nachrichten (einschließlich des Nachrichtentextes und der Medien-URLs) von Braze an andere Plattformen weiterzuleiten, einschließlich jedes Kundensupport-Tools. Weitere Informationen finden Sie unter [Unterstützte Personalisierungsschilder]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/). 

Um Informationen an Braze zu senden, z. B. um anzuzeigen, dass sich ein Benutzer in einem aktiven Supportgespräch befindet, können Sie ein benutzerdefiniertes Attribut protokollieren (z. B. ein boolesches "hat einen bestehenden Support-Chat = wahr/falsch") und dies als Segmentierungskriterium in ihren Marketingkampagnen verwenden. Sie können auch Deeplink zwischen zwei Chat-Threads erstellen, um Nutzer:innen vom Marketing-Thread zum Support-Thread zu leiten und umgekehrt. 

#### Speichert Braze die Antworten der Benutzer? 
Nachrichten werden nur so lange gespeichert, bis sie verarbeitet werden. Um auf Benutzernachrichten zuzugreifen, verwenden Sie Currents. 

#### Wie müssen die Telefonnummern der Benutzer in Braze gespeichert werden? 
Benutzertelefonnummern müssen im [FormatE.164 ]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/#formatting) gespeichert werden.

#### Welche Arten von Rich Media werden in WhatsApp-Vorlagen unterstützt? 
Sie können Bilder, Handlungsaufforderungen (URL oder Telefonnummer) und Schnellantwortschaltflächen zu WhatsApp-Vorlagen hinzufügen. Sie können diese Elemente hinzufügen, wenn Sie Templates direkt in WhatsApp erstellen. 

#### Kann ich Benutzertelefonnummern importieren? 
Ja Sie können [Benutzertelefonnummern importieren]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/). 

#### Was ist eine Unternehmensverifizierung? 
Die Unternehmensverifizierung ist ein WhatsApp-Konzept, mit dem sichergestellt werden soll, dass es sich bei der Marke um ein legitimes Unternehmen handelt. Sie kann im WhatsApp Manager abgeschlossen werden. Eine Überprüfung des Unternehmens ist auch erforderlich, um das Messaging zu skalieren. Ohne Unternehmensverifizierung können Kund:innen nur bis zu 250 eindeutige Endnutzer:innen in einem rollierenden 24-Stunden-Zeitraum senden. 

#### Was ist ein offizielles Geschäftskonto? 
OBA ist optional und wird mit einem grünen Häkchen neben Ihrem Anzeigenamen angezeigt. Sie können ein offizielles Geschäftskonto beantragen, nachdem Sie die Geschäftsverifizierung abgeschlossen haben. Beachten Sie, dass die Unternehmensverifizierung und ein offizielles Geschäftskonto unterschiedliche WhatsApp-Konzepte sind. 

#### Welche Metriken sind im Braze Dashboard verfügbar? 
Sie können eindeutige Empfänger, Sendungen, Zustellungen, Lesevorgänge und Fehlschläge im Braze-Dashboard sehen. Beachten Sie, dass die Lesebestätigungen der Endnutzer:innen auf „Ein“ festgelegt sein müssen, damit Braze die Lesevorgänge verfolgen kann. Sie können auch Konversions-Events einrichten, um die Kampagnenleistung zu überwachen, ähnlich wie bei anderen Kanälen. 

#### Was ist eine WhatsApp-Konversation? 
WhatsApp ist ein Kanal, der sich auf 2-Wege-Nachrichten konzentriert und sich daher auf Konversationen konzentriert (anstatt auf die Anzahl der einzelnen Nachrichten). Eine Konversation ist eine 24-stündige Verbindung zwischen einem Unternehmen und einem oder einer Endnutzer:in.

- **Von Unternehmen initiierte Konversation**: Eine Konversation, bei der das Unternehmen zunächst eine genehmigte Vorlagennachricht an den Endbenutzer sendet. Sobald das Unternehmen eine Nachricht sendet, beginnt das 24-Stunden-Fenster.
- **Benutzer-initiierte Konversation**: Ein Gespräch, bei dem der Endbenutzer eine Nachricht an das Unternehmen sendet. Wenn das Unternehmen eine Nachricht als Antwort sendet, beginnt das 24-Stunden-Fenster.

#### Welche Faktoren wirken sich auf die Qualitätsbewertung von Telefonnummern aus, und was passiert, wenn meine Qualitätsbewertung zu niedrig ist? 
Zu den Faktoren, die sich auf die Bewertung der Telefonnummernqualität auswirken, gehören ein Endnutzer, der ein Unternehmen blockiert (und die Gründe, die er angibt, wenn er ein Unternehmen blockiert) und ein Endnutzer, der ein Unternehmen meldet. 

Wenn die Qualitätsbewertung niedrig ist, ändert sich der Status der Telefonnummer von **Verbunden** zu **Markiert**. Wenn sich die Qualität innerhalb von sieben Tagen nicht verbessert, wird der Status auf **Verbunden** zurückgesetzt. Das Nachrichtenlimit wird jedoch auf die nächste Stufe herabgesetzt. Zum Beispiel hat eine Telefonnummer, die früher ein Limit von 100.000 Nachrichten hatte, jetzt ein Limit von 10.000 Nachrichten.
