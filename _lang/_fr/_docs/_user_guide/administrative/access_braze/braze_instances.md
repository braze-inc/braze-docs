---
nav_title: Instances de Braze
article_title: Instances de Braze
page_order: 0
page_type: Référence
description: "Cet article de référence liste les URL et les terminaux du tableau de bord pour les instances Braze disponibles."
---

# Instances de Braze

_Il s'agit de l'URL que les utilisateurs de Braze ont besoin pour se connecter à Braze, accéder à l'API et intégrer votre SDK_

Braze gère un certain nombre d'instances différentes pour notre tableau de bord, notre SDK et nos terminaux REST, que nous appelons "clusters". Votre gestionnaire d'intégration de Braze vous indiquera le cluster sur lequel vous êtes.

La connexion à [dashboard.braze.com](https://dashboard.braze.com) vous enverra automatiquement à la bonne adresse du cluster.

| Instance | URL                            | Point de terminaison REST     | Point de terminaison SDK     |
| -------- | ------------------------------ | ----------------------------- | ---------------------------- |
| US-01    | https://dashboard-01.braze.com | https://rest.iad-01.braze.com | https://sdk.iad-01.braze.com |
| US-02    | https://dashboard-02.braze.com | https://rest.iad-02.braze.com | https://sdk.iad-02.braze.com |
| US-03    | https://dashboard-03.braze.com | https://rest.iad-03.braze.com | https://sdk.iad-03.braze.com |
| US-04    | https://dashboard-04.braze.com | https://rest.iad-04.braze.com | https://sdk.iad-04.braze.com |
| US-05    | https://dashboard-05.braze.com | https://rest.iad-05.braze.com | https://sdk.iad-05.braze.com |
| US-06    | https://dashboard-06.braze.com | https://rest.iad-06.braze.com | https://sdk.iad-06.braze.com |
| US-08    | https://dashboard-08.braze.com | https://rest.iad-08.braze.com | https://sdk.iad-08.braze.com |
| EU-01    | https://dashboard-01.braze.eu  | https://rest.fra-01.braze.eu  | https://sdk.fra-01.braze.eu  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert important %}
Lors de l'intégration de votre SDK, utilisez le "point de terminaison SDK". Lorsque vous passez des appels à notre API REST, utilisez le "Point de terminaison REST".
{% endalert %}
