
document.querySelector("#loginBtn").addEventListener("click",test);

async function test() {
	
	let id = document.querySelector("#id").value;
	let pw = document.querySelector("#pw").value;
	console.log(id,pw);
	let data = JSON.stringify({sign:"login",id:id,pw:pw});
	//console.log(data);
	// stringify 는 json 으로 바꿔준다.
	//console.log(data);
	
	let myObject = await fetch("main",{method:"POST",body:data}); // post 로 주고싶으면 {} 로 옵션을 주면 된다.
	let myText = await myObject.text();		// 위의 FormData는 js 객체이다.
	
	console.log(myText);
	console.log(myObject);
	console.log(JSON.parse(myText));
	
	myText=JSON.parse(myText);
	document.querySelector("#loginSpan").innerHTML=myText.name+"<button class='btn btn-info' id='logoutBtn'>logout";
}