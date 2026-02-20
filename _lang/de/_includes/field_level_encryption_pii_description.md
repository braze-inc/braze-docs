{% comment %}
  Beschreibung der Verschlüsselung von Bezeichnern auf Feldebene und PII. Verwendung in Verschlüsselungsdokumenten und Versionshinweisen auf Feldebene.
  Parameter:
  - Link (optional): Wenn gesetzt, wird "Bezeichnerfeld-Verschlüsselung" in diesen Link eingepackt (e.g. {{site.baseurl}}/user_guide/analytics/field_level_encryption/).
{% endcomment %}
{% if include.link %}
Mit [identifier field-level encryption]({{ site.baseurl }}/{{ include.link }}) können Sie E-Mail-Adressen nahtlos mit dem AWS Key Management Service (KMS) verschlüsseln, um die in Braze freigegebenen personenbezogenen Daten (PII) zu minimieren. Bei der Verschlüsselung werden sensible Daten durch Chiffretext ersetzt, d.h. durch unlesbare verschlüsselte Informationen.
{% else %}
Mit der Verschlüsselung auf Bezeichnerfeld-Ebene können Sie E-Mail-Adressen nahtlos mit dem AWS Key Management Service (KMS) verschlüsseln, um die in Braze freigegebenen personenbezogenen Daten (PII) zu minimieren. Bei der Verschlüsselung werden sensible Daten durch Chiffretext ersetzt, d.h. durch unlesbare verschlüsselte Informationen.
{% endif %}
