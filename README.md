# hackathon-team1-backend

- [프론트엔드 리포지토리](https://github.com/kucc/hackathon-team1-frontend)
- [서비스 배포 링크](https://hackathon-team1-frontend.vercel.app/)
- [서버 배포 링크](https://118.67.143.134:8080/)

## 서비스 한 줄 소개
대학생의 일정을 우선순위별로 관리하고 월간 및 일별로 조회 가능한 일정 관리 시스템

## 일정

개발 시간: 2023년 11월 17일 19시 ~ 2023년 11월 11일 09시

<details>
    <summary>상세 일정</summary>
    <table style="text-align: center; width: 800px">
        <tr>
            <th>TIME</th>
            <th>민재</th>
            <th>준호</th>
            <th>민영</th>
        </tr>
        <tr>
            <td>19:00</td>
            <td>README.md 작성</td>
            <td>프론트 배포</td>
            <td>조이름&로고 만들기<br>아이디어 구체화</td>
        </tr>
        <tr>
            <td>20:00</td>
            <td>FastAPI 폴더 구조 생성<br>test용 API 구현</td>
            <td>템플릿 찾아보기</td>
            <td>와이어프레임</td>
        </tr>
        <tr>
            <td>21:00</td>
            <td colspan="3">와이어프레임 보고 UI, UX 구체화</td>
        </tr>
        <tr>
            <td>22:00</td>
            <td>데이터 모델링<br>API 리스트 작성</td>
            <td>Figma 사용<br>API 리스트 작성</td>
            <td>디자인</td>
        </tr>
        <tr>
            <td>23:00</td>
            <td>개발</td>
            <td>개발</td>
            <td>로직 작성</td>
        </tr>
        <tr>
            <td>06:00</td>
            <td colspan="3">GPT-4 Turbo를 사용한 챗봇 기능 추가</td>
        </tr>
        <tr>
            <td>07:00</td>
            <td colspan="3">테스트</td>
        </tr>
    </table>
</details>

## 💻 Team 8 소개

<table align="center" style = "table-layout: auto; width: 100%; table-layout: fixed;">
  <tr>
    <td>
       <img width="200" src = "https://avatars.githubusercontent.com/u/75142329?v=4" />
    </td>
    <td>
      <img width="200" src = "https://avatars.githubusercontent.com/u/124476542?v=4"/>
    </td>
    <td>
      <img width="200" src = "https://avatars.githubusercontent.com/u/108617193?v=4"/>
    </td>
  </tr> 
  <tr>
    <th align="center">권민재</th>
    <th align="center">문준호</th>
    <th align="center">안민영</th>
  </tr>
  <tr>
    <td align="center">
      <a href="https://github.com/mjkweon17">mjkweon17</a>
    </td>
    <td align="center">
      <a href="https://github.com/juknow">juknow</a>
    </td>
        <td align="center">
      <a href="https://github.com/minyeoong">minyeoong</a>
    </td>
  </tr>
  <tr>
    <th align="center">Backend, CI/CD</th>
    <th align="center">Frontend, Design</th>
    <th align="center">Project Managing</th>
  </tr>
</table>

### 도움 주신 분들
<table align="center" style = "table-layout: auto; width: 100%; table-layout: fixed;">
  <tr>
    <td>
       <img width="200" src = "https://avatars.githubusercontent.com/u/99082370?v=4" />
    </td>
    <td>
      <img width="200" src = "https://avatars.githubusercontent.com/u/52532871?v=4"/>
    </td>
    <td>
      <img width="200" src = "https://avatars.githubusercontent.com/u/16236317?v=4"/>
    </td>
  </tr> 
  <tr>
    <th align="center">최어진</th>
    <th align="center">김현채</th>
    <th align="center">RanolP</th>
  </tr>
  <tr>
    <td align="center">
      <a href="https://github.com/oeozinni">oeozinni</a>
    </td>
    <td align="center">
      <a href="https://github.com/r-4bb1t">r-4bb1t</a>
    </td>
        <td align="center">
      <a href="https://github.com/ranolp">ranolp</a>
    </td>
  </tr>
  <tr>
    <th align="center">Design</th>
    <th align="center">Frontend, Design</th>
    <th align="center">Frontend</th>
  </tr>
</table>

## 🛠 Frontend Tech Stack
| Framework | React |
|:---|:---|
| Language | HTML, CSS, Javascript, React |
| Deployment | Vercel |

## 🛠 Backend Tech Stack
| Framework | FastAPI |
|:---|:---|
| Language | Python 3.10 |
| Database/ORM | MySQL, Naver Cloud Platform - Cloud DB for MySQL, SQLAlchemy |
| ETC | ngrok, Swagger, Channel Talk, [ERDCloud](https://www.erdcloud.com/d/9pM4F45F62tvMWBT3), MySQL Workbench, GPT-4 Turbo |

## 다이어그램

### ERD
<img width = "800" src = "https://user-images.githubusercontent.com/75142329/283930400-24865302-da6f-4a89-9629-4543410ed373.png" >

## 기능
- 캘린더
- 월간 일정 조회
- 일일 일정 조회
- 일정 추가
- 우선순위에 따른 일정 목록 추천
- 일정 관리 비서 추가
  - DB에 있는 일정들을 학습한 GPT-4 Turbo

## API 리스트
![image](https://github.com/kucc/hackathon-team1-backend/assets/75142329/a268ce4e-ee90-41c3-859f-ee9adc5df8d1)


## 웹 화면
![image](https://github.com/kucc/hackathon-team1-backend/assets/75142329/143dd97d-13dd-4335-a231-992ecab441ec)
