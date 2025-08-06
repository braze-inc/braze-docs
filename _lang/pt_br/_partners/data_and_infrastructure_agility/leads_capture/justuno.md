---
nav_title: Justuno
article_title: Justuno
description: "Saiba como integrar o Justuno ao Braze para que você possa aproveitar os dados do cliente em ambas as plataformas para criar experiências mais personalizadas para todos os públicos."

alias: /partners/justuno
page_type: partner
search_tag: Partner
---

# Justuno

> [O Justuno](https://www.justuno.com/) permite criar experiências de visitantes totalmente otimizadas para todos os seus públicos com segmentos dinâmicos, oferecendo o direcionamento mais avançado disponível - tudo sem afetar a velocidade do site ou aumentar o trabalho de desenvolvimento. Analise as taxas de conversão visualizando análises de dados personalizadas, como o número de perfis criados, a taxa de visitantes de retorno influenciados e as páginas por sessão para manter uma vantagem de marketing em seu setor. A Justuno o capacita a aumentar a receita por visitante, estabelecer engajamentos significativos com os clientes e expandir seus negócios. Otimize toda a jornada do público de ponta a ponta com uma plataforma conectada.

## Casos de uso

O Braze permite que qualquer profissional de marketing colete e aja com base em qualquer quantidade de dados de qualquer fonte, para que você possa se engajar de forma criativa com os clientes em tempo real, em todos os canais, a partir de uma única plataforma.

A integração do Justuno e do Braze lhe dá o melhor dos dois mundos. Você pode combinar os dados do cliente salvos no Braze com os dados do visitante e do cliente salvos no Justuno e criar experiências mais personalizadas para todos os públicos. Isso aumenta a eficácia de suas campanhas de marketing e o engajamento dos clientes.

## Pré-requisitos

| Chave da API REST do Braze | Uma chave da API REST do Braze com as permissões `users.track` e `custom_attributes.get`.<br><br>Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Seu URL do ponto de extremidade REST. Seu endpoint dependerá do [URL do Braze para sua instância]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints).
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração do Justuno com o Braze

### Etapa 1: Criar atributos personalizados no Braze

Para sincronizar as atribuições do usuário do Justuno para o Braze, será necessário criar esses atributos no Braze, caso ainda não o tenha feito. Você pode fazer isso acessando **Configurações de dados** > **Atributos personalizados** e, em seguida, criando seus atributos personalizados. Para obter um passo a passo completo, consulte [Gerenciando atributos personalizados no Braze]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/).

### Etapa 2: Adicionar o app Braze ao Justuno

#### Etapa 2.1: Adicione-o à sua conta

Para adicionar o aplicativo Braze à sua conta Justuno, acesse **Configurações da conta** > **Apps** e, em seguida, procure e selecione o aplicativo Braze.

![A página "Connect Apps" (Conectar aplicativos) no Justuno com o aplicativo Braze mostrado na lista de resultados de pesquisa.]({% image_buster /assets/img/justuno/search-for-braze.png %})

Digite a chave de API e o URL de base [que você criou anteriormente](#prerequisites) e selecione **Connect (Conectar**).

![A janela pop-up de autenticação do Braze solicita uma chave de API do Braze e um URL de base.]({% image_buster /assets/img/justuno/authenticate-braze.png %}){: style="max-width:75%;"}

#### Etapa 2.2: Adicione-o ao seu fluxo de trabalho

Para adicionar o aplicativo Braze ao seu [fluxo de trabalho Justuno](https://hub.justuno.com/knowledge/workflows-overview), arraste e solte a ação **Sync to App** em seu fluxo de trabalho e, em seguida, escolha **Select App** > **Braze**.

![A opção "Select App" (Selecionar aplicativo), localizada na ação "Sync to App" (Sincronizar com o aplicativo).]({% image_buster /assets/img/justuno/select-app.png %}){: style="max-width:45%;"}

### Etapa 3: Conecte seus grupos de inscrições do Braze

Para enviar dados de perfil do Justuno para um e-mail específico do Braze ou para um grupo de inscrições para e-mail ou SMS, você precisará adicionar o ID deles ao app do Braze em seu fluxo de trabalho do Justuno.

| Tipo de ID                          | Necessário? | Descrição                                                                                                   |
|----------------------------------|-----------|---------------------------------------------------------------------------------------------------------------|
| ID do grupo de inscrições do Braze SMS  | Sim       | Esse ID é usado para coletar o consentimento de SMS dos perfis de usuário. Se nenhuma ID for inserida no Justuno, os perfis não terão consentimento quando o Justuno empurrar esse perfil para o Braze. |
| ID do grupo de inscrições para e-mail do Braze | Não        | Se essa ID não for inserida no Justuno, o Justuno enviará os dados do perfil para o Braze como um usuário sem grupos de inscrições associados. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Etapa 3.1: Localize as IDs no Braze

Para localizar essas IDs no dashboard do Braze:

1. Acesse **Público** > **Inscrições**.
2. Para cada grupo de inscrições, note a ID localizada na coluna ID.

#### Etapa 3.2: Adicione as IDs ao app Braze

Em seu fluxo de trabalho Justuno, abra o app Braze e insira os IDs de cada grupo de inscrições.

![O aplicativo Braze foi aberto em um fluxo de trabalho Justuno com a opção de adicionar IDs de grupo de inscrições para e-mail e SMS.]({% image_buster /assets/img/justuno/enter-subscription-groups.png %}){: style="max-width:55%;"}

### Etapa 4: Configure suas atribuições

As seguintes atribuições são sincronizadas automaticamente do Justuno para o Braze:

- E-mail  
- Telefone  
- Nome  
- Sobrenome  
- Idioma  
- Gênero  
- País

Para sincronizar atribuições adicionais:

1. No app Braze em seu fluxo de trabalho, selecione **Sync Another Property (Sincronizar outra propriedade**).
    ![O app Braze foi aberto em um fluxo de trabalho Justuno mostrando a opção "Sync Another Property" (Sincronizar outra propriedade).]({% image_buster /assets/img/justuno/sync-another-property.png %}){: style="max-width:55%;"}
2. Escolha quais atribuições do Braze você gostaria de sincronizar.
3. Combine as propriedades no Justuno com seus equivalentes no Braze (como identificadores sociais, data de aniversário, preferências de compras, respostas a pesquisas e similares). Lembre-se de que essas propriedades são consideradas dados de terceiros ou de terceiros. Para saber mais, consulte [Justuno: Coleta de dados de visitantes](https://www.justuno.com/guides/zero-first-party-data/).
4. No construtor de fluxo de trabalho, escolha **Salvar**, **Pré-visualizar** ou **Publicar** seu fluxo de trabalho.
    ![O menu "Publish" (Publicar) foi aberto com as opções de salvar, fazer uma prévia ou mostrar o histórico da versão.]({% image_buster /assets/img/justuno/publish-workflow.png %}){: style="max-width:45%;"}

## Coisas para saber

- Você deve inserir manualmente o ID do grupo de inscrições nas configurações do app.  
- Os seguintes tipos de dados do Braze **não** são suportados: Objeto, vetor de objetos.  
- O consentimento implícito de SMS é fornecido quando o campo de consentimento de SMS do Justuno não é usado.  
- O consentimento explícito por SMS será respeitado se o design do Justuno incluir o campo de consentimento.
