---
nav_title: "Anonyme Nutzer:innen"
article_title: Anonyme Benutzer
page_order: 0
page_type: reference
description: "Dieser Artikel bietet eine Übersicht über anonyme Nutzer:innen und User-Aliasing. Er erläutert ihre Bedeutung und wie Sie sie in Ihren Nachrichten nutzen können."

---

# Anonyme Nutzer:innen

> Nutzer:innen werden als anonyme Nutzer:innen erkannt, die Ihre Website oder Anwendung besuchen, ohne sich anzumelden, wie ein Gast. Diese Nutzer:innen verfügen nicht über `external_ids`, die zum Update von Nutzerprofilen mit der Braze API verwendet werden, aber sie verfügen dennoch über [Datenpunkte]({{site.baseurl}}/user_guide/data/data_points/), die ihnen zugeordnet sind und die Sie in Ihren Segmenten gezielt einsetzen können.

Wenn ein anonymer Nutzer:innen Ihre Website oder Anwendung besucht, erstellt das Braze SDK ein "anonymes" Nutzerprofil und ordnet ihn diesem zu. Während der Benutzer surft, erfasst das SDK automatisch Daten für sein anonymes Benutzerprofil, z. B. Nutzungsinformationen, Geräteinformationen und mehr, wenn Sie angepasste Attribute und angepasste Events eingerichtet haben.

Sie können mit gefangenen anonymen Nutzer:innen Folgendes tun:

- Nachrichten an Nutzer:innen, bevor sie sich anmelden
- Erfassen Sie das Profil eines Nutzers, bevor er sich anmeldet, damit Ihnen keine relevanten Daten entgehen.
- Fördern Sie die Vervollständigung des Profils mit einer Nachricht, wenn ein Nutzer:innen sein Profil nur teilweise vervollständigt.
- Vervollständigen Sie das Profil eines Nutzers, wenn er sich anmeldet, damit Sie Messaging auf anderen Plattformen abbrechen können (z.B. keine Nachricht "Kostenloser Versand bei der 1\. App-Bestellung" senden, wenn der Nutzer bereits App-Bestellungen getätigt hat)
- Engagieren Sie Nutzer:innen, die eine Absicht zum Ausstieg zeigen, indem Sie sie ermutigen, ein Profil zu erstellen, ihren Warenkorb zu überprüfen oder eine andere Aktion durchzuführen.

## Funktionsweise

{% multi_lang_include anonymous_users/about_anonymous_users.md section='user_guide' %}

## User-Aliasing für Nutzer:innen zuweisen

{% multi_lang_include anonymous_users/about_user_aliases.md section='user_guide' %}

## Zusammenführung anonymer Nutzer:innen  

Manchmal handelt es sich bei anonymen Nutzerprofilen um Duplikate, die die gleiche Telefonnummer oder E-Mail Adresse wie andere Nutzer:in haben. Eines der Duplikate kann sogar ein identifiziertes Nutzerprofil sein. Diese Duplikate können mit [POST zu einem Nutzerprofil zusammengeführt werden: Zusammenführen Nutzer:innen Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) oder eines der Zusammenführungs-Tools auf der Braze-Plattform, wie z.B. die [regelbasierte Zusammenführung]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#rules-based-merging).

## Anwendungsfälle

### Targeting anonymer Nutzer:innen in Ihrem Segment

Da anonyme Nutzer:innen keine `external_id` haben, können Sie sie mit dem Filter für die Segmentierung **Externe ID ist leer**" in großen Mengen targetieren. Um die Genauigkeit zu erhöhen, können Sie den anonymen Nutzer:innen, die Sie targetieren möchten, ein angepasstes Attribut hinzufügen und danach filtern.

Nehmen wir an, Sie weisen das angepasste Attribut "is_lead_profile" jedem anonymen Nutzerprofil zu. Sie können diese Profile mit einem oder beiden Filtern targeting:

- **Externe Nutzer-ID ist leer**
- "is_lead_profile" **ist wahr**

![Segmente filtern nach einer leeren externen ID eines Nutzers und einem echten "is_lead_profile" angepassten Attribut.]({% image_buster /assets/img/getting_started/anonymous_users.png %})

### Erfassen von Kassendaten eines anonymen Nutzer:in

Sie können die Daten eines anonymen Nutzers (oder Gastbesuchers) an der Kasse erfassen, indem Sie während des Bestellvorgangs ein User-Aliasing-Profil erstellen. Wenn ein anonymer Nutzer über ein Web-Capture-Formular auscheckt, lassen Sie einen API-Aufruf triggern, um ein User-Aliasing-Profil zu erstellen und ein Kauf-Event zu protokollieren. Anschließend können Sie das erstellte Nutzerprofil über die Braze API aktualisieren.

Hier ist ein Beispiel für eine Nutzlast, die generiert wird, wenn das Web-Capture-Formular übermittelt wird:

{% raw %}
```json
{
    "purchase":[
        {
            "user_alias": {"alias_name": "Joedoe", "alias_label": "full_name"},
            "app_id": "11dk3k9d-2183-3948-k02b-kw3938109k12od",
            "product_id": "jacket",
            "currency": "USD",
            "price": 80.00,
            "time": "2025-01-05T19:20:30+01:00",
            "properties": {
                "color": "brown",
                "monogram": "ABC",
                "checkout_duration": 180,
                "size": "Small",
                "brand": "Natural Essence"
            }
        }
    ]
}
```
{% endraw %}

