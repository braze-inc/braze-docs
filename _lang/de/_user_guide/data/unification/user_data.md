---
nav_title: Nutzerdaten
article_title: Nutzerdaten in Braze
page_order: 3.5
layout: dev_guide
guide_top_header: "Nutzerdaten in Braze"
guide_top_text: "Bevor Sie Ihre Braze-Implementierung abschließen, sollten Sie ein Gespräch zwischen Ihrem Marketing-Team und Ihrem Entwicklungsteam über Ihre Marketingziele führen. Es ist sinnvoll, diese Ziele zu berücksichtigen und davon ausgehend zu entscheiden, welche Daten getrackt werden sollen und wie diese Daten mit Braze getrackt werden."

page_type: landing
description: "Auf dieser Landing-Page finden Sie Artikel zur Datenerfassung von Nutzer:innen. Hier finden Sie Ressourcen zu Archivierungsdefinitionen, zum Importieren von Nutzer:innen, zum Nutzerprofil-Lebenszyklus, zu Anwendungsfällen, Best Practices und mehr."

guide_featured_title: "Abschnittsartikel"
guide_featured_list:
  - name: SDK-Datenerfassung
    link: /docs/user_guide/data/unification/user_data/sdk_data_collection/
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: Nutzerprofil-Lebenszyklus
    link: /docs/user_guide/data/unification/user_data/user_profile_lifecycle/
    image: /assets/img/braze_icons/refresh-ccw-05.svg
  - name: Best Practices für die Datenerfassung
    link: /docs/user_guide/data/unification/user_data/best_practices/
    image: /assets/img/braze_icons/thumbs-up.svg
  - name: Anwendungsfall-Beispiel für die Datenerfassung
    link: /docs/user_guide/data/unification/user_data/collection_use_case/
    image: /assets/img/braze_icons/data.svg
  - name: Nutzer:innen importieren
    link: /docs/user_guide/data/unification/user_data/import_users/
    image: /assets/img/braze_icons/users-01.svg
  - name: Nutzer:innen löschen
    link: /docs/user_guide/data/unification/user_data/delete_users/
    image: /assets/img/braze_icons/edit-05.svg
  - name: Anonyme Nutzer:innen
    link: /docs/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users/
    image: /assets/img/braze_icons/user-circle.svg
  - name: Sprachcodes für Nutzer:innen
    link: /docs/user_guide/data/unification/user_data/language_codes/
    image: /assets/img/braze_icons/globe-04.svg
---

<br>

{% alert important %}
Braze sperrt Nutzer:innen („Dummy-Nutzer:innen") mit mehr als 5 Millionen Sitzungen und nimmt deren SDK-Ereignisse nicht mehr auf, da diese in der Regel das Ergebnis einer fehlerhaften Integration sind. Wenn Sie feststellen, dass dies bei einer legitimen Nutzerin oder einem legitimen Nutzer passiert ist, kontaktieren Sie Ihren Braze Account Manager.
{% endalert %}

<br>