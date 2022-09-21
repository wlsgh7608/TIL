package dto;

public class Member {
	private String id;
	private String pw;
	private String name;
	public Member(String id, String pw, String name) {
		setId(id);
		setPw(pw);
		setName(name);
	}
	public String getId() {
		return id;
	}
	public void setId(String id) {
		if(id!=null) 
		this.id = id;
	}
	public String getPw() {
		return pw;
	}
	public void setPw(String pw) {
		if(pw!=null)
		this.pw = pw;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		if(name!=null)
		this.name = name;
	}
	@Override
	public String toString() {
		return "Member [id=" + id + ", pw=" + pw + ", name=" + name + "]";
	}
	
	
	

}
