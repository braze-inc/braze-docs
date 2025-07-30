---
nav_title: Redirecionamento de usuários
article_title: Redirecionamento de usuários
page_order: 3
description: "Este artigo de referência aborda como os usuários podem redirecionar suas mensagens por meio das interações do WhatsApp."
page_type: reference
channel:
  - WhatsApp
---

# Redirecionamento de usuários 

> Além de alterar o estado da inscrição do usuário, a Braze também registrará as interações com o perfil do usuário para filtragem e envio de mensagens.<br><br>Esses filtros e disparadores permitem filtrar os usuários que receberam mensagens do WhatsApp ou que receberam mensagens do WhatsApp de uma campanha específica do WhatsApp ou de uma etapa do Canva.

## Opções de redirecionamento

{% alert note %}
Ao criar públicos com redirecionamento de usuários, talvez seja necessário incluir ou excluir determinados usuários com base em suas preferências e para cumprir as leis de privacidade, como o direito de "Não vender ou compartilhar" de acordo com a CCPA. Os profissionais de marketing devem implementar os filtros relevantes para a elegibilidade dos usuários nos critérios de entrada do Canva e/ou da campanha.
{% endalert %}

### Filtrar usuários por WhatsApp

Os usuários podem ser filtrados por quando receberam um WhatsApp pela última vez ou se receberam um WhatsApp de uma campanha específica do WhatsApp. Os filtros podem ser definidos na etapa Usuários-alvo do criador de campanhas.

**Filtrar pelo último WhatsApp recebido**<br>
![Filtrar por ter recebido uma mensagem do WhatsApp em 22 de abril de 2025.]({% image_buster /assets/img/whatsapp/whatsapp23.png %}){: style="max-width:75%"}

**Filtrar por mensagens recebidas da campanha do WhatsApp**<br>
Filtra os usuários que receberam uma mensagem de uma campanha específica do WhatsApp. Com esse filtro, você também tem a opção de filtrar as pessoas que não receberam mensagens de uma campanha do WhatsApp.<br>
![Filtrar por receber uma campanha do WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp22.png %}){: style="max-width:75%"}

### Filtrar por engajamento
Redirecione os usuários que leram ou não uma campanha do WhatsApp ou uma etapa do Canva. 

**Redirecionamento de usuários que abriram/leram uma campanha específica do WhatsApp**
1. Crie um segmento usando o filtro **Clicked/Opened Campaign (Campanha clicada/aberta** ).
2. Selecione **ler mensagem do WhatsApp**.
3. Escolha a campanha desejada.<br>

![Filtrar por ter lido uma mensagem do WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp21.png %}){: style="max-width:75%"}

**Redirecione os usuários que abriram/leram uma etapa específica do Canva**
1. Crie um segmento usando o filtro **Etapa clicada/aberta**.
2. Selecione **ler mensagem do WhatsApp**.
3. Escolha o Canvas e as etapas do Canva desejados.<br>

![Filtrar por ler uma etapa do WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp20.png %}){: style="max-width:75%"}

**Filtrar por campanha ou atribuição do Canva**<br>
Filtre os usuários que abriram/leram uma campanha específica do WhatsApp ou um componente ou tag do Canva.

![Filtrar por abrir uma mensagem específica do WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp19.png %}){: style="max-width:75%"}

