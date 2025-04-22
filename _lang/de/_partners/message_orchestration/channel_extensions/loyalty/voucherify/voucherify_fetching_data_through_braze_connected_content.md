---
nav_title: Abrufen von Daten über Connected-Content
article_title: Abruf von Daten über Connected-Content mit Voucherify
page_order: 2
alias: /partners/voucherify/connected_content/
description: "Dieser referenzierte Artikel beschreibt, wie Sie Daten aus der Voucherify API über Braze Connected-Content abrufen und Nachrichten an bestimmte Segmente von Braze senden können."
page_type: partner
search_tag: Partner
---

# Abrufen von Daten über Connected-Content

> Mit Braze Connected-Content können Sie Daten aus der Voucherify API abrufen und Nachrichten an bestimmte Segmente von Braze senden. Dieser referenzierte Artikel zeigt Ihnen, wie Sie Connected-Content-Skripte einrichten, um Voucherify-Gutscheine zu veröffentlichen, neue Empfehlungsgeber einzuladen, den Saldo von Treuekarten abzurufen und vieles mehr.

_Diese Integration wird von Voucherify gepflegt._

## Über die Integration

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

Besuchen Sie das Voucherify [GitHub Repository](https://github.com/voucherifyio/braze-connected-content), um Beispiele für Connected-Content-Skripte zu sehen.

## Sicherheitseinstellungen

Ohne die folgenden Einstellungen wird jedes Mal, wenn eine Connected-Content Nachricht getriggert wird, die Voucherify API mindestens zwei Mal aufgerufen. Diese Einstellungen reduzieren die Anzahl der API-Aufrufe, die Braze in Rechnung gestellt werden, und verringern das Risiko, an das Hard-Blocking-API-Limit zu stoßen, das die Zustellung von Nachrichten unterbrechen kann.

{% tabs %}
{% tab Rate-Limiter %}

**Rate-Limiter**

Stellen Sie sicher, dass Sie [die Anzahl der Nachrichten begrenzen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting), die von Braze pro Minute gesendet werden. Dies schützt sowohl die APIs von Braze als auch von Voucherify vor zu viel Traffic aus Ihrer Kampagne. Begrenzen Sie beim Targeting von Nutzern:innen bei der Einrichtung von Kampagnen die Sendegeschwindigkeit auf 500 Nachrichten pro Minute.

![]({% image_buster /assets/img/voucherify/voucherify_cc_limiter.png %})

{% endtab %}
{% tab Caching %}

**Zwischenspeicherung bei POST-Aufrufen**

Connected-Content-Aufrufe, die über HTTP POST erfolgen, werden standardmäßig nicht zwischengespeichert und stellen zwei API-Anfragen für jeden veröffentlichten Code. Dieses Verhalten kann Ihre APIs überfordern. Der Caching-Mechanismus erlaubt es Ihnen, dies auf einen API-Aufruf pro Gutscheinveröffentlichung zu beschränken. 

{% alert important %}
Alle Beispiele für Connected-Content in diesem Tutorial enthalten Standard-Caching, um die Anzahl der von Braze getriggerten API-Aufrufe zu reduzieren.
{% endalert %}

So fügen Sie die Zwischenspeicherung für POST-Aufrufe hinzu:

1. Fügen Sie ein Attribut {% raw %}`:cache_max_age`{% endraw %} hinzu. Standardmäßig beträgt die Dauer der Zwischenspeicherung 5 Minuten. Sie können die Dauer in Sekunden anpassen. Sie kann zwischen 5 Minuten und 4 Stunden eingestellt werden. Beispiel: {% raw %}`:cache_max_age 3600`{% endraw %} wird für 1 Stunde zwischengespeichert.
2. Geben Sie einen Caching-Schlüssel {% raw %}`cache_id={{cache_id}}`{% endraw %} im Abfrageparameter des Ziel-Endpunkts an, damit Braze eine eindeutige Veröffentlichung identifizieren kann. Definieren Sie zunächst die Variable und fügen Sie dann den eindeutigen Query String an Ihren Endpunkt an. Dadurch wird jede Veröffentlichung durch die {% raw %}`source_id`{% endraw %} unterschieden.

![]({% image_buster /assets/img/voucherify/voucherify_cc_cache.png %})

_Beachten Sie die Konsequenzen:_ Braze speichert die API-Aufrufe auf der Grundlage der URL. Der eindeutige String, der als Abfrageparameter verwendet wird, wird von Voucherify ignoriert, aber er unterscheidet verschiedene API-Anfragen für Braze und erlaubt es, jeden eindeutigen Versuch separat zwischenzuspeichern. Ohne diesen Abfrageparameter erhält jede Kund:in den Cache den gleichen Code für die Dauer des Caches.

{% endtab %}
{% tab Attribut "Wiederholung %}

**Attribut "Wiederholung**

Da Connected-Content die Voucherify-Antwort nicht validiert, empfehlen wir zusätzlich das Hinzufügen eines Attributs [zur Wiederholung]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries) im Connected-Content-Skript. Die Logik von Connected-Content versucht, die Nachricht fünfmal zu wiederholen, bevor sie abgebrochen wird (sie respektiert den Rate-Limiter). Mit dieser Methode können Sie verhindern, dass die Veröffentlichung von Codes fehlschlägt, wenn es etwas länger dauert, Daten von Voucherify abzurufen.

Wenn Sie {% raw %}`:retry`{% endraw %} nicht verwenden, wird Braze unabhängig von der von Voucherify zurückgegebenen Antwort versuchen, die Verteilung zu versenden, was dazu führen kann, dass E-Mails ohne einen veröffentlichten Code erzeugt werden.

![]({% image_buster /assets/img/voucherify/voucherify_cc_retry.png %})

{% endtab %}
{% tab Eindeutige Veröffentlichungen %}

**Eindeutige Veröffentlichung pro Kund:in**

Der Parameter {% raw %}`source_id`{% endraw %} im Skriptkörper sorgt dafür, dass jeder Kund:in einer einzigen Kampagne von Braze nur einen eindeutigen Code erhalten kann. Selbst wenn Braze die Anfrage versehentlich vervielfacht, erhält jeder Nutzer:innen denselben eindeutigen Code, der ihm/ihr in der ersten Nachricht mitgeteilt wurde.

![]({% image_buster /assets/img/voucherify/voucherify_cc_sourceId_unique_publication.png %})

Sie können {% raw %}`{{source_id}}`{% endraw %} und seine Auswirkungen auf Publikationen mit den folgenden Konfigurationen ändern:

| Konfiguration | Wirkung |
| ------------- | ------ |
| {% raw %}`{{campaign.${dispatch_id}}}`{% endraw %} | Kund:innen innerhalb einer einzigen Aussendung verwenden dieselbe Publikation. |
| {% raw %}`{{campaign.${api_id}}}`{% endraw %} | Alle Kund:innen einer Kampagne verwenden die gleiche Publikation. |
| {% raw %}`{{${user_id}}}`{% endraw %} oder {% raw %}`{{${braze_id}}}`{% endraw %} | Sorgt dafür, dass jede Kund:in dieselbe Publikation verwendet, egal welche Kampagne gesendet wird (Sie können {% raw %}`${user_id}`{% endraw %} verwenden, das eine {% raw %}`external_id`{% endraw %} ist, und {% raw %}`${braze_id}`{% endraw %}, das eine interne ID ist). |
| {% raw %}`{{campaign.${dispatch_id}}}`{% endraw %} und {% raw %}`{{campaign.${user_id}}}`{% endraw %} | Jede Kund:in einer einzigen Aussendung verwendet dieselbe eindeutige Veröffentlichung. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Einmaliges Beitreten %}

**Einmaliges Beitreten**

Wenn Ihre Voucherify Kampagne ein Limit hat _, dem Kunden nur einmal beitreten können_, entfernen Sie die ID der Veröffentlichungsquelle aus dem Skriptkörper. Voucherify bestätigt, dass jede Nachricht von Braze an denselben Kund:in denselben Code zugestellt wird, der an erster Stelle veröffentlicht wurde.

![]({% image_buster /assets/img/voucherify/voucherify_cc_join_once.png %}){: style="max-width:50%;"}

Ihr Connected-Content-Skript sollte folgendermaßen aussehen:

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

Beachten Sie, dass alle folgenden Anwendungsfälle die ID der Voucherify-Publikationsquelle und die Braze Cache- und Wiederholungsparameter verwenden, um die von einer Braze-Kampagne aufgerufenen APIs zu begrenzen. Sie müssen sich über die folgenden Konsequenzen im Klaren sein:

- Es ist nicht möglich, in einer einzigen Kampagne von Braze verschiedene Codes zu veröffentlichen und an ein und denselben Kund:in zu senden.
- Wenn Ihre Voucherify Kampagne das _Feature "Nur einmal beitreten_" verwendet, müssen Sie `source_id` aus dem Connected-Content-Body entfernen, wie oben im Tab "Einmal beitreten" beschrieben.

Besuchen Sie das Voucherify [GitHub Repository](https://github.com/voucherifyio/braze-connected-content), um Beispiele für Connected-Content-Skripte zu sehen.

### Veröffentlichen und versenden Sie einen eindeutigen Gutschein Code

In diesem Anwendungsfall ruft das Connected-Content-Skript die Voucherify API auf, um einen eindeutigen Gutscheincode zu veröffentlichen und ihn in der Nachricht von Braze zu versenden. Jede Nutzer:in von Braze erhält nur einen eindeutigen Code.

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

### Neue Empfehlungen einladen

Wenn Sie möchten, dass ein Kunde an einem Empfehlungsprogramm teilnimmt, müssen Sie dieser Person einen Empfehlungscode zuweisen. Der Connected-Content bleibt derselbe wie im vorangegangenen Beispiel. Mit diesem Connected-Content-Skript können Sie eindeutige Codes für Empfehlungen an ausgewählte Nutzer:innen von Braze veröffentlichen und versenden. Jeder Nutzer:in erhält nur einen Code, den er mit anderen Nutzern:innen teilen kann, um neue Empfehlungen zu erhalten. 

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

Hier sehen Sie einen Anwendungsfall für ein Connected-Content-Skript, das den aktuellen Treuesaldo auf der Grundlage des Codes der Treuekarte abruft, der zuvor als angepasstes Attribut an Braze gesendet wurde. Beachten Sie, dass Sie den Code der Treuekarte als angepasstes Attribut im Profil des Nutzers:in von Braze speichern müssen, bevor Sie dieses Skript verwenden.

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

### Angepassten Code erstellen

Connected-Content ist ein leistungsstarkes Werkzeug, das die Einführung kreativer Szenarien zulässt. Sie können einen angepassten Code erstellen, der auf den Profilinformationen des Kunden:in basiert.

Hier ist ein Snippet, das die Telefonnummer der Kund:in berücksichtigt, um einen eindeutigen Code zu generieren. In diesem Anwendungsfall ruft das Connected-Content-Skript die Voucherify API auf, um einen angepassten Code für einen Gutschein zu veröffentlichen.

1.  Definieren Sie zunächst alle benötigten Variablen. Dann erstellen Sie einen Gutscheincode, der mit dem Präfix "SummerTime-" beginnt, und der Rest des Codes wird die Telefonnummer der Kund:in sein. Sie können selbst entscheiden, welches angepasste Attribut Sie Ihren Coupon Codes zugrunde legen möchten.  
    
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
    
2.  Als nächstes fragen Sie Voucherify an, um einen einzelnen Code in der Kampagne zu generieren. Wir geben den Namen des zu erstellenden Codes in der URL an:  
    
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

3.  Veröffentlichen Sie schließlich den Code, den Sie gerade erstellt haben. Der Code Snippet sieht fast genauso aus wie der, den Sie für die Generierung eines zufälligen Gutscheins aus einer Kampagne verwendet haben. Dieses Mal haben wir es jedoch auf einen bestimmten Code abgesehen.  
    
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

Als Ergebnis erhält der Kund:in die folgende E-Mail:  

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

## Abgerufene Daten in Messaging-Nachrichten anzeigen

Wir gehen davon aus, dass Sie bereits eine Braze-Kampagne oder ein Braze-Canvas haben, in dem Sie das Connected-Content-Skript verwenden möchten.

### Schritt 1: Connected-Content-Skript zur Nachrichten-Vorlage hinzufügen

1.  Kopieren Sie das Skript Connected-Content und fügen Sie es unter dem Tag {% raw %}`<body>`{% endraw %} in eine HTML-Vorlage für Nachrichten ein. Ersetzen Sie **CAMPAIGN_ID** durch eine Voucherify {% raw %}`campaign_id`{% endraw %}, die Sie aus der URL-Adresse des Dashboards der Kampagne von Voucherify kopieren.<br>![]({% image_buster /assets/img/voucherify/voucherify_cc_campaignId.png %}){: style="margin-top:15px;margin-bottom:15px;"}
    {% raw %}  
    ```
    assign voucherify_campaign_id = "camp_Y7h1meBSyybsNs7UpSVVZZce"
    ```
    {% endraw %}

2. Geben Sie Ihren Voucherify API Endpunkt an. Wenn Sie nicht wissen, wie Ihr API Endpunkt lautet, können Sie ihn unter **Projekteinstellungen** > **Allgemein** > **API Endpunkt** überprüfen.<br>
    {% raw %}
    ```
    YOUR API ENDPOINT/v1/publications?cache_id={{cache_id}}
    ```
    {% endraw %}
    
    | Gemeinsamer Cluster   | Endpunkt für Braze Connected-Content          |
    | ---------------- | --------------------------------------------- |
    | Europa (Standard) | https://api.voucherify.io/v1/publications     |
    | Vereinigte Staaten    | https://us1.api.voucherify.io/v1/publications |
    | Asien (Singapur) | https://as1.api.voucherify.io/v1/publications |
    {: .reset-td-br-1 .reset-td-br-2 role="presentation" }
    
3.  Fügen Sie Ihre API-Schlüssel zur Authentifizierung hinzu. Sie finden `Voucherify-App-Id` und `Voucherify-App-Token` in Ihren **Projekteinstellungen > Allgemein > Anwendungstasten.**<br>![]({% image_buster /assets/img/voucherify/voucherify_cc_app_keys.png %}){: style="margin-top:15px;margin-bottom:15px;"}
    {% raw %}
    ```
    "X-App-Id": "VOUCHERIFY-APP-ID",
    "X-App-Token": "VOUCHERIFY-APP-TOKEN"
    ```
    {% endraw %}
    
Jetzt ist Ihr Connected-Content-Skript einsatzbereit.

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

Antworten von der Voucherify API werden von Connected-Content unter dem Wert des Parameters {% raw %}`:save`{% endraw %} gespeichert. Zum Beispiel:

{% raw %}

```liquid
:save member
```
{% endraw %}

Damit können Sie Daten aus einer Voucherify-Antwort in Nachrichten von Braze abrufen und anzeigen.

Sie können Snippets erstellen, die den veröffentlichten Code, das Guthaben der Kundenkarte, das Ablaufdatum und andere Parameter anzeigen, die in der Antwort der Voucherify API im JSON-Format enthalten sind.

Um beispielsweise den veröffentlichten Code in einer Nachrichten-Vorlage anzuzeigen, müssen Sie ein Snippet erstellen, das einen eindeutigen Code aus dem Gutschein-Objekt abruft.

Connected-Content-Skript:

![Connected-Content-Skript zum Speichern einer Voucherify-Antwort am Ende des Connected-Content-Aufrufs]({% image_buster /assets/img/voucherify/voucherify_cc_save_parameter.png %})

Snippet in Braze Nachricht Template:

{% raw %}

```liquid
{{publication.voucher.code}}
```

{% endraw %}

Als Ergebnis erhält jede Kund:in eine Nachricht mit einem eindeutigen Code, der automatisch ihrem Profil zugeordnet wird. Jedes Mal, wenn der Nutzer:in einen Code erhält, wird dieser in seinem Profil in Voucherify veröffentlicht.

Um einen von der Voucherify API abgerufenen Treuekarten-Saldo anzuzeigen, müssen Sie das folgende Snippet erstellen:

{% raw %}

```liquid
{{member.loyalty_card.balance}}
```

{% endraw %}

wobei das Mitglied ein Wert des Parameters {% raw %}`:save`{% endraw %} im Connected-Content-Skript ist.

{% raw %}

```liquid
:save member
```

{% endraw %}

Wir raten Ihnen dringend, sich nicht ausschließlich auf den 'Vorschau-Modus' zu verlassen und mehrere Testnachrichten zu versenden, um sicherzustellen, dass alles wie gewünscht funktioniert.

### Schritt 3: Rate-Limiter einrichten

Verwenden Sie beim Einrichten eines Kampagnen-Ziels erweiterte Einstellungen, um die Anzahl der pro Minute gesendeten Nachrichten zu begrenzen.

![]({% image_buster /assets/img/voucherify/voucherify_cc_limiter.png %})

Lesen Sie mehr über Rate-Limiter und Frequency-Capping in der Braze [Dokumentation]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting).

