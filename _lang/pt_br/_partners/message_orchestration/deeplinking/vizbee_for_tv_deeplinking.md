---
nav_title: Vizbee
article_title: Vizbee para deep linking de TV
alias: /partners/vizbee/
page_type: partner
description: "Este artigo de referência descreve a parceria entre a Braze e a Vizbee e como usá-la para oferecer suporte ao deep linking de TV."
search_tag: Partner

---
# Vizbee {#vizbee}

> [O Vizbee](https://vizbee.tv/) ativa a capacitação de todos os smartphones e TVs inteligentes em sua casa para trabalharem juntos como um dispositivo contínuo para proporcionar excelentes experiências ao usuário. A Vizbee ajuda a usar os canais de marketing existentes para app móvel, como notificações, deep linkings e e-mails, para adquirir e engajar com praticidade os espectadores em todos os dispositivos de TV conectada (CTV) (como Roku, FireTV, TV Samsung, TV LG etc.).

_Essa integração é mantida pela Vizbee._

## Sobre a integração

A integração do Braze e do Vizbee permite que você use um único console para programar suas campanhas de marketing para adquirir e reter espectadores em apps de streaming em dispositivos móveis e de CTV. Com essa integração, você pode:
- Programe uma notificação móvel para os usuários direcionados que, ao serem tocados, podem resultar na visualização do app móvel ou invocar perfeitamente a reprodução em um dispositivo de streaming ou TV nas proximidades.
- Programe uma campanha de envio de e-mail marketing para usuários direcionados, o que, ao ser ativado, pode resultar em instalações automáticas do app CTV e fazer login do usuário em um dispositivo CTV, como Roku ou FireTV.

## Pré-requisitos

| Requisito | Descrição |
|---|---|
| Conta Vizbee | É necessário ter uma conta [Vizbee](https://vizbee.tv/) para aproveitar essa parceria. É necessário registrar seu app na Vizbee e ter um ID da Vizbee atribuída. |
| app iOS ou Android | Essa integração é compatível com os apps para iOS e Android. Dependendo da sua plataforma, trechos de código podem ser necessários em seu aplicativo. |
| SDK do Vizbee | Além do SDK da Braze obrigatório, você deve instalar o SDK da Vizbee. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

Siga as instruções do [Guia de integração SDKs](https://console.vizbee.tv/app/vzb1765003429/develop/guides/ios-continuity) da Vizbee para configurar sua integração com a Braze. Aqui você pode encontrar orientações sobre deep linking do celular para a TV, instalações de apps de TV e atribuição de visualizações. 

### Visualização de relatórios de instalação e atribuição {#vizbee-tv-app-installs-viewership-attribution}

A Vizbee e a Braze também capacitam você a visualizar o desempenho holístico das suas campanhas em dispositivos móveis e de CTV. O SDK da Vizbee envia eventos personalizados para o SDK da Braze que podem ser visualizados nos seus relatórios de campanha no dashboard da Braze.


