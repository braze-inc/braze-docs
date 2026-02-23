{% comment %}
  Early access or beta alert. Use for features/endpoints in early access or beta.
  Parameters:
  - feature (required): The feature or subject, e.g. "This endpoint", "SCIM provisioning", "The Okta integration"
  - type (optional): "early_access" (default) or "beta"
{% endcomment %}
{% if include.type == "beta" %}
{% alert important %}
{{ include.feature }} is currently in beta. Contact your Braze account manager if you're interested in participating in the beta.
{% endalert %}
{% else %}
{% alert important %}
{{ include.feature }} is currently in early access. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}
{% endif %}
