package controller;

import java.io.BufferedReader;
import java.io.IOException;
import javax.servlet.ServletConfig;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;



@WebServlet("/main")
public class DispatcherServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;

	public void init(ServletConfig config) throws ServletException {
		// TODO Auto-generated method stub
	}

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		System.out.println("doGet 호출됨");
		String sign = request.getParameter("sign");
		System.out.println(sign);
	}


	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		System.out.println("doPost 호출됨");
		try {
			JSONParser parser = new JSONParser();
			JSONObject json = (JSONObject) parser.parse(request.getReader());
			String sign = (String) json.get("sign");
			String id = (String) json.get("id");
			String pw = (String) json.get("pw");
			System.out.println(sign+", "+id+", "+pw);
			// login...
			json = new JSONObject();
			json.put("name", "ryeohwan");
			json.put("age", 20);
			response.getWriter().append(json.toJSONString());
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
			
		
	}

}
