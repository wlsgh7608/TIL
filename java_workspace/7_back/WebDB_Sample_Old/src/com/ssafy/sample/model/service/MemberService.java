package com.ssafy.sample.model.service;

import com.ssafy.sample.dto.Member;
import com.ssafy.sample.model.dao.MemberDao;

public class MemberService {
	MemberDao memberDao;
	private static MemberService instance;
	
	private MemberService() {
		memberDao = MemberDao.getInstance();
	}
	public static MemberService getInstance() {
		if(instance == null) instance = new MemberService();
		return instance;
	}

	public Member login(String id, String pw) {
		return memberDao.login(id,pw);
	}
}
