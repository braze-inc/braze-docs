---
nav_title: Dynamische Code-Generierung
article_title: Punchh Dynamische Code-Generierung
page_order: 2
description: "Dieser referenzierte Artikel beschreibt, wie Sie die dynamische Code-Generierung von Punchh in Braze verwenden."
page_type: partner
search_tag: Partner
---

# Dynamische Code-Erstellung mit Punchh

> Ein Gutscheincode ist ein eindeutiger Code, der von einem einzelnen Nutzer:innen verwendet werden kann (entweder einmalig oder mehrfach). Das Punchh-Framework generiert Coupon Codes, die in einer mobilen App oder am Point-of-Sale (POS) System verarbeitet werden können.

_Diese Integration wird von Punchh gepflegt._

## Über die Integration

Mit dem Punchh Coupon Framework und Braze können Sie die folgenden Szenarien realisieren:

- Generieren Sie einen Code, wenn der Gast in einer E-Mail auf einen Link zur Generierung eines Gutscheins klickt: Der Gutschein-Code wird dynamisch generiert und auf einer Internetseite angezeigt.
- Generieren Sie einen Gutscheincode, wenn der Gast eine E-Mail öffnet: Der Gutschein-Code wird dynamisch generiert und als Bild in der E-Mail angezeigt.

## Integration dynamischer Code-Generierung für Gutscheine

### Schritt 1: Erstellen Sie eine Kampagne mit Coupons

1. Erstellen Sie mit einer Punchh-Gutscheinkampagne eine dynamische Generierungs-Gutscheinkampagne, wie in der folgenden Abbildung gezeigt.
2. Das Punchh Coupon Framework generiert die folgenden Parameter, um die dynamische Generierung von Coupons zu ermöglichen:
    - Token zur dynamischen Generierung von Coupons: Dies ist ein vom System generiertes Token für die Verschlüsselung.
    - Dynamische URL für die Erstellung von Coupons: Diese URL wird als Link oder Bild in die E-Mail eingebettet, je nach Bedarf des Unternehmens.

![Das Formular zum Erstellen einer Kampagne in Punchh.]({% image_buster /assets/img/punchh/punchh8.png %}){: style="max-width:60%;"}

### Schritt 2: Signatur generieren und URL konstruieren

Die Bibliothek JWT.IO dekodiert, überprüft und generiert JSON-Web-Tokens, eine offene, dem Industriestandard RFC 7519 entsprechende Methode zur sicheren Darstellung von Ansprüchen zwischen zwei Parteien. 

Die folgenden `ClaimType` Namen können verwendet werden, um die Eindeutigkeit von Gästen und Gutscheinen zu gewährleisten:

- `campaign_id`ID: steht für die vom System generierte ID der Punchh-Kampagne.
- `email`: steht für die E-Mail Adresse des Nutzers:innen. 
- `first_name`Nutzer:in: erfasst den Vornamen des Nutzers:innen. 
- `last_name`: erfasst den Nachnamen des Nutzers:in.

Um die dynamische Code API von Punchh zu nutzen, muss ein JWT Token erstellt werden. Fügen Sie die folgende Liquid-Vorlage zu Ihrem Braze-Dashboard in den Nachrichtentext des Kanals ein, den Sie verwenden möchten:

{% raw %}
```liquid
{% assign header = '{"alg":"HS256","typ":"JWT"}' | base64_encode | replace: '=', '' | replace: '+', '-' | replace: '/', '_' %}

{% capture payload_raw %}

{
  "campaign_id": "CAMPAIGN_ID",
  "email": "{{${email_address}}}",
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}"
}

{% endcapture %}

{% assign payload = payload_raw | replace: ' ', '' | replace: '\n', '' | base64_encode | replace: '=', '' | replace: '+', '-' | replace: '/', '_' %}

{% assign unsigned_token = header | append: "." | append: payload %}

{% assign secret = "DYNAMIC_COUPON_GENERATION_TOKEN" %}

{% assign signature_raw = unsigned_token | hmac_sha256_base64: secret %}

{% assign signature = signature_raw | replace: '=', '' | replace: '+', '-' | replace: '/', '_' %}

{% assign jwt = unsigned_token | append: "." | append: signature %}

```
{% endraw %}


Ersetzen Sie Folgendes:

| Platzhalter        | Beschreibung                                          |
|--------------------|------------------------------------------------------|
| `DYNAMIC_COUPON_GENERATION_TOKEN` | Ihr dynamischer Token für die Generierung von Coupons. |
| `CAMPAIGN_ID`                     | Ihre Kampagne ID.                     |

### Schritt 3: Coupon Code an Nachricht anhängen

#### Verlinkung zur Punchh-Webseite

Um einen Link zu einer von Puncch gehosteten Internetseite zu erstellen, fügen Sie der dynamischen Generierungs-URL [, die Sie zuvor erstellt haben](#step-1-create-a-coupon-campaign-in-punchh), `{% raw %}{{jwt}}{% endraw %}` hinzu. Ihr Link sollte ähnlich wie der folgende aussehen: 

{% raw %}
```
https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX?sign={{jwt}}
```
{% endraw %}

Wenn ein Nutzer:innen auf die Gutschein-URL klickt, wird er auf eine von Punchh gehostete Internetseite weitergeleitet, auf der der generierte Gutschein angezeigt wird.

![Beispiel für eine Bestätigungsnachricht, nachdem ein Nutzer:innen erfolgreich einen Coupon Code generiert hat.]({% image_buster /assets/img/punchh/punchh7.png %})

#### Code über JSON als reinen Text extrahieren

Um eine JSON-Antwort zurückzugeben, fügen Sie `{% raw %}{{jwt}}{% endraw %}` an die dynamische Generierungs-URL an, [die Sie zuvor erstellt haben](#step-1-create-a-coupon-campaign-in-punchh), und fügen dann `.json` nach dem Token in den URL-String ein. Ihr Link sollte ähnlich wie der folgende aussehen:

{% raw %}
```liquid
https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX.json?sign={{jwt}}
```
{% endraw %}

Sie könnten dann [Connected-Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/) nutzen, um den Code als reinen Text in jede Nachricht einzufügen. Zum Beispiel:

{% raw %}
```liquid
{% connected_content https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX.json?sign={{jwt}} :save punchh_coupon %}
{{punchh_coupon.coupon}}
````
{% endraw %}

#### Ein Bild mit dem Inhalt einer E-Mail verknüpfen

So verknüpfen Sie den Code mit einem Bild:

1. Fügen Sie `{% raw %}{{jwt}}{% endraw %}` an die dynamische Generierungs-URL an [, die Sie zuvor erstellt haben](#step-1-create-a-coupon-campaign-in-punchh).
2. Fügen Sie `.png` nach dem Token in den URL String ein.
3. Betten Sie Ihren Link in einen HTML {% raw %}`<img>`{% endraw %} Tag ein.

{% tabs local %}
{% tab Beispieleingabe %}
{% raw %}
```liquid
<img src="https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX.png?sign={{jwt}}">
````
{% endraw %}
{% endtab %}

{% tab Beispiel-Ausgabe %}
![Gerenderte Ausgabe des Tags für den Code des Gutscheins.]({% image_buster /assets/img/punchh/punchh9.png %})
{% endtab %}
{% endtabs %}

## Fehlermeldungen

| Fehlercode | Fehlermeldung | Beschreibung |
| --- | --- | --- |
| `coupon_code_expired` | Dieser Promo Code ist abgelaufen | Der Code wird nach dem konfigurierten Verfallsdatum verwendet. |
| `coupon_code_success` | Herzlichen Glückwunsch, der Promo Code wurde erfolgreich angewendet. | Der Code wird erfolgreich verwendet. |
| `coupon_code_error` | Bitte geben Sie einen gültigen Promo Code ein | Der verwendete Code ist ungültig. |
| `coupon_code_type_error` | Falscher Coupon-Typ. Dieser Coupon kann nur auf `%{coupon_type}` eingelöst werden. | Wenn ein Code, der am POS verwendet werden soll, in der Mobile App verwendet wird, tritt dieser Fehler auf. |
| `usage_exceeded` | Die Kampagne für diesen Code ist voll. Bitte versuchen Sie es beim nächsten Mal. | Die Nutzung des Codes übersteigt die Anzahl der Nutzer:innen, die ihn verwenden dürfen. Wenn die Dashboard-Konfiguration beispielsweise die Verwendung eines Codes durch 3.000 Nutzer:innen zulässt und die Anzahl der Nutzer:innen 3.000 übersteigt, wird dieser Fehler angezeigt. |
| `usage_exceeded_by_guest` | Dieser Promo Code wurde bereits verarbeitet. | Die Nutzung des Codes durch einen Nutzer:in übersteigt die Anzahl der möglichen Nutzungen. Die Dashboard-Konfiguration erlaubt es beispielsweise, dass ein einziger Code dreimal von einem Nutzer:innen verwendet werden kann. Wenn es mehr als das verwendet wird, tritt dieser Fehler auf. |
| `already_used_by_other_guest` | Dieser Promo-Code wurde bereits von einem anderen Gast verwendet. | Ein anderer Nutzer:innen hat den Code bereits verwendet. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

