# PowerPoint 슬라이드 노트 제거

[English](README.md) | 한국어

## 이 스킬의 목적

PowerPoint(`.pptx`) 프레젠테이션의 슬라이드 노트를 제거하고, 같은 슬라이드를 유지하면서 노트가 없는 새 파일로 저장합니다. 발표자 노트가 포함되지 않은 사본을 공유할 때 사용합니다. 이 스킬은 Python과 `python-pptx` 라이브러리를 사용하며, 기본 출력 파일 이름에는 원본 이름 뒤에 `-denoted`가 추가됩니다.

전체 작업 절차와 사전 요구 사항은 [SKILL.md](SKILL.md)를 참조하십시오.

## GitHub Copilot CLI로 설치

GitHub Copilot CLI를 설치한 뒤 터미널에서 다음 명령을 실행합니다.

```sh
copilot plugin marketplace add justinyoo/skills
copilot plugin install pptx-denote@justinyoo-skills
```

마켓플레이스를 이미 등록했다면 첫 번째 명령은 건너뜁니다. 전체 컬렉션을 설치했다면 이 스킬도 포함되어 있습니다.

다른 에이전트, 설치 방법, 로컬 체크아웃에 관한 내용은 [스킬 설치 안내서](../../docs/skills-installation-guide.md)를 참조하십시오.

## 사용법

GitHub Copilot CLI 세션에서 다음과 같이 요청합니다.

```text
/pptx-denote "community-meetup.pptx"에서 모든 슬라이드 노트를 제거해 주십시오.
```
