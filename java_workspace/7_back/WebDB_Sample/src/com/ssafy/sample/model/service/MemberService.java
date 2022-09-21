package com.ssafy.sample.model.service;

public class MemberService {
	MemberDao mamberDao;
	
	private static MemberService instance;
	
	private MemberService() {
		mamberDao = MemberDao.getInstance();
	}
	
	public static MemberService getInstance() {
		if(instance == null) instance = new MemberService();
		return instance;
	}
	
	public Member login(String id, String pw) {
		return mamberDao.login(id,pw);
	}
}
