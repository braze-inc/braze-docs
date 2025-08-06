---
nav_title: Knak
article_title: Knak
alias: /partners/knak/
description: "Este artigo de referência descreve a parceria entre Braze e Knak, uma plataforma de criação de campanhas que permite criar e-mails totalmente responsivos em minutos ou horas, em vez de dias ou semanas, e exportá-los como templates prontos para uso no Braze."
page_type: partner
search_tag: Knak

---

# Knak

> [Knak](https://knak.com/) é a primeira plataforma de criação de campanhas construída para equipes de marketing empresarial usarem internamente. A plataforma é intuitiva e fácil de usar e permite que qualquer pessoa crie e-mails e landing pages da marca em minutos, sem precisar de código ou ajuda externa.

_Esta integração é mantida pela Knak._

## Sobre a integração

A integração Braze e Knak permite que você crie e-mails totalmente responsivos em minutos ou horas, em vez de dias ou semanas, e os exporte como modelos Braze prontos para uso. Knak é feito para profissionais de marketing que desejam aprimorar a criação de e-mails para campanhas gerenciadas no Braze, sem a necessidade de agências externas ou codificação manual. 

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta da Knak | É necessário ter uma conta Knak para aproveitar esta parceria. |
| Chave da API REST do Braze | Uma chave da API REST da Braze com permissões completas de **modelos**. <br><br>Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST do Braze | [Sua URL de endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Seu endpoint dependerá do URL do Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso

Knak é feito para profissionais de marketing que desejam aprimorar a criação de seus e-mails, sem necessidade de codificação ou ajuda externa. É ótimo para aqueles que:
- Usam modelos simples para e-mails e querem mudar de patamar
- Dependa de agências externas ou desenvolvedores para criar e-mails para a Braze
- Quer retomar o controle criativo sobre a criação de ativo e chegar ao mercado consideravelmente mais rápido

## Integração

### Etapa 1: Configure sua integração

Na Knak, navegue para **Integrations > Platforms > + Add New Integration** (Integrações > Plataformas > + Adicionar nova integração).

![Adicionar botão de integração]({% image_buster /assets/img/knak/integration-setup-step-2-add-new-integration.png %})

Em seguida, selecione a plataforma **Braze** e forneça a chave de API e o endpoint REST da Braze. Clique em **Criar Nova Integração** para completar sua integração. 

![Criar nova integração]({% image_buster /assets/img/knak/integration-setup-step-4-add-api-key.png %})

### Etapa 2: Sincronize seus templates Knak

No Knak, localize um e-mail que você gostaria de sincronizar com o Braze e selecione **Publicar** e depois **Sincronizar**.

![Integração Knak 1]({% image_buster /assets/img/knak/integration-post-step-1-sync.png %})

Em seguida, verifique o nome do e-mail e clique em **Sync** (Sincronizar).

![Integração Knak 2]({% image_buster /assets/img/knak/integration-post-step-2-asset-name.png %})

## Usando a Integração

Você pode encontrar seus e-mails da Knak carregados na Braze em **Engajamento > Modelos e mídia**. Eles serão bonitos, de acordo com a marca e totalmente responsivos. O único limite é a sua própria criatividade!


