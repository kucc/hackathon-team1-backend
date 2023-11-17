fetch('https://62b7-128-134-157-9.ngrok-free.app/test')
  .then(response => response.json())
  .then(data => {
    // JSON 데이터를 다루는 코드 작성
    data.forEach(item => {
      console.log('이름:', item.name);
      console.log('나이:', item.age);
      console.log('ID:', item.id);
      console.log('-----------------');
    });
  })
  .catch(error => {
    console.error('API 호출 중 오류가 발생했습니다:', error);
  });