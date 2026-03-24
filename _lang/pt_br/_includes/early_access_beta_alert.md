{% comment %}
  Alerta de acesso antecipado ou beta. Use para recursos/pontos finais em acesso antecipado ou beta.
  Parâmetros:
  - recurso (obrigatório): O recurso ou assunto, e.g. "Este ponto final", "provisionamento SCIM", "A integração Okta"
  - tipo (opcional): "early_access" (padrão) ou "beta"
{% endcomment %}
{% if include.type == "beta" %}
{% alert important %}
{{ include.feature }} está atualmente em beta. Entre em contato com o gerente da sua conta Braze se estiver interessado em participar da versão beta.
{% endalert %}
{% else %}
{% alert important %}
{{ include.feature }} está atualmente em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar do acesso antecipado.
{% endalert %}
{% endif %}
