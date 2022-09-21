let cookie_loginId = $.cookie("loginId");
if(cookie_loginId){
	document.querySelector("#loginSpan").innerHTML =cookie_loginId+ " <button>logout</button>";
}


document.querySelector("#loginBtn").addEventListener("click",login);


async function login(){
	let id = document.querySelector("#id").value ;
	let pw= document.querySelector("#pw").value;
	let data = JSON.stringify({sign:"login",id,pw}); // 비구조화 할당 = 구조 분해 할당 a:a => a로 가능 JSONString	
	data = await fetch("main",{method:"POST",body:data}); // Response
	data = await data.text(); // 응답 text json
	data = JSON.parse(data); // js 객체
	console.log(data);
	if(data.loginId){
		document.cookie = "loginId="+data.loginId;
		document.querySelector("#loginSpan").innerHTML =data.loginId+ " <button>logout</button>";
		
	}else{
		
	}
	
}