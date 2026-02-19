{% comment %}
  Acceso anticipado o alerta beta. Utilízalo para características/puntos finales en acceso anticipado o beta.
  Parámetros:
  - característica (obligatoria): La característica o tema, e.g. "Este punto final", "Aprovisionamiento SCIM", "La integración Okta"
  - tipo (opcional): "early_access" (predeterminado) o "beta"
{% endcomment %}
{% if include.type == "beta" %}
{% alert important %}
{{ include.feature }} está actualmente en fase beta. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en la versión beta.
{% endalert %}
{% else %}
{% alert important %}
{{ include.feature }} está actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en el acceso anticipado.
{% endalert %}
{% endif %}
