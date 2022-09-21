<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
	<%@ include file="/include/head.jsp" %>
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet">
  	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js"></script>
</head>
<body>
	<%@ include file="/include/nav.jsp" %>

	<%-- 페이지만의 내용 --%>
	<div class="container p-4">
	
	  <h2>상품 정보 목록</h2>
		<table class="table table-hover">
	    <thead>
	      <tr>
	        <th>Product Code</th>
	        <th>Model</th>
	        <th>price</th>
	      </tr>
	    </thead>
	    <tbody>
	    <!-- error 가 나도 view 에서 표현하는거라 error 표시되지 않게 하겠다는 것이다. -> 에러 메세지 없이 나오면 el 이 괴롭힌다.... -->
	    <c:forEach items="${productList}" var ="product">  
	    <!-- 꺼낸 값을 var 로 하는 건데 여기선 product로 하겠다. -->
	    <tr>
	        <td>${product.productCode }</td>
	        <td>${product.model }</td>
	        <td>${product.price }</td>
	    </tr>
	    </c:forEach>
	      
	    </tbody>
		</table>
	
	</div>
	<%-- --%>
<%@ include file="/include/footer.jsp" %>