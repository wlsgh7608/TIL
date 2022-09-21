package com.ssafy.sample.controller;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletConfig;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import com.ssafy.sample.model.service.memberService;


@WebServlet("/main")
public class DispatcherServlet extends HttpServlet {
	MemberService memberService;
	
	public void init(ServletConfig config) throws ServletException {
		memberService = MemberService.getInstance();
	}

	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
	}


	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		RequestDispatcher disp = null;
		String sign = request.getParameter("sign");
		if(sign != null) {
			if(sign.equals("login")) {
				String id = request.getParameter("id");
				String pw = request.getParameter("pw");
				Member member = memberService.login(id,pw);
				if(member != null) {
					HttpSession session = request.getSession();
					session.setAttribute("member", member);
				}
				disp = request.getRequestDispatcher("index.jsp");
			}
		}else {
			disp = request.getRequestDispatcher("error/error.jsp");
		}
		disp.forward(request, response);
	}

}
