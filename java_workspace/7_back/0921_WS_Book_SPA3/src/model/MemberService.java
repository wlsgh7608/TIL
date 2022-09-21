package model;

import dto.Member;

public class MemberService {
	private static MemberService instance;
	MemberDao memberdao;
	
	private MemberService() {
		memberdao = MemberDao.getInstance();
	}
	
	public static MemberService getInstance() {
		if(instance==null) {
			instance= new MemberService();
		}
		return instance;
	}
	
	public Member login(String id,String pw) {
		
		return memberdao.login(id,pw);
	}
	
	public int memberInsert(Member member) {
		System.out.println(memberdao);
		return memberdao.memberInsert(member);
	}

}
