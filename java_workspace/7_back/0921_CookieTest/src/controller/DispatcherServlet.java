package controller;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

@WebServlet("/DispatcherServlet")
public class DispatcherServlet extends HttpServlet {
	public void init() throws ServletException {
		
	}

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		System.out.println("DO  GET 할당!");
		HttpSession session =  request.getSession(); // 안 갖고왔으면 할당받음
		System.out.println(session.getId());
		Cookie c = new Cookie("loginedName","kjh");
		c.setMaxAge(60*60*24*365);
		c.setHttpOnly(true); //js 탈취 방어
		c.setSecure(true); // https에서만 사용가능
		response.addCookie(c);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
