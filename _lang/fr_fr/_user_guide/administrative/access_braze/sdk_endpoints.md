---
nav_title: "Points d'extrémité de l'API et du SDK"
article_title: "Points d'extrémité de l'API et du SDK"
page_order: 1
page_type: reference
description: "Cet article de référence répertorie les URL du tableau de bord, les points d'extrémité de l'API et les points d'extrémité du SDK pour les instances Braze disponibles."

---

# Points d'extrémité de l'API et du SDK

> Votre instance Braze détermine l'URL nécessaire pour se connecter à Braze, accéder à l'API et intégrer votre SDK. Pour en savoir plus sur le SDK de Braze, consultez notre cours d'apprentissage Braze, [Braze 101](https://learning.braze.com/braze-101).

Braze gère un certain nombre d'instances différentes pour notre tableau de bord, notre SDK et nos endpoints REST, que nous appelons "clusters". Votre gestionnaire d'onboarding de Braze vous indiquera sur quel cluster vous vous trouvez.

En vous connectant à [dashboard.braze.com](https://dashboard.braze.com) vous enverra automatiquement à la bonne adresse du cluster.

{% multi_lang_include data_centers.md datacenters='instances' %}

{% alert important %}
Lors de l'intégration de votre SDK, utilisez l'endpoint SDK. Lorsque vous faites appel à notre API REST, utilisez l'endpoint REST.
{% endalert %}

Pour plus de détails sur l'accès à l'API, consultez notre [article sur l'aperçu de l'API.]({{site.baseurl}}/api/basics/) 
