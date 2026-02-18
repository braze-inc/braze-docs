{% comment %}
  Descripción del cifrado a nivel de campo identificador y PII. Utilízalo en el documento de encriptación a nivel de campo y en las notas de publicación.
  Parámetros:
  - enlace (opcional): Si se establece, la "encriptación a nivel de campo del identificador" se envolverá en este enlace (e.g. {{site.baseurl}}/user_guide/analytics/field_level_encryption/).
{% endcomment %}
{% if include.link %}
Utilizando [cifrado a nivel de campo identificador]({{ site.baseurl }}/{{ include.link }}), puedes cifrar fácilmente las direcciones de correo electrónico con el servicio de administración de claves (KMS) de AWS para minimizar la información de identificación personal (PII) compartida en Braze. La encriptación sustituye los datos sensibles por texto cifrado, que es información encriptada ilegible.
{% else %}
Mediante el cifrado a nivel de campo identificador, puedes cifrar fácilmente las direcciones de correo electrónico con el servicio de administración de claves (KMS) de AWS para minimizar la información de identificación personal (PII) compartida en Braze. La encriptación sustituye los datos sensibles por texto cifrado, que es información encriptada ilegible.
{% endif %}
