---
nav_title: VISTO
article_title: VISTO
description: ""
alias: /partners/seen/
page_type: partner
search_tag: Partner
---

# VISTO

>  

## Casos de uso

 

## Pré-requisitos

Antes de começar, você precisará do seguinte:

| Pré-requisito          | Descrição                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Uma campanha SEEN   | É necessária uma campanha SEEN para aproveitar essa parceria.                                                                     |
| Fonte de dados   | Você precisará enviar dados ao SEEN para personalizar seus vídeos. Certifique-se de que todos os dados relevantes estejam disponíveis no Braze e que você passe os dados com **braze_id** como identificador. |
| URL do webhook de transformação de dados do Braze   | A transformação de dados do Braze será usada para reformatar os dados de entrada do SEEN para que possam ser aceitos pelo endpoint /users/track do Braze. |

## Limite de taxa



## Integração do SEEN com o Braze

 Este exemplo usa um webhook POST para enviar dados ao SEEN e uma transformação de dados para receber os dados de volta ao Braze. Se você tiver várias campanhas de vídeo com o SEEN, repita o processo para conectar o Braze a todas as campanhas de vídeo.

{% alert tip %}

{% endalert %}

### Etapa 1: Criar uma campanha de webhook

 Dê um nome à sua campanha e consulte a tabela a seguir para criar seu webhook:

{% raw %}
<table>
  <thead>
    <tr>
      <th><strong>Campo</strong></th>
      <th><strong>Informações</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>URL do webhook</strong></td>
      <td>Use o seguinte URL de webhook. Você receberá seu <code>campaign_slug</code> do SEEN para chamar o endpoint correto.<br><br><code>https://api.seen.io/v1/campaigns/{campaign_slug}/receivers/</code></td>
    </tr>
    <tr>
      <td><strong>Método HTTP</strong></td>
      <td>Use o <code>POST</code> método.</td>
    </tr>
    <tr>
      <td><strong>Corpo da solicitação</strong></td>
      <td>Digite o corpo da solicitação em um texto bruto semelhante ao seguinte.<br><br><pre><code>[
    {
    "first_name":"{{${first_name}}}",
    "last_name":"{{${last_name}}}",
    "email":"{{${email_address}}}",
    "customer_id":"{{${braze_id}}}"
    }
]</code></pre><br>Para saber mais, consulte <a href="https://docs.seen.io/api-documentation/ntRoJJ3rXoHzFXhA94JiHB/overview/tvy2F5tS3JRM7DfcHwz5fK#request-content">API do SEEN</a>.</td>
    </tr>
    <tr>
      <td><strong>Cabeçalhos da solicitação</strong></td>
      <td>Use as informações a seguir para preencher os cabeçalhos de sua solicitação:<br>- <strong>Autorização:</strong> <code>Token {token}</code><br>- <strong>Content-Type:</strong> <code>application/json</code><br><br>Você receberá seu token de autenticação do SEEN.</td>
    </tr>
  </tbody>
</table>
{% endraw %}
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Agora é possível testar o webhook com um usuário, alternando para a guia **Teste**.

 

### Etapa 2: Criar transformação de dados

1.  Essas são as duas atribuições que usaremos neste exemplo.
2. 
3. Dê um nome à sua transformação e, em seguida, selecione **Iniciar do zero** e defina **Destino** como **POST: Rastreamento de usuários**.
4. Selecione **Compartilhar o URL do webhook com o SEEN**.
5. Você pode usar o código abaixo como ponto de partida para a transformação:

```javascript
let brazecall = {
  "attributes": [
    {
      "braze_id": payload.customer_id,
      "_update_existing_only": true,
      "landing_page_url": payload.landing_page_url,
      "email_thumbnail_url": payload.email_thumbnail_url
    }
  ]
};
return brazecall;
```
{% alert note %}
Se você quiser incluir outros dados, certifique-se de incluí-los também. Lembre-se de discutir também com o SEEN para que a carga útil do retorno de chamada inclua todos os campos necessários.
{% endalert %}

{: start="6"}
6\. Envie uma carga útil de teste para o endpoint fornecido. 

```json
{
        "customer_id": "101",
        "campaign_slug": "onboarding",
        "landing_page_url": "your.subdomain.com/v/12345",
        "video_url": "https://motions.seen.io/298abdcf-1f0f-46e7-9c26-a35b4c1e83cc/d3c1dffdf063986ad521a63e3e68fd7d1100c90a/output.m3u8",
        "thumbnail_url": "https://motions.seen.io/298abdcf-1f0f-46e7-9c26-a35b4c1e83cc/d3c1dffdf063986ad521a63e3e68fd7d1100c90a/thumbnail.jpg",
        "email_thumbnail_url": "https://motions.seen.io/298abdcf-1f0f-46e7-9c26-a35b4c1e83cc/d3c1dffdf063986ad521a63e3e68fd7d1100c90a/email_thumbnail.jpg"
       
}
```

{: start="7"}
7\. Selecione **Validate (Validar** ) para garantir que tudo funcione como planejado.
8\. 
