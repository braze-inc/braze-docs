{% comment %}
  얼리 액세스 또는 베타 알림. 얼리 액세스 또는 베타 버전의 기능/엔드포인트에 사용하세요.
  매개변수:
  - 기능(필수): 기능 또는 주제, e.g. "이 엔드포인트", "SCIM 프로비저닝", "Okta 통합"
  - 유형(선택 사항): "early_access" (기본값) 또는 "베타"
{% endcomment %}
{% if include.type == "beta" %}
{% alert important %}
{{ include.feature }} 는 현재 베타 버전입니다. 베타 참여에 관심이 있으시면 Braze 계정 관리자에게 문의하세요.
{% endalert %}
{% else %}
{% alert important %}
{{ include.feature }} 는 현재 얼리 액세스 중입니다. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}
{% endif %}
