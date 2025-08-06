---
nav_title: Anúncios de leads do Facebook via Zapier
article_title: Anúncios de leads do Facebook via Zapier
description: "Esse artigo de referência descreve a integração entre o Braze e o Facebook Lead Ads via Zapier para automatizar a transferência de dados de leads do Facebook para o Braze, ativando o engajamento em tempo real e ações de acompanhamento personalizadas."
alias: /partners/facebook_via_zapier/
page_type: partner
search_tag: Partner

---

# Anúncios de leads do Facebook por meio da integração com o Zapier

> Com a integração do Facebook Lead Ads via <a href="https://zapier.com/" target="_blank">Zapier</a>, você pode importar seus leads do Facebook para o Braze e rastrear um evento personalizado quando os leads forem capturados. 

O Facebook Lead Ads é um formato de anúncio que permite que as empresas coletem informações de leads diretamente no Facebook. Esses anúncios são projetados para tornar o processo de geração de leads fácil e prático. Ao utilizar uma integração Zapier e Braze, você pode automatizar a transferência de dados de leads do Facebook para o Braze, ativando o engajamento em tempo real e ações de acompanhamento personalizadas. 

## Pré-requisitos

| Solicitações | Descrição |
|---|---|
| Conta Zapier | É necessário ter uma conta do Zapier para usar a parceria. Essa integração requer o uso de <a href="https://zapier.com/app/pricing/" target="_blank">apps Zapier premium</a>, então verifique se o seu plano do Zapier tem acesso a aplicativos premium. |
| <a href="https://www.facebook.com/business/help/540596413257598?id=735435806665862/" target="_blank">Acesso a leads do Facebook</a> | O acesso ao Facebook Leads é necessário para cada conta de anúncio que você planeja usar com a Braze. |
| <a href="https://www.facebook.com/business/help/1710077379203657?id=180505742745347" target="_blank">Gerente de negócios do Facebook</a> | Você usará o Facebook Business Manager, uma ferramenta centralizada para gerenciar os ativos do Facebook da sua marca (por exemplo, contas de anúncios, páginas e apps), como parte dessa integração. |
| <a href="https://www.facebook.com/business/help/195296697183682?id=829106167281625/" target="_blank">Conta de anúncios do Facebook</a> | Você precisará de uma conta de anúncios ativa no Facebook vinculada ao gerente de negócios da sua marca. <br><br>Confirme se você tem a permissão "Manage ad accounts" (Gerenciar contas de anúncios) para cada conta de anúncios que planeja usar com a Braze e se aceitou os termos e condições da conta de anúncios. |
| <a href="https://www.facebook.com/business/help/183277585892925?id=420299598837059/" target="_blank">Página do Facebook</a> | Você precisará de uma página ativa no Facebook vinculada ao gerente de negócios da sua marca. <br><br>Certifique-se de ter as permissões "Manage Pages" (Gerenciar páginas) para cada página do Facebook que planeja usar com o Braze. |
| Ponto de extremidade REST do Braze | Você precisa saber qual é o [URL do endpoint REST]({{site.baseurl}}/api/basics/#api-definitions). Seu endpoint de API corresponde ao URL do dashboard de sua instância do Braze. <br><br> Por exemplo, se o URL do dashboard for `https://dashboard-03.braze.com`, seu endpoint será `dashboard-03`. |
| Chave da API REST do Braze | Confirme se você tem uma chave da API REST da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: Crie uma campanha de Lead Ads com um formulário instantâneo

No Gerenciador de anúncios do Facebook, crie <a href="https://www.facebook.com/business/help/397336587121938?id=735435806665862&helpref=uf_permalink" target="_blank">uma campanha de leads do Facebook e um formulário de anúncios de leads do Facebook</a>.

É possível usar um endereço de e-mail ou um número de telefone ao fazer uma solicitação ao [endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para atualizar ou criar o perfil do usuário. Por esse motivo, inclua um **campo de contato** para **e-mail** ou **telefone** no seu formulário de anúncio de leads. Se estiver coletando nomes ou sobrenomes, colete-os separadamente no seu formulário em vez de usar nomes completos.

### Etapa 2: Conecte sua conta do Facebook ao Zapier 

#### Etapa 2a: Selecione seu método de conexão no Zapier

No Zapier, acesse **Apps** para pesquisar os aplicativos do Facebook disponíveis. Selecione **Facebook Lead Ads** ou **Facebook Lead Ads (for Business admins)**.

Para saber mais sobre esses dois métodos de conexão de sua conta do Facebook ao Zapier, consulte:

- <a href="https://help.zapier.com/hc/en-us/articles/8496123584781-How-to-get-started-with-Facebook-Lead-Ads-for-Business-Admins-on-Zapier#h_01HC9VZFZG0GR2KRYM5EQJN329" target="_blank">Anúncios de leads do Facebook (para administradores de empresas)</a>
- <a href="https://help.zapier.com/hc/en-us/articles/8496061306253#h_01HC9VMZ2XP0017AR6SE7S30JG" target="_blank">Anúncios de leads do Facebook</a>

![]({% image_buster /assets/img/fb_lead_ads_zapier/integration1.png %}){: style="max-width:80%;"}

#### Etapa 2b: adicione o Zapier ao acesso de leads no Facebook Business Manager

Em seu Facebook Business Manager, acesse **Integrações** > **Acesso a leads** no menu à esquerda. Selecione sua página do Facebook e clique em **CRMs**. Na guia de CRM, selecione **Assign CRMs** (Atribuir CRMs) e adicione o **Zapier**.

![]({% image_buster /assets/img/fb_lead_ads_zapier/integration2.png %}){: style="max-width:80%;"}

Para obter as etapas para atribuir o Zapier como uma integração de CRM, consulte a <a href="https://www.facebook.com/business/help/540596413257598?id=735435806665862" target="_blank">documentação</a> do Facebook.

### Etapa 3: crie seu Zap

#### Etapa 3a: Criar o disparador 

Depois de conectar sua conta do Facebook, você poderá criar um Zap. Como **Trigger** (Gatilho), selecione **Facebook Lead Ads** ou **Facebook Lead Ads (for Business Admins)** com base na sua escolha na etapa 2. 

![]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap1.png %}){: style="max-width:80%;"}

Para o **evento**, selecione **New Leads** > **Continue** (Novos leads > Continuar). 

![]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap2.png %}){: style="max-width:80%;"}

Selecione sua conta do Facebook e, em seguida, **Continue**. 

![]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap3.png %}){: style="max-width:80%;"}

Selecione sua página do Facebook e o formulário instantâneo que você criou anteriormente e, em seguida, **Continue**.

![]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap4.png %}){: style="max-width:80%;"}

Em seguida, teste esse gatilho. Depois de validar a saída do formulário, selecione **Continue with selected record** (Continuar com o registro selecionado).

#### Etapa 3b: Criar uma ação

adicione uma nova etapa e selecione **Webhooks by Zapier**. Em seguida, selecione **Custom Request (Solicitação personalizada** ) para o campo **Event (Evento** ) e clique em **Continue (Continuar**). 

![]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap5.png %}){: style="max-width:80%;"}

Por fim, configure sua solicitação personalizada inserindo campos em sua carga útil. O trecho de código a seguir mostra um exemplo de carga útil. 

```
{
    "attributes": [
        {
            "email": "<insert_email_field>",
            "first_name": "<insert_first_name_field>",
            "last_name": "<insert_last_name_field>",
            "lead_form": "<insert_form_name_field>",
            "fb_campaign": "<insert_campaign_id_field>",
            "fb_ad_set": "<insert_campaign_id_field>",
            "fb_ad": "<insert_campaign_id_field>",
            "email_subscribe": "subscribed",
            "subscription_groups" : [{
                "subscription_group_id": "<subscription_group_id>",
                "subscription_state": "subscribed"
                }
            ]
        }
    ],
    "events": [
        {
            "email": "<insert_email_field>",
            "name": "<insert_custom_event_name>",
            "time": "<insert_timestamp_field>",
            "_update_existing_only": false
        }
    ]
}`
```

Aqui está um exemplo de como fica no Zapier:

![]({% image_buster /assets/img/fb_lead_ads_zapier/configuration_example.png %}){: style="max-width:80%;"}

Depois de configurar o webhook, selecione **Continue and test** (Continuar e testar). Se o teste for bem-sucedido, você poderá publicar seu Zap.

### Etapa 4: Teste seu Zap de anúncios de leads do Facebook

Para testar isso de ponta a ponta, use a Leads Ads Testing Tool (Ferramenta de testes de anúncios de leads) do Facebook no console de desenvolvedor do Facebook. Para saber mais, consulte <a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/testing-troubleshooting/" target="_blank">Testes e solução de problemas</a>.

## Gerenciamento de identidade do usuário

Essa integração permite atribuir seus leads do Facebook por e-mail por meio do [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#example-request-for-updating-a-user-profile-by-phone-number).

* Se o e-mail corresponder a um perfil de usuário existente, a Braze atualizará o perfil com os dados de usuário do Facebook.
* Se houver vários perfis de usuário com o mesmo e-mail, o Braze priorizará o perfil atualizado mais recentemente com um ID externo para atualizações.
* Se a ID externa não existir, o Braze dará prioridade ao perfil atualizado mais recentemente com o envio de e-mail correspondente.
* Se não houver um perfil com o e-mail fornecido, a Braze criará um novo perfil e um novo perfil de usuário alias. Para identificar os perfis de usuário de alias recém-criados, use o [endpoint `/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/).

{% alert note %}
Você também pode usar um número de telefone ou ID externo como parte da solicitação ao Braze se esses campos estiverem disponíveis e forem o identificador primário que você deseja para a integração. Para fazer isso, modifique a carga útil da sua solicitação conforme indicado no [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).
{% endalert %}

## Solução de problemas

{% details O teste do gatilho e da ação deu certo, mas por que não consigo publicar meu Zapier Zap? %}
Para usar essa integração, você deve ter um <a href="https://zapier.com/app/pricing/" target="_blank">plano Zapier</a> que ofereça suporte a apps premium.
{% enddetails %}

{% details Por que os leads do Facebook não estão sendo sincronizados com o Braze? %}
1. Verifique se você tem acesso de administrador à sua página do Facebook, conta de anúncios e acesso a leads. Em seguida, reconecte sua conta no Zapier.
2. Verifique se o formulário instantâneo que você criou no Facebook mapeia o formulário selecionado em sua etapa de disparo. 
3. Verifique se você atribuiu o Zapier ao acesso de leads em **Facebook Business Manager** > **Integrations** > **Lead Access** (Facebook Business Manager > Integrações > Acesso de leads).
{% enddetails %}

{% details Por que estou vendo perfis de usuário duplicados com o mesmo e-mail? %}
Há maneiras exclusivas de criar e gerenciar perfis de usuários no Braze com base no [ciclo de vida do perfil do usuário]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-profile-lifecycle).

Dependendo dos seus processos internos e de quando você estiver disparando a criação de clientes no Braze, poderá encontrar perfis de usuário duplicados devido a uma condição de corrida do perfil de usuário que está sendo criado pela integração e quando o usuário é criado a partir do seu sistema. É possível [mesclar perfis de usuários]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) no Braze.
{% enddetails %}

{% details Não tenho uma conta no Zapier. Como posso disparar webhooks do Facebook Lead Ads na Braze? %}
Se você não usa nem planeja usar o Zapier, é possível criar a integração diretamente do Facebook para a Braze. Consulte a <a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/" target="_blank">documentação do Lead Ads</a> para obter mais informações.

Para recuperar leads do Facebook, use <a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#webhooks" target="_blank">webhooks</a>. Consulte a <a href="https://developers.facebook.com/docs/graph-api/webhooks/getting-started" target="_blank">documentação de webhooks</a> para começar a usar webhooks no Facebook.

Depois de estabelecer o URL dos webhooks no Facebook, trabalhe com sua equipe para determinar o melhor caminho para encaminhar os dados para o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Semelhante à abordagem do Zapier, recomendamos fazer uma [solicitação por e-mail]({{site.baseurl}}/api/endpoints/user_data/post_user_track#example-request-for-updating-a-user-profile-by-phone-number) pelo endpoint `users/track`.
{% enddetails %}

{% alert tip %}
Para obter mais dicas de solução de problemas, consulte o <a href="https://help.zapier.com/hc/en-us/articles/8495982030861-Common-Problems-with-Facebook-Lead-Ads#h_01HC9V6Y652KQYYY96YG99T423" target="_blank">guia de solução de problemas de leads do Facebook do Zapier</a>.
{% endalert %}


