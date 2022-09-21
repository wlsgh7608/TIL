document.querySelector("#loginBtn").addEventListener("click",login);  // login()하면 안된다!!

async function login(){
	let id = document.querySelector("#id").value;
	let pw = document.querySelector("#pw").value;
	let data = JSON.stringify({sign:"login", id:id, pw:pw});
	
	let responseObject = await fetch("main",{method :"POST", body:data});  // {} 라는 옵션이 들어가고 "url" 이 들어간다.
	console.log(responseObject);
	
	data = await responseObject.text();
	console.log(data);
	
	data = JSON.parse(data); // parse 로 js 객체로 바꿔준다.
	console.log(data);
	document.querySelector("#loginSpan").innerHTML = data.name + "<button class = 'btn btn-warning'>logout</button>";
}