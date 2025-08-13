---
nav_title: 워크숍
article_title: Amazon Personalize 워크숍
alias: /partners/amazon_personalize_workshop/
description: "이 참조 문서에서는 Amazon Personalize를 구성하고 연결된 콘텐츠를 사용하여 Braze 환경에 통합하는 과정을 설명합니다."
page_type: partner
search_tag: Partner
---

# Amazon Personalize 워크숍

> 이 참조 문서에서는 Amazon Personalize를 구성하고 연결된 콘텐츠를 사용하여 Braze 환경에 통합하는 과정을 안내합니다. 이 작업은 Amazon Personalize 솔루션을 배포하고 훈련시키는 데 필요한 모든 단계를 안내하고 Braze 이메일 캠페인에 통합하는 실습 워크숍을 통해 수행됩니다.

_This integration is maintained by Amazon Personalize._

## 통합 정보

The following examples are deployed in a fully-functional example eCommerce site called the Retail Demo Store. 이 튜토리얼의 리소스와 코드는 [AWS 샘플 리테일 데모 스토어](https://github.com/aws-samples/retail-demo-store/)에 게시되어 있습니다. 이 참조 아키텍처 구현을 사용하여 Amazon Personalize를 자체 환경에 구현하는 개요로 사용할 수 있습니다.

## 요구 사항

[Retail Demo Store 리포지토리](https://github.com/aws-samples/retail-demo-store/)를 복제하고 워크숍 환경을 AWS 계정에 배포하는 단계를 따릅니다. 워크숍을 완료하고 통합 코드를 실행하려면 AWS 계정이 필요합니다.

## 통합 아키텍처

Before setting up Braze to send personalized messages to users, review the relevant components required for a typical eCommerce website, using the Retail Demo Store architecture as an example.

![Braze 개인화 아키텍처를 분해하여 다양한 구성 요소가 서로 어떻게 상호 작용하는지 설명하는 이미지입니다.]({% image_buster /assets/img/amazon_personalize/braze-personalize-arch.png %}){: style="max-width:70%" }

1. Retail Demo Store의 웹 UI는 AWS Amplify JavaScript 라이브러리를 사용하여 Amazon Personalize에 교육 이벤트를 보냅니다.
2. Braze 캠페인 사용자 기록은 글로벌 스토어 사용자 서비스에서 업데이트됩니다.
3. Braze 캠페인이 실행될 때 연결된 콘텐츠 템플릿을 사용하여 Personalize에서 추천을 가져와 대상 사용자의 이메일 템플릿을 채웁니다.
4. 제품 카탈로그 정보는 추천 모델을 훈련하는 데에도 사용할 수 있습니다.

Braze는 사용자의 행동 또는 고객 프로필의 속성에 따라 사용자에게 이메일을 보냅니다. 이 데이터는 사용자를 식별하고 고객 프로필을 구축하여 메시지나 이메일을 보낼 시기를 결정하는 데 도움이 될 수 있습니다.

이 이벤트 데이터 흐름은 Amazon Personalize에 전송되는 행동 이벤트 데이터와 병렬로 발생합니다. 이 워크숍에서는 데모 스토어가 Amplify를 사용하여 이벤트를 Personalize로 보냅니다. 이 데이터는 추천 모델을 훈련하는 데 사용되며, 이후 Braze 연결된 콘텐츠 호출에서 사용되어 Braze 캠페인이 실행될 때 사용자에게 맞게 콘텐츠를 개인화할 수 있습니다.

Braze 연결된 콘텐츠는 AWS에서 실행되는 추천 서비스를 통해 이러한 추천을 받을 수 있습니다. 리테일 데모 스토어 워크숍은 예제 추천 서비스 배포를 보여줍니다. 자체 인프라의 배포 시나리오에서 유사한 서비스를 배포하여 자체 카탈로그 서비스에서 항목을 가져와야 합니다.

## 참조 아키텍처 워크숍 설정

### 1단계: AWS 계정에 Retail Demo Store 배포

![사용 가능한 AWS 리전의 이미지입니다.][2]{: style="float:right;max-width:40%;margin-top:15px;margin-bottom:10px;"}

다음 표에서 **AWS 리전**을 선택하고 **스택 시작**을 선택합니다. 이 목록은 프로젝트를 배포할 수 있는 모든 가능한 리전을 나타내지 않습니다. Retail Demo Store를 배포하기 위해 현재 구성된 리전만 나타냅니다.

템플릿에 대한 모든 기본 매개변수를 수락합니다. 모든 프로젝트 리소스의 배포에는 25~30분이 소요됩니다.

### 2단계: 구축 Amazon Personalize 캠페인

개인화된 제품 추천을 제공하기 전에 먼저 머신 러닝 모델을 훈련시키고 Amazon Personalize에서 추천을 받을 수 있는 추론 엔드포인트를 제공해야 합니다. 1단계에서 배포된 CloudFormation 템플릿에는 단계별 자세한 지침고 함께 Jupyter 노트북을 제공하는 Amazon SageMaker 노트북 인스턴스가 포함되어 있습니다.

1. 1단계에서 AWS CloudFormation 템플릿을 배포한 AWS 계정에 로그인합니다.
2. Amazon SageMaker 콘솔에서 **노트북 인스턴스**를 선택합니다.
3. **RetailDemoStore** 노트북 인스턴스를 보지 못하면 1단계에서 프로젝트를 배포한 동일한 지역에 있는지 확인하십시오.
4. 노트북 인스턴스에 액세스하려면 **Jupyter 열기** 또는 **JupyterLab 열기**를 선택하십시오.
5. 노트북 인스턴스에 대해 Jupyter 웹 인터페이스가 로드되면 `workshop/1-Personalization/1.1-Personalize.ipynb` 노트북을 선택합니다. 노트북 하위 디렉토리를 보려면 `workshop` 폴더를 선택해야 할 수 있습니다.
6. `1.1-Personalize` 노트북을 열면 각 셀을 실행하여 워크숍을 진행합니다. Jupyter 툴 모음에서 **실행**을 선택하여 셀의 코드를 순차적으로 실행할 수 있습니다. 노트북을 완료하는 데 약 두 시간이 걸립니다.

### 3단계: Braze에서 개인화된 이메일 전송

Amazon Personalize 솔루션과 캠페인이 마련되면, 리테일 데모 스토어의 인스턴스가 이메일 캠페인에 추천을 제공할 준비가 됩니다. 1단계에서는 데모 웹 애플리케이션과 모든 관련 서비스(이메일 캠페인을 Braze와 연결된 콘텐츠를 통해 통합하는 데 필요한 추천 서비스 포함)를 배포했으며, 여기에는 2단계에서 배포한 Amazon Personalize 캠페인이 사용됩니다.

2단계의 개인화 워크숍과 유사하게, 다음 Braze 메시징 워크숍은 Braze와 Amazon Personalize 통합 설정 단계를 안내합니다.

1. 1단계에서 AWS CloudFormation 템플릿을 배포한 AWS 계정에 로그인합니다.
2. Amazon SageMaker 콘솔에서 **노트북 인스턴스**를 선택합니다.
3. **RetailDemoStore** 노트북 인스턴스를 보지 못하는 경우 프로젝트를 배포한 AWS 리전과 동일한 리전에 있는지 확인합니다.
4. 노트북 인스턴스에 액세스하려면 **Jupyter 열기** 또는 **JupyterLab 열기**를 선택하십시오.
5. 노트북 인스턴스에 대해 Jupyter 웹 인터페이스가 로드되면 `workshop/4-Messaging/4.2-Braze.ipynb` 노트북을 선택합니다. 노트북 하위 디렉토리를 보려면 `workshop` 폴더를 선택해야 할 수 있습니다.
6. `4.2-Braze` 노트북을 열면 각 셀을 실행하여 워크숍을 진행합니다. Jupyter 툴 모음에서 **실행**을 선택하여 셀의 코드를 순차적으로 실행할 수 있습니다. 노트북을 완료하는 데 약 1시간이 걸립니다.

### 4단계: 리소스 정리

향후 요금 발생을 피하려면 1단계에서 생성한 AWS CloudFormation 스택을 삭제하여 Retail Demo Store 프로젝트에서 생성한 AWS 리소스를 삭제하십시오.


[1]: {% image_buster /assets/img/amazon_personalize/braze-personalize-arch.png %}
[2]: {% image_buster /assets/img/amazon_personalize/region.png %}