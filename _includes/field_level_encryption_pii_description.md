{% comment %}
  Description of identifier field-level encryption and PII. Use in field-level encryption doc and release notes.
  Parameters:
  - link (optional): If set, "identifier field-level encryption" will be wrapped in this link (e.g. {{site.baseurl}}/user_guide/analytics/field_level_encryption/).
{% endcomment %}
{% if include.link %}
Using [identifier field-level encryption]({{ site.baseurl }}/{{ include.link }}), you can seamlessly encrypt email addresses with AWS Key Management Service (KMS) to minimize personally identifiable information (PII) shared in Braze. Encryption replaces sensitive data with ciphertext, which is unreadable encrypted information.
{% else %}
Using identifier field-level encryption, you can seamlessly encrypt email addresses with AWS Key Management Service (KMS) to minimize personally identifiable information (PII) shared in Braze. Encryption replaces sensitive data with ciphertext, which is unreadable encrypted information.
{% endif %}
