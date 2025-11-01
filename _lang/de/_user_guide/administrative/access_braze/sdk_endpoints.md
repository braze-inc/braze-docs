---
nav_title: API- und SDK-Endpunkte
article_title: API und SDK Endpunkte
page_order: 1
page_type: reference
description: "Dieser Referenzartikel listet die Dashboard-URLs, API-Endpunkte und SDK-Endpunkte für verfügbare Braze-Instanzen auf."

---

# API- und SDK-Endpunkte

> Ihre Braze-Instanz bestimmt die URL, die für die Anmeldung bei Braze, den Zugriff auf die API und die Integration Ihres SDK erforderlich ist. Erfahren Sie mehr über das Braze-SDK in unserem Braze-Lernkurs, [Braze 101](https://learning.braze.com/braze-101).

Braze verwaltet eine Reihe verschiedener Instanzen für unser Dashboard, SDK und REST-Endpunkte, die wir „Cluster“ nennen. Ihr:e Braze Onboarding-Manager:in wird Ihnen mitteilen, in welchem Cluster Sie sich befinden.

Wenn Sie sich bei [dashboard.braze.com](https://dashboard.braze.com) anmelden, werden Sie automatisch an die richtige Cluster-Adresse weitergeleitet.

{% multi_lang_include data_centers.md datacenters='instances' %}

{% alert important %}
Wenn Sie Ihr SDK integrieren, verwenden Sie den SDK-Endpunkt. Wenn Sie unsere REST-API aufrufen, verwenden Sie den REST-Endpunkt.
{% endalert %}

Einzelheiten zum Zugriff auf die API finden Sie in unserem [Artikel zur API-Übersicht]({{site.baseurl}}/api/basics/). 
