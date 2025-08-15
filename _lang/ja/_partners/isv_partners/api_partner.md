---
nav_title: APIパートナー統合
alias: /api_partner_integration/
hidden: true
---

# APIパートナーとの統合

> `User-Agent` ヘッダーの構文など、パートナー API 連携の要件についてご紹介します。

{% alert important %}
これまで、パートナーは API リクエストのパートナーフィールドに名前を追加する必要がありました。このフォーマットはサポートされなくなり、現在は `User-Agent` ヘッダーが必要となりました。
{% endalert %}

## ユーザーエージェント

トラフィックの送信元を明確に識別する `User-Agent` ヘッダーを含める必要があります。これにより、共有顧客は Braze の API 使用状況レポートでパートナーのトラフィックを確認ができ、Braze のエンジニアはベストプラクティスに従っていないパートナー統合を特定することができます。一般に、使用するユーザーエージェントは、すべてのトラフィックで 1 つのみにする必要があります。

### 構文

`User-Agent` ヘッダーは以下のフォーマット ([RFC 7231](https://datatracker.ietf.org/doc/html/rfc7231#page-46) 標準と同様) に従う必要があります。

```bash
User-Agent: partner-OrganizationName-ProductName/ProductVersion
```

以下を置き換えます。

| placeholder | 説明 |
|-------------|-------------|
| `OrganizationName` | Pascal ケースでフォーマットされた組織名。 |
| `ProductName` | Pascal ケースでフォーマットされた製品名。 |
| `ProductVersion` | 製品のバージョン番号。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 例

たとえば、Snowflake のクラウドデータ取り込みの場合、以下が正しいユーザーエージェントとされます。

```bash
User-Agent: partner-Snowflake-CloudDataIngestion/179
```

しかし、以下の場合はトラフィックの送信元が明確に特定されないため、正しくないとされます。

```bash
User-Agent: axios/1.4.0
``` 
