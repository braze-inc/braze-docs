{% if include.variable_name == "dnd editors" %}

{% alert important %}
ドラッグ＆ドロップ・エディターにアクセスするには、IT管理者に連絡し、ファイアウォールが`*.bz-rndr.com` allowlistedになっていることを確認する。
{% endalert %}

{% elsif include.variable_name == "email html editor" %}

{% alert important %}
HTMLエディタにアクセスするには、IT管理者に連絡し、ファイアウォールが`*.bz-rndr.com` allowlistedになっていることを確認する。
{% endalert %}

{% endif %}