---
nav_title: VISTO
article_title: VISTO
description: "Este artigo de referência descreve a parceria entre o Braze e a SEEN, uma plataforma de criação de vídeos personalizados para aumentar o engajamento ao longo da jornada do cliente."
alias: /partners/seen/
page_type: partner
search_tag: Partner
---

# VISTO

> A [SEEN](https://seen.io/) é uma plataforma de personalização de vídeo que permite que as empresas criem e desenvolvam vídeos com base em seus clientes para proporcionar uma experiência mais envolvente. Com o SEEN, você pode criar um vídeo com base em seus dados, personalizá-lo em escala na nuvem e distribuí-lo onde for melhor.

## Casos de uso

O SEEN oferece personalização automatizada de vídeo em toda a jornada do cliente. Os usos comuns incluem integração, fidelidade, inscrever-se e conversão, recuperar e combater o churn.

## Pré-requisitos

Antes de começar, você precisará do seguinte:

| Pré-requisito          | Descrição                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Uma campanha SEEN   | É necessária uma campanha SEEN para aproveitar essa parceria.                                                                     |
| Fonte de dados   | Você precisará enviar dados ao SEEN para personalizar seus vídeos. Certifique-se de que todos os dados relevantes estejam disponíveis no Braze e que você passe os dados com **braze_id** como identificador. |
| URL do webhook de transformação de dados do Braze   | A transformação de dados do Braze será usada para reformatar os dados de entrada do SEEN para que possam ser aceitos pelo endpoint /users/track do Braze. |

## Limite de taxa

Atualmente, a API do SEEN aceita 1.000 chamadas por hora.

## Integração do SEEN com o Braze

No exemplo a seguir, enviaremos os dados de usuários ao SEEN para geração de vídeo e receberemos um link de landing page exclusivo e uma miniatura personalizada e exclusiva de volta ao Braze para distribuição. Este exemplo usa um webhook POST para enviar dados ao SEEN e uma transformação de dados para receber os dados de volta ao Braze. Se você tiver várias campanhas de vídeo com o SEEN, repita o processo para conectar o Braze a todas as campanhas de vídeo.

{% alert tip %}
Se tiver algum problema, entre em contato com o gerente de sucesso do cliente da SEEN para obter assistência.
{% endalert %}

### Etapa 1: Criar uma campanha de webhook

Crie uma nova [campanha de webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks) no Braze. Dê um nome à sua campanha e consulte a tabela a seguir para criar seu webhook:

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

Se tudo estiver funcionando como planejado, acesse o Braze e defina a taxa de envio da campanha como 10 **mensagens por minuto**. Dessa forma, você não excederá o limite de frequência do SEEN de 1.000 chamadas por hora.

### Etapa 2: Criar transformação de dados

1. Crie novos campos de [atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes) para `landing_page_url` e `email_thumbnail_url`. Essas são as duas atribuições que usaremos neste exemplo.
2. Abra [Transformação de dados]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/creating_a_transformation/#prerequisites) em **Configurações de dados** e selecione **Criar transformação**.
3. Dê um nome à sua transformação e, em seguida, selecione **Iniciar do zero** e defina **Destino** como **POST: Rastreamento de usuários**.
4. Selecione **Compartilhar a URL do webhook com o SEEN**.
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
6\. Envie uma carga útil de teste para o endpoint fornecido. Se quiser usar a carga útil de retorno de chamada definida na [documentação do SEEN](https://docs.seen.io/api-documentation/ntRoJJ3rXoHzFXhA94JiHB/callbacks/k9DEbcgkq3Vr2pxbHyPQbp), você mesmo poderá enviá-la com o [Postman](https://www.postman.com/) ou outro serviço semelhante:

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
7\. Selecione **Validate (Validar)** para garantir que tudo funcione como planejado.
8\. Selecione **Save** and **Activate** (Salvar e ativar).
