---
nav_title: API und SDK Endpunkte
article_title: API und SDK Endpunkte
page_order: 1
page_type: reference
description: "Dieser Referenzartikel listet die Dashboard-URLs, API-Endpunkte und SDK-Endpunkte für verfügbare Braze-Instanzen auf."

---

# API- und SDK-Endpunkte

> Ihre Braze-Instanz bestimmt die URL, die für die Anmeldung bei Braze, den Zugriff auf die API und die Integration Ihres SDK erforderlich ist. Erfahren Sie mehr über das Braze-SDK in unserem Braze-Lernkurs, [Braze 101][1].

Braze verwaltet eine Reihe verschiedener Instanzen für unser Dashboard, SDK und REST-Endpunkte, die wir „Cluster“ nennen. Ihr:e Braze Onboarding-Manager:in wird Ihnen mitteilen, in welchem Cluster Sie sich befinden.

Wenn Sie sich bei [dashboard.braze.com](https://dashboard.braze.com) anmelden, werden Sie automatisch an die richtige Cluster-Adresse weitergeleitet.

|Instanz|URL|REST-Endpunkt|SDK-Endpunkt|
|---|---|---|
|US-01| `https://dashboard-01.braze.com` | `https://rest.iad-01.braze.com` | `sdk.iad-01.braze.com` |
|US-02| `https://dashboard-02.braze.com` | `https://rest.iad-02.braze.com` | `sdk.iad-02.braze.com` |
|US-03| `https://dashboard-03.braze.com` | `https://rest.iad-03.braze.com` | `sdk.iad-03.braze.com` |
|US-04| `https://dashboard-04.braze.com` | `https://rest.iad-04.braze.com` | `sdk.iad-04.braze.com` |
|US-05| `https://dashboard-05.braze.com` | `https://rest.iad-05.braze.com` | `sdk.iad-05.braze.com` |
|US-06| `https://dashboard-06.braze.com` | `https://rest.iad-06.braze.com` | `sdk.iad-06.braze.com` |
|US-07| `https://dashboard-07.braze.com` | `https://rest.iad-07.braze.com` | `sdk.iad-07.braze.com` |
|US-08| `https://dashboard-08.braze.com` | `https://rest.iad-08.braze.com` | `sdk.iad-08.braze.com` |
|EU-01| `https://dashboard-01.braze.eu` | `https://rest.fra-01.braze.eu` | `sdk.fra-01.braze.eu` |
|EU-02| `https://dashboard-02.braze.eu` | `https://rest.fra-02.braze.eu` | `sdk.fra-02.braze.eu` |
|AU-01| `https://dashboard.au-01.braze.com`| `https://rest.au-01.braze.com` | `sdk.au-01.braze.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
Wenn Sie Ihr SDK integrieren, verwenden Sie den SDK-Endpunkt. Wenn Sie unsere REST-API aufrufen, verwenden Sie den REST-Endpunkt.
{% endalert %}

Einzelheiten zum Zugriff auf die API finden Sie im Artikel [API-Übersicht][2]. 


[1]: https://learning.braze.com/braze-101
[2]: {{site.baseurl}}/api/basics/