---
nav_title: Dynamische Code-Generierung
article_title: Punchh Dynamische Code-Generierung
page_order: 2
description: "Dieser Referenzartikel beschreibt, wie Sie die dynamische Codegenerierung von Punchh in Braze verwenden."
page_type: partner
search_tag: Partner
---

# Dynamische Codegenerierung mit Punchh

> Ein Gutscheincode ist ein eindeutiger Code, der von einem einzelnen Benutzer verwendet werden kann (entweder einmalige oder mehrfache Verwendung). Das Punchh-Framework generiert Coupon-Codes, die in einer mobilen App oder am Point-of-Sale (POS)-System verarbeitet werden können.

Mit dem Punchh Coupon Framework und Braze können Sie die folgenden Szenarien realisieren:

- Generieren Sie einen Gutscheincode, wenn der Gast in einer E-Mail auf einen Link zur Erstellung eines Gutscheins klickt: Der Gutscheincode wird dynamisch generiert und auf einer Webseite angezeigt.
- Generieren Sie einen Gutscheincode, wenn der Gast eine E-Mail öffnet: Der Gutscheincode wird dynamisch generiert und in der E-Mail als Bild angezeigt.

## Integration der dynamischen Gutscheincode-Generierung

### Schritt 1: Erstellen Sie eine Coupon-Kampagne

1. Erstellen Sie mit einer Punchh-Gutscheinkampagne eine Kampagne zur dynamischen Generierung von Gutscheinen, wie in der folgenden Abbildung gezeigt.
2. Das Punchh Coupon Framework generiert die folgenden Parameter, um die dynamische Coupon-Generierung zu ermöglichen:
    - Dynamischer Coupon-Generierungs-Token: Dies ist ein vom System generiertes Sicherheits-Token für die Verschlüsselung.
    - URL für die Erstellung dynamischer Coupons: Diese URL wird als Link oder Bild in die E-Mail eingebettet, je nach Bedarf des Unternehmens.

![Das Formular zum Erstellen einer Coupon-Aktion in Punchh.]({% image_buster /assets/img/punchh/punchh8.png %}){: style="max-width:60%;"}

### Schritt 2: Signatur generieren und URL konstruieren

Die Bibliothek JWT.IO dekodiert, verifiziert und generiert JSON-Web-Tokens, eine offene, dem Industriestandard RFC 7519 entsprechende Methode zur sicheren Darstellung von Ansprüchen zwischen zwei Parteien. 

Die folgenden `ClaimType` Namen können verwendet werden, um die Einzigartigkeit von Gästen und Gutscheinen zu gewährleisten:

- `campaign_id`: steht für die vom System generierte Punchh-Kampagnen-ID.
- `email`: steht für die E-Mail-Adresse des Benutzers. 
- `first_name`: Erfasst den Vornamen des Benutzers. 
- `last_name`: Erfasst den Nachnamen des Benutzers.

Um die dynamische Gutscheincode-API von Punchh zu verwenden, muss ein JWT-Token erstellt werden. Fügen Sie die folgende Liquid-Vorlage in Ihrem Braze-Dashboard in den Nachrichtentext des gewünschten Channels ein:

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
| `DYNAMIC_COUPON_GENERATION_TOKEN` | Ihr dynamischer Coupon-Generierungs-Token. |
| `CAMPAIGN_ID`                     | Ihre Kampagnen-ID.                     |

### Schritt 3: Gutscheincode an den Nachrichtentext anhängen

#### Verlinkung zur Punchh-Webseite

Um einen Link zu einer von Puncch gehosteten Webseite zu erstellen, fügen Sie `{% raw %}{{jwt}}{% endraw %}` zu der dynamischen Generierungs-URL hinzu [, die Sie zuvor erstellt haben](#step-1-create-a-coupon-campaign-in-punchh). Ihr Link sollte ähnlich wie der folgende aussehen: 

{% raw %}
```
https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX?sign={{jwt}}
```
{% endraw %}

Wenn ein Benutzer auf die Gutschein-URL klickt, wird er auf eine von Punchh gehostete Webseite weitergeleitet, auf der sein generierter Gutschein angezeigt wird.

![Beispiel für eine Bestätigungsmeldung, nachdem ein Benutzer erfolgreich einen Gutscheincode erstellt hat.]({% image_buster /assets/img/punchh/punchh7.png %})

#### Code über JSON als reinen Text extrahieren

Um eine JSON-Antwort zurückzugeben, fügen Sie `{% raw %}{{jwt}}{% endraw %}` an die dynamische Generierungs-URL an, [die Sie zuvor erstellt haben](#step-1-create-a-coupon-campaign-in-punchh), und fügen Sie dann `.json` nach dem Token in die URL-Zeichenfolge ein. Ihr Link sollte ähnlich wie der folgende aussehen:

{% raw %}
```liquid
https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX.json?sign={{jwt}}
```
{% endraw %}

Sie können dann [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/) nutzen, um den Code als reinen Text in jeden Nachrichtentext einzufügen. Zum Beispiel:

{% raw %}
```liquid
{% connected_content https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX.json?sign={{jwt}} :save punchh_coupon %}
{{punchh_coupon.coupon}}
````
{% endraw %}

#### Ein Bild mit dem Inhalt einer E-Mail verknüpfen

So verknüpfen Sie den Gutscheincode mit einem Bild:

1. Fügen Sie `{% raw %}{{jwt}}{% endraw %}` an die dynamische Generierungs-URL an [, die Sie zuvor erstellt haben](#step-1-create-a-coupon-campaign-in-punchh).
2. Fügen Sie `.png` nach dem Token in die URL-Zeichenfolge ein.
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
![Gerenderte Ausgabe des Gutscheincode-Bild-Tags.]({% image_buster /assets/img/punchh/punchh9.png %})
{% endtab %}
{% endtabs %}

## Fehlermeldungen

| Fehlercode | Fehlermeldung | Beschreibung |
| --- | --- | --- |
| `coupon_code_expired` | Dieser Promo-Code ist abgelaufen | Der Code wird nach dem konfigurierten Verfallsdatum verwendet. |
| `coupon_code_success` | Glückwunsch, Promo-Code erfolgreich angewendet. | Der Code wird erfolgreich verwendet. |
| `coupon_code_error` | Bitte geben Sie einen gültigen Promo-Code ein | Der verwendete Code ist ungültig. |
| `coupon_code_type_error` | Falscher Coupon-Typ. Dieser Coupon kann nur auf `%{coupon_type}` eingelöst werden. | Wenn ein Code, der an der Kasse verwendet werden soll, in der Mobile App verwendet wird, tritt dieser Fehler auf. |
| `usage_exceeded` | Die Kampagne für diesen Gutscheincode ist voll. Bitte versuchen Sie es beim nächsten Mal. | Die Nutzung des Codes übersteigt die Anzahl der Benutzer, die ihn verwenden dürfen. Wenn die Dashboard-Konfiguration beispielsweise zulässt, dass ein Code von 3.000 Benutzern verwendet werden kann und die Anzahl der Benutzer 3.000 übersteigt, tritt dieser Fehler auf. |
| `usage_exceeded_by_guest` | Dieser Promo-Code wurde bereits verarbeitet. | Die Verwendung des Codes durch einen Benutzer übersteigt die Anzahl der Male, die ein Benutzer ihn verwenden kann. Die Dashboard-Konfiguration erlaubt es zum Beispiel, dass ein einziger Code dreimal von einem Benutzer verwendet werden kann. Wenn es mehr als das verwendet wird, tritt dieser Fehler auf. |
| `already_used_by_other_guest` | Dieser Promo-Code wurde bereits von einem anderen Gast verwendet. | Ein anderer Benutzer hat den Code bereits verwendet. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
