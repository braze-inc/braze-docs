---
nav_title: Instances de Braze
article_title: Instances de Braze
page_order: 0
page_type: reference
description: "Cet article de référence répertorie les URL de tableau de bord et les terminaux pour les instances de Braze disponibles."

---

# Instances de Braze

> L’instance Braze est l’URL requise pour se connecter à Braze, accéder à l’API et intégrer votre SDK.

Braze gère plusieurs instances différentes pour notre tableau de bord et nos endpoints REST et SDK, que nous appelons des « clusters ». Le gestionnaire d’onboarding de Braze vous indiquera le cluster sur lequel vous vous trouvez.

La connexion à [dashboard.braze.com](https://dashboard.braze.com) vous enverra automatiquement à l’adresse de cluster correcte.

|Instance|URL|Endpoint REST|Endpoint SDK|
|---|---|---|
|US-01| `https://dashboard-01.braze.com` | `https://rest.iad-01.braze.com` | `sdk.iad-01.braze.com` |
|US-02| `https://dashboard-02.braze.com` | `https://rest.iad-02.braze.com` | `sdk.iad-02.braze.com` |
|US-03| `https://dashboard-03.braze.com` | `https://rest.iad-03.braze.com` | `sdk.iad-03.braze.com` |
|US-04| `https://dashboard-04.braze.com` | `https://rest.iad-04.braze.com` | `sdk.iad-04.braze.com` |
|US-05| `https://dashboard-05.braze.com` | `https://rest.iad-05.braze.com` | `sdk.iad-05.braze.com` |
|US-06| `https://dashboard-06.braze.com` | `https://rest.iad-06.braze.com` | `sdk.iad-06.braze.com` |
|US-08| `https://dashboard-08.braze.com` | `https://rest.iad-08.braze.com` | `sdk.iad-08.braze.com` |
|EU-01| `https://dashboard-01.braze.eu` | `https://rest.fra-01.braze.eu` | `sdk.fra-01.braze.eu` |
|EU-02| `https://dashboard-02.braze.eu` | `https://rest.fra-02.braze.eu` | `sdk.fra-02.braze.eu` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert important %}
Lors de l’intégration de votre SDK, utilisez l’endpoint SDK. Lorsque vous passez des appels vers notre API REST, utilisez l’endpoint REST.
{% endalert %}
