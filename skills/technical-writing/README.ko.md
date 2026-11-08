# 영어 기술 문서 작성

[English](README.md) | 한국어

## 이 스킬의 목적

의미, 근거, 용어, 작성자의 문체를 보존하면서 영어 기술 문서와 기타 영어 글을 작성, 교정, 수정 또는 검토합니다. 기존 문서와 프로젝트의 문체를 우선하며, 별도의 영어 변종이 지정되지 않은 새 문서에는 미국식 영어를 기본으로 사용합니다. 스크립트, 패키지 또는 외부 교정 서비스는 필요하지 않습니다.

ISO 24495-1과 ASD-STE100은 서로 보완적인 관점을 제공하지만, 어느 한쪽도 이 스킬의 전체 범위를 다루지는 않습니다. 이 스킬은 표준 준수나 인증을 주장하지 않고 일부 원칙을 참고합니다. 출처 목록에는 사전과 공공 부문 및 출판 분야의 스타일 가이드도 상황에 따라 참고할 자료로 나열되어 있으며, 보편적인 규칙으로 취급하지 않습니다. 자세한 내용은 [출처 비교 및 사용 조건](references/sources.md)과 권위 있는 작업 절차를 제공하는 [SKILL.md](SKILL.md)를 참조하십시오.

## GitHub Copilot CLI로 설치

GitHub Copilot CLI를 설치한 뒤 터미널에서 다음 명령을 실행합니다.

```sh
copilot plugin marketplace add justinyoo/skills
copilot plugin install technical-writing@justinyoo-skills
```

마켓플레이스를 이미 등록했다면 첫 번째 명령은 건너뜁니다. 전체 컬렉션을 설치했다면 이 스킬도 포함되어 있습니다.

다른 에이전트, 설치 방법, 로컬 체크아웃에 관한 내용은 [스킬 설치 안내서](../../docs/skills-installation-guide.md)를 참조하십시오.

## 사용법

GitHub Copilot CLI 세션에서 다음과 같이 요청합니다.

```text
/technical-writing 다음 영어 절차를 의미를 바꾸지 않고 명확하게 수정해 주십시오: "You may restart the service only after the backup completes. Do not disable audit logging."
```
