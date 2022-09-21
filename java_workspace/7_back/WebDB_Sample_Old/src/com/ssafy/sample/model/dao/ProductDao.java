package com.ssafy.sample.model.dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

import com.ssafy.sample.dto.Product;
import com.ssafy.sample.model.service.ProductService;

public class ProductDao {
	Connection con;
	private static ProductDao instance;
	
	private ProductDao() {
		try {
			Class.forName("com.mysql.cj.jdbc.Driver");
			con = DriverManager.getConnection("jdbc:mysql://localhost:3306/temp","ssafy","ssafy");
		}catch(Exception e) {
			e.printStackTrace();
		}
	}
	public static ProductDao getInstance() {
		if(instance == null) instance = new ProductDao();
		return instance;
	}
	
	public int registProduct(Product p) {
		String sql ="insert into product(productCode,model,price) value(?,?,?)";
		try(PreparedStatement stmt = con.prepareStatement(sql)) {
			stmt.setInt(1, p.getProductCode());
			stmt.setString(2, p.getModel());
			stmt.setInt(3, p.getPrice());
			return stmt.executeUpdate();
		}catch(Exception e) {
			e.printStackTrace();
			return 0;
			
		}
	}
	
	public List<Product> listProduct(){
		String sql = "select * from product";
		try(PreparedStatement stmt = con.prepareStatement(sql)){
			ResultSet rs = stmt.executeQuery(sql);
			List<Product> list = new ArrayList<>();
			while(rs.next()) {
				list.add(new Product(rs.getString("model"), rs.getInt("productCode"), rs.getInt("price")));
			}
			return list;
		}catch(Exception e) {
			e.printStackTrace();
			return null;
		}
	}
}
