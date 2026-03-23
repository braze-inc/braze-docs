{% if include.alert == "Shopify deprecation" %}

{% alert important %}
Une [nouvelle version de l'intégration Shopify]({{site.baseurl}}/partners/shopify/#new-shopify-integration) sera publiée par étapes à partir d'avril 2025. Les phases seront basées sur le type de boutique Shopify et l'ID externe utilisé pour configurer l'intégration initiale. <br><br>**L'ancienne version de l'intégration ne sera plus disponible après le 28 août 2025. Effectuez la mise à jour vers la nouvelle version avant cette date afin de continuer à utiliser l'intégration sans problème.**
{% endalert %}

{% endif %}

{% if include.alert == 'Web push private browsing' %}

{% alert important %}
Les fenêtres de navigation privée ne prennent pas en charge les notifications push Web.
{% endalert %}

{% endif %}

{% if include.alert == 'BCC address billable emails' %}

{% alert important %}
L'ajout d'une adresse CCI à votre campagne ou canvas entraîne le doublement de vos e-mails facturables pour la campagne ou le composant Canvas, car Braze envoie un message à votre utilisateur et un autre à votre adresse CCI.
{% endalert %}

{% endif %}

{% if include.alert == 'Android notification priority' %}

{% alert important %}
Le paramètre Priorité d'affichage des notifications n'est plus utilisé sur les appareils fonctionnant sous Android O ou version ultérieure. Sur ces appareils, définissez la priorité via [la configuration du canal de notification](https://developer.android.com/training/notify-user/channels#importance).
{% endalert %}

{% endif %}

{% if include.alert == "Email via SMS" %}

{% alert important %}
N'envoyez pas d'e-mails transactionnels légalement obligatoires aux passerelles SMS, car il y a de fortes chances que ces e-mails ne soient pas délivrés.
<br><br>
Bien que les e-mails envoyés en utilisant un numéro de téléphone et le domaine de passerelle du fournisseur (connu sous le nom de MM3) puissent être reçus sous forme de message SMS (texte), certains de nos fournisseurs d'e-mail ne prennent pas en charge ce comportement. Par exemple, si vous envoyez un e-mail à un numéro de téléphone T-Mobile (tel que « 9999999999@tmomail.net »), votre message SMS sera envoyé à la personne qui possède ce numéro de téléphone sur le réseau T-Mobile.
<br><br>
Gardez à l'esprit que même si ces e-mails ne sont pas délivrés à la passerelle SMS, ils seront tout de même comptabilisés dans votre facturation d'e-mails. Pour éviter d'envoyer des e-mails à des passerelles non prises en charge, consultez la [liste des noms de domaine des passerelles non prises en charge](https://www.fcc.gov/consumer-governmental-affairs/about-bureau/consumer-policy-division/can-spam/domain-name-downloads).
{% endalert %}

{% endif %}

{% if include.alert == 'SDK auth' %}

{% alert important %}
Pour renforcer la sécurité, nous vous recommandons d'activer notre fonctionnalité d'[authentification SDK]({{site.baseurl}}/developer_guide/authentication/) afin d'empêcher l'usurpation d'identité des utilisateurs.
{% endalert %}

{% endif %}

{% if include.alert == 'Preference Center warning' %}

{% alert important %}
Certains navigateurs, comme les applications Naver Android et iOS, ne prennent pas en charge le centre de préférences de Braze. Si vous pensez que certains de vos utilisateurs utilisent ces navigateurs, envisagez de leur proposer d'autres méthodes pour gérer leurs préférences d'e-mail.
{% endalert %}

{% endif %}

{% if include.alert == 'Purchase event deprecation' %}

{% alert important %}
Les plans visant à supprimer progressivement l'événement d'achat seront annoncés en 2026. L'événement d'achat sera à terme remplacé par de nouveaux [événements recommandés pour le commerce électronique]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/), qui offriront des fonctionnalités améliorées en matière de segmentation, de reporting, d'analytique, et plus encore. Cependant, les nouveaux événements eCommerce ne prendront pas en charge les fonctionnalités existantes liées à l'événement d'achat, telles que la valeur vie client (LTV) ou les rapports sur le chiffre d'affaires dans les Canvas ou les campagnes. Pour obtenir la liste complète des fonctionnalités liées aux événements d'achat, consultez la section [Enregistrement des événements d'achat]({{site.baseurl}}/user_guide/data/activation/custom_data/purchase_events/#logging-purchase-events).
{% endalert %}

{% endif %}

{% if include.alert == 'Purchase event deprecation for eCommerce filters' %}

{% alert important %}
Les plans visant à supprimer progressivement l'événement d'achat seront annoncés en 2026. L'événement d'achat sera à terme remplacé par de nouveaux [événements recommandés pour le commerce électronique]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/), qui offriront des fonctionnalités améliorées en matière de segmentation, de reporting, d'analytique, et plus encore. Lorsque ce sera le cas, les filtres de segment ne s'afficheront plus sous le comportement d'achat. Pour obtenir une liste complète des événements d'achat, reportez-vous à la section [Enregistrement des événements d'achat]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/#logging-purchase-events).
{% endalert %}

{% endif %}

{% if include.alert == 'S3 file bucket export' %}

{% alert important %}
Les fichiers exportés stockés dans les compartiments S3 sont automatiquement supprimés après l'expiration du lien de téléchargement (quatre heures après l'envoi de l'e-mail d'exportation, sauf indication contraire).
{% endalert %} 

{% endif %}

{% if include.alert == 'Shopify customer create' %}

{% alert important %}
L'intégration Shopify prend en charge les webhooks de création et de mise à jour des clients Shopify, qui se trouvent dans vos paramètres de configuration des données. Lorsqu'un profil utilisateur est créé ou mis à jour dans Shopify, un profil utilisateur correspondant est créé ou mis à jour dans Braze. <br><br>Ces actions ne déclenchent pas d'événements personnalisés dans Braze et servent uniquement à [synchroniser les données utilisateur Shopify avec Braze]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview/#how-the-integration-works). Les données synchronisées comprennent les [attributs personnalisés]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#supported-shopify-custom-attributes), les [attributs standard]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#supported-shopify-standard-attributes) et, si cette option est activée dans votre configuration, les [états des groupes d'abonnement]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview#syncing-shopify-email-and-sms-marketing-opt-ins).
{% endalert %}

{% endif %}

{% if include.alert == 'context variable' %}

{% alert important %}
Les propriétés d'entrée Canvas font partie des variables de contexte Canvas. Cela signifie que `canvas_entry_properties` est référencé en tant que `context`. Chaque variable `context` comprend un nom, un type de données et une valeur pouvant inclure du Liquid. Actuellement, `canvas_entry_properties` reste rétrocompatible. Pour plus de détails, consultez les sections [Contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#how-it-works) et [Objet de contexte Canvas]({{site.baseurl}}/api/objects_filters/context_object).
{% endalert %}

{% endif %}

{% if include.alert == 'Braze Agents' %}

{% alert important %}
Ce partenaire n'apparaît sur votre page **Partenaires technologiques** que si vous avez activé [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/). Pour obtenir de l'aide pour démarrer, contactez votre Customer Success Manager.
{% endalert %}

{% endif %}

{% if include.alert == 'time filter types' %}

{% alert important %}
**Choix entre les types de filtre « Jour de l'année » et « Heure »** : lorsque vous filtrez des variables de contexte contenant des dates, sélectionnez le type de comparaison approprié selon que la date se répète chaque année ou non :

- **Utilisez « Jour de l'année »** lorsque la date se répète chaque année (par exemple, les anniversaires, les dates commémoratives ou les fêtes comme Noël). Ce type de comparaison se base sur le jour de l'année (1-365/366), sans tenir compte de l'année.
- **Utilisez « Heure »** lorsque la date est absolue et ne se répète pas (par exemple, les dates de fin de contrat, les dates de rendez-vous ou les dates de renouvellement d'abonnement). Ce type de comparaison se base sur l'horodatage complet, année incluse.

L'utilisation de « Jour de l'année » pour des dates absolues peut produire des résultats incorrects ou inattendus, car le calcul ignore la composante année. Par exemple, si vous comparez une date de fin de contrat en avril pour déterminer si elle se situe dans les 63 prochains jours, « Jour de l'année » peut générer des correspondances erronées, car seuls les numéros de jour sont comparés (119 contre 359) sans tenir compte du fait qu'avril est en réalité dans 188 jours.

**Règle générale** : cette date se répète-t-elle chaque année ? **Oui** → Utilisez « Jour de l'année ». **Non** → Utilisez « Heure ».
{% endalert %}

{% endif %}

{% if include.alert == 'granular permissions ea' %}

{% alert important %}
Les autorisations granulaires sont actuellement en accès anticipé. Lorsque la migration sera planifiée pour votre société, vos administrateurs Braze recevront des e-mails et des bannières dans le tableau de bord les informant de la [migration des autorisations granulaires]({{site.baseurl}}/granular_permissions_migration/).
{% endalert %}

{% endif %}

{% if include.alert == 'Shopify cart token alias' %}

{% alert important %}
Pour cette intégration, l'alias d'utilisateur doit respecter le format suivant afin que Braze puisse associer les webhooks au profil utilisateur correspondant :<br><br>
- `alias_label` : `shopify_cart_${cartToken}`
- `alias_name` : `shopify_cart_token`
{% endalert %}

{% endif %}