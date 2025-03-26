---
nav_title: Abrufen von Daten über Connected Content
article_title: Abruf von Daten über Connected Content mit Voucherify
page_order: 2
alias: /partners/voucherify/connected_content/
description: "Dieser Referenzartikel beschreibt, wie Sie über Braze Connected Content Daten aus der Voucherify API abrufen und Nachrichten an bestimmte Braze-Segmente senden können."
page_type: partner
search_tag: Partner
---

# Abrufen von Daten über Connected Content

> Mit Braze Connected Content können Sie Daten von der Voucherify-API abrufen und Nachrichten an bestimmte Braze-Segmente senden. Dieser Referenzartikel zeigt Ihnen, wie Sie Skripte für Connected Content einrichten, um Voucherify-Gutscheine zu veröffentlichen, neue Werber einzuladen, das Guthaben von Kundenkarten abzurufen und vieles mehr.

Das Grundschema des Skripts sieht wie folgt aus:
{% raw %}
```json
{% connected content
  "voucherify-API-ENDPOINT-url"
  :method post
  :headers {
    "X-App-Id": "Voucherify-API-key",
    "X-App-Token": "Voucherify-Secret-key",
  }
  :content_type application/json
  :retry
  :save {{result_variable}}
}
```
{% endraw %}

Besuchen Sie das Voucherify [GitHub-Repository](https://github.com/voucherifyio/braze-connected-content), um Beispiele für Connected Content-Skripte zu sehen.

## Sicherheitseinstellungen

Wenn Sie die folgenden Einstellungen nicht vornehmen, wird die Voucherify-API bei jeder Auslösung einer Connected Content-Nachricht mindestens zwei Mal aufgerufen. Diese Einstellungen reduzieren die Anzahl der API-Aufrufe, die Braze in Rechnung gestellt werden, und verringern das Risiko, dass das Hard-Blocking-API-Limit erreicht wird, das die Nachrichtenzustellung unterbrechen kann.

{% tabs %}
{% tab Ratenbegrenzer %}

**Ratenbegrenzer**

Stellen Sie sicher, dass Sie [die Anzahl der]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting) von Braze gesendeten [Nachrichten]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting) pro Minute [begrenzen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting). Dies schützt sowohl Braze als auch Voucherify APIs vor zu viel Traffic aus Ihrer Kampagne. Wenn Sie bei der Einrichtung der Kampagne Nutzer ansprechen, begrenzen Sie die Versandrate auf 500 Nachrichten pro Minute.

![]({% image_buster /assets/img/voucherify/voucherify_cc_limiter.png %})

{% endtab %}
{% tab Caching %}

**Zwischenspeicherung bei POST-Aufrufen**

Connected Content-Aufrufe, die über HTTP POST erfolgen, werden standardmäßig nicht zwischengespeichert und es werden zwei API-Anfragen für jeden veröffentlichten Code gestellt. Dieses Verhalten kann Ihre API-Grenzen überfordern. Der Caching-Mechanismus ermöglicht es Ihnen, dies auf einen API-Aufruf pro Gutscheinveröffentlichung zu beschränken. 

{% alert important %}
Alle Beispiele für Connected Content in diesem Tutorial enthalten ein Standard-Caching, um die Anzahl der von Braze ausgelösten API-Aufrufe zu reduzieren.
{% endalert %}

So fügen Sie die Zwischenspeicherung für POST-Aufrufe hinzu:

1. Fügen Sie ein Attribut {% raw %}`:cache_max_age`{% endraw %} hinzu. Die Dauer der Zwischenspeicherung beträgt standardmäßig 5 Minuten. Sie können die Dauer in Sekunden angeben. Sie kann zwischen 5 Minuten und 4 Stunden eingestellt werden. Beispiel: {% raw %}`:cache_max_age 3600`{% endraw %} wird für 1 Stunde zwischengespeichert.
2. Geben Sie einen Caching-Schlüssel {% raw %}`cache_id={{cache_id}}`{% endraw %} im Abfrageparameter des Ziel-Endpunkts an, damit Braze eine eindeutige Veröffentlichung identifizieren kann. Definieren Sie zunächst die Variable und fügen Sie dann den eindeutigen Abfrage-String an Ihren Endpunkt an. Dadurch wird jede Veröffentlichung durch die {% raw %}`source_id`{% endraw %} unterschieden.

![]({% image_buster /assets/img/voucherify/voucherify_cc_cache.png %})

_Beachten Sie die Konsequenzen:_ Braze speichert die API-Aufrufe auf der Grundlage der URL. Die eindeutige Zeichenkette, die als Abfrageparameter verwendet wird, wird von Voucherify ignoriert, aber sie unterscheidet verschiedene API-Anfragen für Braze und ermöglicht es, jeden einzelnen Versuch separat zu cachen. Ohne diesen Abfrageparameter erhält jeder Kunde denselben Gutscheincode für die Dauer des Caches.

{% endtab %}
{% tab Attribut Wiederholen %}

**Attribut Wiederholen**

Connected Content validiert die Voucherify-Antwort nicht, daher empfehlen wir zusätzlich das Hinzufügen eines [Retry-Attributs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries) in das Connected Content-Skript. Die Logik von Connected Content wird fünfmal versuchen, die Nachricht zu wiederholen, bevor sie abgebrochen wird (dabei wird der Ratenbegrenzer beachtet). Mit dieser Methode können Sie verhindern, dass die Veröffentlichung des Codes fehlschlägt, wenn es etwas länger dauert, die Daten von Voucherify abzurufen.

Wenn Sie {% raw %}`:retry`{% endraw %} nicht verwenden, wird Braze unabhängig von der von Voucherify zurückgegebenen Antwort versuchen, die Verteilung zu versenden, was dazu führen kann, dass E-Mails ohne einen veröffentlichten Code erzeugt werden.

![]({% image_buster /assets/img/voucherify/voucherify_cc_retry.png %})

{% endtab %}
{% tab Einzigartige Veröffentlichungen %}

**Einmalige Veröffentlichung pro Kunde**

Der Parameter {% raw %}`source_id`{% endraw %} im Skriptkörper sorgt dafür, dass jeder Kunde nur einen einzigen Code in einer einzigen Braze-Kampagne erhalten kann. Selbst wenn Braze die Anfrage unbeabsichtigt vervielfältigt, erhält jeder Benutzer denselben eindeutigen Code, der ihm in der ersten Nachricht mitgeteilt wurde.

![]({% image_buster /assets/img/voucherify/voucherify_cc_sourceId_unique_publication.png %})

Sie können {% raw %}`{{source_id}}`{% endraw %} und seine Auswirkungen auf Publikationen mit den folgenden Konfigurationen ändern:

| Konfiguration | Wirkung |
| ------------- | ------ |
| {% raw %}`{{campaign.${dispatch_id}}}`{% endraw %} | Kunden innerhalb eines Versandes verwenden dieselbe Publikation. |
| {% raw %}`{{campaign.${api_id}}}`{% endraw %} | Alle Kunden innerhalb einer Kampagne verwenden dieselbe Veröffentlichung. |
| {% raw %}`{{${user_id}}}`{% endraw %} oder {% raw %}`{{${braze_id}}}`{% endraw %} | Stellt sicher, dass jeder Kunde dieselbe Veröffentlichung verwendet, unabhängig davon, welche Kampagne gesendet wird (Sie können {% raw %}`${user_id}`{% endraw %} verwenden, das eine {% raw %}`external_id`{% endraw %} ist, und {% raw %}`${braze_id}`{% endraw %}, das eine interne ID ist). |
| {% raw %}`{{campaign.${dispatch_id}}}`{% endraw %} und {% raw %}`{{campaign.${user_id}}}`{% endraw %} | Jeder Kunde innerhalb eines Versands verwendet dieselbe einzigartige Veröffentlichung. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Einmaliges Beitreten %}

**Einmaliges Beitreten**

Wenn Ihre Voucherify-Kampagne eine Beschränkung hat, dass _Kunden nur einmal teilnehmen können_, entfernen Sie die Veröffentlichungsquellen-ID aus dem Skriptkörper. Voucherify wird bestätigen, dass jede Nachricht von Braze an denselben Kunden denselben Code liefert, der an erster Stelle veröffentlicht wurde.

![]({% image_buster /assets/img/voucherify/voucherify_cc_join_once.png %}){: style="max-width:50%;"}

Ihr Skript für Connected Content sollte wie folgt aussehen:

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${api_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign cache_id = braze_campaign_id | append: customer_id %}
{% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}

{% connected_content
   https://api.voucherify.io/v1/publications?cache_id={{cache_id}}
   :method post
   :headers {
    "X-App-Id": "VOUCHERIFY-APP-ID",
    "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :body campaign={{voucherify_campaign_id}}&customer={{customer_id}}&channel=Braze
   :content_type application/json
   :cache_max_age
   :retry
   :save publication
 %}
```

{% endraw %}
{% endtab %}
{% endtabs %}

## Anwendungsfälle

Beachten Sie, dass alle unten aufgeführten Anwendungsfälle die Voucherify-Publikationsquellen-ID und die Braze-Cache- und Wiederholungsparameter verwenden, um die von einer Braze-Kampagne aufgerufenen API-Aufrufe zu begrenzen. Sie müssen sich über die folgenden Konsequenzen im Klaren sein:

- Es ist nicht möglich, in einer einzigen Braze-Kampagne verschiedene Codes zu veröffentlichen und an denselben Kunden zu senden.
- Wenn Ihre Voucherify-Kampagne die _Funktion "Nur einmal beitreten_" verwendet, müssen Sie `source_id` aus dem Body des Connected Content entfernen, wie oben auf der Registerkarte "Einmal beitreten" beschrieben.

Besuchen Sie das Voucherify [GitHub-Repository](https://github.com/voucherifyio/braze-connected-content), um Beispiele für Connected Content-Skripte zu sehen.

### Veröffentlichen und versenden Sie einzigartige Gutscheincodes

In diesem Anwendungsfall ruft das Skript Connected Content die Voucherify-API auf, um einen eindeutigen Gutscheincode zu veröffentlichen und ihn in der Braze-Nachricht zu versenden. Jeder Braze-Benutzer erhält nur einen einzigen Code.

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${api_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign source_id = braze_campaign_id | append: customer_id %}
{% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}
{% assign cache_id = source_id %}

{% connected_content
   YOUR API ENDPOINT/v1/publications?cache_id={{cache_id}}
   :method post
   :headers {
        "X-App-Id": "VOUCHERIFY-APP-ID",
        "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :body campaign={{voucherify_campaign_id}}&customer={{customer_id}}&channel=Braze&source_id={{source_id}}
   :content_type application/json
   :cache_max_age
   :retry
   :save publication
 %}
```

{% endraw %}

### Neue Empfehlungsgeber einladen

Wenn Sie möchten, dass ein Kunde an einem Empfehlungsprogramm teilnimmt, müssen Sie dieser Person einen Empfehlungscode zuweisen. Der Verbundene Inhalt bleibt derselbe wie im vorangegangenen Beispiel. Mit diesem Skript für Connected Content können Sie einzigartige Empfehlungscodes veröffentlichen und an ausgewählte Braze-Benutzer senden. Jeder Nutzer erhält nur einen Empfehlungscode, den er mit anderen Nutzern teilen kann, um neue Empfehlungen zu erhalten. 

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${api_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign source_id = braze_campaign_id | append: customer_id %}
{% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}
{% assign cache_id = source_id %}

{% connected_content
   YOUR API ENDPOINT/v1/publications?cache_id={{cache_id}}
   :method post
   :headers {
        "X-App-Id": "VOUCHERIFY-APP-ID",
        "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :body campaign={{voucherify_campaign_id}}&customer={{customer_id}}&channel=Braze&source_id={{source_id}}
   :content_type application/json
   :cache_max_age
   :retry
   :save publication
 %}
```

{% endraw %}

### Guthaben der Treuekarte abrufen

Hier sehen Sie einen Anwendungsfall für ein Skript für Connected Content, das den aktuellen Treuebonus auf der Grundlage des Treuekartencodes abruft, der zuvor als benutzerdefiniertes Attribut an Braze gesendet wurde. Beachten Sie, dass Sie den Treuekartencode als benutzerdefiniertes Attribut im Profil des Braze-Benutzers speichern müssen, bevor Sie dieses Skript verwenden.

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${api_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign source_id = braze_campaign_id | append: customer_id %}
{% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}
{% assign cache_id = source_id %}

{% connected_content
   YOUR API ENDPOINT/v1/loyalties/members/{{custom_attribute.${loyalty.card}}}?cache_id={{cache_id}}
   :method get
   :headers {
        "X-App-Id": "VOUCHERIFY-APP-ID",
        "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :content_type application/json
   :cache_max_age
   :retry
   :save member
 %}
```

{% endraw %}

### Benutzerdefinierten Code erstellen

Connected Content ist ein leistungsstarkes Tool, das die Einführung kreativer Szenarien ermöglicht. Sie können einen benutzerdefinierten Gutscheincode auf der Grundlage der Profilinformationen des Kunden erstellen.

Hier ist ein Codeschnipsel, der die Telefonnummer des Kunden berücksichtigt, um einen eindeutigen Code zu erzeugen. In diesem Anwendungsfall ruft das Skript Connected Content die Voucherify-API auf, um einen benutzerdefinierten Coupon-Code zu veröffentlichen.

1.  Definieren Sie zunächst alle benötigten Variablen. Erstellen Sie dann einen Gutscheincode, der mit dem Präfix "SummerTime-" beginnt, und der Rest des Codes wird die Telefonnummer des Kunden sein. Sie können selbst entscheiden, auf welchem Attribut Sie Ihre Gutscheincodes basieren möchten.  
    
    {% raw %}
    
    ```liquid
    {% assign braze_campaign_id = {{campaign.${dispatch_id}}} %}
    {% assign customer_id = {{${user_id}}} %}
    {% assign phoneNumber = {{${phone_number}}} %}
    {% assign source_id = braze_campaign_id | append: customer_id %}
    {% assign cache_id = source_id %}
    {% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}
    {% assign prefix = "SummerTime-" %}
    ```
    
    {% endraw %}
    
2.  Als nächstes fordern Sie Voucherify auf, einen einzelnen Code in der Kampagne zu generieren. Wir geben den Namen des zu erstellenden Gutscheincodes in der URL an:  
    
    {% raw %}
    
    ```liquid
    {% connected_content
       YOUR-API-ENDPOINT/v1/campaigns/{{voucherify_campaign_id}}/vouchers/{{prefix}}{{phoneNumber}}?cache_id={{cache_id}}
       :method post
       :headers {
            "X-App-Id": "VOUCHERIFY-APP-ID",
            "X-App-Token": "VOUCHERIFY-APP-TOKEN"
       }
       :content_type application/json
       :cache_max_age 
       :save voucher_created
       :retry
    %}  
    ```  
    
    {% endraw %}  

3.  Veröffentlichen Sie schließlich den Code, den Sie gerade erstellt haben. Das Codeschnipsel sieht fast genauso aus wie das, das Sie für die Generierung eines zufälligen Gutscheins aus einer Kampagne verwendet haben. Dieses Mal haben wir es jedoch auf einen bestimmten Gutscheincode abgesehen.  
    
    {% raw %}  
    
    ```liquid
    {% connected_content
       YOUR-API-ENDPOINT/v1/publications?cache_id={{cache_id}}
       :method post
       :headers {
           "X-App-Id": "VOUCHERIFY-APP-ID",
           "X-App-Token": "VOUCHERIFY-APP-TOKEN"
       }
       :body voucher={{prefix}}{{phoneNumber}}&customer={{customer_id}}&channel=Braze&source_id={{source_id}}
       :content_type application/json
       :cache_max_age 
       :save publication
       :retry
    %}
    ```
    
    {% endraw %}

Infolgedessen erhält der Kunde die folgende E-Mail:  

![]({% image_buster /assets/img/voucherify/voucherify_cc_custom_code_email.png %})

Hier ist das komplette Snippet, das in diesem Beispiel verwendet wird:

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${dispatch_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign phoneNumber = {{${phone_number}}} %}
{% assign source_id = braze_campaign_id | append: customer_id %}
{% assign cache_id = source_id %}
{% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}
{% assign prefix = "Your Prefix" %}

{% connected_content
   YOUR-API-ENDPOINT/v1/campaigns/{{voucherify_campaign_id}}/vouchers/{{prefix}}{{phoneNumber}}?cache_id={{cache_id}}
   :method post
   :headers {
        "X-App-Id": "VOUCHERIFY-APP-ID",
        "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :content_type application/json
   :cache_max_age 
   :save voucher_created
   :retry
%} 

{% connected_content
   YOUR-API-ENDPOINT/v1/publications?cache_id={{cache_id}}
   :method post
   :headers {
       "X-App-Id": "VOUCHERIFY-APP-ID",
       "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :body voucher={{prefix}}{{phoneNumber}}&customer={{customer_id}}&channel=Braze&source_id={{source_id}}
   :content_type application/json
   :cache_max_age 
   :save publication
   :retry
%}
```

{% endraw %}

## Abgerufene Daten in Braze-Nachrichten anzeigen

Wir gehen davon aus, dass Sie bereits eine Braze-Kampagne oder ein Canvas haben, in dem Sie das Skript Connected Content verwenden möchten.

### Schritt 1: Skript "Verbundener Inhalt" zur Nachrichtenvorlage hinzufügen

1.  Kopieren Sie das Skript Connected Content und fügen Sie es unter dem Tag {% raw %}`<body>`{% endraw %} in eine HTML-Vorlage für eine Nachricht ein. Ersetzen Sie **CAMPAIGN_ID** durch eine Voucherify {% raw %}`campaign_id`{% endraw %}, die von der URL-Adresse des Voucherify-Kampagnen-Dashboards kopiert wurde.<br>![]({% image_buster /assets/img/voucherify/voucherify_cc_campaignId.png %}){: style="margin-top:15px;margin-bottom:15px;"}
    {% raw %}  
    ```
    assign voucherify_campaign_id = "camp_Y7h1meBSyybsNs7UpSVVZZce"
    ```
    {% endraw %}

2. Geben Sie Ihren Voucherify-API-Endpunkt an. Wenn Sie nicht wissen, wie Ihr API-Endpunkt lautet, können Sie ihn unter **Projekteinstellungen** > **Allgemein** > **API-Endpunkt** überprüfen.<br>
    {% raw %}
    ```
    YOUR API ENDPOINT/v1/publications?cache_id={{cache_id}}
    ```
    {% endraw %}
    
    | Gemeinsamer Cluster   | Endpunkt für Braze Connected Content          |
    | ---------------- | --------------------------------------------- |
    | Europa (Standard) | https://api.voucherify.io/v1/publications     |
    | Vereinigte Staaten    | https://us1.api.voucherify.io/v1/publications |
    | Asien (Singapur) | https://as1.api.voucherify.io/v1/publications |
    {: .reset-td-br-1 .reset-td-br-2 role="presentation" }
    
3.  Fügen Sie Ihre API-Schlüssel für die Authentifizierung hinzu. Sie finden `Voucherify-App-Id` und `Voucherify-App-Token` in Ihren **Projekteinstellungen > Allgemein > Anwendungstasten.**<br>![]({% image_buster /assets/img/voucherify/voucherify_cc_app_keys.png %}){: style="margin-top:15px;margin-bottom:15px;"}
    {% raw %}
    ```
    "X-App-Id": "VOUCHERIFY-APP-ID",
    "X-App-Token": "VOUCHERIFY-APP-TOKEN"
    ```
    {% endraw %}
    
Jetzt ist Ihr Skript für Connected Content einsatzbereit.

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${api_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign source_id = braze_campaign_id | append: customer_id %}
{% assign voucherify_campaign_id = "camp_Y7h1meBSyybsNs7UpSVVZZce" %}
{% assign cache_id = source_id %}

{% connected_content
   https://api.voucherify.io/v1/publications?cache_id={{cache_id}}
   :method post
   :headers {
        "X-App-Id": "490a3fb6-a",
        "X-App-Token": "328099d5-a"
   }
   :body campaign={{voucherify_campaign_id}}&customer={{customer_id}}&channel=Braze&source_id={{source_id}}
   :content_type application/json
   :cache_max_age
   :retry
   :save publication
 %}
```

{% endraw %}

### Schritt 2: Erstellen Sie ein Snippet zur Anzeige der abgerufenen Daten

Antworten von der Voucherify API werden von Connected Content unter dem Wert des Parameters {% raw %}`:save`{% endraw %} gespeichert. Zum Beispiel:

{% raw %}

```liquid
:save member
```
{% endraw %}

Damit können Sie Daten aus einer Voucherify-Antwort in Braze-Nachrichten abrufen und anzeigen.

Sie können Snippets erstellen, die den veröffentlichten Code, das Guthaben der Kundenkarte, das Ablaufdatum und andere Parameter anzeigen, die in der Antwort im JSON-Format von der Voucherify API enthalten sind.

Um zum Beispiel den veröffentlichten Code in einer Nachrichtenvorlage anzuzeigen, müssen Sie ein Snippet erstellen, das einen eindeutigen Code aus dem Gutscheinobjekt abruft.

Skript "Connected Content":

![Skript für Connected Content, das zeigt, wie eine Voucherify-Antwort am Ende des Aufrufs von Connected Content gespeichert wird]({% image_buster /assets/img/voucherify/voucherify_cc_save_parameter.png %})

Snippet in der Braze Nachrichtenvorlage:

{% raw %}

```liquid
{{publication.voucher.code}}
```

{% endraw %}

Als Ergebnis erhält jeder Kunde eine Nachricht mit einem eindeutigen Code, der automatisch seinem Profil zugeordnet wird. Jedes Mal, wenn der Benutzer einen Code erhält, wird er in seinem Profil in Voucherify veröffentlicht.

Um das Guthaben einer Kundenkarte anzuzeigen, das von der Voucherify-API abgerufen wurde, müssen Sie das folgende Snippet erstellen:

{% raw %}

```liquid
{{member.loyalty_card.balance}}
```

{% endraw %}

wobei das Mitglied ein Wert des Parameters {% raw %}`:save`{% endraw %} im Skript Connected Content ist.

{% raw %}

```liquid
:save member
```

{% endraw %}

Wir raten Ihnen dringend, sich nicht ausschließlich auf den 'Vorschaumodus' zu verlassen und mehrere Testnachrichten zu versenden, um sicherzustellen, dass alles so funktioniert, wie es sollte.

### Schritt 3: Ratenbegrenzer einrichten

Wenn Sie ein Kampagnenziel einrichten, verwenden Sie die erweiterten Einstellungen, um die Anzahl der pro Minute gesendeten Nachrichten zu begrenzen.

![]({% image_buster /assets/img/voucherify/voucherify_cc_limiter.png %})

Lesen Sie mehr über Rate Limiter und Frequency Capping in der Braze [Dokumentation]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting).
