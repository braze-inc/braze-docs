---
nav_title: Branch para deep linking
article_title: Branch para deep linking
alias: /partners/branch_for_deeplinking/
page_type: partner
description: "Este artigo de referência descreve a parceria entre a Braze e a Branch e como usá-la para oferecer suporte às suas práticas de deep linking."
search_tag: Partner

---

# Branch para deep linking {#branch}

{% multi_lang_include video.html id="PwGKqfwV-Ss" align="right" %}

> A [Branch][1] é uma plataforma de deeplinking móvel que ajuda a adquirir, engajar e medir em todos os dispositivos, canais e plataformas por meio de uma visão holística de todos os pontos de contato dos usuários.

A integração entre a Braze e a Branch permite oferecer melhores experiências aos seus clientes, pois você pode [atribuir]({{site.baseurl}}/partners/advertising_technologies/attribution/branch_for_attribution/) adequadamente o início da jornada do usuário e conectá-los por deep linking ao local pretendido.

## Integração

Siga as instruções do [guia de integração de SDKs da Branch](https://help.branch.io/developers-hub/docs/native-sdks-overview) para configurar sua integração. Consulte os casos de uso adicionais a seguir.

### Suporte a links universais do iOS

Para obter suporte ao envio de links universais do iOS como deep links na Braze:

1. Siga a documentação da Branch para configurar [links universais][3].
2. Implemente o método [`BrazeDelegate`][4][braze(_:shouldOpenURL:)][5] em sua integração do SDK do Braze para [rotear links universais][6] de dentro do seu app.

### Deep linking em e-mails

Consulte nossa documentação sobre [links universais e llinks de app]({{site.baseurl}}/help/help_articles/email/universal_links/)


O vínculo a números de telefone (anexando `tel` a `href`) não é compatível com o aplicativo Gmail para iOS, a menos que o usuário conceda permissões de chamada ao app.

Dependendo de seu ESP, pode ser necessária uma personalização adicional para oferecer suporte a links universais com rastreamento de cliques. Essas informações estão descritas em nosso artigo específico. Você também pode consultar as seguintes referências para saber mais:

- [SendGrid][7]
- [SparkPost][9]

[1]: https://branch.io/
[2]: {{site.baseurl}}/partners/branch_for_attribution/
[3]: https://help.branch.io/developers-hub/docs/ios-universal-links
[4]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate
[5]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:shouldopenurl:)-6xxc5
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking/#linking-handling-customization
[7]: https://help.branch.io/using-branch/page/braze-sendgrid
[9]: https://help.branch.io/using-branch/page/braze-sparkpost
