---
nav_title: Configuração do WhatsApp
article_title: Configuração do WhatsApp
alias: /partners/whatsapp/
description: "Este artigo aborda como configurar o canal WhatsApp da Braze, incluindo pré-requisitos e próximos passos sugeridos."
page_type: partner
search_tag: Partner
page_order: 1
channel:
  - WhatsApp
search_rank: 2
---

# Configuração do WhatsApp

> [O envio de mensagens comerciais do WhatsApp](https://www.whatsapp.com/) é uma plataforma popular de envio de mensagens ponto a ponto usada em todo o mundo, oferecendo envio de mensagens baseado em conversas para empresas.	

## Pré-requisitos

Reconheça o seguinte antes de prosseguir com a integração:

- **Política de aceitação:** O WhatsApp exige que as empresas obtenham a aceitação dos clientes para o envio de mensagens.
- **Regras de conteúdo do WhatsApp:** O WhatsApp tem várias [regras de conteúdo](https://www.whatsapp.com/legal/commerce-policy?l=en) que precisam ser seguidas.
- **Conformidade:** Cumprir toda a documentação aplicável da Braze e da Meta e quaisquer [políticas aplicáveis da Meta](https://www.whatsapp.com/legal/?lang=en).
- **Limites de conversação de 24 horas:** Depois que uma empresa envia uma mensagem modelada inicial ou um usuário envia uma mensagem, ocorrerá uma janela de 24 horas onde as duas partes podem enviar mensagens de um lado para o outro. 
- **Iniciando conversa:** Os usuários podem iniciar uma conversa a qualquer momento. Uma empresa só pode iniciar uma conversa através de um modelo de mensagem aprovado.
<br><br>

| Requisito| Descrição|
| ---| --- |
| Conta do Meta Business Manager | Uma conta Meta Business é necessária para aproveitar este canal de envio de mensagens. |
| Conta do WhatsApp Business | Uma conta do WhatsApp Business é necessária para aproveitar este canal de envio de mensagens. |
| Número de telefone do WhatsApp | Você precisa adquirir um número de telefone que atenda aos requisitos do [Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) ou [On-Premises API](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers) para uso do canal de envio de mensagens.  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: Conecte o WhatsApp Messenger ao Braze

No Braze, acessar **Integrações de Parceiros** > **Parceiros de Tecnologia** e procurar por **WhatsApp**.

Na página de parceiros do WhatsApp, selecione **Iniciar Integração**.

![Página de parceiros do WhatsApp com um botão para iniciar a integração.]({% image_buster /assets/img/whatsapp/whatsapp1.png %}){: style="max-width:70%;"}

Na janela aberta, selecione **Próximo** até que o botão **Iniciar Integração** apareça. Selecione o botão para iniciar o processo de integração.

![Instruções para conectar o Braze ao WhatsApp.]({% image_buster /assets/img/whatsapp/instructions.png %}){: style="max-width:50%;"}

### Etapa 2: Configuração do WhatsApp

Em seguida, você será solicitado pelo fluxo de trabalho de configuração da Braze. Para obter um passo a passo detalhado, consulte a [inscrição incorporada no WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/). 

Dentro deste fluxo, você irá:
1. Crie ou selecione suas contas do Meta e do WhatsApp Business. Certifique-se de revisar as [diretrizes de nome de exibição do WhatsApp](https://www.facebook.com/business/help/757569725593362). <br><br>É provável que você já tenha pelo menos uma conta comercial Meta existente em sua empresa. Se for esse o caso, selecione aquele em que você gostaria que sua conta do WhatsApp Business ficasse. As permissões de usuário e a verificação de negócios para o WhatsApp serão controladas centralmente na sua conta Meta Business.<br><br>
2. Crie seu perfil do WhatsApp Business.
3. Verifique seu número do WhatsApp Business.<br><br>

Após a configuração ser concluída, um grupo de inscrições dedicado no WhatsApp será criado para seus usuários.

### Etapa 3: Criar modelos de WhatsApp

Somente modelos de mensagens do WhatsApp aprovados podem ser usados para iniciar conversas com os clientes. Os modelos do WhatsApp podem ser criados no [Meta Business Manager](https://www.facebook.com/business/help/2055875911147364?id=2129163877102343). Para ver uma lista dos recursos de envio de mensagens do WhatsApp suportados pelo Braze, confira [Recursos do WhatsApp suportados]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#supported-whatsapp-features).

1. **Navegue até o [gerenciador de modelos](https://business.facebook.com/wa/manage/message-templates)**<br>
No Meta Business Manager, em **Ferramentas de Conta**, selecione **Modelos de Mensagem**.
Em seguida, selecione **Criar Modelos**.<br><br>![]({% image_buster /assets/img/whatsapp/whatsapp2.png %}){: style="max-width:100%;"}<br><br>
2. **Configurações de mensagem**<br>
No novo criador de modelo de mensagem, selecione a categoria da sua mensagem, nomeie seu modelo e escolha os idiomas que deseja suportar. Você pode excluir ou adicionar mais idiomas depois.<br><br> 
	As categorias de modelo de mensagem disponíveis incluem as seguintes:
	- Marketing: Envie ofertas promocionais, anúncios de produtos e mais para aumentar a conscientização e o engajamento
	- Utilidade: Enviar atualizações de conta, atualizações de pedidos, alertas e mais para compartilhar informações importantes
	- Autenticação: Envie códigos que permitam aos seus clientes acessar suas contas<br><br> 
	![]({% image_buster /assets/img/whatsapp/whatsapp3.png %}){: style="max-width:100%;"}<br><br>
3. **Editar modelo**<br>
Em seguida, solicitaremos que você crie seu modelo de mensagem. <br><br>Aqui, você pode fornecer um cabeçalho de texto ou mídia, o corpo do texto, um rodapé de mensagem e botões. Observe que cabeçalhos de vídeo e documento não estão disponíveis atualmente, e cabeçalhos devem ser do tipo texto ou imagem. Uma prévia da sua mensagem será mostrada à direita. <br><br>Embora o Meta não seja compatível com o Liquid, você pode criar modelos em variáveis que podem ser substituídas posteriormente na Braze por variáveis Liquid. Selecione o botão **\+ Adicionar variável** para fazer isso.<br><br>![]({% image_buster /assets/img/whatsapp/whatsapp4.png %}){: style="max-width:100%;"}<br><br>Após concluir seu modelo, pressione **Enviar**. 

#### Tempo de aprovação do modelo

Você pode verificar o status de aprovação do seu modelo de mensagem na página **Modelo de Mensagem** no Meta Business Manager, ou ao criar uma campanha ou canva no Braze. Além disso, você pode ser notificado por e-mail pela equipe do WhatsApp dependendo das suas permissões de notificação. 

{% alert note %}
Modelos aprovados podem ser usados em quantas campanhas e canvas você quiser. Eles também podem ser enviados para quantos usuários inscritos você quiser. Isso é verdade, a menos que a qualidade do modelo diminua.
{% endalert %}

### Etapa 4: Criar uma campanha no WhatsApp

Depois que os modelos do WhatsApp forem aprovados, você pode ir para o dashboard para criar um [canva ou campanha do WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/). 

{% alert note %}
Depois que sua conta do WhatsApp Business for criada, a Meta determinará seu limite inicial de envio de mensagens. Para saber mais, confira [throughput]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/10dlc/#throughput).
{% endalert %}

## Próximos passos

Após concluir a integração, recomendamos concluir os dois seguintes processos do Meta:
- [Verificação de Negócios](https://www.facebook.com/business/help/2058515294227817?id=180505742745347)
	- Você pode já ter a verificação comercial se tiver usado um Gerenciador de Negócios Meta existente. 
- [Conta Comercial Oficial](https://www.facebook.com/business/help/604726921052590?ref=search_new_0)

Recomendamos também ler sobre [números de telefone de usuários]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/) e adicionar quaisquer usuários que precisarão de acesso para criar [modelos de mensagens em sua organização](https://www.facebook.com/business/help/2169003770027706?id=2190812977867143).

### API de Armazenamento Local do WhatsApp Cloud

A Braze é compatível com a [API Local de Armazenamento em Nuvem](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/local-storage?content_id=ka6F9gESPqhQpm5) do WhatsApp. Para habilitar isso, entre em contato com o seu gerente de suporte ao cliente da Braze.

