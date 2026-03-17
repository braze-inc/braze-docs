{% comment %}
  Descripción del cifrado a nivel de campo del identificador y la información de identificación personal (PII). Úsalo en documentos de cifrado a nivel de campo y notas de lanzamiento.
  Parámetros:
  - enlace (opcional): Si se establece, el «cifrado a nivel de campo del identificador» se incluirá en este enlace (e.g. {{site.baseurl}}/user_guide/analytics/field_level_encryption/).
{% endcomment %}
{% if include.link %}
Mediante el cifrado a nivel de ]({{ site.baseurl }}/{{ include.link }})campo identificador, puedes cifrar fácilmente las direcciones de correo electrónico con AWS Key Management Service (KMS) para minimizar la información de identificación personal (PII) compartida en Braze. La encriptación sustituye los datos sensibles por texto cifrado, que es información encriptada ilegible.
{% else %}
Mediante el cifrado a nivel de campo identificador, puedes cifrar fácilmente las direcciones de correo electrónico con el servicio de administración de claves (KMS) de AWS para minimizar la información de identificación personal (PII) compartida en Braze. La encriptación sustituye los datos sensibles por texto cifrado, que es información encriptada ilegible.
{% endif %}
