# ✅ Postman API 테스트

이 디렉토리는 RealWorld API 애플리케이션의 기능 테스트 자동화를 위한 Postman 테스트 컬렉션과 환경 설정 파일을 포함하고 있습니다.  
실제 유효 토큰을 기반으로 다양한 시나리오를 구성하여 API 동작을 검증.

---

## 🔧 필요 사항

- **Postman v10 이상 설치** ([다운로드 링크](https://www.postman.com/downloads/))
- **테스트 대상 서버 실행 중** (백엔드 URL: `http://localhost:3000`)
- 테스트 컬렉션: `API_Test_Postman_Collections_elice_project.json`
- 환경 변수 파일: `API_Test_Postman_Environment.json`

---

## 🚀 테스트 실행 방법

1. Postman을 실행합니다.
2. `File > Import` 메뉴에서 아래 두 JSON 파일을 가져옵니다:
   - `API_Test_Postman_Environment.json` (환경 변수)
   - `API_Test_Postman_Collections_elice_project.json` (테스트 컬렉션)
3. 오른쪽 상단의 환경 드롭다운에서 `Elice_Environment`를 선택합니다.
4. `Elice_2th_Project` 컬렉션을 Runner 또는 Newman으로 실행합니다.

---

## 📁 테스트 시나리오 구성

**컬렉션 이름**: `Elice_2th_Project`  
각 폴더는 독립적인 테스트 단위이며, 사용자 흐름에 맞춘 순서로 구성되어 있습니다.

### 🧪 회원가입(Sign Up)
- 입력값 미입력, 유효성 실패 케이스
- 정상 회원가입 → JWT 저장 (`pm.environment.set("token", ...)`)

### 🔐 로그인(Sign In)
- 이메일/비밀번호 누락, 유효하지 않은 입력
- 정상 로그인 → 토큰 저장 및 이후 요청에 사용

### 👤 사용자 프로필(Profile)
- 현재 사용자 조회 (`/api/user`)
- 프로필 조회 및 수정 (`/api/profiles/:username`)

### 📝 게시글(Postpage)
- 게시글 작성 (성공/실패 케이스 포함)
- 상세 조회, 수정, 삭제, 목록 필터링

### 👥 소셜(Follow/Feed)
- 팔로우: 랜덤 사용자 팔로우 및 피드 반영 확인
- 언팔로우: 피드에서 해당 사용자 게시글 제거 확인

### ❤️ 좋아요(Favorite)
- 좋아요 클릭 → 프로필의 Favorite 탭에 반영 확인
- 좋아요 취소 후 Favorite 탭에서 제거 확인

### 🏷️ 태그(Tag)
- 전체 태그 목록 조회 (`/api/tags`)
- 랜덤 태그 선택 → 해당 태그 기반 게시글 목록 확인

---

## 📊 테스트 결과 및 유지보수

- 모든 요청은 `Tests` 스크립트를 포함하고 있으며, 응답 상태코드 및 본문 구조를 검증합니다.
- 동적 변수(`token`, `username`, `slug` 등)는 사전 요청(pre-request) 및 환경 변수에서 자동 처리됩니다.
- 실패 시 콘솔 및 응답 패널에서 원인 분석 가능

---

## ⚙️ CI/CD 연동 (선택 사항)

- `Newman` CLI를 통해 자동화 테스트 가능
- `htmlextra` 플러그인으로 시각화된 리포트 생성  
- *일부 테스트 및 환경변수 Newman 에서 인식 불가*

```bash
newman run API_Test_Postman_Collections_elice_project.json \
  -e API_Test_Postman_Environment.json \
  -r htmlextra \
  --reporter-htmlextra-export ./postman_api_report.html
