package com.ssafy.sample.dto;

public class Product {
	String model;
	int productCode, price;
	public String getModel() {
		return model;
	}
	public void setModel(String model) {
		this.model = model;
	}
	public int getProductCode() {
		return productCode;
	}
	public void setProductCode(int productCode) {
		this.productCode = productCode;
	}
	public int getPrice() {
		return price;
	}
	public void setPrice(int price) {
		this.price = price;
	}
	public Product(String model, int productCode, int price) {
		setModel(model);  // null 체크 해줘야 한다.
		setProductCode(productCode);
		setPrice(price);
	}
	@Override
	public String toString() {
		return "Product [model=" + model + ", productCode=" + productCode + ", price=" + price + "]";
	}
	
	
}
