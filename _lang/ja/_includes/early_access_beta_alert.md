{% comment %}
  アーリーアクセスまたはベータ版警告。アーリーアクセスやベータ版の機能/エンドポイントに使用する。
  パラメータだ：
  - 機能（必須）である：その特徴や対象は、e.g 。"このエンドポイント"、"SCIMプロビジョニング"、"Okta統合"
  - type（オプション）： "early_access" (デフォルト）または "beta"
{% endcomment %}
{% if include.type == "beta" %}
{% alert important %}
{{ include.feature }} は現在ベータ版である。ベータ版への参加に興味がある場合は、Brazeのアカウント・マネージャーに連絡を。
{% endalert %}
{% else %}
{% alert important %}
{{ include.feature }} は現在早期アクセス中である。早期アクセスへの参加に興味がある方は、Brazeのアカウントマネージャーに連絡を。
{% endalert %}
{% endif %}
