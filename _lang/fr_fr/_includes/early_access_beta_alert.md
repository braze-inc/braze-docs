{% comment %}
  Accès anticipé ou alerte bêta. À utiliser pour les fonctionnalités/endpoints en accès anticipé ou en version bêta.
  Paramètres :
  - fonctionnalité (obligatoire) : La fonctionnalité ou le sujet, e.g. « Ce endpoint », « Provisioning SCIM », « L'intégration Okta »
  - type (facultatif) :"early_access"(par défaut) ou « bêta »
{% endcomment %}
{% if include.type == "beta" %}
{% alert important %}
{{ include.feature }} est actuellement en version bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à la bêta.
{% endalert %}
{% else %}
{% alert important %}
{{ include.feature }} est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}
{% endif %}
