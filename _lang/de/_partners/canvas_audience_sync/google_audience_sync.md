---
nav_title: Google
article_title: Canvas Audience Sync mit Google
alias: /google_audience_sync/
description: "Dieser Artikel referenziert die Verwendung von Braze Audience Sync für Google, um Anzeigen auf der Grundlage von verhaltensbezogenen Triggern, Segmentierung und mehr zuzustellen."
Tool:
  - Canvas
page_order: 3

---

# Zielgruppe Sync zu Google

{% alert important %}
Google aktualisiert seine [EU-Richtlinie zur Einwilligung der Nutzer:innen](https://www.google.com/about/company/user-consent-policy/) als Reaktion auf die Änderungen des [Digital Markets Act (DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html), der ab dem 6\. März 2024 in Kraft tritt. Diese neue Änderung erfordert, dass Werbetreibende bestimmte Informationen an ihre Nutzer:innen im EWR, in Großbritannien und in der Schweiz weitergeben und die notwendige Zustimmung von ihnen einholen. Weitere Informationen finden Sie in der folgenden Dokumentation.
{% endalert %}

Die Braze Audience Sync to Google Integration ermöglicht es Marken, die Reichweite ihrer kanalübergreifenden Customer Journeys auf Google Search, Google Shopping, Gmail, YouTube und Google Display auszudehnen. Mithilfe Ihrer First-Party-Daten von Kund:in können Sie Anzeigen auf der Grundlage von dynamischen Verhaltenstriggern, Segmentierung und mehr sicher zustellen. Jedes Kriterium, das Sie normalerweise zum Triggern einer Nachricht (z.B. Push, E-Mail oder SMS) im Rahmen eines Braze-Canvas verwenden, kann verwendet werden, um eine Anzeige für diesen Nutzer:innen über Googles [Customer Match](https://support.google.com/google-ads/answer/6379332?hl=en) zu triggern.

{% alert note %}
Die Braze Audience Sync to Google Integration wird für Google Ads unterstützt, nicht für Google Ads Manager:in.
{% endalert %}

Google Ads generiert keine ähnlichen Zielgruppen, auch bekannt als "Lookalike Audiences", mehr für Targeting und Reporting. Lesen Sie die [Dokumentation von Google Ads](https://support.google.com/google-ads/answer/12463119?), um mehr zu erfahren.

**Häufige Anwendungsfälle für die Synchronisierung von angepassten Zielgruppen sind:**
- Targeting von hochwertigen Nutzer:innen über mehrere Kanäle, um Käufe oder Engagement zu fördern.
- Retargeting von Nutzer:innen, die auf andere Marketing-Kanäle weniger responsiv sind.
- Erstellen von Zielgruppen, um zu verhindern, dass Nutzer:innen, die bereits treue Verbraucher:innen Ihrer Marke sind, Werbung erhalten.

{% alert note %}
Mit diesem Feature können Marken kontrollieren, welche spezifischen First-Party-Daten mit Google geteilt werden. Bei Braze werden die Integrationen, mit denen Sie Ihre First-Party-Daten teilen können und mit denen Sie sie nicht teilen können, genauestens geprüft. Erfahren Sie mehr über unsere [Braze Datenschutz-Richtlinien](https://www.braze.com/privacy).
{% endalert %}

## Voraussetzungen

Vergewissern Sie sich, dass die folgenden Artikel erstellt und ausgefüllt sind, bevor Sie Ihren Google Audience-Schritt in Canvas einrichten.

| Anforderung | Herkunft | Beschreibung |
| ----------- | ------ | ----------- |
| Google Ads Konto | [Google](https://support.google.com/google-ads/answer/6366720?hl=en) | Ein aktives Google Ads-Konto für Ihre Marke.<br><br>Wenn Sie eine Zielgruppe für mehrere verwaltete Konten freigeben möchten, können Sie Ihre Zielgruppen in Ihr [Manager:in-Konto](https://support.google.com/google-ads/answer/6139186) hochladen. |
| Google Ads-Bedingungen und Google Ads-Richtlinien | [Google](https://support.google.com/adspolicy/answer/54818?hl=en) | Bei der Nutzung von Braze Audience Sync müssen Sie die [Google-Anzeigenbedingungen](https://payments.google.com/u/0/paymentsinfofinder?hostOrigin=aHR0cHM6Ly9wYXltZW50cy5nb29nbGUuY29tOjQ0Mw..&sri=-40) und die [Google-Anzeigenrichtlinien](https://support.google.com/adspolicy/answer/6008942?sjid=15557182366992806023-NC) akzeptieren und sicherstellen, dass Sie diese einhalten, einschließlich der [EU-Richtlinie zur Einwilligung der Nutzer](https://www.google.com/about/company/user-consent-policy/):innen.<br><br>Informieren Sie sich bei Ihrem Team der Rechtsabteilung über die neue Richtlinie von Google zur Einwilligung von Nutzern in der EU, um sicherzustellen, dass Sie eine angemessene Einwilligung einholen, um die Dienste von Google Ads für Ihre Nutzer:innen im EWR, Großbritannien und der Schweiz zu nutzen. |
| Google Customer Match | [Google](https://support.google.com/google-ads/answer/6299717) |  Kund:in ist nicht für alle Anzeigenkunden verfügbar.<br><br>**Um Kund:in zu verwenden, muss Ihr Konto über ein solches verfügen:**<br>\- Ein guter Verlauf bei der Einhaltung der Richtlinien<br>\- Ein guter Verlauf der Zahlungen<br>\- Mindestens 90 Tage Verlauf in Google Ads<br>\- Mehr als USD 50.000 Gesamtausgaben auf Lebenszeit. Für Werbetreibende, deren Konten in anderen Währungen als USD geführt werden, wird Ihr Ausgabenbetrag anhand der durchschnittlichen monatlichen Konversionsrate für diese Währung in USD umgerechnet.<br><br>Wenn Ihr Konto diese Kriterien nicht erfüllt, ist Ihr Konto derzeit nicht berechtigt, Customer Match zu verwenden.<br><br>Wenden Sie sich an Ihre Google Ads-Vertretung, um weitere Informationen zur Verfügbarkeit von Customer Match für Ihr Konto zu erhalten. |
| Google-Zustimmungs-Signale | [Google](https://support.google.com/google-ads/answer/14310715) |  Wenn Sie mit dem Dienst Customer Match von Google Anzeigen für Endnutzer:in im EWR schalten möchten, müssen Sie Braze die folgenden angepassten Attribute (boolesch) als Teil der EU-Zustimmungsrichtlinien von Google übergeben. Weitere Einzelheiten finden Sie unter [Einholung der Zustimmung für Endnutzer:innen aus dem EWR, Großbritannien und der Schweiz](#collecting-consent-for-eea-uk-and-switzerland-end-users): <br> - `$google_ad_user_data` <br> - `$google_ad_personalization` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Erforderliche SDK-Versionen

Wenn Sie Braze SDKs zum Sammeln von Einwilligungssignalen verwenden, stellen Sie sicher, dass Sie die folgenden Mindestversionen erfüllen:

{% sdk_min_versions swift:7.6.0 android:1.3.2 web:3.0.0 %}

### Einholung der Zustimmung für Endnutzer:innen aus dem EWR, Großbritannien und der Schweiz

Die Richtlinie von Google zur Einwilligung der Nutzer in der EU verlangt von den Werbetreibenden, dass sie ihren Nutzer:innen im EWR, in Großbritannien und in der Schweiz die folgenden Informationen zur Verfügung stellen und deren Einwilligung einholen:

* Die Verwendung von Cookies oder anderer lokaler Speicherung, sofern dies gesetzlich vorgeschrieben ist; und
* Die Erfassung, Weitergabe und Verwendung ihrer persönlichen Daten für die Personalisierung von Anzeigen.

Dies betrifft weder US-amerikanische Nutzer:innen noch andere Nutzer:innen, die sich außerhalb des EWR, Großbritanniens oder der Schweiz befinden. Wenden Sie sich an Ihr juristisches Team, um sich über die neue EU-Zustimmungsrichtlinie von Google zu informieren und sicherzustellen, dass Sie eine angemessene Zustimmung für die Nutzung der Dienste von Google Ads für Ihre Nutzer:innen im EWR, in Großbritannien und in der Schweiz einholen.

Gemäß dem Digital Markets Act (DMA), der am 6\. März 2024 in Kraft tritt, müssen Marketer die Zustimmung der Nutzer:innen aus dem EWR, Großbritannien und der Schweiz einholen, wenn sie Daten mit Google teilen. Im Rahmen dieser Änderung können Sie beide Zustimmungssignale in Braze als die folgenden booleschen angepassten Attribute erfassen:

* `$google_ad_user_data`
* `$google_ad_personalization`

Braze wird die Daten aus diesen angepassten Attributen mit den entsprechenden [Einwilligungsfeldern in Google](https://support.google.com/google-ads/answer/14310715#:~:text=These%20consent%20fields%20are%3A) synchronisieren.

#### Verwaltung widerrufener Einwilligungen

Um Ihre Zielgruppenlisten auf dem neuesten Stand zu halten, falls ein EWR-Endnutzer zur Zielgruppenliste hinzugefügt wurde und anschließend eine der beiden Zustimmungen (`$google_ad_user_data` oder `$google_ad_personalization`) zurückgezogen hat, müssen Sie ein Canvas einrichten, um Nutzer:innen aus den bestehenden Zielgruppenlisten zu entfernen, indem Sie einen Audience Sync-Schritt verwenden.

{% alert note %}
Wenn ein EWR-Bürger zuvor seine Zustimmung für beide Signale gegeben hat, werden diese Daten weiterhin für Googles Customer Match verwendet, bis die Liste abläuft oder der Zustimmungsstatus explizit über Google Audience Sync aktualisiert wird, oder beides.
{% endalert %}

#### Tipps

* Senden Sie den Wert als booleschen Typ, nicht als String-Typ.
* Stellen Sie dem Namen des Attributs das Dollarzeichen ($) voran. Braze verwendet ein Dollarzeichen am Anfang des Namens eines Attributs, um zu verdeutlichen, dass es sich um einen speziellen und reservierten Schlüssel handelt.
* Geben Sie den Namen des Attributs in Kleinbuchstaben ein.
* Sie können einen Nutzer:innen zwar nicht explizit als nicht spezifiziert festlegen, aber wenn Sie einen Wert `null` oder `nil` oder einen anderen Wert als `true` oder `false` senden, wird Braze diesen Nutzer:innen als `UNSPECIFIED` an Google weitergeben.
* Neu hinzugefügte oder aktualisierte Nutzer:innen ohne Angabe eines der beiden Attribute werden mit Google synchronisiert, wobei diese Attribute als nicht spezifiziert markiert sind.

Wenn Sie versuchen, einen Nutzer:innen aus dem EWR zu synchronisieren, ohne die erforderlichen Einwilligungsfelder und den erteilten Status zu haben, wird Google dies ablehnen und keine Anzeigen für diesen Nutzer:innen schalten. Wenn einem Nutzer:innen im EWR ohne dessen ausdrückliche Zustimmung eine Anzeige geschaltet wird, können Sie außerdem haftbar gemacht werden und ein finanzielles Risiko eingehen. Um dies zu vermeiden, empfehlen wir, Kampagnen mit Segmentierungsfiltern zu versenden, die nur Nutzer:innen aus dem EWR, Großbritannien und der Schweiz mit den Attributen `true` Google consent einschließen. Weitere Einzelheiten zur EU-Richtlinie über die Zustimmung der Nutzer:innen zum Hochladen von Kund:innen finden Sie in den [FAQ](https://support.google.com/google-ads/answer/14310715) von Google.

### Einrichten Ihres Canvas

Nach der Synchronisierung mit Braze stehen Ihnen die folgenden Attribute für die Zustimmung in Ihren Nutzerprofilen und für die Segmentierung zur Verfügung:

- `$google_ad_user_data`
- `$google_ad_personalization`

In jedem Canvas, in dem Sie Endnutzer:innen aus dem EWR, Großbritannien und der Schweiz mit Hilfe von Google Audience Sync zu einer Zielgruppe zusammenstellen, müssen Sie diese Nutzer:innen ausschließen, wenn beide Attribute für die Zustimmung einen Wert haben, der nicht `true` ist. Dies kann erreicht werden, indem diese Nutzer:innen segmentiert werden, wenn die Zustimmungswerte auf `true` eingestellt sind. Dadurch wird auch sichergestellt, dass die genaueren Analytics der Nutzer:innen synchronisiert werden, da wir wissen, dass Google diese Nutzer:innen aus den Zielgruppen ausschließt. Wenn Sie Google Audience Sync verwenden, um Nutzer:innen aus einer Zielgruppe zu entfernen, sind die Attribute für die Zustimmung nicht erforderlich.

## Integration

### Schritt 1: Google-Konto verbinden

Um loszulegen, gehen Sie zu **Partnerintegrationen** > **Technologiepartner** > **Google Ads** und wählen Sie **Google Ads verbinden**. Sie werden in einem Modal aufgefordert, die mit Ihrem Google Ads-Konto verknüpfte E-Mail auszuwählen und dann Braze Zugriff auf Ihr Google Ads-Konto zu gewähren.

Nachdem Sie Ihr Google Ads-Konto erfolgreich verbunden haben, werden Sie zu Ihrer Google Ads-Partnerseite weitergeleitet. Sie werden dann aufgefordert, die Anzeigenkonten auszuwählen, auf die Sie im Braze Workspace zugreifen möchten.

![Ein GIF, das den Workflow einer erfolgreichen Verbindung eines Google Ads-Kontos mit Braze zeigt.]({% image_buster /assets/img/google_sync/googlesync.gif %}){: style="max-width:85%;"}

#### Exportieren Sie iOS IDFA oder Google Advertising IDs

Wenn Sie iOS IDFA oder Google Advertising IDs in Ihre Zielgruppen-Synchronisierung exportieren möchten, benötigt Google Ihre iOS App ID und Android App ID in den Anfragen. Wählen Sie unter Google Audience Sync die Option **Mobile Werbe-IDs hinzufügen**, geben Sie die ID Ihrer iOS-App und Android-App (Name des App-Pakets) ein und speichern Sie beide.

<br><br>
![Die aktualisierte Seite der Google Ads-Technologie zeigt die verbundenen Anzeigenkonten an, was eine erneute Synchronisierung der Konten und das Hinzufügen von IDs für mobile Werbung zulässig macht.]({% image_buster /assets/img/google_sync/google_sync5.png %}){: style="max-width:75%;"}
<br><br>

Wenn Sie mehrere Apps in einem Workspace haben, können Sie bei der Einrichtung jede Ihrer App IDs eingeben, da die mobilen Anzeigen-IDs für Ihre Nutzer:innen in allen Apps gleich sind. Das liegt daran, dass sowohl der Android GAID als auch der iOS IDFA universelle Bezeichner für Anzeigen auf dem Gerät sind und nicht App-spezifisch. Um mobile Werbe-IDs für Nutzer:innen einer bestimmten App zu synchronisieren, können Sie Segmentierungsfilter ("Zuletzt verwendete bestimmte App" oder "Neueste App-Version") verwenden, um diese Nutzer:innen gezielt anzusprechen.

### Schritt 2: Hinzufügen eines Google Audience-Schritts in Canvas Flow

Fügen Sie eine Komponente in Ihrem Canvas hinzu und wählen Sie dann **Audience Sync**.

![Das Menü zum Auswählen einer Canvas-Komponente im Editor.]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![Der zur Nutzer:in hinzugefügte Schritt der Audience Sync.]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Schritt 3: Sync-Einrichtung

1. Wählen Sie **Angepasste Zielgruppe**, um den Komponenteneditor zu öffnen.
2. Wählen Sie **Google** als Audience Sync Partner aus.

![Die Einstellungen des Schritts Zielgruppe synchronisieren mit der Option, einen Partner auszuwählen, um die Synchronisierung zu starten.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

{: start="3"}
3\. Wählen Sie das gewünschte Google-Anzeigenkonto aus.
4\. Geben Sie in der Dropdown-Liste **Neue oder bestehende Zielgruppe auswählen** den Namen einer neuen oder bestehenden Zielgruppe ein. 

{% tabs %}
{% tab Eine neue Zielgruppe erstellen %}

1. Geben Sie einen Namen für die neue angepasste Zielgruppe ein.
2. Wählen Sie **Nutzer:innen zur Zielgruppe hinzufügen**.
3. Wählen Sie die First-Party-Daten der Nutzer:innen aus, die Sie an Ihre Zielgruppe senden möchten. Sie können entweder wählen:

- **Kontaktinformationen für Kund**:in: Enthält die E-Mail- oder Telefonnummern Ihrer Nutzer:innen, oder beides, wenn sie in Braze vorhanden sind. Google verlangt, dass es sich dabei um ein einziges Feld handelt, das zu synchronisieren ist, und nicht um separate Bezeichner. Sie können dieses einzelne Feld auch verwenden, wenn Sie nur einen der Bezeichner haben.
- **Mobile Advertiser ID**: Wählen Sie entweder iOS IDFA oder Android GAID. Aufgrund der Google-Anforderungen für den Kundenabgleich können Sie nicht beide IDs für mobile Werbetreibende in denselben Kund:inenlisten haben.

{: start="4"}
4\. Als nächstes speichern Sie Ihre Zielgruppe, indem Sie den Button **Zielgruppe erstellen** unten im Schritteditor auswählen.

![Erweiterte Ansicht der Komponente Custom Audience Canvas. Hier wird das gewünschte Anzeigenkonto ausgewählt, eine neue Zielgruppe erstellt und das Kontrollkästchen "Kundenkontaktinfo" aktiviert.]({% image_buster /assets/img/audience_sync/g_sync.png %})

Nutzer:innen werden im oberen Bereich des Schritteditors benachrichtigt, wenn die Zielgruppe erfolgreich erstellt wurde oder wenn dabei Fehler auftreten. Nutzer:innen können diese Zielgruppe referenzieren, um sie später in Canvas zu entfernen, da die Zielgruppe im Entwurfsmodus erstellt wurde. 

![Eine Meldung, die erscheint, nachdem eine neue Zielgruppe in der Canvas-Komponente erstellt wurde.]({% image_buster /assets/img/audience_sync/g_sync3.png %})

Wenn Sie ein Canvas mit einer neuen Zielgruppe starten, erstellt Braze beim Start des Canvas eine neue angepasste Zielgruppe und synchronisiert anschließend die Nutzer:innen nahezu in Realtime, sobald sie den Google Audience-Schritt betreten. 

{% alert important %}
Aufgrund der Anforderungen von Google an den Kundenabgleich können Sie keine Kontaktinformationen von Kund:innen und IDs von mobilen Werbetreibenden in denselben Kundenlisten haben. Google Customer Match verwendet dann diese Informationen, um zu bestimmen, wer innerhalb von Google Search, Google Display, YouTube und Google Mail als Targeting geeignet ist. Weitere Einzelheiten zu den Anforderungen von Google Customer Match finden Sie in der [Dokumentation](https://support.google.com/google-ads/answer/7474166?hl=en&ref_topic=6296507).
{% endalert %}
{% endtab %}
{% tab Mit einer bestehenden Zielgruppe synchronisieren %}

Braze bietet auch die Möglichkeit, Nutzer:innen aus bestehenden Google Kund:innen-Listen hinzuzufügen oder zu entfernen, um sicherzustellen, dass diese Zielgruppen aktuell sind. Zum Synchronisieren mit einer bestehenden Zielgruppe:

1. Wählen Sie eine bestehende angepasste Zielgruppe für die Synchronisierung aus.
2. Wählen Sie, ob Sie **der Zielgruppe etwas hinzufügen** oder **aus ihr entfernen** möchten.
3. Braze fügt Nutzer:innen nahezu in Realtime hinzu oder entfernt sie, sobald sie den Schritt Google Audience betreten. 
4. Nachdem Sie Ihre Google Audience konfiguriert haben, wählen Sie **Fertig**. Ihr Google Audience-Schritt enthält Details über die neue Zielgruppe.

![Erweiterte Ansicht der Komponente Custom Audience Canvas. Hier werden das gewünschte Anzeigenkonto und die bestehende Zielgruppe ausgewählt sowie der Radio Button "Nutzer:innen zur Zielgruppe hinzufügen".]({% image_buster /assets/img/audience_sync/g_sync2.png %})

{% endtab %}
{% endtabs %}

### Schritt 4: Canvas starten

Vervollständigen Sie den Rest Ihrer Nutzer:innen in Canvas und starten Sie dann! Wenn Sie sich für die Erstellung einer neuen Zielgruppe entschieden haben, erstellt Braze die Zielgruppe innerhalb von Google und fügt dann Nutzer:innen hinzu, wenn sie diesen Schritt in Ihrem Canvas erreichen. Wenn Sie ausgewählt haben, Nutzer:innen einer bestehenden Zielgruppe hinzuzufügen oder zu entfernen, wird Braze Nutzer:innen entweder hinzufügen oder entfernen, wenn sie diesen Schritt in ihrer User Journey erreichen.

Die Nutzer:innen bringen dann die nächste Komponente des Canvas voran, wenn es eine gibt, oder verlassen den Canvas, wenn es der letzte Schritt der User Journey ist. 

## Überlegungen zur Synchronisierung von Nutzer:innen und Rate-Limits

Wenn Nutzer:innen die Audience Sync-Komponente erreichen, wird Braze diese Nutzer:innen nahezu in Realtime synchronisieren und dabei die Rate-Limits der Google Ads API beachten. In der Praxis bedeutet dies, dass Braze versuchen wird, alle 5 Sekunden so viele Nutzer:innen wie möglich zu verarbeiten, bevor diese an Google weitergeleitet werden. 

Sobald ein Kunde kurz davor ist, das Rate-Limit der Google Ads API zu erreichen, gibt Google Braze eine Rückmeldung zu den Empfehlungen für Wiederholungsversuche. Erreicht eine Braze-Kund:in ihr Rate-Limit, wird Braze-Canvas die Synchronisierung für bis zu ~13 Stunden wiederholen. Wenn die Synchronisierung nicht möglich ist, werden diese Nutzer:innen unter der Metriken Users Errored aufgeführt.

## Analytics verstehen 

Die folgende Tabelle enthält Metriken und Beschreibungen, die Ihnen helfen, die Analytics Ihres Audience Sync-Schrittes besser zu verstehen.

| Metrisch | Beschreibung |
| ------ | ----------- |
| *Eingetreten* | Anzahl der Nutzer:innen, die diesen Schritt eingegeben haben, um mit Google synchronisiert zu werden. |
| *Fortgefahren mit nächstem Schritt* | Wie viele Nutzer:innen zur nächsten Komponente vorgebracht wurden, falls es eine gibt. Alle Nutzer:innen werden automatisch vorangebracht. Wenn dies der letzte Schritt in der Canvas-Verzweigung ist, wird diese Metrik 0 sein. |
| *Nutzer:innen synchronisiert* | Anzahl der Nutzer:innen, die erfolgreich mit Google synchronisiert wurden. |
| *Nutzer:in nicht synchronisiert* | Anzahl der Nutzer:innen, die nicht synchronisiert wurden, weil Felder zum Abgleich fehlen oder das Attribut Zustimmung auf `false` gesetzt wurde. |
| *Fehler bei Nutzer:innen* | Anzahl der Nutzer:innen, die aufgrund eines Fehlers nicht mit Google synchronisiert wurden, nach ~13 Stunden Wiederholungsversuchen. Bei bestimmten Fehlern, wie z.B. Unterbrechungen der Google Ads APIs Dienste, wird Canvas die Synchronisierung für bis zu ~13 Stunden wiederholen. Wenn die Synchronisierung zu diesem Zeitpunkt immer noch nicht möglich ist, wird das Feld *Nutzer:innen nicht synchronisiert* ausgefüllt. |
| *Nutzer:innen ausstehend* | Anzahl der Nutzer:innen, die derzeit von Braze für die Synchronisierung mit Google verarbeitet werden. |
| *Canvas wurde verlassen* | Anzahl der Nutzer:innen, die den Canvas verlassen haben. Dies geschieht, wenn der letzte Schritt in einem Canvas ein Google-Schritt ist. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Häufig gestellte Fragen

### Warum kann ich in meiner Google Audience Step-Konfiguration nicht mehrere Felder für die Übereinstimmung auswählen?

Google Customer Match stellt strenge Anforderungen an die Formatierung dieser Zielgruppen und die darin enthaltenen Kund:innen-Informationen. Insbesondere müssen die IDs der mobilen Werbetreibenden getrennt von den Kontaktinformationen der Kund:innen (wie E-Mail und Telefonnummer) hochgeladen werden. Weitere Einzelheiten finden Sie in [der Dokumentation von Google Customer Match](https://support.google.com/google-ads/answer/7659867?hl=en#undefined).

### Wie lange dauert es, bis meine Zielgruppen in Google synchronisiert sind?

Es kann zwischen 6 und 12 Stunden dauern, bis eine Zielgruppe mit Google synchronisiert ist. 

### Ich habe eine Zielgruppe synchronisiert. Warum ist die Größe der Zielgruppe in Google gleich Null?

Aus Datenschutzgründen wird die Größe der Nutzer:innen-Liste auf Null gesetzt, bis die Liste mindestens 1.000 Mitglieder hat. Danach wird die Größe auf die zwei höchstwertigen Stellen gerundet.

### Ich habe eine Zielgruppe mit Google synchronisiert, aber meine Anzeigen werden nicht geschaltet.

Vergewissern Sie sich, dass Ihre Zielgruppen mindestens 5.000 Nutzer:innen enthalten, damit die Anzeigenschaltung beginnen kann.

### Wie kann ich den Fehler "Mobile App IDs Deleted" beheben?

Wenn Sie Zielgruppen mit Google synchronisieren, wird dieser Fehler ausgelöst, wenn Sie die Synchronisierung von mobilen Bezeichnern als Teil Ihrer Synchronisierungen ausgewählt haben, aber die IDs Ihrer mobilen Apps von der Google Partnerseite gelöscht haben. Um dieses Problem zu beheben, stellen Sie sicher, dass Sie die entsprechenden IDs für mobile Apps für iOS und Android auf der Partnerseite von Google hinzugefügt haben.


