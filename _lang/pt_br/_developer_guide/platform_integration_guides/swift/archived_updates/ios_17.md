---
nav_title: Guia de atualização do iOS 17
article_title: Guia de atualização do iOS 17
page_order: 7
platform: 
  - iOS
description: "Este artigo aborda insights sobre a versão do iOS 17 para ajudar você a fazer upgrade do seu SDK sem problemas."
hidden: true
noindex: true
---

# Guia de atualização do iOS 17

> Quer saber como a Braze está se preparando para o próximo lançamento do iOS? Este artigo resume nossos insights sobre o lançamento do iOS 17 para ajudá-lo a criar uma experiência perfeita para você e seus usuários.

## Compatibilidade com iOS 17 e Xcode 15

O Braze Swift SDK e o Objective C SDK são compatíveis com versões anteriores do Xcode 14 e do Xcode 15 e com dispositivos iOS 17.

## Alterações no iOS 17

### Rastreamento de links e remoção de parâmetros UTM

Uma das mudanças importantes no iOS 17 é o bloqueio de parâmetros UTM no Safari. Os parâmetros UTM são pedaços de código adicionados aos URLs, que são frequentemente usados em campanhas de marketing para medir a eficácia de e-mails, SMS e outros canais de envio de mensagens. 

Essa alteração não afeta o rastreamento de cliques por e-mail do Braze e os envios de encurtamento de links por SMS.

### Transparência no rastreamento de aplicativos

A Apple anunciou seu compromisso de expandir o escopo do [Ad Tracking Transparency (ATT)](https://support.apple.com/en-us/HT212025), que ativa a capacidade dos usuários de controlar se um aplicativo pode acessar sua atividade em apps e sites pertencentes a outras empresas. A versão 17 do iOS contém dois recursos importantes da ATT: manifestos de privacidade e fazer login no código.

#### Manifestos de privacidade

A Apple agora exige um arquivo de manifesto de privacidade que descreva o motivo pelo qual seu app e os SDKs de terceiros coletam dados, juntamente com seus métodos de coleta de dados. A partir do iOS 17.2, a Apple bloqueará todos os endpoints de rastreamento declarados em seu app até que o usuário final aceite o prompt da ATT.

O Braze lançou nosso próprio manifesto de privacidade, juntamente com novas APIs flexíveis que redirecionam automaticamente os dados de rastreamento declarados para pontos de extremidade dedicados em `-tracking`. Para saber mais, consulte o [manifesto de privacidade da Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/privacy_manifest).

#### Assinatura de código

A assinatura de código permite que os desenvolvedores que usam um SDK de terceiros em seu aplicativo validem que o mesmo desenvolvedor fez o login em versões anteriores no Xcode. 

### SDK do Braze e privacidade

A Apple também anunciou que divulgará uma lista de SDKs de terceiros que são considerados "afetando a privacidade" no final de 2023. Espera-se que esses SDKs tenham um impacto especialmente alto na privacidade do usuário pela Apple.

Ao contrário dos SDKs de rastreamento tradicionais, projetados para monitorar usuários em vários sites e aplicativos, o SDK da Braze se concentra no envio de mensagens de dados primários e nas experiências de usuários.

Embora não esperemos que o SDK da Braze seja incluído nessa lista, pretendemos monitorar essa situação de perto e lançar as atualizações necessárias.
