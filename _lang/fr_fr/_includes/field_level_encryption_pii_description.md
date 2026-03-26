{% comment %}
  Description du chiffrement au niveau du champ d'identifiant et des informations personnelles identifiables. Veuillez vous référer au document sur le chiffrement au niveau du champ et aux notes de mise à jour.
  Paramètres :
  - lien (facultatif) : Si cette option est activée, le « chiffrement au niveau du champ d'identifiant » sera intégré dans ce lien (e.g. {{site.baseurl}}/user_guide/analytics/field_level_encryption/).
{% endcomment %}
{% if include.link %}
Grâce au chiffrement au niveau du champ]({{ site.baseurl }}/{{ include.link }}) d'identifiant, vous pouvez de façon fluide chiffrer les adresses e-mail avec AWS Key Management Service (KMS) afin de minimiser les informations personnelles identifiables (PII) partagées dans Braze. Le chiffrement remplace les données sensibles par du texte chiffré, c'est-à-dire des informations cryptées et non lisibles.
{% else %}
Grâce au chiffrement au niveau du champ d'identification, vous pouvez chiffrer de façon fluide/sans heurts les adresses e-mail avec AWS Key Management Service (KMS) afin de minimiser les informations personnelles identifiables (PII) partagées dans Braze. Le chiffrement remplace les données sensibles par du texte chiffré, c'est-à-dire des informations cryptées et non lisibles.
{% endif %}
