# AI 코딩 에이전트를 위한 스킬

[English](README.md) | 한국어

AI 코딩 에이전트를 위한 **스킬** 모음입니다. 스킬은 특정 작업(예: PowerPoint에서 발표자 노트 제거)을 수행할 때 에이전트가 읽고 실행할 수 있는 도메인별 지식과 선택적 실행 스크립트를 패키징합니다.

에이전트는 스킬의 `SKILL.md`를 읽고 안내에 따라 필요한 번들 스크립트를 실행합니다.

> [!NOTE]
> 먼저 아래의 [GitHub Copilot CLI 설치 안내](#스킬-설치)를 확인하십시오. 다른 에이전트, 설치 범위, 로컬 체크아웃, 기본 마켓플레이스 및 플러그인 설치 방법은 [스킬 설치 안내서](docs/skills-installation-guide.md)를 참조하십시오.

## 리포지토리 구조

```text
.
├── AGENTS.md             # 이 리포지토리에서 작업하는 AI 코딩 에이전트 안내
├── docs/                 # 설치 및 유지 관리 안내서
└── skills/
    └── <skill-name>/
        ├── README.md     # 필수: 사용자용 개요, 설치 및 사용법
        ├── SKILL.md      # 필수: 스킬 설명 및 사용 안내
        ├── plugin.json   # 필수: 개별 Copilot 플러그인 메타데이터
        ├── thumbnail.png # 선택: 렌더링된 썸네일
        ├── thumbnail.svg # 선택: 편집 가능한 썸네일 원본
        └── scripts/      # 선택: 스킬 실행을 지원하는 스크립트
```

- 각 스킬은 `skills/<skill-name>/` 디렉터리에 있습니다.
- `<skill-name>`은 `pptx-denote`처럼 소문자와 하이픈으로 구성합니다(kebab-case).
- 모든 스킬 디렉터리에는 `README.md`, `SKILL.md`, `plugin.json`이 있어야 합니다. README는 스킬을 소개하고 개별 설치 방법과 사용 예시를 제공합니다. 에이전트용 지침은 `SKILL.md`를 기준으로 합니다. 스킬 프런트매터의 이름과 플러그인 이름은 디렉터리 이름과 일치해야 하며, 플러그인의 `"skills": "./"` 설정은 해당 디렉터리의 `SKILL.md`를 노출합니다.
- 지원 코드는 스킬 디렉터리의 `scripts/` 하위 디렉터리에 둡니다.
- 스킬의 `SKILL.md`에 안내된 경우 참조 문서, 템플릿, 규칙 등 지원 자료를 위한 하위 디렉터리를 추가할 수 있습니다.

## 사용 가능한 스킬

| 스킬 | 설명 |
| ---- | ---- |
| [`create-prd`](skills/create-prd/README.ko.md) | 사용자 제공 맥락과 인터뷰를 바탕으로 제품 요구 사항 문서(PRD)를 작성하거나 업데이트하고, 부족한 세부 정보를 보완합니다. |
| [`create-tdd`](skills/create-tdd/README.ko.md) | 필수 PRD와 TRD를 바탕으로 기술 설계 문서(TDD)를 작성하거나 업데이트합니다. 설계 제안과 적응형 인터뷰를 진행하고 기존 ADR을 참조합니다. |
| [`create-trd`](skills/create-trd/README.ko.md) | 적응형 인터뷰를 통해 PRD의 보완 문서인 기술 요구 사항 문서(TRD)를 작성하거나 업데이트합니다. PRD가 없으면 먼저 작성할지 확인합니다. |
| [`korean-technical-writing`](skills/korean-technical-writing/README.md) | 의미를 보존하면서 한국어 기술 문서와 일반 문서를 작성, 교정, 수정 또는 검토합니다. |
| [`localizations`](skills/localizations/README.ko.md) | 로케일별 규칙에 따라 지원 대상 로케일로 콘텐츠를 현지화합니다. |
| [`pptx-denote`](skills/pptx-denote/README.ko.md) | `python-pptx` 라이브러리를 사용하여 PowerPoint 프레젠테이션의 모든 슬라이드 노트를 제거합니다. |
| [`technical-writing`](skills/technical-writing/README.ko.md) | 의미를 보존하면서 영어 기술 문서와 일반 문서를 작성, 교정, 수정 또는 검토합니다. |

## 스킬 사용 방법

1. 개요와 개별 설치 방법은 스킬 README에서 확인하거나 아래 안내에 따라 전체 컬렉션을 설치합니다.
1. 스킬의 `SKILL.md`를 열고 **How it works** 또는 **동작 방식** 섹션을 읽습니다.
1. 에이전트에게 스킬을 사용하도록 요청합니다.

   예를 들어 GitHub Copilot CLI에서 다음과 같이 요청합니다.

    ```text
    pptx-denote 스킬을 사용해 "my-presentation.pptx"에서 발표자 노트를 제거해 주십시오.
    ```

## 스킬 설치

GitHub Copilot CLI를 설치한 뒤, 이 리포지토리를 마켓플레이스로 추가하고 컬렉션 플러그인을 설치합니다.

```sh
copilot plugin marketplace add justinyoo/skills
copilot plugin install justinyoo-skills@justinyoo-skills
```

`justinyoo-skills` 플러그인에는 이 컬렉션의 모든 스킬이 포함되어 있습니다. 컬렉션 전체 대신 개별 스킬을 설치하려면 마켓플레이스를 등록한 뒤 스킬을 검색하고 설치합니다.

```sh
copilot plugin marketplace browse justinyoo-skills
copilot plugin install <skill-name>@justinyoo-skills
```

`<skill-name>`을 `create-prd`와 같은 목록의 스킬 이름으로 바꿉니다. 같은 스킬을 중복 설치하지 않도록 컬렉션 플러그인 또는 개별 플러그인 중 하나를 선택합니다. 직접 플러그인을 설치하는 방법, `npx skills`를 사용하는 방법, 로컬 체크아웃 및 다른 코딩 에이전트에 관한 내용은 [설치 안내서](docs/skills-installation-guide.md)를 참조하십시오.

## 새 스킬 추가

### `create-skill`을 사용한 지원 작성(권장)

코딩 에이전트에서 외부 `create-skill` 스킬을 사용합니다. 에이전트에서 이미 사용할 수 있는 설치본이 있으면 재사용하고, 없다면 필요에 따라 설치하기 전에 승인을 받습니다. GitHub Copilot에서는 다음 명령을 사용합니다.

```sh
npx skills add jongio/skills --skill create-skill -g --agent github-copilot
```

다른 에이전트 식별자는 [설치 안내서](docs/skills-installation-guide.md#install-with-the-skills-cli)를 참조하십시오. 그런 다음 다음과 같이 에이전트에 요청합니다.

```text
create-skill을 사용해 <task>용 <skill-name> 스킬을 만들어 주십시오.
이 리포지토리의 skills/ 구조를 따르고 기존 사용자 지정 콘텐츠를 보존해 주십시오.
```

스킬이 누락된 요구 사항을 확인하고 미리 보기 계획을 생성하도록 합니다. 제안된 파일, 대상 경로, 사전 요구 사항, 등록 변경 사항을 검토한 뒤 정확한 계획을 승인합니다. 도우미는 외부 도구로 유지합니다. `create-skill` 설치본이나 리포지토리 관리 프레임워크를 리포지토리에 포함하거나 CI에 작성 단계를 추가하지 마십시오.

### 직접 작성(대안)

도우미를 사용할 수 없거나 직접 작성하려는 경우 다음 절차를 따릅니다.

1. `skills/<skill-name>/`을 만듭니다.
2. 올바른 YAML 프런트매터(`name`, `description`)가 포함된 `SKILL.md`를 추가합니다.
3. 스킬의 목적, GitHub Copilot CLI 설치 방법, 현실적인 사용 프롬프트 하나를 설명하는 `README.md`를 추가합니다. 다른 설치 방법은 `SKILL.md`와 공용 설치 안내서에 연결합니다.
4. 동일한 스킬 이름과 마켓플레이스 항목에 맞는 버전, `"skills": "./"` 설정을 포함한 `plugin.json`을 추가합니다.
5. 실행 가능한 코드는 `SKILL.md`에 정확한 실행 방법을 설명하고 스킬의 `scripts/` 디렉터리에 둡니다.
6. 사전 요구 사항(라이브러리, 도구)과 설치 방법을 명시합니다.
7. 스킬은 자체 완결형으로 만들고, 하나의 작업에 집중시키며, 가능한 경우 멱등성을 유지합니다.

어느 방법을 사용하든 [스킬 변경 체크리스트](docs/repository-maintenance.md#skill-change-checklist)를 따라 README, 마켓플레이스 항목, 플러그인 메타데이터 및 해당되는 종속성 설정을 일관되게 유지합니다. 작성 규칙은 [AGENTS.md](AGENTS.md)를 참조하십시오.

## 리포지토리 유지 관리

스킬 변경 체크리스트, 종속성 없이 실행할 수 있는 로컬 리포지토리 테스트, 선택적 정적 스킬 린트, CI 동작은 [리포지토리 유지 관리 안내서](docs/repository-maintenance.md)를 참조하십시오.

이 리포지토리에는 작성한 스킬과 배포 매니페스트가 포함되어 있으며, 번들형 리포지토리 생성기나 `create-skill` 설치본은 포함되어 있지 않습니다. GitHub Actions는 고정된 검증 도구를 임시 실행기 디렉터리에 설치합니다. GitHub Pages는 구성되어 있지 않습니다.

## 기여

새 스킬 기여를 환영합니다. [AGENTS.md](AGENTS.md)의 규칙을 따르고 각 스킬이 명확히 정의된 하나의 작업에 집중하도록 해 주십시오.
