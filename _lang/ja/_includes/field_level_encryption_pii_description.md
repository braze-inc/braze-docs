{% comment %}
  識別子フィールドレベルの暗号化と個人識別情報（PII）の説明。フィールドレベル暗号化のドキュメントとリリースノートで使用する。
  パラメータ：
  - リンク（任意）：設定されている場合、「識別子フィールドレベルの暗号化」はこのリンクで囲まれる。e.g {{site.baseurl}}/user_guide/analytics/field_level_encryption/).
{% endcomment %}
{% if include.link %}
識別子フィールドレベルの暗号化を使用すれば、AWS Key Management Service]({{ site.baseurl }}/{{ include.link }})（KMS）でメールアドレスをシームレスに暗号化できる。これにより、Braze内で共有される個人識別情報（PII）を最小限に抑えられる。暗号化は機密データを暗号文に置き換えます。これは読み取れない暗号化された情報です。
{% else %}
識別子フィールドレベルの暗号化を使用すると、AWS Key Management Service (KMS) を使用してメールアドレスをシームレスに暗号化し、Braze で共有される個人を特定できる情報 (PII) を最小限に抑えることができます。暗号化は機密データを暗号文に置き換えます。これは読み取れない暗号化された情報です。
{% endif %}
