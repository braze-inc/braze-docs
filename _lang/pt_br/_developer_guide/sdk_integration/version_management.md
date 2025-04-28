---
page_order: 10
nav_title: Gerenciamento de versões
article_title: Sobre o gerenciamento de versões do Braze SDK
description: "Saiba mais sobre o gerenciamento de versões do Braze SDK."
---

# Sobre o gerenciamento de versões

> Saiba mais sobre o gerenciamento de versões do Braze SDK, para que seu app possa se manter atualizado com os recursos e as melhorias de qualidade mais recentes. Como as versões mais antigas do SDK podem não receber o patch, a correção de bug ou o suporte mais recentes, recomendamos sempre mantê-lo atualizado como parte de seu ciclo de vida de desenvolvimento contínuo.

## Recomendações de controle de versão

Todos os SDKs do Braze aderem à [Semantic Versioning Specification (SemVer)](https://semver.org/), portanto, dado um número de versão `MAJOR.MINOR.PATCH`, recomendamos o seguinte:

|versão|Sobre esta versão|Recomendação|
|-------|------------------|--------------|
| `PATCH` | As atualizações são sempre ininterruptas e incluem correções de bugs importantes. Eles sempre estarão seguros. | Você deve sempre tentar atualizar para a versão mais recente do patch de sua versão principal e secundária atual imediatamente. |
| `MINOR` | As atualizações são sempre ininterruptas e incluem novas funcionalidades líquidas. Eles nunca exigirão alterações no código de seu aplicativo. | Embora não seja necessário fazer isso imediatamente, você deve atualizar para a versão secundária mais recente de sua versão principal atual assim que possível. 
| `MAJOR` | As atualizações são mudanças significativas e podem exigir alterações no código do aplicativo. | Como isso pode exigir alterações no código, atualize para a versão principal mais recente em um período que seja melhor para a sua equipe. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert note %}
Às vezes, novas atualizações do Android ou do sistema operacional da Apple exigem alterações no SDK do Braze. Para garantir que seu app seja compatível com telefones mais novos, é importante manter o SDK atualizado.
{% endalert %}

## Sobre problemas conhecidos

Para garantir que as nossas alterações não danifiquem os seus pipelines de compilação, **nunca alteraremos ou removeremos uma versão depois que ela for publicada em um sistema de distribuição, mesmo**que essa versão específica tenha problemas conhecidos.

Nesses casos, documentaremos o problema no [changelog do Braze SDK]({{site.baseurl}}/developer_guide/changelogs/) e, em seguida, lançaremos um novo patch para as versões principais ou secundárias afetadas o mais rápido possível.
