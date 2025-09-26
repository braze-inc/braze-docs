---
nav_title: Facebook
article_title: Exportação do público do Facebook
alias: /partners/facebook/
description: "Este artigo de referência descreve a parceria entre a Braze e o Facebook, uma plataforma social líder para as marcas alcançarem e se engajarem com seus clientes."
page_type: partner
search_tag: Partner

---

# Exportação do público do Facebook

> A integração entre o Braze e o Facebook permite que você exporte manualmente seus segmentos do Braze para o Facebook para criar públicos personalizados do Facebook. Essa é uma exportação única e estática de público e só criará novos públicos personalizados no Facebook.

Os casos de uso comuns para exportar públicos personalizados do Facebook incluem:
- Redirecionamento de usuários em pontos específicos do seu ciclo de vida
- Criação de listas de direcionamento de exclusão
- Criação de [públicos semelhantes](https://www.facebook.com/business/help/164749007013531?id=401668390442328) para adquirir novos usuários com mais eficiência
<br><br>

{% alert note %}
A exportação do público do Facebook usa o **token de acesso do usuário** para autorizar solicitações.<br><br>
Se você estiver usando esse recurso juntamente com o recurso de [sincronização do público do Facebook]({{site.baseurl}}/audience_sync_facebook/), o Braze usará, por padrão, o **token de usuário do sistema** mais confiável que você já gerou para autorizar solicitações.
{% endalert %}

{% alert note %}
Se estiver participando do teste das contas de trabalho do Meta na versão beta, desconecte e reconecte sua conta à [página de parceiro do Facebook]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync#step-1-connect-to-facebook).
{% endalert %}

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| [Gerente de negócios do Facebook](https://www.facebook.com/business/help/113163272211510?id=180505742745347) | Uma ferramenta centralizada para gerenciar os ativos do Facebook da sua marca (por exemplo, contas de anúncios, páginas, apps). |
| [Conta de anúncios do Facebook](https://www.facebook.com/business/help/910137316041095?id=420299598837059) | Uma conta de anúncios ativa do Facebook vinculada ao gerente de negócios da sua marca que você deseja usar com os públicos personalizados do Braze.<br><br>Certifique-se de que o administrador do seu gerente de negócios do Facebook lhe concedeu permissões de administrador para as contas de anúncios do Facebook que você planeja usar com o Braze e que você aceitou os termos e condições da sua conta de anúncios. Caso contrário, não será possível acessar nenhuma conta de anúncios do Facebook no Braze. |
| [Termos de públicos personalizados do Facebook](https://www.facebook.com/ads/manage/customaudiences/tos.php)| Você deve aceitar os Termos de Públicos Personalizados do Facebook para suas contas de anúncios do Facebook que planeja usar com o Braze.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: conecte-se ao Facebook

1. No dashboard da Braze, acesse **Integrações de parceiros** > **Parceiros de tecnologia** e selecione **Facebook**. 

{: start="2"}
2\. No módulo Facebook Audience Export, selecione **Connect Facebook**. <br><br>![Página de parceiros de tecnologia do Facebook na plataforma Braze.]({% image_buster /assets/img/fb/afb_1.png %}){: style="max-width:70%;"}

{: start="3"}
3\. Na janela de diálogo oAuth do Facebook, autorize o Braze a criar públicos personalizados em suas contas de anúncios do Facebook. <br><br>![A primeira caixa de diálogo do Facebook solicitando "Connect as X" (Conectar-se como X), em que X é seu nome de usuário do Facebook.]({% image_buster /assets/img/fb/afb_3.png %}){: style="max-width:30%;"}  ![A segunda caixa de diálogo do Facebook solicitando permissão para gerenciar anúncios de suas contas de anúncios.]({% image_buster /assets/img/fb/afb_2.png %}){: style="max-width:40%;"}

{: start="4"}
4\. Depois que o Braze estiver vinculado à sua conta do Facebook, selecione as contas de anúncios que deseja sincronizar em seu espaço de trabalho do Braze. <br><br>![Uma lista de contas de anúncios disponíveis que você pode conectar ao Facebook.]({% image_buster /assets/img/fb/afb_4.png %}){: style="max-width:70%;"}<br><br> Depois de se conectar, você será levado de volta à página do parceiro, onde poderá ver quais contas estão conectadas e desconectar contas existentes. <br><br> ![Uma versão atualizada da página de parceiros de tecnologia do Facebook mostrando as contas de anúncios conectadas com sucesso.]({% image_buster /assets/img/fb/afb_5.png %}){: style="max-width:70%;"}<br>
<br> Sua conexão com o Facebook é aplicada no nível do espaço de trabalho do Braze. Se o administrador do Facebook remover você do Facebook Business Manager ou do acesso às contas conectadas do Facebook, o Braze detectará um token inválido. Como resultado, suas Canvas ativas que usam etapas de público do Facebook mostrarão erros, e o Braze não poderá sincronizar usuários. 

{% alert important %}
Para os clientes que já passaram pelo processo de revisão do app do Facebook para o [Gerenciamento de anúncios](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) e [o Acesso padrão ao Gerenciamento de anúncios](https://developers.facebook.com/docs/marketing-api/access#standard), o token de usuário do sistema ainda será válido para a etapa do público do Facebook. Não será possível editar ou revogar o token de usuário do sistema do Facebook por meio da página de parceiro do Facebook. Em vez disso, é possível conectar sua conta do Facebook para substituir o token de usuário do sistema do Facebook no espaço de trabalho do Braze. 

<br><br>A nova configuração do Facebook oAuth também se aplicará às [exportações do Facebook por meio de segmentos]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook/#prerequisites).
{% endalert %}

### Etapa 2: Exporte seus usuários para o Facebook

No Braze, a exportação do público do Facebook pode ser acessada por meio da página **Segmentos**. 

1. Na página **Segments (Segmentos)**, selecione o segmento que você deseja exportar.
2. Selecione **Dados do usuário** e, em seguida, selecione **Exportar como público do Facebook**. <br><br>![A seção "Segment Details" (Detalhes do segmento) de um segmento com "User Data" (Dados de usuários) selecionado para exibir um menu suspenso de opções que inclui "Export as Facebook Audience" (Exportar como público do Facebook).]({% image_buster /assets/img/fb/afb_6.png %})

{: start="3"}
3\. Se ainda não tiver ativado o Facebook na Braze, você verá uma indicação para acessar a página de parceiros de tecnologia do Facebook no dashboard. Se já tiver ativado o Facebook por meio de **Technology Partners** > **Facebook**, poderá selecionar sua conta de anúncios do Facebook e os campos de usuário a serem exportados. <br><br> Há três campos de usuário possíveis que podem ser exportados:
- IDFA do dispositivo
- Número de telefone 
- E-mail

{% alert note %}
Só é possível selecionar um campo de usuário em uma única exportação. Se você escolher mais de um tipo de dados, o Braze criará um público personalizado separado para cada um deles.
{% endalert %}

{: start="4"}
4\. Depois de selecionar o campo do usuário, selecione **Export Segment (Exportar segmento)**. Assim como as exportações CSV, você receberá um e-mail quando o segmento terminar de ser exportado para o Facebook.
5\. Visualize o público personalizado no [Gerenciador de anúncios do Facebook](https://www.facebook.com/ads/manager/audiences/manage/).

{% alert important %}
Devido a razões de privacidade do usuário, o Facebook não permite que você veja:

- Os usuários exatos que foram adicionados com sucesso a um público personalizado. [Saiba mais.](https://www.facebook.com/business/help/112061095610075)
- O tamanho do público personalizado. [Saiba mais.](https://marketingland.com/exclusive-facebook-will-no-longer-show-audience-reach-estimates-for-custom-audiences-after-vulnerability-detected-236923)
{% endalert %}

#### Configuração de sua exportação de público

Ao criar públicos do Facebook, talvez seja necessário incluir ou excluir determinados usuários com base em suas preferências e para cumprir as leis de privacidade, como o direito de "Não vender ou compartilhar" de acordo com a [CCPA](https://oag.ca.gov/privacy/ccpa). Os profissionais de marketing devem implementar os filtros relevantes para a elegibilidade dos usuários em seus critérios de entrada no Canva. Abaixo, listamos algumas opções. 

- Se você coletou o [IDFA do iOS por meio do SDK do Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection), poderá usar o filtro **Ads Tracking Enabled (Rastreamento de anúncios ativado** ). Selecione o valor como `true` para enviar os usuários apenas para destinos do Audience Sync que eles aceitaram. 

![]({% image_buster /assets/img/tiktok/tiktok16.png %}){: style="max-width:75%;"}

- Se estiver coletando aceitações, recusas, `Do Not Sell Or Share` ou outros atributos personalizados relevantes, inclua-os nos critérios de entrada do canva como um filtro: 

![Um Canva com um público de entrada de "opted_in_marketing" é igual a "true".]({% image_buster /assets/img/tiktok/tiktok13.png %}){: style="max-width:75%;"}


#### Públicos semelhantes

Depois de exportar com êxito um segmento como um público do Facebook, você poderá criar grupos adicionais usando o Facebook [Lookalike Audiences](https://www.facebook.com/business/help/164749007013531?id=401668390442328). Esse recurso analisa os dados demográficos, os interesses e outras atribuições do público escolhido e cria um novo público de pessoas com atributos semelhantes.

