{% comment %}
  Beschreibung der Verschlüsselung auf Feldebene für Bezeichner und PII. Bitte beachten Sie die Dokumentation und die Versionshinweise zur Feldverschlüsselung.
  Parameter:
  - Link (optional): Wenn diese Option aktiviert ist, wird die „Bezeichner-Feldverschlüsselung“ in diesen Link eingebunden.e.g {{site.baseurl}}/user_guide/analytics/field_level_encryption/).
{% endcomment %}
{% if include.link %}
Mit der [Bezeichner-Verschlüsselung]({{ site.baseurl }}/{{ include.link }})] können Sie E-Mail-Adressen nahtlos mit AWS Key Management Service (KMS) verschlüsseln, um die Weitergabe personenbezogener Daten (PII) in Braze zu minimieren. Bei der Verschlüsselung werden sensible Daten durch Chiffretext ersetzt, d.h. durch unlesbare verschlüsselte Informationen.
{% else %}
Mit der Verschlüsselung auf Bezeichnerfeld-Ebene können Sie E-Mail-Adressen nahtlos mit dem AWS Key Management Service (KMS) verschlüsseln, um die in Braze freigegebenen personenbezogenen Daten (PII) zu minimieren. Bei der Verschlüsselung werden sensible Daten durch Chiffretext ersetzt, d.h. durch unlesbare verschlüsselte Informationen.
{% endif %}
