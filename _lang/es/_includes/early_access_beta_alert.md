{% comment %}
  Acceso anticipado o alerta beta. Úsalo para características/puntos finales en acceso anticipado o beta.
  Parámetros:
  - característica (obligatoria): La característica o el tema, e.g. «Este punto final», «aprovisionamiento SCIM», «la integración de Okta»
  - tipo (opcional):"early_access"  (predeterminado) o «beta»
{% endcomment %}
{% if include.type == "beta" %}
{% alert important %}
{{ include.feature }} Actualmente se encuentra en fase beta. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en la versión beta.
{% endalert %}
{% else %}
{% alert important %}
{{ include.feature }} Actualmente se encuentra en fase de acceso anticipado. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en el acceso anticipado.
{% endalert %}
{% endif %}
