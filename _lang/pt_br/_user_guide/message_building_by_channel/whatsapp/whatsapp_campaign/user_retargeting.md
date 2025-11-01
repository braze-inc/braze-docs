---
nav_title: Redirecionamento de usuários
article_title: Redirecionamento de usuários
page_order: 4
description: "Este artigo de referência aborda como os usuários podem redirecionar suas mensagens por meio das interações do WhatsApp."
page_type: reference
channel:
  - WhatsApp
---

# Redirecionamento de usuários 

> Além de alterar o estado da assinatura do usuário, o Braze também registrará as interações com o perfil do usuário para filtrar e acionar mensagens.<br><br>Esses filtros e acionadores permitem filtrar os usuários que receberam mensagens do WhatsApp ou que receberam mensagens do WhatsApp de uma campanha específica do WhatsApp ou de uma etapa do Canvas.

## Opções de redirecionamento

{% alert note %}
Ao criar públicos com redirecionamento de usuários, talvez você queira incluir ou excluir determinados usuários com base em suas preferências e para cumprir as leis de privacidade, como o direito de "Não vender ou compartilhar" de acordo com a CCPA. Os profissionais de marketing devem implementar os filtros relevantes para a elegibilidade dos usuários em seus critérios de entrada do Canvas e/ou da Campanha.
{% endalert %}

### Filtrar usuários por WhatsApp

Os usuários podem ser filtrados pela última vez que receberam um WhatsApp ou se receberam um WhatsApp de uma campanha específica do WhatsApp. Os filtros podem ser definidos na etapa Usuários-alvo do criador de campanhas.

**Filtrar pelo último WhatsApp recebido**<br>
Filtro para o último recebimento de uma mensagem do WhatsApp em 22 de abril de 2025.]({% image_buster /assets/img/whatsapp/whatsapp23.png %}){: style="max-width:75%"}

**Filtrar por mensagens recebidas da campanha do WhatsApp**<br>
Filtra os usuários que receberam uma mensagem de uma campanha específica do WhatsApp. Com esse filtro, você também tem a opção de filtrar as pessoas que não receberam mensagens de uma campanha do WhatsApp.<br>
Filtro para receber uma campanha do WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp22.png %}){: style="max-width:75%"}

### Filtrar por engajamento
Redirecione os usuários que leram ou não uma campanha do WhatsApp ou uma etapa do Canvas. 

**Redirecione os usuários que abriram/leram uma campanha específica do WhatsApp**
1. Crie um segmento usando o filtro **Clicked/Opened Campaign (Campanha clicada/aberta** ).
2. Selecione **ler mensagem do WhatsApp**.
3. Escolha a campanha desejada.<br>

\![Filtro por ter lido uma mensagem do WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp21.png %}){: style="max-width:75%"}

**Redirecione os usuários que abriram/leram uma etapa específica do Canvas**
1. Crie um segmento usando o filtro **Clicked/Opened Step (Etapa clicada/aberta** ).
2. Selecione **ler mensagem do WhatsApp**.
3. Escolha o Canvas e as etapas do Canvas desejados.<br>

\![Filtro para leitura de uma etapa do WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp20.png %}){: style="max-width:75%"}

**Filtrar por campanha ou atribuição do Canvas**<br>
Filtre os usuários que abriram/leram uma campanha específica do WhatsApp ou um componente ou tag do Canvas.

\![Filtro para abrir uma mensagem específica do WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp19.png %}){: style="max-width:75%"}

