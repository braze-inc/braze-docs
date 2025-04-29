---
nav_title: "Points d'extrémité de l'API et du SDK"
article_title: "Points d'extrémité de l'API et du SDK"
page_order: 1
page_type: reference
description: "Cet article de référence répertorie les URL du tableau de bord, les endpoints de l’API et les endpoints du SDK pour les instances Braze disponibles."

---

# Points d'extrémité de l'API et du SDK

> Votre instance Braze détermine l'URL nécessaire pour se connecter à Braze, accéder à l'API et intégrer votre SDK. Pour en savoir plus sur le SDK de Braze, consultez notre cours d'apprentissage Braze, [Braze 101](https://learning.braze.com/braze-101).

Braze gère plusieurs instances différentes pour notre tableau de bord et nos endpoints REST et SDK, que nous appelons des « clusters ». Le gestionnaire d’onboarding de Braze vous indiquera le cluster sur lequel vous vous trouvez.

La connexion à [dashboard.braze.com](https://dashboard.braze.com) vous enverra automatiquement à l’adresse de cluster correcte.

{% multi_lang_include data_centers.md datacenters='instances' %}

{% alert important %}
Lors de l’intégration de votre SDK, utilisez l’endpoint SDK. Lorsque vous passez des appels vers notre API REST, utilisez l’endpoint REST.
{% endalert %}

Pour plus de détails sur l'accès à l'API, consultez notre [article sur l'aperçu de l'API.]({{site.baseurl}}/api/basics/) 
