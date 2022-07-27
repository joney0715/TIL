# 6장 인증과 권한 부여 - AWS Identity and Access Management

## 6-1 IAM 자격 증명

### IAM 정책

* IAM 정책은 AWS 리소스에 연결된 작업을 정의하는 문서
* 정책 문서에서 효과를 지정해서 작업을 허용할지 여부를 결정 (효과 값은 허용 또는 거부를 사용)
* IAM 정책은 사전에 설정된 정책을 검색해서 찾거나 JSON형식의 정책을 생성도 가능 (하기 예시 참고)
* 기본적으로 명시하지 않은 작업은 모두 거부
* 모두 허용을 하고 일부는 거부하는 효율적인 제어 가능
* 허용과 거부가 충돌하는 경우는 거부를 우선으로 적용

{
	“version” : “2012-10-17”,
	“Statement” : [
		{
			“Effect” : “Allow”,
			“Action” : “*”,
			”Resource” : “*”
		}
	]
} 

### 사용자와 루트 계정

* 루트 계정을 보호하는 다음과 같은 방법이 있음
    - 루트와 연결된 모든 액세스 키를 삭제
    - 길고 복잡하게 비밀번호를 만들고 안전한 비밀번호 보관서에 저장
    - 루트 계정에 멀티 펙터 인증(MFA)을 사용
    - 가능하면 아무데서나 루트를 사용해서 관리 및 운영을 수행하지 않음
* 최소 하나의 사용자를 새로 생성해서 충분한 권한을 할당 필요
* 주 관리자에게는 AdminstratorAccess 정책을 부여 (다른 사용자에게 권한을 부여할 수 있는 권한)

### 액세스 키

* 액세스 키는 프로그래밍 방식 또는 CLI를 통해 액세스할 때 인증에 사용
* 애플리케이션에 사용자 이름과 비밀번호를 입력하는 방식 이외에 액세스 키 ID와 보안 액세스 키로 로컬 환경에서 액세스 할 수 있게 함

* 미사용 키 비활성화
    - 보안을 위해 사용하지 않는 키는 비활성화 또는 삭제 필요

* 키 교체
    - 키 사용 기간이 길수록 보안에 취약해지므로 오래된 키는 정기적으로 폐기 필요 (30일 주기로 감사 필요)
    - EC2 리소스에게 다른 AWS 서비ㅅ에 액세스할 권한을 부여하는 IAM 역할에서는 키 교체가 자동으로 이뤄짐
    - 부여된 키를 자체 애플리케이션에서 사용하면 관리가 복잡해지므로 다음의 절차 필요
        1. 각 사용자에게 새로운 액세스 키를 생성, 사용자가 자신의 키를 관리하도록 권한도 부여
        2. 새로운 키를 사용하도록 애플리케이션 설정을 업데이트
        3. 이전 키를 비활성화 (삭제하지 않음)
        4. 애플리케이션을 관찰해서 모든 갱신이 성공적인지 확인 (CLI 명령으로 확인 가능)
        5. 애플리케이션이 이전 키를 사용하지 않는 것이 확인되면 이전 키를 삭제

### 그룹

* 계정이 많이지면 관리가 복잡해지므로 그룹 생성하여 연결
* IAM 그룹을 이요하면 특정 직무 유형의 액세스 프로필을 변경할 때 그룹만 업데이트하면 편리함

### 역할

* IAM 역할은 임시 자격 증명으로 계정의 리소스에 액세스하려는 사용자나 서비스의 요청에 사용
* 다른 AWS 계정의 사용자나 연동 인증 서비스를 사용해 로그인한 사용자에게 계정의 리소스에 액세스할 수 있게 임시로 권한 부여 가능
* 만료 기간 기본 설정은 12시간
* 새로운 역할은 액세스 권한을 부여할 신뢰할 수 있는 엔티티를 정해서 생성 (신뢰할 수 있는 엔티티는 4가지)
    - AWS 서비스
    - 다른 AWS 계정 (계정 ID)
    - Amazon, Facebook, Google 로그인을 사용해서 인증하는 웹 자격 증명
    - 별도록 정의한 SAML 공급자를 통한 SAML 2.0
* 엔티티가 정의되면 자체 정책 문서를 작성해서 연결하거나, 미리 설정된 IAM 정책을 할당해서 사용 권한 부여
* 신뢰할 수 있는 엔티티에 새 역할을 부여하면 AWS는 AWS STS(Security Token Service)를 사용해서 기간 한정 보안 토큰을 발급
* 


## 6-2 인증 도구

* AWS는 최대한 많은 사용자와 리소스를 관리할 수 있는 다양한 인증 도구를 제공
* Amazon Cognito, AWS Managed Microsoft AD, AWS Single Sign-On 서비스는 사용자 인증을 처리하기 위한 서비스
* AWS KMS, AWS Secrets Manager, AWS CloudHSM 은 암호화 키와 인증 기밀의 관리를 단순화

### Amazon Cognito

* Cognito는 모바일과 웹 앱 개발자에게 두 가지 중요한 인증 기능 제공
    - Cognito의 사용자 풀로 애플리케이션에 사용자 등록과 로그인을 추가 가능
    - Cognito의 자격 증명 풀로 애플리케이션 사용자에게 AWS 계정 내 다른 서비스 액세스를 임시로 제어 가능
* Cognito는 가입하거나 로그인할 때 사용자가 자격 증명하는 방법을 정의해서 새로운 사용자 풀을 구축
* 비밀번호 복잡도, 멀티 팩터 인증, 전자 메일 확인을 위한 최소 요구 사항을 설정 가능
* 자격 증명 풀을 설정할 때 사용자가 어떤 서비스를 사용할지 정의 가능
* IAM 역할을 자격 증명 풀에 할당하고, 풀이 활성화 되면 리소스에 액세스할 수 있도록 설정

### AWS Managed Microsoft AD

* AWS Managed Microsoft AD는 다른 디렉터리 관리 도구처럼 AWS Directory Service로 AWS에 액세스 가능하게 함
* Directory Service 도구는 대용량 데이터를 처리하고 AWS 운영에 통합하는 기능을 제공
* 기본적으로 Active Directory가 VPC에서 실행되는 Microsoft Sharepoint, NET, SQL Server 기반 워크로드를 AWS 리소스에 연결하는 방식을 제어
* Managed Microsoft AD 컨트롤러는 데이터 복제와 소프트웨어 업데이트를 비롯한 필요한 인프라 관리 모두 AWS가 자동으로 처리

### AWS Single Sign-On (SSO)

* SSO를 사용하면 AWS Directory Service에 구성된 기존 Microsoft Active Directory로 간편하게 사용자 인증과 권한 부여를 수행 가능
* AWS Organizations 내 여러 AWS 계정에도 액세스 가능
* SSO는 SAML2.0을 지원하는 사용자 지정 애플리케이션 외에 Saleforece, Box, Office 365와 같은 범용 애플리케이션의 액세스도 지원
* AWS Organizations는 여러 개 AWS 계정을 정책 기반 제어로 관리 가능한 서비스
* AWS 계정이 2개 이상인 기업에서 클라우드에 배포된 자산을 파악하고 과금을 통합하는데 사용

SAML : Security Assertion Markup Language

### AWS Key Management Service

* AWS의 여타 서비스와 밀접하게 통합돼서 암호화 키 관리를 수행
* KMS는 시스템 전반에서 중앙 집중적으로 암호화를 완벽하게 제어하고 관리하는 수단 제공
* KMS는 데이터 보호에 사용할 키를 생성, 추적, 교체, 삭제 가능
* AWS CloudTrail과 통합해서 규제 준수에 관련된 주요 이벤트를 모두 기록 가능

### AWS Secrets Manager

* AWS 서비스가 아닌, 자체 애플리케이션이 사용할 리소스의 비밀번호나 타사 API 키를 관리해야하는 경우, AWS Secrets Manager를 사용
* Secrets Manager를 사용해서 요청 시마다 애플리케이션에 최신의 자격 증명을 전달하고 자격 증명 교체도 자동으로 처리하는 것이 효율적

### AWS CloudHSM (Hardware Security Module)

* AWS CloudHSM은 자체 웹 서버 인프라를 대체해서 클라우드에서 암호화 작업을 수행하는 가상 컴퓨팅 장치 클러스터
* 웹 서버에서 수행했던 암호화 키 생성, 저장, 관리를 대신 수행
    - 개발자는 애플리케이션 개발에 시간 투자 가능
* AWS CloudHSM은 KMS와 유사한 서비스를 제공하지만 아래와 같은 특성이 있음
    - 키는 사용자만 제어할 수 있는 전용 타사 인증 하드웨어 보안 모듈에 저장
    - FIPS 140-2 규정 준수
    - PKCS#11, Java JCE 또는 Microsoft CNG 인터페이스를 사용해 애플리케이션과 통합
    - VPC 내 고성능 암호화 가속화 (대향 암호화)

