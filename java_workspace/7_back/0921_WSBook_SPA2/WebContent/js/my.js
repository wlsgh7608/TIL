let cookie_loginId = $.cookie("loginId");
if(cookie_loginId){
	document.querySelector("#loginSpan").innerHTML = cookie_loginId+" <button id='logoutBtn'>logout</button>";
}
document.querySelector("#loginBtn").addEventListener("click",login);


async function login(){
	let id = document.querySelector("#id").value;
	let pw = document.querySelector("#id").value;
	let data = JSON.stringify({sign:"login",id,pw}); // 비구조화 할당
	
	data = await fetch("main",{method:"POST",body:data});
	data = await data.text();
	data = JSON.parse(data);
	if(data.loginId){
		$.cookie("loginId",data.loginId);
		document.querySelector("#loginSpan").innerHTML = data.loginId+" <button>logout</button>";
	}else{
		
		alert(data.msg);
	}
}