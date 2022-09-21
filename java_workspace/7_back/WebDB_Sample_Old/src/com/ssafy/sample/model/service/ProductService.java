package com.ssafy.sample.model.service;


import java.util.List;

import com.ssafy.sample.dto.Product;
import com.ssafy.sample.model.dao.ProductDao;

public class ProductService {
	ProductDao productDao;
	private static ProductService instance;
	
	private ProductService() {
		productDao = ProductDao.getInstance();
	}
	public static ProductService getInstance() {
		if(instance == null) instance = new ProductService();
		return instance;
	}
	
	public int registProduct(Product p) {
		return productDao.registProduct(p);
	}
	public List<Product> listProduct() {
		return productDao.listProduct();
	}
}
