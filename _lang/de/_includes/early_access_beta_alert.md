{% comment %}
  Frühzeitiger Zugang oder Beta-Benachrichtigung. Bitte verwenden Sie diese für Features/Endpunkte im Early Access oder in der Beta-Phase.
  Parameter:
  - Feature (erforderlich): Das Feature oder Thema, e.g. „Dieser Endpunkt“, „SCIM-Bereitstellung“, „Die Okta-Integration“
  - Typ (optional):"early_access"(Standard) oder „beta“
{% endcomment %}
{% if include.type == "beta" %}
{% alert important %}
{{ include.feature }} befindet sich derzeit in der Beta-Phase. Wenden Sie sich an Ihre:n Braze-Kundenbetreuer:in, wenn Sie an einer Teilnahme an der Beta interessiert sind.
{% endalert %}
{% else %}
{% alert important %}
{{ include.feature }} befindet sich derzeit im Early Access. Wenden Sie sich an Ihren Braze-Account Manager, wenn Sie sich für die Teilnahme am Early Access interessieren.
{% endalert %}
{% endif %}
