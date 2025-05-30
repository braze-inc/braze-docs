# Angepasste Domains

> Auf dieser Seite erfahren Sie, wie Sie angepasste Domains verwenden können, um ein konsistentes Markenimage darzustellen. 

{% alert note %}
Kontaktieren Sie Ihren Braze-Konto Manager:in, wenn Sie mit angepassten Domains beginnen möchten.
{% endalert %}

## Domain-Anforderungen

- Die Domains müssen Ihnen gehören und von Ihnen verwaltet werden.
- Die für dieses Feature verwendete Domain muss eindeutig sein (d.h. sich von der Domain Ihrer Website unterscheiden), und die Domain kann nicht zum Hosten von Webinhalten verwendet werden.
  - Sie können auch eindeutige Subdomains verwenden, wie `sms.braze.com` oder `whatsapp.braze.com`.

### Angepasste Domains delegieren

Wenn Sie Ihre Domain an Braze delegieren, kümmern wir uns automatisch um die Erneuerung des Zertifikats, um eine Unterbrechung des Dienstes zu verhindern. 

Um Ihre Domain an Braze zu delegieren, gehen Sie wie folgt vor: 

1. Teilen Sie Ihrem Customer-Success-Manager eine Domain mit, die die oben genannten Anforderungen erfüllt. Braze prüft dann die bestehende DNS-Konfiguration für die Domain und bestätigt dies:

- Es existieren keine CAA-Aufzeichnungen ODER
- CAA-Datensätze **existieren**, haben aber einen Datensatz für {% raw %}`<any number> issue "letsencrypt.org"`{% endraw %} oder {% raw %}`<anynumber> issuewild "letsencrypt.org"`{% endraw %}

{:start="2"}
2\. Erstellen Sie vier neue A-Einträge (einen für jede IP) und vergewissern Sie sich, dass dies die einzigen A-Einträge für den Domain-Link-Host sind:
- `151.101.130.133`
- `151.101.194.133`
- `151.101.2.133`
- `151.101.66.133`

## Angepasste Domains verwenden

Nach ihrer Konfiguration können angepasste Domains einer oder mehreren WhatsApp- und SMS-Abo-Gruppen zugewiesen werden. 

![Abogruppeneinstellungen ermöglichen die Auswahl einer Link-Shorting-Domain.][7]

{% if include.channel == 'WhatsApp' %}
Kampagnen, die mit eingeschaltetem Click Tracking versendet werden oder in WhatsApp Nachrichten-Templates integriert sind, verwenden die zugewiesene Domain, die Ihren Abo-Gruppen zugeordnet ist.

![Vorschau des Nachrichten-Editors von WhatsApp mit einer verkürzten Link-Domain, die sich von der Domain im Feld "Nachricht" unterscheidet.][6]
{% endif %}

{% if include.channel == 'SMS' %}
Kampagnen, die mit aktivierter Linkverkürzung versendet werden, verwenden die Domain, die Ihrer Abo-Gruppe für SMS zugewiesen ist.

![Vorschau des SMS-Editors mit einer verkürzten Link-Domain, die sich von der Domain im Feld "Nachricht" unterscheidet.][8]
{% endif %}

## Häufig gestellte Fragen

### Können delegierte Domains von mehreren Abo-Gruppen gemeinsam genutzt werden?

Ja Eine einzelne Domain kann mit mehreren Abo-Gruppen verwendet werden. Wählen Sie dazu für jede Abo-Gruppe die Domain aus, mit der sie verknüpft werden soll.

### Können delegierte Domains von mehreren Workspaces gemeinsam genutzt werden?

Ja Domains können mit Abo-Gruppen in mehreren Workspaces verknüpft werden, sofern diese zu demselben Unternehmen gehören.

[6]: {% image_buster /assets/img/custom_domain_whatsapp_composer.png %}
[7]: {% image_buster /assets/img/custom_domain.png %}
[8]: {% image_buster /assets/img/custom_domain2.png %}