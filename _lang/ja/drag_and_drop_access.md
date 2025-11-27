{% if include.variable_name == "dnd editors" %}

{% alert important %}
ドラッグアンドドロップエディタにアクセスするには、IT 管理者に問い合わせて、ファイアウォールに`*.bz-rndr.com` が許可されていることを確認します。
{% endalert %}

{% elsif include.variable_name == "email html editor" %}

{% alert important %}
HTML エディタにアクセスするには、IT 管理者に問い合わせて、ファイアウォールに`*.bz-rndr.com` が許可されていることを確認します。
{% endalert %}

{% endif %}