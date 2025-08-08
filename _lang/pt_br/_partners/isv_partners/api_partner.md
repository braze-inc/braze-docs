---
nav_title: Integração com parceiros da API
alias: /api_partner_integration/
hidden: true
---

# Integração com parceiros da API

> Saiba mais sobre os requisitos para integrações com parceiros de API, como a sintaxe dos cabeçalhos `User-Agent`.

{% alert important %}
Anteriormente, os parceiros eram obrigados a adicionar seu nome ao campo de parceiro em suas solicitações de API. Essa formatação não é mais suportada e agora é necessário um cabeçalho `User-Agent`.
{% endalert %}

## Agentes do usuário

É necessário incluir um cabeçalho `User-Agent` que identifique claramente a origem do tráfego. Isso permite que nossos clientes compartilhados vejam o tráfego de parceiros nos relatórios de uso da API do Braze e ativa os engenheiros do Braze para identificar as integrações que não estão seguindo as práticas recomendadas. Em geral, você deve usar apenas um único agente de usuário para todo o seu tráfego.

### Sintaxe

Seu cabeçalho `User-Agent` deve obedecer ao seguinte formato (que é semelhante ao padrão [RFC 7231](https://datatracker.ietf.org/doc/html/rfc7231#page-46) ):

```bash
User-Agent: partner-OrganizationName-ProductName/ProductVersion
```

Substitua o seguinte:

| Espaço reservado | Descrição |
|-------------|-------------|
| `OrganizationName` | O nome de sua organização formatado em letras maiúsculas e minúsculas. |
| `ProductName` | O nome do seu produto formatado em letras maiúsculas e minúsculas. |
| `ProductVersion` | O número da versão de seu produto. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Exemplos

Por exemplo, o seguinte seria um agente de usuário correto para o Cloud Data Ingestion da Snowflake:

```bash
User-Agent: partner-Snowflake-CloudDataIngestion/179
```

No entanto, isso seria incorreto porque não identifica claramente a origem do tráfego:

```bash
User-Agent: axios/1.4.0
``` 
