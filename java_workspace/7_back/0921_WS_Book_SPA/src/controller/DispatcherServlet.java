package controller;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletConfig;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import com.google.gson.JsonObject;
import com.google.gson.JsonParser;



/**
 * Servlet implementation class DispatcherServlet
 */
@WebServlet("/main")
public class DispatcherServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
	public void init(ServletConfig config) throws ServletException {
		// TODO Auto-generated method stub
	}

	protected void process(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = response.getWriter();
		
		JsonObject json = (JsonObject) JsonParser.parseReader(request.getReader());
		String sign = json.get("sign").getAsString();
		if(sign!=null) {
			String id = json.get("id").getAsString();
			String pw= json.get("pw").getAsString();
			
			System.out.println(id+" "+pw);
			//login 처리
			HttpSession session = request.getSession();
			session.setAttribute("loginId", id);
			json = new JsonObject();
			json.addProperty("loginId", id);
			out.append(json.toString());
			System.out.println(json.toString());
			
			
		}else {
			json = new JsonObject();
			json.addProperty("msg", "error");
			out.append(json.toString());
		}
		
		JsonParser parser = new JsonParser();
		parser.parse(request.getReader());
		
		
		
		
		
		
		
//		String sign = request.getParameter("sign");
//		if(sign!=null) {
//			if(sign.equals("login")) {
//				String id = request.getParameter("id");
//				String pw = request.getParameter("id");
//				//login....
////				Member m = new Member()
//				HttpSession session = request.getSession();
//				session.setAttribute("loginId",id);
//				
//			}
//			
//		}else {
//			out.append("error");
//		}
		
	}

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		process(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		process(request, response);
	}

}
