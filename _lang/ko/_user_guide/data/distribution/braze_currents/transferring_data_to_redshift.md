---
nav_title: Redshift로 데이터 전송
article_title: 데이터를 Redshift로 전송
page_order: 8
page_type: tutorial
description: "이 사용법 문서에서는 추출, 변환, 로드(ETL) 프로세스를 통해 Amazon S3에서 Redshift로 데이터를 전송하는 방법을 안내합니다."
tool: Currents

---

# Redshift로 데이터 전송

> [Amazon Redshift는](https://aws.amazon.com/redshift/) Amazon S3와 함께 Amazon Web Services에서 실행되는 인기 있는 데이터 웨어하우스입니다. Currents의 Braze 데이터는 Redshift로 직접 전송할 수 있도록 구조화되어 있습니다.

다음은 Amazon S3에서 Redshift로 데이터를 전송하는 방법을 설명합니다. 이 과정은 추출, 변환, 로드(ETL) 프로세스를 통해 이루어집니다. 전체 소스 코드는 Currents 예제 [GitHub 리포지토리](https://github.com/Appboy/currents-examples)를 참조하십시오.

{% alert important %}
이는 데이터를 가장 유리한 장소로 이전할 때 선택할 수 있는 여러 옵션 중 하나일 뿐입니다.
{% endalert %}

## S3에서 Redshift 로더 개요

[`s3loader.py`](https://github.com/Appboy/currents-examples/tree/master/redshift-s3-loader) 스크립트는 이미 복사된 파일을 추적하기 위해 동일한 Redshift 데이터베이스에 별도의 매니페스트 테이블을 사용합니다. 일반 구조는 다음과 같습니다:

1. S3의 모든 파일을 나열한 다음, 매니페스트 테이블의 내용과 비교하여 마지막으로 실행한 `s3loader.py` 이후의 새로운 파일을 식별합니다.
2. 새로운 파일을 포함하는 [매니페스트](http://docs.aws.amazon.com/redshift/latest/dg/loading-data-files-using-manifest.html) 파일을 생성합니다.
3. 매니페스트 파일을 사용하여 S3에서 Redshift로 새로운 파일을 복사하는 `COPY` 쿼리를 실행합니다.
4. 복사된 파일의 이름을 Redshift의 별도 매니페스트 테이블에 삽입합니다.
5. 커밋합니다.

## 종속성

로더를 실행하려면 AWS Python SDK와 Psycopg를 설치해야 합니다:

```bash
pip install boto3
pip install psycopg2
```

## 권한

### S3 읽기 권한이 있는 Redshift 역할

아직 하지 않았다면, [AWS 설명서](http://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-create-an-iam-role.html)를 따라 S3의 파일에서 `COPY` 명령을 실행할 수 있는 역할을 생성하십시오.

### Redshift VPC 인바운드 규칙

Redshift 클러스터가 VPC에 있는 경우, S3 로더를 실행하는 서버에서 연결을 허용하도록 VPC를 구성해야 합니다. Redshift 클러스터로 들어가서 로더가 연결할 VPC 보안 그룹 항목을 선택합니다. 그런 다음, 새로운 인바운드 규칙을 추가합니다: **유형** = Redshift, **프로토콜** = TCP, **포트** = 클러스터의 포트, **소스** = 로더를 실행하는 서버의 IP(또는 테스트를 위한 "어디서나").

### S3 전체 액세스 권한이 있는 Identity and Access Management (IAM) 사용자

S3 로더는 Currents 데이터가 포함된 파일에 대한 읽기 액세스와 Redshift `COPY` 명령을 위해 생성된 매니페스트 파일의 위치에 대한 전체 액세스가 필요합니다. [IAM 콘솔](https://console.aws.amazon.com/iam/home#/users)에서 `AmazonS3FullAccess` 권한으로 새로운 Identity and Access Management (IAM) 사용자를 생성하십시오. 자격 증명을 저장하십시오. 로더에 전달해야 합니다.

환경 변수, 공유 자격 증명 파일 (`~/.aws/credentials`) 또는 [AWS 구성 파일](http://boto3.readthedocs.io/en/latest/guide/configuration.html#configuring-credentials)을 통해 로더에 액세스 자격 증명을 전달할 수 있습니다. 또는 `S3LoadJob` 객체 내의 `aws_access_key_id` 및 `aws_secret_access_key` 필드에 할당하여 로더에 직접 포함할 수 있지만, 소스 코드 내에 자격 증명을 하드 코딩하는 것은 권장하지 않습니다.

## Usage

### 샘플 사용법

다음 샘플 프로그램은 S3에서 Redshift의 `content_card_impression` 테이블로 `users.messages.contentcard.Impression` 이벤트에 대한 데이터를 로드합니다.

```
if __name__ == '__main__':
    host = '{YOUR_CLUSTER}.redshift.amazonaws.com'
    port = 5439
    database = '{YOUR_DATABASE}'
    user = '{YOUR_USER}'
    password = '{YOUR_PASSWORD}'
    role = '{YOUR_REDSHIFT_ROLE_ARN}'

    # Do not hard code these credentials.
    aws_access_key_id = None
    aws_secret_access_key = None

    # Content Card Impression Avro fields:
    #   id            - string
    #   user_id       - string
    #   external_user_id - string (nullable)
    #   app_id        - string
    #   content_card_id  - string
    #   campaign_id   - string (nullable)
    #   send_id       - string (nullable)
    #   time          - int
    #   platform      - string (nullable)
    #   device_model  - string (nullable)

    print('Loading Content Card Impression...')
    cc_impression_s3_bucket = '{YOUR_CURRENTS_BUCKET}'
    cc_impression_s3_prefix = '{YOUR_CURRENTS_PREFIX}'
    cc_impression_redshift_table = 'content_card_impression'
    cc_impression_redshift_column_def = [
        ('id', 'text'),
        ('user_id', 'text'),
        ('external_user_id', 'text'),
        ('app_id', 'text'),
        ('content_card_id', 'text'),
        ('campaign_id', 'text'),
        ('send_id', 'text'),
        ('time', 'integer'),
        ('platform', 'text'),
        ('device_model', 'text')
    ]

    cc_impression_redshift = RedshiftEndpoint(host, port, database, user, password,
        cc_impression_redshift_table, cc_impression_redshift_column_def)
    cc_impression_s3 = S3Endpoint(cc_impression_s3_bucket, cc_impression_s3_prefix)

    cc_impression_job = S3LoadJob(cc_impression_redshift, cc_impression_s3, role,
        aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    cc_impression_job.perform()
```

### 자격증명

로더를 실행하려면 Redshift 클러스터의 `host`, `port`, `database`와 `user` 및 `password`를 제공해야 합니다. 이 Redshift 사용자는 `COPY` 쿼리를 실행할 수 있습니다. 또한, 이전 섹션에서 생성한 S3 읽기 액세스가 있는 Redshift 역할의 ARN을 제공해야 합니다.

```
host = '{YOUR_CLUSTER}.redshift.amazonaws.com'
port = 5439
database = '{YOUR_DATABASE}'
user = '{YOUR_USER}'
password = '{YOUR_PASSWORD}'
role = '{YOUR_REDSHIFT_ROLE_ARN}'
```

### 작업 구성

이벤트 파일의 S3 버킷 및 접두사와 로드할 Redshift 테이블 이름을 제공해야 합니다.

또한, 로더에서 요구하는 "자동" 옵션으로 Avro 파일을 `COPY`하려면 Redshift 테이블의 열 정의가 샘플 프로그램에 표시된 Avro 스키마의 필드 이름과 일치해야 하며, 적절한 유형 매핑이 필요합니다(예: `string`에서 `text`으로, `int`에서 `integer`으로).

모든 파일을 한 번에 복사하는 데 너무 오랜 시간이 걸린다면 로더에 `batch_size` 옵션을 전달할 수도 있습니다. `batch_size`를 전달하면 로더가 한 번에 하나의 배치를 점진적으로 복사하고 커밋할 수 있습니다. 모든 것을 동시에 복사할 필요가 없습니다. 하나의 배치를 로드하는 데 걸리는 시간은 `batch_size`뿐만 아니라 파일 크기와 Redshift 클러스터 크기에 따라 다릅니다.

```
# Content Card Impression Avro fields:
#   id            - string
#   user_id       - string
#   external_user_id - string (nullable)
#   app_id        - string
#   content_card_id  - string
#   campaign_id   - string (nullable)
#   send_id       - string (nullable)
#   time          - int
#   platform      - string (nullable)
#   device_model  - string (nullable)
cc_impression_s3_bucket = '{YOUR_CURRENTS_BUCKET}'
cc_impression_s3_prefix = '{YOUR_CURRENTS_PREFIX}'
cc_impression_redshift_table = 'content_card_impression'
cc_impression_redshift_column_def = [
    ('id', 'text'),
    ('user_id', 'text'),
    ('external_user_id', 'text'),
    ('app_id', 'text'),
    ('content_card_id', 'text'),
    ('campaign_id', 'text'),
    ('send_id', 'text'),
    ('time', 'integer'),
    ('platform', 'text'),
    ('device_model', 'text')
]
cc_impression_batch_size = 1000
```