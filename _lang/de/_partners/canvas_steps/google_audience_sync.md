---
nav_title: Google
article_title: Canvas Audience Sync mit Google
alias: /google_audience_sync/
description: "In diesem Referenzartikel erfahren Sie, wie Sie Braze Audience Sync für Google verwenden, um Anzeigen auf der Grundlage von verhaltensbezogenen Auslösern, Segmentierung und mehr zu schalten."
Tool:
  - Canvas
page_order: 3

---

# Audience Sync mit Google

{% alert important %}
  Weitere Informationen finden Sie in der folgenden Dokumentation.
{% endalert %}

Die Braze Audience Sync to Google-Integration ermöglicht es Marken, die Reichweite ihrer kanalübergreifenden Customer Journeys auf Google Search, Google Shopping, Gmail, YouTube und Google Display auszudehnen. Mithilfe Ihrer First-Party-Kundendaten können Sie auf sichere Weise Anzeigen auf der Grundlage dynamischer verhaltensbezogener Auslöser, Segmentierung und mehr schalten. Jedes Kriterium, das Sie normalerweise zum Auslösen einer Nachricht (z. B. Push, E-Mail oder SMS) im Rahmen eines Braze Canvas verwenden, kann zum Auslösen einer Anzeige für diesen Nutzer über Googles [Customer Match](https://support.google.com/google-ads/answer/6379332?hl=en) verwendet werden.

{% alert important %}
Ab dem 1\. Mai 2023 wird Google Ads keine ähnlichen Zielgruppen, auch bekannt als "Lookalike Audiences", für Targeting und Reporting mehr generieren. Weitere Informationen finden Sie in der [Google Ads-Dokumentation](https://support.google.com/google-ads/answer/12463119?).
{% endalert %}

**Häufige Anwendungsfälle für die Synchronisierung von Custom Audiences sind:**
- Ansprechen von hochwertigen Nutzern über mehrere Kanäle, um Käufe oder Engagement zu fördern.
- Retargeting von Nutzern, die auf andere Marketingkanäle weniger gut reagieren.
- Erstellen von Unterdrückungszielgruppen, um zu verhindern, dass Nutzer Werbung erhalten, wenn sie bereits treue Kunden Ihrer Marke sind.

{% alert note %}
Mit dieser Funktion können Marken kontrollieren, welche spezifischen Daten von Erstanbietern mit Google geteilt werden. Bei Braze werden die Integrationen, mit denen Sie Ihre Erstanbieterdaten teilen können und nicht teilen können, genauestens geprüft. Um mehr über unsere Braze-Datenschutzrichtlinie zu erfahren, klicken Sie [hier](https://www.braze.com/privacy).
{% endalert %}

## Voraussetzungen



| Anforderung | Herkunft | Beschreibung |
| ----------- | ------ | ----------- |
| Google Ads-Konto | [Google](https://support.google.com/google-ads/answer/6366720?hl=en) | Ein aktives Google-Anzeigenkonto für Ihre Marke.<br><br>Wenn Sie eine Zielgruppe für mehrere verwaltete Konten freigeben möchten, können Sie Ihre Zielgruppen in Ihr [Manager-Konto](https://support.google.com/google-ads/answer/6139186) hochladen. |
| Google Ads-Bedingungen und Google Ads-Richtlinien | [Google](https://support.google.com/adspolicy/answer/54818?hl=en) | Bei der Nutzung von Braze Audience Sync müssen Sie die [Google-Anzeigenbedingungen](https://payments.google.com/u/0/paymentsinfofinder?hostOrigin=aHR0cHM6Ly9wYXltZW50cy5nb29nbGUuY29tOjQ0Mw..&sri=-40) und die [Google-Anzeigenrichtlinien](https://support.google.com/adspolicy/answer/6008942?sjid=15557182366992806023-NC) akzeptieren und sicherstellen, dass diese eingehalten werden, einschließlich der für Sie geltenden [EU-Nutzerzustimmungsrichtlinie](https://www.google.com/about/company/user-consent-policy/).<br><br>Informieren Sie sich bei Ihrer Rechtsabteilung über die neuen EU-Zustimmungsrichtlinien von Google, um sicherzustellen, dass Sie eine angemessene Zustimmung für die Nutzung der Google Ads-Dienste für Ihre Endnutzer im EWR, in Großbritannien und in der Schweiz einholen. |
| Google Customer Match | [Google](https://support.google.com/google-ads/answer/6299717) |  Customer Match ist nicht für alle Inserenten verfügbar.<br><br>**Um Customer Match nutzen zu können, muss Ihr Konto über Folgendes verfügen:**<br>\- Eine gute Geschichte der Einhaltung von Richtlinien<br>\- Eine gute Zahlungsmoral<br>\- Mindestens 90 Tage Historie in Google Ads<br>\- Mehr als USD 50.000 Gesamtausgaben im Leben. Für Inserenten, deren Konten in anderen Währungen als USD geführt werden, wird Ihr Ausgabenbetrag anhand des durchschnittlichen monatlichen Umrechnungskurses für diese Währung in USD umgerechnet.<br><br>Wenn Ihr Konto diese Kriterien nicht erfüllt, ist Ihr Konto derzeit nicht berechtigt, Customer Match zu nutzen.<br><br>Wenden Sie sich an Ihren Google Ads-Vertreter, um weitere Informationen zur Verfügbarkeit von Customer Match für Ihr Konto zu erhalten. |
| Google-Zustimmungs-Signale | [Google](https://support.google.com/google-ads/answer/14310715) |  Wenn Sie Anzeigen für Endnutzer aus dem EWR über den Google Customer Match Service schalten möchten, müssen Sie Braze die folgenden benutzerdefinierten Attribute (boolesch) als Teil der EU-Zustimmungsrichtlinie von Google übergeben. Weitere Einzelheiten finden Sie unter [Einholung der Zustimmung für Endnutzer aus dem EWR, Großbritannien und der Schweiz](#collecting-consent-for-eea-uk-and-switzerland-end-users): <br> - `$google_ad_user_data` <br> - `$google_ad_personalization` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Wenn Sie Braze SDKs zum Sammeln von Einwilligungssignalen verwenden, stellen Sie sicher, dass Sie die folgenden Mindestversionen erfüllen:

{% sdk_min_versions swift:7.6.0 android:1.3.2 web:3.0.0 %}

### Einholung der Zustimmung für Endnutzer aus dem EWR, Großbritannien und der Schweiz

Die Google-Richtlinie zur Einwilligung der Nutzer in der EU verpflichtet die Inserenten, ihren Endnutzern aus dem EWR, Großbritannien und der Schweiz Folgendes mitzuteilen und deren Einwilligung einzuholen:

* Die Verwendung von Cookies oder anderer lokaler Speicherung, wenn dies gesetzlich vorgeschrieben ist; und
* Die Erfassung, Weitergabe und Verwendung ihrer persönlichen Daten zur Personalisierung von Werbung.

Dies betrifft weder US-Endnutzer noch andere Endnutzer, die sich außerhalb des EWR, Großbritanniens oder der Schweiz befinden. Beraten Sie sich mit Ihrer Rechtsabteilung über die neuen EU-Zustimmungsrichtlinien von Google, um sicherzustellen, dass Sie eine angemessene Zustimmung für die Nutzung der Google Ads-Dienste für Ihre Endnutzer aus dem EWR, Großbritannien und der Schweiz einholen.

Gemäß den Anforderungen des Digital Markets Act (DMA), der ab dem 6\. März 2024 in Kraft tritt, müssen Werbetreibende die Zustimmung der Endnutzer aus dem EWR, Großbritannien und der Schweiz einholen, wenn sie Daten mit Google austauschen. Im Rahmen dieser Änderung können Sie beide Einwilligungssignale in Braze als die folgenden booleschen benutzerdefinierten Attribute erfassen:

* `$google_ad_user_data`
* `$google_ad_personalization`

Braze synchronisiert die Daten aus diesen benutzerdefinierten Attributen mit den entsprechenden [Einwilligungsfeldern in Google](https://support.google.com/google-ads/answer/14310715#:~:text=These%20consent%20fields%20are%3A).

#### Verwaltung widerrufener Einwilligungen

Um Ihre Zielgruppenlisten auf dem neuesten Stand zu halten, falls ein EWR-Endbenutzer zur Zielgruppenliste hinzugefügt wurde und anschließend eine der beiden Zustimmungen (`$google_ad_user_data` oder `$google_ad_personalization`) zurückzieht, müssen Sie eine Leinwand einrichten, um Benutzer aus den bestehenden Zielgruppenlisten zu entfernen, indem Sie einen Schritt zur Zielgruppensynchronisierung verwenden.

{% alert note %}
Wenn ein EWR-Bürger zuvor seine Zustimmung für beide Signale gegeben hat, werden diese Daten weiterhin für Google Customer Match verwendet, bis die Liste abläuft oder der Zustimmungsstatus explizit über Google Audience Sync aktualisiert wird oder beides.
{% endalert %}

#### Tipps

* Senden Sie den Wert als booleschen Typ, nicht als String-Typ.
* Stellen Sie dem Attributnamen das Dollarzeichen ($) voran. Braze verwendet ein Dollarzeichen am Anfang eines Attributnamens, um anzuzeigen, dass es sich um einen speziellen und reservierten Schlüssel handelt.
* 
* Sie können einen Benutzer zwar nicht explizit als nicht spezifiziert festlegen, aber wenn Sie einen Wert `null` oder `nil` oder einen Wert, der nicht `true` oder `false` ist, senden, wird Braze diesen Benutzer als `UNSPECIFIED` an Google weitergeben.
* Neu hinzugefügte oder aktualisierte Nutzer, die keines der beiden Zustimmungsattribute angeben, werden mit Google synchronisiert, wobei diese Zustimmungsattribute als nicht spezifiziert markiert sind.

Wenn Sie versuchen, einen EWR-Nutzer ohne die erforderlichen Einwilligungsfelder und den erteilten Status zu synchronisieren, wird Google dies ablehnen und keine Anzeigen für diesen Nutzer schalten. Außerdem können Sie haftbar gemacht werden und ein finanzielles Risiko eingehen, wenn einem EWR-Nutzer eine Anzeige ohne dessen ausdrückliche Zustimmung angezeigt wird. Um dies zu vermeiden, empfehlen wir, Kampagnen mit Segmentfiltern zu versenden, die nur Nutzer aus dem EWR, Großbritannien und der Schweiz mit `true` Google-Zustimmungsattributen enthalten. Weitere Einzelheiten zu den EU-Nutzerzustimmungsrichtlinien für Customer Match Upload-Partner finden Sie in den [FAQ](https://support.google.com/google-ads/answer/14310715) von Google.

### Einrichten Ihres Canvas

Nachdem Sie mit Braze synchronisiert haben, sind die folgenden Einwilligungsattribute in Ihren Benutzerprofilen und für die Segmentierung verfügbar:

- `$google_ad_user_data`
- `$google_ad_personalization`

In jedem Canvas, in dem Sie Endnutzer aus dem EWR, Großbritannien und der Schweiz ansprechen und eine Google Audience Sync verwenden, um Nutzer zu einer Zielgruppe hinzuzufügen, müssen Sie diese Nutzer ausschließen, wenn beide Zustimmungsattribute einen Wert haben, der nicht `true` ist. Dies kann erreicht werden, indem diese Benutzer segmentiert werden, wenn die Zustimmungswerte auf `true` eingestellt sind. Dies stellt auch sicher, dass die genaueren Analysen der Nutzer synchronisiert werden, da wir wissen, dass Google diese Nutzer aus den Zielgruppen ausschließen wird. Beachten Sie, dass die Zustimmungsattribute nicht erforderlich sind, wenn Sie Google Audience Sync verwenden, um Nutzer aus einer Zielgruppe zu entfernen.

## Integration

### Schritt 1: Google-Konto verbinden

Um loszulegen, gehen Sie zu **Partnerintegrationen** > **Technologiepartner** > **Google Ads** und wählen Sie **Google Ads verbinden**. 

 



#### 

 

<br><br>
![Die aktualisierte Google Ads Technologieseite zeigt die verbundenen Anzeigenkonten an und ermöglicht es Ihnen, Konten neu zu synchronisieren und mobile Werbe-IDs hinzuzufügen.]({% image_buster /assets/img/google_sync/google_sync5.png %}){: style="max-width:75%;"}
<br><br>

  

### Schritt 2: Fügen Sie einen Google Audience-Schritt in Canvas Flow hinzu



 

### Schritt 3: Sync-Einrichtung

1. 
2. 



{: start="3"}
3\. Wählen Sie das gewünschte Google-Anzeigenkonto.
4\.  

{% tabs %}
{% tab Ein neues Publikum schaffen %}

1. 
2. 
3.  Sie können entweder wählen:

- **Kontaktinformationen für Kunden**:   
- **Mobile Advertiser ID**:  

{: start="4"}
4\. 

![Erweiterte Ansicht der Komponente Custom Audience Canvas. Hier wird das gewünschte Anzeigenkonto ausgewählt, eine neue Zielgruppe erstellt und das Kontrollkästchen "Kundenkontaktinformationen" aktiviert.]({% image_buster /assets/img/audience_sync/g_sync.png %})

Die Benutzer werden oben im Schritteditor benachrichtigt, wenn die Audienz erfolgreich erstellt wurde oder wenn während dieses Prozesses Fehler auftreten. Da die Zielgruppe im Entwurfsmodus erstellt wurde, können Benutzer auf diese Zielgruppe verweisen, um sie später in der Canvas-Reise zu entfernen. 

![Eine Warnung, die erscheint, nachdem eine neue Zielgruppe in der Canvas-Komponente erstellt wurde.]({% image_buster /assets/img/audience_sync/g_sync3.png %})

 

{% alert important %}
Aufgrund der Anforderungen von Google an den Kundenabgleich können Sie keine Kundenkontaktinformationen und IDs von mobilen Werbetreibenden in denselben Kundenlisten haben. Google Customer Match verwendet dann diese Informationen, um zu bestimmen, wer in der Google-Suche, Google Display, YouTube und Google Mail als Zielgruppe in Frage kommt. Weitere Einzelheiten zu den Anforderungen von Google Customer Match finden Sie in der entsprechenden [Dokumentation](https://support.google.com/google-ads/answer/7474166?hl=en&ref_topic=6296507).
{% endalert %}
{% endtab %}
{% tab Synchronisieren Sie mit einer bestehenden Zielgruppe %}

Braze bietet auch die Möglichkeit, Nutzer aus bestehenden Google-Kundenlisten hinzuzufügen oder zu entfernen, um sicherzustellen, dass diese Zielgruppen aktuell sind. 

1. 
2. 
3.  
4.  Ihr Google Audience-Schritt enthält Details über die neue Zielgruppe.

![Erweiterte Ansicht der Komponente Custom Audience Canvas. Hier werden das gewünschte Anzeigenkonto und die bestehende Zielgruppe ausgewählt sowie das Optionsfeld "Benutzer zur Zielgruppe hinzufügen".]({% image_buster /assets/img/audience_sync/g_sync2.png %})

{% endtab %}
{% endtabs %}

### Schritt 4: Canvas starten

Vervollständigen Sie den Rest Ihrer User Journey in Canvas und starten Sie dann! Wenn Sie sich für die Erstellung einer neuen Zielgruppe entschieden haben, erstellt Braze die Zielgruppe in Google und fügt dann Nutzer hinzu, sobald sie diesen Schritt in Ihrem Canvas erreichen. Wenn Sie die Option gewählt haben, Benutzer zu einer bestehenden Zielgruppe hinzuzufügen oder zu entfernen, wird Braze Benutzer entweder hinzufügen oder entfernen, wenn sie diesen Schritt in ihrer User Journey erreichen.

Die Benutzer gelangen dann zur nächsten Komponente des Canvas, falls es eine gibt, oder verlassen das Canvas, wenn es der letzte Schritt der User Journey ist. 

## Überlegungen zur Benutzer-Synchronisierung und Ratenbegrenzung

Sobald Nutzer die Audience Sync-Komponente erreichen, synchronisiert Braze diese Nutzer nahezu in Echtzeit und respektiert dabei die Ratenbeschränkungen der Google Ads API. In der Praxis bedeutet dies, dass Braze versuchen wird, alle 5 Sekunden so viele Nutzer wie möglich zu verarbeiten, bevor diese Nutzer an Google weitergeleitet werden. 

Sobald ein Kunde kurz vor dem Erreichen des Google Ads API-Ratenlimits steht, gibt Google Braze eine Rückmeldung mit Empfehlungen für Wiederholungsversuche. Wenn ein Braze-Kunde sein Tariflimit erreicht, wird Braze the Canvas die Synchronisierung bis zu ~13 Stunden lang wiederholen. Wenn die Synchronisierung nicht möglich ist, werden diese Benutzer unter der Metrik Fehlerhafte Benutzer aufgeführt.

## Analytik verstehen 

Die folgende Tabelle enthält Metriken und Beschreibungen, die Ihnen helfen, die Analysen Ihres Audience Sync-Schrittes besser zu verstehen.

| Metrisch | Beschreibung |
| ------ | ----------- |
| *Eingetreten* | Anzahl der Nutzer, die diesen Schritt eingegeben haben, um mit Google synchronisiert zu werden. |
| *Fortgefahren mit nächstem Schritt* | Wie viele Benutzer sind zur nächsten Komponente weitergegangen, falls es eine gibt. Alle Benutzer werden automatisch vorrücken. Wenn dies der letzte Schritt in der Canvas-Verzweigung ist, wird diese Metrik 0 sein. |
| *Nutzer:innen synchronisiert* | Anzahl der Nutzer, die erfolgreich mit Google synchronisiert wurden. |
| *Nutzer:in nicht synchronisiert* | Anzahl der Benutzer, die nicht synchronisiert wurden, weil Felder zum Abgleich fehlten oder eines der Zustimmungsattribute auf `false` gesetzt war. |
| *Fehler bei Nutzer:innen* | Anzahl der Nutzer, die aufgrund eines Fehlers nicht mit Google synchronisiert wurden, nach ~13 Stunden Wiederholungsversuchen. Bei bestimmten Fehlern, wie z.B. Unterbrechungen des Google Ads API-Dienstes, wird Canvas die Synchronisierung bis zu ~13 Stunden lang wiederholen. Wenn die Synchronisierung zu diesem Zeitpunkt immer noch nicht möglich ist, wird das Feld *Benutzer nicht synchronisiert* ausgefüllt. |
| *Nutzer:innen ausstehend* | Anzahl der Nutzer, die derzeit von Braze für die Synchronisierung mit Google bearbeitet werden. |
| *Canvas wurde verlassen* | Anzahl der Benutzer, die den Canvas verlassen haben. Dies geschieht, wenn der letzte Schritt in einem Canvas ein Google-Schritt ist. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Häufig gestellte Fragen

### 

Google Customer Match stellt strenge Anforderungen daran, wie diese Zielgruppen formatiert werden und welche Kundeninformationen enthalten sind. Insbesondere müssen die IDs der mobilen Werbetreibenden getrennt von den Kontaktinformationen der Kunden (wie E-Mail und Telefonnummer) hochgeladen werden. 

### 

Es kann zwischen 6 und 12 Stunden dauern, bis ein Publikum mit Google synchronisiert ist. 

### 

 Danach wird die Größe auf die zwei höchstwertigen Stellen gerundet.

### 



### 

 


[1]: {% image_buster /assets/img/google_sync/google_sync1.png %}
[2]: {% image_buster /assets/img/google_sync/google_sync2.png %}
[3]: {% image_buster /assets/img/google_sync/google_sync3.png %}
[4]: {% image_buster /assets/img/google_sync/google_sync4.png %}
[6]: {% image_buster /assets/img/google_sync/google_sync6.png %}
[8]: {% image_buster /assets/img/google_sync/google_sync8.png %}
[13]: {% image_buster /assets/img/tiktok/tiktok13.png %}
[16]: {% image_buster /assets/img/tiktok/tiktok16.png %}
[18]: {% image_buster /assets/img/audience_sync/audience_sync3.png %}
[19]: {% image_buster /assets/img/audience_sync/audience_sync4.png %}
[20]: {% image_buster /assets/img/audience_sync/audience_sync5.png %}
[21]: {% image_buster /assets/img/audience_sync/g_sync.png %}
[22]: {% image_buster /assets/img/audience_sync/g_sync2.png %}
[23]: {% image_buster /assets/img/audience_sync/g_sync3.png %}
