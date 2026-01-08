---
nav_title: Daten Modelle
article_title: Erstellen eines B2B-Datenmodells
page_order: 0
page_type: reference
description: "Hier erfahren Sie, wie Sie mit den Daten-Tools von Braze B2B-Modelle erstellen können."
---

# Erstellen eines B2B-Datenmodells

> Dieser Anwendungsfall zeigt, wie Sie mit den Daten-Tools von Braze ein effektives und effizientes B2B-Datenmodell erstellen können, das Sie beim Targeting, Triggern, Personalisieren und Versenden von Nachrichten an Ihre Nutzer:innen unterstützt. 

{% alert note %}
Diese Empfehlungen können sich im Laufe der Zeit ändern, wenn Braze seine B2B-Funktionen ausbaut.
{% endalert %}

Bevor wir uns damit befassen, wie Sie Ihr B2B-Datenmodell einrichten können, sollten Sie einige Konzepte und Begriffe kennen lernen.

Es gibt vier primäre B2B-Objekte, die Sie für die Durchführung von B2B-Kampagnen benötigen.

| Objekt | Beschreibung |
| --- | --- |
| Leads | Eine Aufzeichnung potenzieller Kunden, die Interesse an einem Produkt oder einer Dienstleistung gezeigt haben, aber noch nicht als Verkaufschance qualifiziert wurden. |
| Kontakte | Typischerweise Personen, die qualifiziert und von einem Lead in einen Kontakt umgewandelt wurden, um eine Opportunity zu verfolgen. |
| Opportunitäten | Ein Datensatz, der die Details eines potenziellen Verkaufs oder eines laufenden Geschäfts verfolgt
| Konten | Ein Datensatz über eine Organisation, die ein qualifizierter potenzieller Kunde, ein bestehender Kunde, ein Partner oder ein Konkurrent ist, der eine Beziehung von ähnlicher Bedeutung unterhält. |
{: .reset-td-br-1 .reset-td-br-2 }

In Braze werden diese vier Objekte kombiniert und auf zwei Objekte reduziert: Benutzerprofile und Geschäftsobjekte.

| Braze-B2B Objekt | Beschreibung | Original B2B-Objekte  |
| --- | --- | --- |
| Benutzerprofile | Diese werden direkt den Leads und Kontakten in Ihrem CRM-System zugeordnet. Da die Leads von Braze erfasst werden, werden sie automatisch als Leads in Ihrem CRM-System angelegt. Wenn sie in Kontakte umgewandelt werden, werden die Kontakt-IDs und -details wieder mit Braze synchronisiert. |Leads<br> Kontakte |
| Business Objekte | Diese lassen sich auf alle Nicht-Nutzer-Objekte in Ihrem Vertriebs-CRM-System abbilden. Dazu gehören Ihre vertriebsspezifischen Objekte, wie z.B. Kontoobjekte und Opportunity-Objekte. | Konten<br> Opportunitäten |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Schritt 1: Erstellen Sie Ihre Geschäftsobjekte in Braze

Geschäftsobjekte sind alle nicht benutzerzentrierten Datensätze. Im B2B-Kontext gehören dazu Ihre Konto- und Opportunity-Daten sowie alle anderen relevanten, nicht nutzerbezogenen Daten, die Ihr Unternehmen verfolgt.

Es gibt zwei Methoden zur Erstellung und Verwaltung Ihrer Geschäftsobjekte in Braze: Kataloge und verbundene Quellen. 

| Methode | Beschreibung |
| --- | --- |
| [Kataloge]({{site.baseurl}}/user_guide/data/activation/catalogs) | Dies sind unabhängige Datenobjekte (ergänzende Datenobjekte) zum primären Benutzerprofil in Braze. In einem B2B-Kontext würden Sie wahrscheinlich Kataloge für Ihre Kunden und Opportunities haben. |
| [Verbundene Quellen]({{site.baseurl}}/user_guide/data/cloud_ingestion/connected_sources/) | Diese erlauben es Braze, Ihr Data Warehouse direkt abzufragen. Wahrscheinlich synchronisieren Sie Ihre Lead-, Kontakt-, Opportunity- und Account-Objekte bereits regelmäßig mit Ihrem Data Warehouse, sodass Sie die Segmentierung von Braze direkt auf dieses Data Warehouse verweisen und es in einer Null-Kopie-Umgebung aktivieren können. |
{: .reset-td-br-1 .reset-td-br-2 }

{% tabs %}
{% tab Catalogs %}

### Option 1: Verwenden Sie Kataloge für Accounts und Opportunities

Kataloge sind Datentabellen, die in Braze gehostet und verwaltet werden. Während Konto- und Opportunity-Daten aus dem CRM-System Ihrer Wahl stammen, würden Sie diese in Braze duplizieren, um sie für Marketingzwecke zu verwenden: Segmentierung auf der Basis von Konten, Marketing auf der Basis von Konten, Lead Management und mehr.

Bei dieser Option empfehlen wir Ihnen, einen Katalog für Ihre Konten und einen für Ihre Opportunities zu erstellen und beide regelmäßig zu aktualisieren, indem Sie Braze-Updates über unsere [Katalog-API]({{site.baseurl}}/api/endpoints/catalogs/) oder [Kataloge Cloud Data Ingestion (CDI)]({{site.baseurl}}/user_guide/data/cloud_ingestion/sync_catalogs_data/) senden. Stellen Sie bei der Erstellung dieser Kataloge sicher, dass die `id` (erste Spalte) Ihres Katalogs mit der `id` in Ihrem CRM-System übereinstimmt.

#### Abbildung über Ihre CRM-Felder

In den nachstehenden Tabellen finden Sie einige Beispiele für Felder, die Sie aus den Konto- und Opportunity-Objekten Ihres CRM übernehmen können.

{% subtabs %}
{% subtab Account catalog %}

In diesem Anwendungsfall ist Salesforce das Beispiel-CRM-System. Sie können jedes Feld, das in den Objekten Ihres CRM enthalten ist, abbilden.

<table border="1">
  <tr>
    <th><b>Braze-Objekt</b></th>
    <th><b>Braze-Feld</b></th>
    <th><b>CRM-Objekt (Salesforce)</b></th>
    <th><b>CRM-Feld (Salesforce)</b></th>
  </tr>
  <tr>
    <td rowspan="4">Katalog > Kontokatalog</td>
    <td><code>id</code></td>
    <td><code>Konto</code></td>
    <td><code>id</code></td>
  </tr>
  <tr>
    <td><code>Kontoname</code></td>
    <td><code>Konto</code></td>
    <td><code>Konto Name</code></td>
  </tr>
  <tr>
    <td><code>Typ</code></td>
    <td><code>Konto</code></td>
    <td><code>Typ</code></td>
  </tr>
  <tr>
    <td><code>OTHER_FIELDS</code></td>
    <td><code>Konto</code></td>
    <td><code>OTHER_FIELDS</code></td>
  </tr>
</table>

##### Beispieltabelle der zugeordneten Kontofelder

![Tabelle der Salesforce-Konten mit den entsprechenden Informationen, wie Rechnungsadresse und Kontoinhaber.]({% image_buster /assets/img/b2b/sf_accounts.png %})

{% endsubtab %}
{% subtab Opportunity catalog %}

In diesem Anwendungsfall ist Salesforce das Beispiel-CRM-System. Sie können jedes Feld, das in den Objekten Ihres CRM enthalten ist, abbilden.

<table border="1">
  <tr>
    <th><b>Braze-Objekt</b></th>
    <th><b>Braze-Feld</b></th>
    <th><b>CRM-Objekt (Salesforce)</b></th>
    <th><b>CRM-Feld (Salesforce)</b></th>
  </tr>
  <tr>
    <td rowspan="4">Katalog > Opportunity-Katalog</td>
    <td><code>id</code></td>
    <td><code>Opportunity</code></td>
    <td><code>id</code></td>
  </tr>
  <tr>
    <td><code>OpportunityName</code></td>
    <td><code>Opportunity</code></td>
    <td><code>Opportunity Name</code></td>
  </tr>
  <tr>
    <td><code>Territorium</code></td>
    <td><code>Opportunity</code></td>
    <td><code>Territorium</code></td>
  <tr>
    <td><code>OTHER_FIELDS</code></td>
    <td><code>Opportunity</code></td>
    <td><code>OTHER_FIELDS</code></td>
  </tr>
  </tr>
</table>

##### Beispieltabelle der zugeordneten Opportunity-Felder

![Tabelle der Salesforce Opportunities mit den entsprechenden Informationen wie Rechnungsadresse und Kontoinhaber.]({% image_buster /assets/img/b2b/sf_opportunities.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Connected sources %}

### Option 2: Nutzen Sie verknüpfte Quellen für Accounts und Opportunities

Angeschlossene Datenquellen sind Datentabellen, die von Ihnen in Ihrem eigenen Data Warehouse gehostet werden und von Braze [CDI Segment-Erweiterungen]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/) abgefragt werden. Im Gegensatz zu Katalogen würden Sie Ihre Geschäftsobjekte (Konten und Opportunities) nicht in Braze duplizieren, sondern in Ihrem Data Warehouse aufbewahren und Ihr Warehouse als Quelle der Wahrheit nutzen.

Wie Sie angeschlossene Quellen einrichten, erfahren Sie unter [Einbindung angeschlossener Quellen]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/connected_sources#integrating-connected-sources).

{% endtab %}
{% endtabs %}

## Schritt 2: Verknüpfen Sie Ihre Geschäftsobjekte mit Benutzerprofilen

Nutzerprofile sind das wichtigste Objekt in Braze, das den Großteil Ihrer demografischen Segmentierung, Triggerung und Personalisierung ermöglicht. Zu den Nutzerprofilen gehören [Standard-Nutzerdaten]({{site.baseurl}}/user_guide/data/user_data_collection/), die von unserem SDK und anderen Quellen erfasst werden, einschließlich [benutzerdefinierter Daten]({{site.baseurl}}/user_guide/data/custom_data/), die entweder in Form von Attributen (demografische Daten), Ereignissen (Verhaltensdaten) oder Käufen (Transaktionsdaten) vorliegen.

### Schritt 2.1: Vertriebs-CRM-IDs auf Braze abbilden

Stellen Sie zunächst sicher, dass Braze und das CRM Ihrer Wahl über einen gemeinsamen Bezeichner verfügen, um Daten auszutauschen. Wir empfehlen, die folgende Tabelle zu verwenden, um die ID-Felder Ihres CRM-Vertriebs auf das Nutzerobjekt von Braze abzubilden. In der folgenden Tabelle ist Salesforce als CRM-System angegeben, aber dies kann mit jedem CRM-System durchgeführt werden.

#### Braze Objekt: Nutzer:in

| Braze-Feld | CRM-Objekt (Salesforce) | CRM-Feld (Salesforce) | Zusätzliche Informationen |
| --- | --- | --- | --- |
| `Aliases.salesforce_lead_id` | Lead | `id` |  \- Nutzer-Alias-Label: `salesforce_lead_id` <br>\- Alias-Name des Benutzers: `lead_id`|
| `Aliases.salesforce_contact_id` | Kontaktieren Sie | `id` | \- Nutzer-Alias-Label: `salesforce_contact_id` <br>\- Alias-Name des Benutzers: `contact_id` |
| `AccountId` | Kontaktieren Sie | `AccountId` | 
| `OpportunityId` (optional, skalar) <br>oder<br> `Opportunities` (optional, Array) | Gelegenheit | `id` | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% alert note %}
Wir empfehlen die Verwendung von [Aliasen]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases) anstelle von `external_id`, um die Bezeichner von Salesforce-Leads und -Kontakten auf Braze zurückzuführen. Dies liegt daran, dass es die Anzahl der erforderlichen Suchvorgänge reduziert, wenn Sie Ihre produktorientierten Wachstumsinitiativen identifizieren und umsetzen.
{% endalert %}

Nachdem Sie Ihre IDs synchronisiert haben, müssen Sie Ihre Braze-Benutzerprofile mit Ihren Geschäftsobjekten verknüpfen. 

### Schritt 2.2: Erstellen Sie eine Beziehung zwischen Benutzerprofilen und Ihren Geschäftsobjekten

{% tabs %}
{% tab Catalogs %}

#### Option 1: Bei der Verwendung von Katalogen

Da Ihre Opportunity- und Kontodaten nun als Braze-Kataloge erfasst sind, müssen Sie eine Beziehung zwischen diesen Katalogen und den Benutzerprofilen herstellen, an die Sie Nachrichten senden möchten. Derzeit sind dafür zwei Schritte erforderlich:

1. Nehmen Sie das Konto (z. B. `account_id (string)`), die Opportunity ID (z. B. `opportunity_ids (array)`) oder beide als Attribute in das Nutzerprofil auf.
2. Protokollieren Sie ein Event (z. B. `account_linked`), das die ID des Kontos als Eigenschaft des Events enthält.

```json
{
  "attributes" : [
    {
      "external_id" : "user1",
      "accountId" : "001J7000004K7AF",
      "opportunityIds" : [
"0064J000004EU59",
"0064J000004EU5G"
]
    }
  ],
  "events" : [
    {
      "external_id" : "user1",
      "name" : "account_linked",
      "time" : "2013-07-16T19:20:45+01:00",
      "properties": {
        "account_id": "001J7000004K7AF"
      }
    }
  ]
}
```

{% endtab %}
{% tab Connected sources %}

#### Option 2: Bei Verwendung angeschlossener Quellen

Eine der Tabellen Ihrer verbundenen Quelle sollte eine `user_id` enthalten, die mit der `external_user_id` übereinstimmt, die in Braze für Ihre Benutzer eingestellt wurde. Die obige Einrichtung des Nutzerprofils verwendet Ihren Lead und `contact_ids` als `external_id`, daher sollten Sie sicherstellen, dass Ihre Lead-/Kontakttabellen diese IDs enthalten.

Wir empfehlen, nicht nur sicherzustellen, dass die IDs übereinstimmen, sondern auch grundlegende Daten auf Kontoebene wie `account_id`, `opportunity_id` und sogar allgemeine firmenbezogene Attribute wie `industry` in die Benutzerprofile zu schreiben, um eine effiziente Segmentierung und Personalisierung zu ermöglichen.

{% endtab %}
{% endtabs %}