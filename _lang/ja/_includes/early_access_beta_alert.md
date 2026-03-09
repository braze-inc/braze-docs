{% comment %}
  早期アクセスまたはベータ版のお知らせだ。早期アクセスまたはベータ版の機能／エンドポイントに使用する。
  パラメータ：
  - 機能（必須）：特徴や主題、e.gこのエンドポイントSCIMプロビジョニングOktaの統合
  - タイプ（任意）："early_access"（デフォルト）または「ベータ」
{% endcomment %}
{% if include.type == "beta" %}
{% alert important %}
{{ include.feature }} 現在はベータ版である。ベータ版への参加に興味がある場合は、Brazeのアカウント・マネージャーに連絡を。
{% endalert %}
{% else %}
{% alert important %}
{{ include.feature }} 現在は早期アクセス中だ。早期アクセスへの参加に興味がある方は、Brazeのアカウントマネージャーに連絡を。
{% endalert %}
{% endif %}
