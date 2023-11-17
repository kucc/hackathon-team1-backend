fetch('https://62b7-128-134-157-9.ngrok-free.app/test')
  .then(response => response.text())
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error('API 호출 중 오류가 발생했습니다:', error);
  });