const dc = document; //document 너무 기니까 dc로 줄여보기
const myList = dc.querySelector(".myList"); //myList class에 해당하는 첫번째 요소 선택

for (let i = 1; i <= 3; i++) {
  //반복문
  let item = dc.createElement("li"); //li 요소를 생성, item으로 명명
  item.innerText = i + " 번째 추가 항목"; //item의 내부 Text를 "i번째 추가 항목"으로 쓰기
  myList.append(item); //myList에 item을 추가
}
