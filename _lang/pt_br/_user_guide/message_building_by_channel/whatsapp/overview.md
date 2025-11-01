---
nav_title: Configuração do WhatsApp
article_title: Configuração do WhatsApp
alias: /partners/whatsapp/
description: "Este artigo aborda como configurar o canal Braze WhatsApp, incluindo os pré-requisitos e as próximas etapas sugeridas."
page_type: partner
search_tag: Partner
page_order: 1
channel:
  - WhatsApp
search_rank: 2
---

# Configuração do WhatsApp

> [O WhatsApp](https://www.whatsapp.com/) Business é uma popular plataforma de mensagens ponto a ponto usada em todo o mundo que oferece mensagens baseadas em conversas para empresas.	

## Pré-requisitos

Confirme o seguinte antes de prosseguir com a integração:

- **Política de adesão:** O WhatsApp exige que as empresas façam com que os clientes aceitem o envio de mensagens.
- **Regras de conteúdo do WhatsApp:** O WhatsApp tem várias [regras de conteúdo](https://www.whatsapp.com/legal/commerce-policy?l=en) que precisam ser seguidas.
- **Conformidade:** Cumprir com toda a documentação aplicável da Braze e da Meta e com todas as [políticas](https://www.whatsapp.com/legal/?lang=en) aplicáveis [da Meta](https://www.whatsapp.com/legal/?lang=en).
- **Limites de conversação de 24 horas:** Depois que uma empresa enviar uma mensagem inicial com modelo ou um usuário enviar uma mensagem, haverá uma janela de 24 horas em que as duas partes poderão enviar e receber mensagens. 
- **Iniciar a conversa:** Os usuários podem iniciar uma conversa a qualquer momento. Uma empresa só pode iniciar uma conversa por meio de um modelo de mensagem aprovado.
<br><br>

| Requisito| Descrição|
| ---| --- |
| Conta do Meta Business Manager | É necessário ter uma conta Meta Business para aproveitar esse canal de mensagens. |
| Conta do WhatsApp Business | É necessário ter uma conta do WhatsApp Business para aproveitar esse canal de mensagens. |
| Número de telefone do WhatsApp | Você deve adquirir um número de telefone que atenda aos requisitos do WhatsApp para a [Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) ou [a On-Premises API](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers) para usar o canal de mensagens.  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: Conectar o WhatsApp Messenger ao Braze

No Braze, vá para **Partner Integrations** > **Technology Partners** e procure o **WhatsApp**.

Na página do parceiro do WhatsApp, selecione **Begin Integration (Iniciar integração**).

Página de parceiro do WhatsApp com um botão para iniciar a integração.]({% image_buster /assets/img/whatsapp/whatsapp1.png %}){: style="max-width:70%;"}

Na janela aberta, selecione **Next** até que o botão **Begin Integration** seja exibido. Selecione o botão para iniciar o processo de integração.

Instruções para conectar o Braze ao WhatsApp.]({% image_buster /assets/img/whatsapp/instructions.png %}){: style="max-width:50%;"}

### Etapa 2: Configuração do WhatsApp

Em seguida, você será solicitado pelo fluxo de trabalho de configuração do Braze. Para obter um passo a passo, consulte a [inscrição incorporada no WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/). 

Nesse fluxo, você terá:
1. Crie ou selecione suas contas do Meta e do WhatsApp Business. Certifique-se de revisar as [diretrizes de nome de exibição do WhatsApp](https://www.facebook.com/business/help/757569725593362). <br><br>É provável que você já tenha pelo menos uma conta Meta Business em sua empresa. Se esse for o caso, selecione aquele em que você gostaria que sua conta do WhatsApp Business ficasse. As permissões de usuário e a verificação comercial do WhatsApp serão controladas de forma centralizada na sua conta do Meta Business.<br><br>
2. Crie seu perfil do WhatsApp Business.
3. Verifique seu número do WhatsApp Business.<br><br>

Após a conclusão da configuração, um grupo de assinatura do WhatsApp dedicado será criado para seus usuários.

### Etapa 3: Criar modelos do WhatsApp

Somente modelos aprovados de mensagens do WhatsApp podem ser usados para iniciar conversas com os clientes. Os modelos do WhatsApp podem ser criados no [Meta Business Manager](https://www.facebook.com/business/help/2055875911147364?id=2129163877102343). Para obter uma lista dos recursos de mensagens do WhatsApp compatíveis com o Braze, consulte [Recursos compatíveis com o WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#supported-whatsapp-features).

1. **Navegue até o [gerenciador de modelos](https://business.facebook.com/wa/manage/message-templates)**<br>
No Meta Business Manager, em **Account Tools**, selecione **Message Templates**.
Em seguida, selecione **Create Templates (Criar modelos**).<br><br>Gerenciador do WhatsApp com uma lista de modelos de mensagens.]({% image_buster /assets/img/whatsapp/whatsapp2.png %}){: style="max-width:100%;"}<br><br>
2. **Configurações de mensagens**<br>
No compositor do novo modelo de mensagem, selecione a categoria da mensagem, dê um nome ao modelo e escolha os idiomas aos quais deseja dar suporte. Você pode excluir ou adicionar mais idiomas posteriormente.<br><br> 
	As categorias de modelos de mensagem disponíveis incluem as seguintes:
	- Marketing: Envie ofertas promocionais, anúncios de produtos e muito mais para aumentar a conscientização e o envolvimento
	- Utilidade: Envie atualizações de conta, atualizações de pedidos, alertas e muito mais para compartilhar informações importantes
	- Autenticação: Envie códigos que permitam que seus clientes acessem suas contas<br><br> 
	Compositor de modelo de mensagem com categorias para marketing, utilidade e autenticação.]({% image_buster /assets/img/whatsapp/whatsapp3.png %}){: style="max-width:100%;"}<br><br>
3. **Editar modelo**<br>
Em seguida, crie seu modelo de mensagem. <br><br>Você pode fornecer um cabeçalho de texto ou mídia, o corpo do texto, um rodapé de mensagem e botões. Observe que os cabeçalhos de vídeo e documento não estão disponíveis no momento, e os cabeçalhos devem ser do tipo texto ou imagem. Qualquer mídia que você adicionar servirá como exemplo para o processo de revisão e **não será** incluída na mensagem modelo. A mídia precisa ser adicionada no Braze. Uma visualização da sua mensagem será exibida em um painel. <br><br>Embora o Meta não seja compatível com o Liquid, você pode criar modelos em variáveis que podem ser substituídas posteriormente no Braze por variáveis do Liquid. Selecione o botão **\+ Adicionar variável** para fazer isso.<br><br>\![Template composer.]({% image_buster /assets/img/whatsapp/whatsapp4.png %}){: style="max-width:100%;"}

Depois de concluir o modelo, pressione **Submit**. 

#### Tempo de aprovação do modelo

Você pode verificar o status de aprovação de seu modelo de mensagem na página **Modelo de mensagem** no Meta Business Manager ou ao criar uma campanha ou Canvas no Braze. Além disso, você pode ser notificado por e-mail pela equipe do WhatsApp, dependendo de suas permissões de notificação. 

{% alert note %}
Os modelos aprovados podem ser usados em quantas campanhas e Canvases você desejar. Eles também podem ser enviados para quantos usuários opt-in você desejar. Isso é verdade, a menos que a qualidade do modelo diminua.
{% endalert %}

### Etapa 4: Criar uma campanha no WhatsApp

Depois que os modelos do WhatsApp forem aprovados, você poderá ir para o painel para criar um [WhatsApp Canvas ou uma campanha]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/). 

{% alert note %}
Depois que sua conta do WhatsApp Business for criada, o Meta determinará seu limite inicial de mensagens. Para saber mais, confira a [taxa de transferência]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/10dlc/#throughput).
{% endalert %}

## Próximas etapas

Depois de concluir a integração, recomendamos a conclusão dos dois processos Meta a seguir:
- [Verificação de negócios](https://www.facebook.com/business/help/2058515294227817?id=180505742745347)
	- Talvez você já tenha uma verificação de negócios se tiver usado um Meta Business Manager existente. 
- [Conta comercial oficial](https://www.facebook.com/business/help/604726921052590?ref=search_new_0)

Também recomendamos ler sobre os [números de telefone dos usuários]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/) e adicionar todos os usuários que precisarão de acesso para criar [modelos](https://www.facebook.com/business/help/2169003770027706?id=2190812977867143) de mensagens [na sua organização](https://www.facebook.com/business/help/2169003770027706?id=2190812977867143).

### WhatsApp Cloud API Armazenamento local

O Braze é compatível com o [armazenamento local da API de nuvem](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/local-storage?content_id=ka6F9gESPqhQpm5) do WhatsApp. Para ativar essa opção, entre em contato com o gerente de suporte ao cliente da Braze.

