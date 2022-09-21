package controller;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import com.google.gson.JsonObject;
import com.google.gson.JsonParser;

import dto.Member;
import model.MemberService;

@WebServlet("/main")
public class DispatcherServlet extends HttpServlet {
	MemberService memberService;
	
	public void init() throws ServletException {
		memberService = MemberService.getInstance();
	}
	protected void process(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = response.getWriter();
		JsonObject reJson = new JsonObject();
		
		JsonObject json = (JsonObject) JsonParser.parseReader(request.getReader());
		String sign = json.get("sign").getAsString();
		if(sign!=null) {
			if(sign.equals("login")) {
				String id = json.get("id").getAsString();
				String pw = json.get("pw").getAsString();
				
				Member m = memberService.login(id, pw);
				if(m!=null) {
					//login
					HttpSession session = request.getSession();
					session.setAttribute("loginId", m.getName());
					reJson.addProperty("loginId", id);
				} else {
					reJson.addProperty("msg", "loginFail");
					
					
					
				}
			} else if(sign.equals("logout")) {
				System.out.println("LOGOUT");
				HttpSession session = request.getSession(false);
				if(session!=null) {
					session.invalidate();
				}
				reJson.addProperty("msg", "ok");
			} else if(sign.equals("memberInsert")) {
				String id = json.get("id").getAsString();
				String pw = json.get("pw").getAsString();
				String name = json.get("name").getAsString();
				System.out.println("memberInsert: "+id+":"+pw+":"+name);
				int i = memberService.memberInsert(new Member(id,pw,name));
				if(i>0) {
					reJson.addProperty("msg","insertOK");
					System.out.println("성공");
					
				}else {
					reJson.addProperty("msg","insertFail");
					System.out.println("실패");
				}
				
			}
		}else {
			reJson.addProperty("msg","error");
		}
		out.append(reJson.toString());
		
		
		
	}
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		process(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		process(request, response);
	}

}
