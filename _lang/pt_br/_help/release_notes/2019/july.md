---
nav_title: Julho
page_order: 6
noindex: true
page_type: update
description: "Este artigo contém notas de versão para julho de 2019."
---

# Julho de 2019

{% alert update %}
A Braze teve dois (você leu certo - **dois**) ciclos de lançamento de produtos este mês! A versão mais recente é notada na parte superior, a anterior [começa mais abaixo nesta página](#earlier-this-month)!
{% endalert %}

## SAML/SSO

O [logon único]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/) (SSO) oferece às empresas uma maneira segura e centralizada de controlar o acesso ao dashboard do Braze. Em resumo, um único conjunto de credenciais pode ser usado para acessar diferentes aplicativos, inclusive a Braze.

Além do [Google Sign-In com suporte a OAuth 2.0](https://developers.google.com/identity/protocols/OAuth2), as empresas gostariam de ter SSO com suporte a SAML (Security Assertion Markup Language). Isso os capacita a se integrar perfeitamente com grandes provedores de identidade (IdPs), incluindo [o Azure Active Directory e o]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/entra/) [Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/), que suportam os mais recentes padrões do setor (SAML 2.0).

Suportes da Braze:
- [OneLogin]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/)
- [Diretório Ativo do Azure]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/entra/)
- [Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/)

## Ajustar a chave de API do evento mostra

Atualizamos a página de parceiros da Adjust para tornar essa chave de API acessível aos clientes.

## Novos parceiros

Alguns novos parceiros se juntaram ao nosso programa Alloys e foram adicionados à nossa documentação Diga olá para:
- [FiveTran]({{site.baseurl}}/partners/fivetran/)
- [Talon.One]({{site.baseurl}}/partners/talonone/)
- [Voucherify]({{site.baseurl}}/partners/voucherify/)

## Aprimoramento dos detalhes da campanha

Os detalhes expandidos da campanha agora são exibidos na seção ...wait for it..**Detalhes da campanha** da **Página de campanha**!

## Mostrar apenas os meus em segmentos e na tela

O filtro de verificação "Only Show Mine" (Mostrar somente o meu) na página **Campaigns** provou ser muito popular. Como resultado, também estamos adicionando essa opção às listas do canvas e dos segmentos!

### Comportamento de avanço

Agora é possível escolher [quando um usuário avança]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/) de uma etapa do Canva para a próxima. Essas opções incluem "Envio de mensagens" e "Todo o público após a postergação".

### Mensagens no app no Canva

[As mensagens no app]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/) agora estão disponíveis no Canvas! Adicione uma etapa do Canva e procure os canais disponíveis para adicionar uma mensagem no app.

# No início deste mês

## Remoção da imagem do perfil do usuário

Estamos removendo as fotos de perfil de usuário exibidas nos perfis e nas pesquisas de usuários do Braze.

## Conteúdo conectado em cartões de conteúdo

Agora você pode usar as strings e a funcionalidade do [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content) nos [cartões de conteúdo]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/).

As chamadas do Connected Content para servidores externos ocorrerão quando um cartão for realmente enviado, não quando o cartão for visualizado pelo usuário. Semelhante ao e-mail, o conteúdo dinâmico será calculado e determinado no momento do envio, e não quando um cartão for realmente visualizado.

## Endereço "de resposta" nulo

Os clientes agora podem definir um valor `null` para o endereço de resposta de uma mensagem de e-mail na página **Configurações de e-mail** no Braze ou usando a [API]({{site.baseurl}}/api/endpoints/messaging/#email-object-specification).  Quando usado, as respostas serão enviadas para o endereço "De" listado.  Agora é possível personalizar o campo de endereço "From" (De) como `dan@emailaddress.com`, e seus clientes poderão responder diretamente a Dan.

Para definir um valor `null` para o endereço de resposta de uma mensagem de e-mail do Braze, acesse **Manage Settings (Gerenciar configurações)** na navegação e, em seguida, a guia **Email Settings (Configurações de e-mail** ). Role até a seção **Outbound Email Settings (Configurações de envio de e-mail** ) e selecione **Exclude "Reply-To" (Excluir "Responder a") e envie respostas para "From" (De)** como endereço padrão.

## Comparações de campanhas

Analise [várias campanhas ao mesmo tempo para comparar a performance relativa delas]({{site.baseurl}}/report_builder/), lado a lado no Braze - em uma única janela!

## Modelo de ID de despacho em mensagens com Liquid

{% alert note %}
O comportamento para `dispatch_id` difere entre o Canvas e as campanhas porque o Braze trata as etapas do Canva (exceto as etapas de entrada, que podem ser programadas) como eventos disparados, mesmo quando são "programadas". Saiba mais sobre o [comportamento do`dispatch_id` ]({{site.baseurl}}/help/help_articles/data/dispatch_id/) em telas e campanhas.
{% endalert %}

Se você quiser rastrear o envio de uma mensagem de dentro da mensagem (em um URL, por exemplo), você pode usar o modelo no `dispatch_id`. Você pode encontrar a formatação para isso em nossa lista de tags de personalização compatíveis, em [Canva Attributes (Atributos da tela]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)).

Isso se comporta exatamente como `api_id`, pois como o `api_id` não está disponível na criação da campanha, ele é modelado como um espaço reservado e será prévia como `dispatch_id_for_unsent_campaign`. O ID é gerado antes que a mensagem seja enviada e será incluído no momento do envio.

{% alert warning %}
O modelo Liquid de `dispatch_id_for_unsent_campaign` não funciona com mensagens no app, pois as mensagens no app não têm um `dispatch_id`.
{% endalert %}

## A configuração "Mostrar somente os meus" persiste

O filtro "Show Only Mine" (Mostrar somente as minhas) na grade da campanha permanecerá ativado sempre que você visitar a página **Campanhas**.

## Atualizações dos Testes A/B

É possível enviar um [teste A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) único com até oito variantes (e controle opcional) para uma porcentagem especificada pelo usuário do público de uma campanha e, em seguida, enviar a melhor variante para o público restante em um horário pré-agendado.
