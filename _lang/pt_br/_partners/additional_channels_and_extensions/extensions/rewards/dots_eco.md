---
nav_title: DOTS.ECO
article_title: DOTS.ECO
description: "Este artigo de referência descreve a integração do Braze e do DOTS.ECO."
alias: /partners/dots.eco/
page_type: partner
search_tag: Partner
---

# DOTS.ECO

> [DOTS.ECO](https://dots.eco) permite recompensar os usuários com impacto ambiental real por meio de certificados digitais rastreáveis. Cada certificado pode incluir metadados, como um URL de certificado compartilhável e um URL de imagem, para que os usuários possam visualizar (e revisitar) sua prova de impacto.

_Essa integração é mantida por DOTS.ECO._

## Sobre essa integração

Braze e DOTS.ECO conectam as jornadas de engajamento do cliente a recompensas de impacto no mundo real. Em uma etapa do Braze Canvas ou da campanha, é possível disparar uma solicitação de criação de certificado DOTS.ECO usando o Connected Content. DOTS.ECO retorna metadados de certificado (como `certificate_url` e `certificate_image_url`) que podem ser armazenados no perfil do usuário como atributos personalizados e reutilizados em canais como mensagens no app, cartões de conteúdo e notificações por push.

## Casos de uso

- Dispare um certificado de impacto quando um usuário concluir um evento-chave (compra, conclusão de nível, inscrição, indicação).
- Mostre uma imagem de certificado personalizado em uma mensagem no app depois que a etapa Connected Content for bem-sucedida.
- Adicione um cartão de conteúdo "View your certificate" com o URL do certificado para acesso posterior.
- Armazene metadados de certificados (como `certificate_url`, `certificate_image_url`, `certificate_header` e `greeting`) como atributos personalizados para reutilização em futuros envios de mensagens.
- Atribua certificados usando um ID de usuário remoto para que os usuários possam reivindicar e visualizar seu impacto posteriormente.
- Execute Testes A/B no envio de mensagens de impacto (cópia/imagens diferentes), mantendo o mesmo fluxo de atualização do usuário DOTS.ECO.


## Pré-requisitos

Antes de começar, você precisa dos seguintes itens:

| Pré-requisito | Descrição |
|---|---|
| Conta DOTS.ECO | DOTS.ECO acesso à conta. |
| DOTS.ECO credenciais | A solicitação deste artigo requer um token de aplicativo DOTS.ECO, uma chave de API e um ID de alocação. Para obtê-los, entre em contato com o gerente de sucesso do cliente do site DOTS.ECO. |
| Chave da API REST do Braze | Uma chave da API REST da Braze com permissões `users.track`. Crie essa chave no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST  do Braze | [Sua URL de endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração DOTS.ECO

### Etapa 1: Crie um Canva e adicione uma etapa de atualização do usuário

No dashboard do Braze, crie uma nova tela que dispara quando um usuário conclui um evento-chave (como uma compra, inscrição ou marco).

Adicione uma etapa de atualização do usuário logo após a etapa de entrada. Essa etapa será usada para chamar a API DOTS.ECO via Connected Content e armazenar os dados de certificado retornados no perfil do usuário.

Use esta etapa para chamar a API DOTS.ECO via Connected Content e armazenar os dados de certificado retornados no perfil do usuário.

### Etapa 2: Crie JSON avançado: Faça uma solicitação POST para DOTS.ECO usando Connected Content

Na etapa **Atualização do usuário**, mude para o **Advanced JSON Editor** e use o Connected Content para fazer uma solicitação POST para a API do certificado DOTS.ECO.

Use a tag `capture` e uma solicitação de Connected Content para chamar o endpoint de certificado de DOTS.ECO. Em seguida, salve a resposta no perfil do usuário como atributos personalizados.

**Exemplo de conteúdo conectado e atualização do usuário**  
{% raw %}
```  
{% capture post_body %} 
{  
  "remote_user_email": "{{${email_address} | default: 'braze+nadav@dots.eco'}}",  
  "app_token": "YOUR_DOTS.ECO_APP_TOKEN",  
  "impact_qty": 1,  
  "remote_user_id": "{{${user_id} | default: ${braze_id}}}",  
  "allocation_id": "YOUR_DOTS.ECO_ALLOCATION_ID"  
}  
{% endcapture %}

{% connected_content https://impact.dots.eco/api/v1/certificate/add?format=sdk  
  :method post  
  :headers { "auth-token": "YOUR_DOTS.ECO_AUTH_TOKEN" }  
  :body {{post_body}}  
  :content_type application/json  
  :save result  
%}

{  
  "attributes": [  
    {  
      "certificate_image_url": "{{result.certificate_image_url}}",  
      "certificate_url": "{{result.certificate_url}}",  
      "certificate_id": "{{result.certificate_id}}"  
    }  
  ]  
}  
```
{% endraw %}

Envie a solicitação para `https://impact.dots.eco/api/v1/certificate/add?format=sdk`.

![DOTS.ECO Etapa de atualização do usuário.]({% image_buster /assets/img/dots_eco/dotseco_user_update.png %})

{% alert important %}  
Essa integração usa o Connected Content dentro de uma etapa **de atualização do usuário** do Canva para chamar a API DOTS.ECO. Teste as solicitações com um cliente de API (por exemplo, Postman) primeiro para validar o token e a carga útil.  
{% endalert %}

### Etapa 3: Exibir o certificado em mensagens

Quando as atribuições do certificado são armazenadas no perfil do usuário, elas podem ser referenciadas nas etapas posteriores da mensagem do Canva.

![DOTS.ECO fluxo.]({% image_buster /assets/img/dots_eco/dots.eco_flow.png %})

![DOTS.ECO Etapa de envio de mensagens.]({% image_buster /assets/img/dots_eco/dotseco_messages.png %})

![DOTS.ECO seção de criador de mensagens.]({% image_buster /assets/img/dots_eco/dotseco_messages_compose.png %})

Por exemplo:  
- Mostre a imagem do certificado em uma mensagem no app usando {% raw %}`{{custom_attribute.${certificate_image_url}}}`{% endraw %}  
- Link para o certificado hospedado usando {% raw %}`{{custom_attribute.${certificate_url}}}`{% endraw %}

![DOTS.ECO comportamento ao clicar em uma mensagem.]({% image_buster /assets/img/dots_eco/dotseco_messages_compose_onclickbehavior.png %})


Isso permite que você personalize mensagens no app, cartões de conteúdo ou notificações por push com confirmação de impacto.

## Solução de problemas

Revise os erros de Connected Content no dashboard do Braze em **Configurações** > **Registro de atividades de mensagens**.

- **Connected Content retorna vazio**: Confirme que `:save result` está definido e que você está fazendo referência aos campos de resposta esperados.
- **As atribuições não estão sendo exibidas na etapa Mensagem**:
  - Confirme se os nomes dos atributos personalizados no Braze correspondem exatamente aos atributos definidos na etapa Atualização do usuário.
  - Na etapa Atualização do usuário, use a guia **Pré-visualização e teste** para confirmar o preenchimento das atribuições. Em seguida, envie um teste para um usuário e confirme se as atribuições estão salvas no perfil do usuário.
- **`422` erro (entidade não processável)**: Confirme se o token do app e a quantidade de impacto são válidos.
- **`401` erro**: Confirme se o token de autenticação está presente e correto.
- **Não há prévia da imagem na etapa de mensagens**: Selecione **Send Test to User (Enviar teste ao usuário** ) na etapa User Update (Atualização do usuário) e, em seguida, faça uma prévia da mensagem usando esse mesmo usuário.