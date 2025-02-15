---
nav_title: "Points d'extrémité de l'API et du SDK"
article_title: "Points d'extrémité de l'API et du SDK"
page_order: 1
page_type: reference
description: "Cet article de référence répertorie les URL du tableau de bord, les endpoints de l’API et les endpoints du SDK pour les instances Braze disponibles."

---

# Points d'extrémité de l'API et du SDK

> Votre instance Braze détermine l'URL nécessaire pour se connecter à Braze, accéder à l'API et intégrer votre SDK. Pour en savoir plus sur le SDK de Braze, consultez notre cours d'apprentissage Braze, [Braze 101][1].

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
|US-07| `https://dashboard-07.braze.com` | `https://rest.iad-07.braze.com` | `sdk.iad-07.braze.com` |
|US-08| `https://dashboard-08.braze.com` | `https://rest.iad-08.braze.com` | `sdk.iad-08.braze.com` |
|EU-01| `https://dashboard-01.braze.eu` | `https://rest.fra-01.braze.eu` | `sdk.fra-01.braze.eu` |
|EU-02| `https://dashboard-02.braze.eu` | `https://rest.fra-02.braze.eu` | `sdk.fra-02.braze.eu` |
|AU-01| `https://dashboard.au-01.braze.com`| `https://rest.au-01.braze.com` | `sdk.au-01.braze.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
Lors de l’intégration de votre SDK, utilisez l’endpoint SDK. Lorsque vous passez des appels vers notre API REST, utilisez l’endpoint REST.
{% endalert %}

Pour plus de détails sur l'accès à l'API, consultez l'[article de présentation de l'API][2]. 


[1]: https://learning.braze.com/braze-101
[2]: {{site.baseurl}}/api/basics/