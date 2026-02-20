{% comment %}
  Description du cryptage au niveau du champ d'identification et des IIP. Utilisation dans la documentation sur le chiffrement au niveau du champ et dans les notes de mise à jour.
  Paramètres :
  - lien (facultatif) : S'il est défini, le "chiffrement au niveau du champ d'identification" sera intégré dans ce lien (e.g. {{site.baseurl}}/user_guide/analytics/field_level_encryption/).
{% endcomment %}
{% if include.link %}
À l'aide du chiffrement au niveau du champ [identifier]({{ site.baseurl }}/{{ include.link }}), vous pouvez chiffrer de façon fluide/sansans heurts les adresses e-mail avec AWS Key Management Service (KMS) pour minimiser les informations personnelles identifiables (PII) partagées dans Braze. Le chiffrement remplace les données sensibles par du texte chiffré, c'est-à-dire des informations cryptées et non lisibles.
{% else %}
Grâce au chiffrement au niveau du champ d'identification, vous pouvez chiffrer de façon fluide/sans heurts les adresses e-mail avec AWS Key Management Service (KMS) afin de minimiser les informations personnelles identifiables (PII) partagées dans Braze. Le chiffrement remplace les données sensibles par du texte chiffré, c'est-à-dire des informations cryptées et non lisibles.
{% endif %}
