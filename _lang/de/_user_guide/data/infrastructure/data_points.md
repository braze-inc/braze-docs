---
nav_title: Datenpunkte
article_title: Datenpunkte – Übersicht
page_order: 10
page_type: reference
description: "In diesem Referenzartikel erfahren Sie, was Datenpunkte bei Braze sind und wie Sie deren Nutzung im Blick behalten können."
search_rank: 6
---

# Datenpunkte

> Bei Braze sind Daten gleichbedeutend mit Aktion: Jede Information, die in Braze eingeht, aktualisiert die Segment-Zugehörigkeit, kann Nachrichten triggern und stornieren, ist sofort für die Personalisierung von Nachrichten verfügbar und vieles mehr. Datenpunkte helfen Ihnen, die wichtigsten Informationen für Ihr Unternehmen zu definieren. Indem Sie sich genau überlegen, welche Daten Sie tracken möchten, stellen Sie sicher, dass Sie das Targeting auf die Daten mit dem höchsten Wirkungsgrad für die Erfahrung Ihrer Nutzer:innen ausrichten.

Die Datenpunkte basieren auf Informationen, die anhand von Nutzerprofilen aufgezeichnet werden. Eine genauere Aufschlüsselung dieser Definition finden Sie in Ihrem Braze-Vertrag. Unser Customer-Success-Team kann Ihnen helfen, die besten Datenpraktiken an Ihre Bedürfnisse anzupassen. 

## Definition

"Datenpunkte" beziehen sich auf eine abrechenbare Nutzungseinheit der Braze-Dienste, gemessen an einem Sitzungsbeginn, einem Sitzungsende, einem angepassten Event oder einem aufgezeichneten Kauf sowie an jedem Attribut, das in einem Endnutzerprofil gesetzt wird. Der Klarheit halber gilt jeder der oben genannten Datenpunkte (wie z. B. Sitzungsbeginn, Sitzungsende, angepasstes Event oder aufgezeichneter Kauf sowie jedes Attribut), die dem Profil eines Endnutzers zu einem bestimmten Zeitpunkt zugeordnet werden, als ein einzelner Datenpunkt.

Daten und Ereignisse, die standardmäßig von den Braze-Diensten erfasst werden, wie z. B. Push-Token, Geräteinformationen und alle Ereignisse zum Tracking des Kampagnen-Engagements, wie z. B. E-Mail-Öffnungen und Klicks auf Push-Benachrichtigungen, werden *nicht* als Datenpunkte gezählt.

Lesen Sie den Abschnitt [Verbrauchszählung](#consumption-count) in diesem Artikel, um zu verstehen, welche Daten auf Ihre Datenpunkt-Zuweisung angerechnet werden.

## Anzeigen der Datenpunkt-Nutzung

Um Ihre Datenpunkt-Nutzung einzusehen, gehen Sie zu **Einstellungen** > **Abrechnung** und wählen Sie den Tab **Gesamtdatenpunkt-Nutzung**.

Weitere Informationen zu den Komponenten des Datenpunkt-Dashboards finden Sie unter [Abrechnung]({{site.baseurl}}/user_guide/administrative/app_settings/subscription_and_usage/).

{% alert tip %}
**Verschwenden Sie keine Datenpunkte – aktualisieren Sie nur sich ändernde Daten!**<br><br>
Um die Datenpunkt-Nutzung zu minimieren, empfehlen wir Ihnen, ein Programm einzurichten, das verhindert, dass immer dieselben unveränderlichen Daten gesendet werden, und nur neue und relevante Daten an Braze weitergibt. Braze wird mit Ihnen zusammenarbeiten, um diese Best Practice während des Onboardings zu etablieren.
{% endalert %}

## Verbrauchszählung

Insgesamt werden Datenpunkte gesammelt, wenn die Profildaten von Nutzer:innen aktualisiert werden oder wenn sie bestimmte Aktionen durchführen. Im Wesentlichen handelt es sich bei den Datenpunkten um die Anzahl der einzelnen `session starts`, `session ends`, `events` und `purchases` Ihrer Nutzer:innen.

In den folgenden Abschnitten finden Sie eine Aufschlüsselung, wie Braze Datenpunkte sammelt. Wenn Sie Fragen zu den Feinheiten der Braze-Datenpunkte haben, kann Ihr Braze Account Manager diese beantworten.

Bei den folgenden Aktionen werden keine Datenpunkte protokolliert:
- Löschen von Nutzer:innen aus Braze
- Verwendung von Connected-Content im Messaging
- Änderungen des Abo-Status global und in Bezug auf Abo-Gruppen
- Umbenennung der externen IDs Ihrer Nutzer:innen durch [API-Aufrufe]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/)
- Blockieren von Ereignissen, Attributen oder Event-Eigenschaften

### Besondere Umstände

#### Arrays

Ein Array ist eine geordnete Sammlung von Elementen, die in einem angepassten Attribut gespeichert sind. Das Update eines Arrays kostet einen Datenpunkt pro API-Aufruf, selbst wenn sich das Array tatsächlich nicht ändert. Wenn Sie beispielsweise eine `remove`-Operation für einen Wert senden, der im Array nicht vorhanden ist, wird trotzdem ein Datenpunkt verbraucht. Ebenso verbraucht das Setzen eines angepassten Attributs auf `null`, um es aus dem Profil zu entfernen, einen Datenpunkt. Wenn Sie einem Array schrittweise Werte hinzufügen, wird dies als ein Datenpunkt pro Wert gezählt. 

{% alert tip %}
Wenn Sie bei einfachen Arrays das gesamte Array auf einmal setzen, gilt dies als ein einziger Datenpunkt. Daher sind Arrays ein hervorragendes Instrument, um Nutzerprofile mit relevanten Informationen auf dem neuesten Stand zu halten und Kosten zu senken. <br><br> Arrays von Objekten verbrauchen einen Datenpunkt für jeden Schlüssel, der aktualisiert wird. Reduzieren Sie unnötigen Datenpunkt-Verbrauch, indem Sie nur Updates an Braze weitergeben.
{% endalert %}

#### Verschachtelte angepasste Attribute

Verschachtelte angepasste Attribute beziehen sich auf ein Objekt, das eine Reihe von Attributen als Eigenschaft eines anderen Attributs definiert. Jeder Schlüssel des Objekts gilt als Datenpunkt.

{% alert note %}
Das Update eines angepassten Attribut-Objekts auf `null` verbraucht ebenfalls einen Datenpunkt.
{% endalert %}

#### CSV

Angepasste Attribute, die über den CSV-Import hochgeladen werden, zählen für Ihre Datenpunkte. Bei CSV-Importen zum Zweck der Segmentierung (Importe mit `external_id`, `braze_id` oder `user_alias_name` als einzigem Feld) werden jedoch keine Datenpunkte protokolliert.

Da bei Änderungen des Abo-Status keine Datenpunkte protokolliert werden, fallen auch beim Update der Felder `email_subscribe`, `push_subscribe`, `subscription_group_id` oder `subscription_state` in Ihrer CSV-Datei keine Kosten an.

## Datenpunkte

{% alert note %}
Die folgenden Tabellen dienen der Veranschaulichung. Die genauen Namenskonventionen, die Groß-/Kleinschreibung und die akzeptierten Werte für bestimmte Felder finden Sie in der entsprechenden Dokumentation für Ihre Ingestionsmethode.
{% endalert %}

{% tabs %}
{% tab Non-billable %}

#### Nicht abrechenbare Datenpunkte (Standard)

<div class="small_table"></div>

| Datentyp | Datenpunkt |
| --------- | ---------- |
| Profildaten | Land |
| Profildaten | Sprache |
| Profildaten | Nutzer-ID |
| Profildaten | Nutzer-Alias |
| Neueste Geräte | Anzahl der Geräte |
| Neueste Geräte | Letzte Uhr |
| Neueste Geräte | App-Version |
| Neueste Geräte | Gerät |
| Neueste Geräte | Geräte-Betriebssystem |
| Kontakt-Einstellungen | E-Mail abonniert |
| Kontakt-Einstellungen | Push abonniert |
| Kontakt-Einstellungen | Für Push registrierte Apps |
| Kontakt-Einstellungen | Abo-Gruppe |
| Erhaltene Kampagnen | E-Mail-Adresse |
| Install-Attribution | Installationsquelle |
| Install-Attribution | Kampagne |
| Install-Attribution | Anzeigengruppe |
| Install-Attribution | Anzeige |
| Verschiedenes | Zufällige Bucket-Nummer |
| Empfangene Canvas-Nachrichten | Empfangene Canvas-Nachrichten |
| Messaging-Engagement | Alle Engagement-Ereignisse (wie Öffnungen, Klicks, Impressionen und Abbrüche) |
| Twitter | Follower |
| Twitter | Folgt |
| Twitter | Anzahl der Tweets |
| Facebook | Likes |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Billable %}

#### Abrechenbare Datenpunkte

{% alert important %}
Das Hinzufügen, Entfernen oder Aktualisieren der folgenden Datentypen führt zu einem abrechenbaren Datenpunkt.
{% endalert %}

<style>
table th:nth-child(1) {
    width: 20%;
}
table th:nth-child(2) {
    width: 30%;
}
table th:nth-child(3) {
    width: 50%;
}
table td {
    word-break: break-word;
}
</style>

| Datentyp | Datenpunkt | Anmerkungen |
| --------- | ---------- | ----- |
| Profildaten | Vorname | |
| Profildaten | Nachname | |
| Profildaten | E-Mail-Adresse | |
| Profildaten | Geschlecht | |
| Profildaten | Altersgruppe | |
| Profildaten | Land | Bei manueller Erfassung. Zählt nicht zum Verbrauch, wenn es automatisch erfasst wird. |
| Profildaten | Ort | |
| Profildaten | Sprache | Bei manueller Erfassung. Zählt nicht zum Verbrauch, wenn sie automatisch erfasst wird. |
| Profildaten | Neuestes Geräte-Locale | |
| Profildaten | Zeitzone | |
| Profildaten | Geburtsdatum (DOB) | |
| Profildaten | Bio | |
| Profildaten | Telefonnummer | |
| App-Nutzungsdaten | Sitzungsbeginn | |
| App-Nutzungsdaten | Sitzungsende | |
| Angepasste Attribute | Alle angepassten Attribute | |
| Angepasste Events | Alle angepassten Events | |
| Angepasste Event-Eigenschaften | Alle angepassten Event-Eigenschaften | Angepasste Event-Eigenschaften, die für die Segmentierung mit den Filtern `X Custom Event Property in Y Days` oder `X Purchase Property in Y Days` aktiviert wurden, werden alle als separate Datenpunkte gezählt – zusätzlich zu dem Datenpunkt, der durch das angepasste Event selbst gezählt wird.
| Käufe | Alle Käufe | |
| Kauf-Details | Alle Kauf-Details | |
| Amplitude-Kohorte – Zuweisung | Alle Zuweisungen | |
| Mixpanel-Kohorte – Zuweisung | Alle Zuweisungen | |
| Hightouch-Kohorte – Zuweisung | Alle Zuweisungen | |
| Appsflyer-Kohorte – Zuweisung | Alle Zuweisungen | |
| Letzter Standort | Alle letzten Standorte | Beim Betreten oder Verlassen von Geofences werden keine Datenpunkte protokolliert, da Geofence-Daten nicht im Nutzerprofil gespeichert werden. Geofences werden von den Standortdiensten von Apple und Google überwacht; Braze wird nur benachrichtigt, wenn Nutzer:innen einen Geofence triggern. |
| Twitter | Nutzername | |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}