{% if include.alert == "Shopify deprecation" %}

{% alert important %}
Une [nouvelle version de l'intégration Shopify]({{site.baseurl}}/partners/shopify/#new-shopify-integration) sera publiée par phases à partir d'avril 2025. Les phases seront basées sur le type de boutique Shopify et l'ID externe utilisé pour configurer l'intégration initiale. <br><br>**L'ancienne version de l'intégration ne sera plus disponible après le 28 août 2025. Mettez à jour la nouvelle version avant cette date pour continuer à utiliser l'intégration sans problème.**
{% endalert %}

{% endif %}

{% if include.alert == "Email via SMS" %}

{% alert important %}
N'envoyez pas d'e-mails transactionnels légalement obligatoires aux passerelles SMS, car il y a de fortes chances que ces e-mails ne soient pas délivrés.
<br><br>
Bien que les e-mails que vous envoyez en utilisant un numéro de téléphone et le domaine de passerelle du fournisseur (connu sous le nom de MM3) puissent entraîner la réception de l'e-mail sous forme de message SMS (texte), certains de nos fournisseurs d'e-mail ne prennent pas en charge ce comportement. Par exemple, si vous envoyez un e-mail à un numéro de téléphone T-Mobile (tel que "9999999999@tmomail.net"), votre message SMS sera envoyé à la personne qui possède ce numéro de téléphone sur le réseau T-Mobile.
<br><br>
Gardez à l'esprit que même si ces e-mails ne sont pas délivrés à la passerelle SMS, ils seront tout de même pris en compte dans votre facturation d'e-mails. Pour éviter d'envoyer des e-mails à des passerelles non prises en charge, consultez la [liste des noms de domaine des passerelles non prises en charge](https://www.fcc.gov/consumer-governmental-affairs/about-bureau/consumer-policy-division/can-spam/domain-name-downloads).
{% endalert %}

{% endif %}

{% if include.alert == 'SDK auth' %}

{% alert important %}
Pour plus de sécurité, nous vous recommandons d'ajouter notre fonctionnalité d'[authentification SDK]({{site.baseurl}}/developer_guide/authentication/) afin d'empêcher l'usurpation d'identité des utilisateurs.
{% endalert %}

{% endif %}

{% if include.alert == 'Preference Center warning' %}

{% alert important %}
Certains navigateurs, comme les applications Naver Android et iOS, ne prennent pas en charge le centre de préférences de Braze. Si vous pensez que certains de vos utilisateurs utilisent ces navigateurs, envisagez de leur proposer d'autres méthodes pour gérer leurs préférences en matière d'e-mail.
{% endalert %}

{% endif %}

{% if include.alert == 'Purchase event deprecation' %}

{% alert important %}
Les plans de suppression progressive de l'événement d'achat seront annoncés à la fin de l'année 2025. À long terme, l'événement d'achat sera remplacé par de nouveaux [événements recommandés par l'eCommerce]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/), qui s'accompagneront de fonctionnalités améliorées en matière de segmentation, de rapports, d'analyse/analyse, etc. Cependant, les nouveaux événements eCommerce ne prendront pas en charge les fonctionnalités existantes liées à l'événement d'achat, telles que la valeur à vie (LTV) ou les rapports sur les chiffres d'affaires dans les Canvases ou les campagnes. Pour obtenir une liste complète des fonctionnalités liées aux événements d'achat, reportez-vous à la section [Enregistrement des événements d'achat]({{site.baseurl}}/user_guide/data/activation/custom_data/purchase_events/#logging-purchase-events).
{% endalert %}

{% endif %}

{% if include.alert == 'S3 file bucket export' %}

{% alert important %}
Les fichiers d'exportation stockés dans les compartiments S3 sont automatiquement supprimés après l'expiration du lien de téléchargement (quatre heures à compter de l'envoi de l'e-mail d'exportation, sauf indication contraire).
{% endalert %} 

{% endif %}

{% if include.alert == 'Shopify customer create' %}

{% alert important %}
L'intégration de Shopify prend en charge les webhooks de création et de mise à jour de clients de Shopify, qui sont situés dans vos paramètres de configuration des données. Lorsqu'un profil utilisateur est créé ou mis à jour dans Shopify, un profil utilisateur correspondant sera créé ou mis à jour dans Braze. <br><br>Ces actions ne déclenchent pas d'événements personnalisés dans Braze et servent uniquement à [synchroniser les données des utilisateurs de Shopify avec Braze]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview/#how-the-integration-works). Les données synchronisées comprennent les [attributs personnalisés]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#supported-shopify-custom-attributes), les [attributs standard]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#supported-shopify-standard-attributes) et, si cette fonction est activée dans votre configuration, les [états des groupes d'abonnement]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview#syncing-shopify-email-and-sms-marketing-opt-ins).
{% endalert %}

{% endif %}

{% if include.alert == 'context variable' %}

{% alert important %}
Si vous participez à l'accès anticipé à Canvas Context, les propriétés d'entrée de Canvas font partie des variables de contexte de Canvas. Cela signifie que `canvas_entry_properties` est maintenant référencé comme `context`. Chaque variable de contexte comprend un nom, un type de données et une valeur qui peut inclure Liquid. Actuellement, `canvas_entry_properties` est toujours rétrocompatible. Pour plus de détails, voir [Contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#how-it-works) et [objet contextuel Canvas]({{site.baseurl}}/api/objects_filters/context_object).
{% endalert %}

{% endif %}