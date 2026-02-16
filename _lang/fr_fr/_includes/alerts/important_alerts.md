{% if include.alert == "Shopify deprecation" %}

{% alert important %}
Une [nouvelle version de l'intégration Shopify]({{site.baseurl}}/partners/shopify/#new-shopify-integration) sera publiée par phases à partir d'avril 2025. Les phases seront basées sur le type de boutique Shopify et l'ID externe utilisé pour configurer l'intégration initiale. <br><br>**L'ancienne version de l'intégration ne sera plus disponible après le 28 août 2025. Mettez à jour la nouvelle version avant cette date pour continuer à utiliser l'intégration sans problème.**
{% endalert %}

{% endif %}

{% if include.alert == 'Web push private browsing' %}

{% alert important %}
Les fenêtres de navigation privée ne prennent pas en charge le push web.
{% endalert %}

{% endif %}

{% if include.alert == 'BCC address billable emails' %}

{% alert important %}
L'ajout d'une adresse CCI à votre campagne ou Canvas a pour effet de doubler le nombre d'e-mails facturables pour la campagne ou le composant Canvas, puisque Braze envoie un message à votre utilisateur et un autre à votre adresse CCI.
{% endalert %}

{% endif %}

{% if include.alert == 'Android notification priority' %}

{% alert important %}
Le paramètre Priorité d'affichage des notifications n'est plus utilisé sur les appareils fonctionnant sous Android O ou une version ultérieure. Sur ces appareils, définissez la priorité par le biais de la [configuration du canal de notification.](https://developer.android.com/training/notify-user/channels#importance)
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
Les plans de suppression progressive de l'événement d'achat seront annoncés en 2026. L'événement d'achat sera finalement remplacé par de nouveaux [événements recommandés pour le commerce électronique]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/), qui s'accompagneront de fonctionnalités améliorées en matière de segmentation, de rapports, d'analyse/analyse, etc. Cependant, les nouveaux événements eCommerce ne prendront pas en charge les fonctionnalités existantes liées à l'événement d'achat, telles que la valeur à vie (LTV) ou les rapports sur les chiffres d'affaires dans les Canvases ou les campagnes. Pour une liste complète des fonctionnalités liées aux événements d'achat, reportez-vous à la section [Enregistrement des événements d'achat.]({{site.baseurl}}/user_guide/data/activation/custom_data/purchase_events/#logging-purchase-events)
{% endalert %}

{% endif %}

{% if include.alert == 'Purchase event deprecation for eCommerce filters' %}

{% alert important %}
Les plans de suppression progressive de l'événement d'achat seront annoncés en 2026. L'événement d'achat sera finalement remplacé par de nouveaux [événements recommandés pour le commerce électronique]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/), qui s'accompagneront de fonctionnalités améliorées en matière de segmentation, de rapports, d'analyse/analyse, etc. Dans ce cas, les filtres de segmentation ne s'afficheront plus sous le comportement d'achat. Pour obtenir une liste complète des événements d'achat, reportez-vous à la section [Enregistrement des événements d'achat]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/#logging-purchase-events).
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
Si vous participez à l'accès anticipé à Canvas Context, les propriétés d'entrée de Canvas font partie des variables de contexte de Canvas. Cela signifie que `canvas_entry_properties` est maintenant référencé comme `context`. Chaque variable de contexte comprend un nom, un type de données et une valeur qui peut inclure Liquid. Actuellement, `canvas_entry_properties` est toujours rétrocompatible. Pour plus de détails, reportez-vous à la section [Objet des propriétés d'entrée du]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/) [contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#how-it-works) et du [canvas]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/).
{% endalert %}

{% endif %}

{% if include.alert == 'time filter types' %}

{% alert important %}
**Choix entre les types de filtres "Jour de l'année" et "Heure" :** Lorsque vous filtrez des variables contextuelles contenant des dates, choisissez le type de comparaison approprié selon que la date se répète ou non chaque année :

- **Utilisez "Jour de l'année"** lorsque la date se répète chaque année (par exemple, les anniversaires, les fêtes comme Noël). Ce type de comparaison calcule sur la base du jour de l'année (1-365/366), sans tenir compte de l'année.
- **Utilisez "Heure"** lorsque la date est une date absolue qui ne se répète pas (par exemple, les dates de fin de contrat, les dates de rendez-vous ou les dates de renouvellement d'abonnement). Ce type de comparaison calcule sur la base de l'horodatage complet, y compris l'année.

L'utilisation de "Jour de l'année" pour les dates absolues peut produire des résultats incorrects ou inattendus, car le calcul ne tient pas compte de l'année. Par exemple, si vous comparez la date de fin d'un contrat futur en avril pour déterminer si elle se situe dans les 63 jours, l'utilisation de "Jour de l'année" risque de ne pas correspondre aux dates car elle ne compare que les nombres de jours (119 contre 359) sans tenir compte du fait que le mois d'avril est en réalité dans 188 jours.

**Ligne directrice générale**: La date se répète-t-elle chaque année ? **Oui** → Utilisez "Jour de l'année". **Non** → Utilisez "Temps".
{% endalert %}

{% endif %}
