<%@ page language="java" contentType="text/html; charset=UTF-8"
   pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt"%>
<%@ taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions"%>

<c:set var="listCount" value="${ requestScope.listCount }" />
<c:set var="startPage" value="${ requestScope.startPage }" />
<c:set var="endPage" value="${ requestScope.endPage }" />
<c:set var="maxPage" value="${ requestScope.maxPage }" />
<c:set var="currentPage" value="${ requestScope.currentPage }" />

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link
	href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css"
	rel="stylesheet">
<link href="resources/css/style.css" rel="stylesheet">
<link href="resources/css/reset.css" rel="stylesheet">
<!-- <link href="resources/css/noticelist.css" rel="stylesheet"> -->

<title>공지사항</title>
<style type="text/css">
.wrap {
	width: 1274px;
	position: relative;
	text-align: center;
	margin: 0 auto;
	margin-top: 0px;
	margin-right: auto;
	margin-bottom: 0px;
	margin-left: auto;
	background: #fff;
	background-image: initial;
	background-position-x: initial;
	background-position-y: initial;
	background-size: initial;
	background-repeat-x: initial;
	background-repeat-y: initial;
	background-attachment: initial;
	background-origin: initial;
	background-clip: initial;
	background-color: rgb(255, 255, 255);
	text-align: left;
}
.s_container {
	width: 956px;
	margin: 0 auto;
	padding-top: 0px;
	padding-bottom: 60px;
	position: relative;
	line-height: 22px;
}
.stab {
	width: 100%;
	margin-top: 50px;
}

body, div {
	font-size: 1.0em;
	font-family: 'Nanum Gothic', 'verdana', 'arial', 'dotum', '돋움';
	color: #6e6e6e;
	letter-spacing: 0px;
}

#scontainer00 {
	width: 100%;
	position: relative;
	margin: 0 auto;
	background: #fff;
	min-height: 700px;
}

.board_search {
	float: right;
	width: 200px;
	height: 39px;
	margin: 0;
	text-align: right;
	top: 100px;
}

#d1_input {
	float: right;
	width: 280px;
	height: 39px;
	font-size: 16px bold;
	text-transform: uppercase;
	letter-spacing: 2px;
	color: black;
	background-color: none;
	border: 2px;
	border-radius: 45px;
	margin: 0;
	text-align: left;
}

#board_area {
	text-align: center;
	font-size: 15px;
	color: #666;
	min-height: 360px;
	font-family: 'NanumGothic', 'Malgun Gothic', 'verdana', 'arial', 'dotum',
		'돋움';
	position: relative;
}
#board_area a:link, #board_area a:visited, #board_area a:active {
	color: #666;
	text-decoration: none;
}
.a_right {
	position: absolute;
	top: 20px;
	right: 0;
}
#board_area a:hover {
	color: #2f2f2f;
}
.color_red {
	color: #d60c0c;
}
input.board_bt_style01 {
	border: 0px;
	color: #fff;
	background: #a17d33;
	width: 83px;
	height: 30px;
	line-height: 29px;
	font-size: 0.9em;
	cursor: pointer;
}
input.board_bt_style02 {
	border: 0px;
	width: 83px;
	height: 30px;
	line-height: 29px;
	color: #7c7b7b;
	background: #e7e7e7;
	font-size: 0.9em;
	cursor: pointer;
}
input.board_bt_style03 {
	border: 0px;
	width: 50px;
	height: 25px;
	line-height: 25px;
	color: #fff;
	background: #666c74;
	font-size: 1em;
	cursor: pointer;
}

/*LIST*/
 .free_board, .free_board_view, .free_board_write {
	width: 100%;
	border-top: 2px solid #a17d33;
}
.free_board th {
	border-bottom: 1px solid #ddd;
	padding: 15px 10px;
	/* background: url("../board_img/line_bg.gif") no-repeat center right; */
}
.free_board td, .free_board_view td {
	border-bottom: 1px solid #ddd;
	padding: 15px 10px;
}
.bor_l {
	border-left: 3px solid #ddd;
}
.bor_r {
	border-right: 3px solid #ddd;
}
.title_area {
	text-align: left;
}
.ttl_area {
	text-align: left;
}

.title_area span {
	font-weight: bold;
	color: #dd4949;
}
.bt_list {
	padding: 6px 25px;
	background: #005faf;
	color: #fff;
	font-weight: bold;
	border: 0px solid;
}
.board_search select {
	height: 25px;
}
.search_b {
	width: 200px;
	height: 25px;
	text-align: left;
	margin-left: 3px;
}
.board_bottom_bar {
	width: 130px;
	_background: #326cb4;
	border: 1px #ddd solid;
	color: #666;
	height: 23px;
	margin-left: 3px;
	line-height: 23px;
}

/* VIEW */
.free_board_view {
	border-bottom: 1px solid #ddd;
}
.free_board_view th {
	border-bottom: 1px solid #ddd;
	padding: 15px 8px;
	background: url("../board_img/line_bg.gif") no-repeat center right;
	text-align: center;
}
.free_board_view td {
	text-align: left;
	padding: 5px 10px;
}
th.board_title01 {
	font-size: 12px;
	font-weight: bold;
	text-align: left;
}
td.board_b {
	border-bottom: 1px solid #ddd;
}
td.board_bn {
	border-bottom: none;
}
.view_pd {
	padding: 15px;
	line-height: 20px;
}
th.board_data {
	font-size: 11px;
	font-weight: normal;
}
th.board_stitle {
	font-weight: normal;
	font-size: 11px;
}
th.a_left {
	text-align: left;
}
.number {
	margin: 20px 0;
	clear: both;
}
.number img {
	vertical-align: middle;
}
td.notice {
	background: #fff;
}
.notice span {
	font-weight: bold;
}
span.notice_bg {
	height: 10px;
	width: 30px;
	margin-top: 1px;
	padding: 4px 5px 0px 5px;
	text-align: center;
	background: #a17d33;
}
th.last_bg {
	background: none;
}
.datedate1 {
	cursor: pointer;
	position: relative;
	left: -180px;
}
.datedate2 {
	cursor: pointer;
	position: relative;
	left: 0px;
	top: -25px
}
.btn {
	border: 0px;
	width: 50px;
	height: 25px;
	line-height: 25px;
	color: #fff;
	background: #666c74;
	font-size: 0.9em;
	cursor: pointer;
	border-radius: 3px;
	position: relative;
	top: -25px;
}
.btn:hover {
	background-color: #F95E25;
}
.btn2 {
	border: 0px;
	color: #fff;
	background: #666c74;
	width: 83px;
	height: 30px;
	line-height: 29px;
	font-size: 14px;
	cursor: pointer;
	border-radius: 5px;
}
.btn2:hover {
	background-color: #F95E25;
}
.select {
	border: 1px solid #ccc;
	height: 25px;
}
.write_btn {
	float: right;
}
.img {
	position: relative;
	top: 0px;
}
.b {
	position: relative;
	top: 8px;
}
.page {
	margin-top: 30px;
	text-align: center;
	margin-botton: 30px;
}
 
 </style>

<script type="text/javascript"
	src="${ pageContext.servletContext.contextPath }/resources/js/jquery-3.6.1.min.js"></script>
<script type="text/javascript">
   function Change3() {
      var key = test3.value
      if (key == 8) {
         document.all["d8"].style.display = "block";
         document.all["d9"].style.display = "none";
      }
      if (key == 9) {
         document.all["d8"].style.display = "none";
         document.all["d9"].style.display = "block";
      }
   }

   //글쓰기 버튼 클릭시 실행되는 함수
   function showWriteForm() {
      //게시원글 쓰기 페이지로 이동 처리
      location.href = "${ pageContext.servletContext.contextPath }/nwform.do";
   }
</script>
</head>

<body>
	<c:import url="/WEB-INF/views/common/nav.jsp" />

	<!-- Wrap -->
	<div id="wrap">
		<!-- Container -->
		<div id="scontainer00">
			<div class="s_container">
				<ul class="stab">
					<a href="${ pageContext.servletContext.contextPath }/nlist.do">
						<%-- <img
                  src="${ pageContext.servletContext.contextPath }/resources/notice_img/n_list.png"
                  onmouseover="this.src='${ pageContext.servletContext.contextPath }/resources/notice_img/n_listo.png'"
                  onmouseout="this.src='${ pageContext.servletContext.contextPath }/resources/notice_img/n_list.png'"> --%>
						<input type="submit" value="전체목록" class="btn2" style="position: relative; left: 430px;">
					</a>
				</ul>
				<!-- 항목별 검색 기능 추가 -->
				<div id="board_area">
					<div class="board_search">
						<select id="test3" onchange="Change3()"
							style="position: relative; left: -305px; top: 25px;">
							<option value="8">제목</option>
							<option value="9">날짜</option>
						</select>
						<div id="d8" style="display: block">
							<form action="nsearchTitle.do" method="get">
								<input type="search" name="keyword" placeholder=" 검색할 내용을 넣으시오"
									style="position: relative; left: -99px; width: 242px;">
								<input type="submit" value="검색" class="btn">
							</form>
						</div>
						<div id="d9" style="display: none">
							<form action="nsearchDate.do" method="get" class="board_search">
								<input type="date" name="begin" class="datedate1"> <input
									type="date" name="end" class="datedate2"> <input
									type="submit" value="검색" class="btn">
							</form>
						</div>
					</div>

					<br> <br> <br>
					<div id="board_area">
						<table cellpadding="0" cellspacing="0" class="free_board"
							summary="" border="0">
							<colgroup>
								<col width="100">
								<col width="">
								<col width="150">
								<col width="120">
								<col width="120">
								<col width="100">
							</colgroup>
							<thead>
								<tr>
									<th>&nbsp;&nbsp;<img
										src="${ pageContext.servletContext.contextPath }/resources/notice_img/t_00.png"></th>
									<th><img
										src="${ pageContext.servletContext.contextPath }/resources/notice_img/t_01.png"></th>
									<th><img
										src="${ pageContext.servletContext.contextPath }/resources/notice_img/t_07.png"></th>
									<th><img
										src="${ pageContext.servletContext.contextPath }/resources/notice_img/t_02.png"></th>
									<th><img
										src="${ pageContext.servletContext.contextPath }/resources/notice_img/t_04.png"></th>
									<th><img
										src="${ pageContext.servletContext.contextPath }/resources/notice_img/t_06.png"></th>
								</tr>
							</thead>
							<tbody>
								<!-- 공지사항 -->
								<c:forEach items="${ requestScope.list }" var="n">
									<tr align="center">
										<td align="center"><c:if test="${ n.importance eq 1 }">${ n.noticeno }</c:if>
											<c:if test="${ n.importance eq 2 }">
												<img
													src="${ pageContext.servletContext.contextPath }/resources/notice_img/notice.png">
											</c:if></td>
										<!-- 공지제목 클릭시 해당 글의 상세보기로 넘어가게 처리 -->
										<c:url var="ndt" value="/ndetail.do">
											<c:param name="noticeno" value="${ n.noticeno }" />
											<c:param name="page" value="${ currentPage }" />
										</c:url>
										<td class="ttl_area"><a href="${ ndt }"
											style="text-decoration: none;">${ n.noticetitle }</a>&nbsp;&nbsp;&nbsp;&nbsp;
											<span class="img"> <c:if test="${ !empty n.attaches }">
													<img
														src="${ pageContext.servletContext.contextPath }/resources/notice_img/upfile.png">&nbsp;&nbsp;
                                       </c:if></span> <c:if
												test="${ empty n.attaches }">&nbsp;&nbsp;</c:if> <!-- new 3일간 표시 -->
											<%-- <!-- 현재시간 -->
                                       <c:set var="now" value="<%=new java.util.Date()%>" /> 
                                    <!-- 현재 날짜 중 '일'만 추출 -->
                                       <fmt:formatDate var="nowday" value="${now }" pattern="dd" />
                                     <!-- 날짜를 숫자로 변환 -->
                                       <fmt:parseNumber var="nowNday" value="${nowday }" type="number" />
                                    <!-- 공지 등록 날짜 중 '일'만 추출 -->
                                        <fmt:formatDate var="noticeDay" value="${n.noticedate }" pattern="dd" /> 
                                    <!-- 게시글 작성날짜를 숫자로 -->
                                       <fmt:parseNumber var="noticeNday" value="${noticeDay}" type="number" /> <!-- 날짜를 숫자로 변환 -->
                                    <!-- 현재시간에서 공지등록 날짜를 뺀 숫자가 0,1,2 인 경우 -->
                                       <!-- 3일동안은 new 표시 -->
                                       <c:choose>
                                       <c:when test="${nowday eq noticeDay }">
                                       &nbsp;&nbsp;&nbsp;&nbsp;<c:if test="${nowNday - noticeNday lt 3 }">
                                       <img src="${ pageContext.servletContext.contextPath }/resources/notice_img/btn_new.gif" alt ="" />
                                       ${nowNday - noticeNday} 
                                       </c:if>
                                       </c:when>
                                       
                                       <c:when test="${nowday ne noticeDay }" >
                                       &nbsp;&nbsp;&nbsp;&nbsp;<c:if test="${(nowNday + 30 ) - noticeNday lt 3 }">
                                       <img src="${ pageContext.servletContext.contextPath }/resources/notice_img/btn_new.gif" alt ="" />
                                       ${(nowNday + 30 ) - noticeNday }
                                       </c:if>
                                       </c:when>
                                 </c:choose> --%> <c:set var="now"
												value="<%=new java.util.Date()%>" /> <!-- 현재시간 --> <fmt:parseNumber
												value="${now.time / (1000*60*60*24)}" integerOnly="true"
												var="today" /> <!-- 현재시간을 숫자로 --> <fmt:parseNumber
												value="${n.noticedate.time / (1000*60*60*24)}"
												integerOnly="true" var="chgDttm" /> <!-- 게시글 작성날짜를 숫자로 -->
											<c:if test="${today - chgDttm le 3}">
												<!-- 3일동안은 new 표시 -->
												<img
													src="${ pageContext.servletContext.contextPath }/resources/notice_img/btn_new.gif"
													alt="new" />
											</c:if> <%-- &nbsp;&nbsp;&nbsp;&nbsp;<c:if test="${ n.noticedate > '2022-11-23' }">
                                       <img src="${ pageContext.servletContext.contextPath }/resources/notice_img/btn_new.gif"></c:if> 
                                       <c:if test="${ n.noticedate < '2022-11-23' }">&nbsp;</c:if>  --%>

										</td>
										<td></td>
										<td>${ n.userid }</td>
										<td><fmt:formatDate value="${ n.noticedate }"
												pattern="yyyy-MM-dd" /></td>
										<td align="center">${ n.readcount }</td>
									</tr>
								</c:forEach>
						</table>
					</div>
				</div>

				<%-- <center> --%>
				<br>

				<ul class="write_btn">
					<c:if test="${ sessionScope.loginMember.admin eq 'Y' }">
						<a href="${ pageContext.servletContext.contextPath }/movewrite.do">
							<%-- <img
                              src="${ pageContext.servletContext.contextPath }/resources/notice_img/n_list2.png"
                              onmouseover="this.src='${ pageContext.servletContext.contextPath }/resources/notice_img/n_list2o.png'"
                              onmouseout="this.src='${ pageContext.servletContext.contextPath }/resources/notice_img/n_list2.png'"> --%>
							<input type="submit" value="글쓰기" class="btn2">
						</a>
					</c:if>
				</ul>
				<!-- 전체 목록 페이징 처리 -->
				<!-- 페이지 표시 영역 -->
				<!-- 1페이지로 이동 처리 -->
				<c:if test="${ empty action }">
					<div class="page">
						<span> <c:if test="${ currentPage eq 1 }">
								<img
									src="${ pageContext.servletContext.contextPath }/resources/notice_img/arrow_l_end.gif">
							</c:if> <c:if test="${ currentPage > 1 }">
								<c:url var="bl" value="/nlist.do">
									<c:param name="page" value="1" />
								</c:url>
								<a href="${ bl }"><img
									src="${ pageContext.servletContext.contextPath }/resources/notice_img/arrow_l_end.gif"></a>
							</c:if> <!-- 이전 페이지그룹으로 이동 처리 --> <c:if
								test="${ (currentPage - 10) < startPage and (currentPage - 10) > 1 }">
								<c:url var="bl2" value="/nlist.do">
									<c:param name="page" value="${ startPage - 10 }" />
								</c:url>
								<a href="${ bl2 }"><img
									src="${ pageContext.servletContext.contextPath }/resources/notice_img/arrow_l.gif"></a> &nbsp;</c:if>
							<c:if
								test="${ !((currentPage - 10) < startPage and (currentPage - 10) > 1) }">
								<img
									src="${ pageContext.servletContext.contextPath }/resources/notice_img/arrow_l.gif">&nbsp;</c:if>
						</span>
						<!-- 현재 페이지가 속한 페이지 그룹 페이지 숫자 출력 -->
						<span
							style="text-align: center; padding: 10px 0px 10px 0px; margin-top: 10px; vertical-align: top;">
							<c:forEach var="p" begin="${ startPage }" end="${ endPage }"
								step="1">
								<c:if test="${ p eq currentPage }">
									<font size="5" style="font-weight: bold"><b>[${ p }]</b>&nbsp;</font>
								</c:if>
								<c:if test="${ p ne currentPage }">
									<c:url var="bl3" value="/nlist.do">
										<c:param name="page" value="${ p }" />
									</c:url>
									<a href="${ bl3 }"><b>${ p }</b>&nbsp;</a>
								</c:if>
							</c:forEach>
						</span>
						<!-- 다음 페이지그룹으로 이동 처리 -->
						<span> <c:if
								test="${ (currentPage + 10) > endPage and (currentPage + 10) < maxPage }">
								<c:url var="bl4" value="/nlist.do">
									<c:param name="page" value="${ endPage + 10 }" />
								</c:url>
								<a href="${ bl4 }"><img
									src="${ pageContext.servletContext.contextPath }/resources/notice_img/arrow_r.gif"></a>
							</c:if> <c:if
								test="${ !((currentPage + 10) > endPage and (currentPage + 10) < maxPage) }">
								<img
									src="${ pageContext.servletContext.contextPath }/resources/notice_img/arrow_r.gif">
							</c:if> <!-- 끝페이지로 이동 처리 --> <c:if test="${ currentPage eq maxPage }">
								<img
									src="${ pageContext.servletContext.contextPath }/resources/notice_img/arrow_r_end.gif"> &nbsp; 
                           </c:if> <c:if test="${ currentPage < maxPage }">
								<c:url var="bl5" value="/nlist.do">
									<c:param name="page" value="${ maxPage }" />
								</c:url>
								<a href="${ bl5 }"><img
									src="${ pageContext.servletContext.contextPath }/resources/notice_img/arrow_r_end.gif"></a> &nbsp;
                           </c:if>
						</span>
					</div>
				</c:if>
				<!-- ----------------------------------------- -->
				<div class="page">
					<c:if test="${ !empty action }">
						<!-- 검색 목록 페이징 처리 -->
						<!-- 페이지 표시 영역 -->
						<!-- 1페이지로 이동 처리 -->
						<c:if test="${ currentPage eq 1 }">
							<img
								src="${ pageContext.servletContext.contextPath }/resources/notice_img/arrow_l_end.gif">
						</c:if>
						<c:if test="${ currentPage > 1 }">
							<c:if test="${ action eq 'title' }">
								<c:url var="nsl" value="nsearchTitle.do">
									<c:param name="keyword" value="${ keyword }" />
									<c:param name="page" value="1" />
								</c:url>
							</c:if>

							<c:if test="${ action eq 'date' }">
								<c:url var="nsl" value="nsearchDate.do">
									<c:param name="begin" value="${ begin }" />
									<c:param name="end" value="${ end }" />
									<c:param name="page" value="1" />
								</c:url>
							</c:if>
							<a href="${ nsl }"><img
								src="${ pageContext.servletContext.contextPath }/resources/notice_img/arrow_l_end.gif"></a>
						</c:if>
						<!-- 이전 페이지그룹으로 이동 처리 -->
						<c:if
							test="${ (currentPage - 10) < startPage and (currentPage - 10) > 1 }">
							<c:if test="${ action eq 'title' }">
								<c:url var="nsl" value="nsearchTitle.do">
									<c:param name="keyword" value="${ keyword }" />
									<c:param name="page" value="${ startPage - 10 }" />
								</c:url>
							</c:if>

							<c:if test="${ action eq 'date' }">
								<c:url var="nsl" value="nsearchDate.do">
									<c:param name="begin" value="${ begin }" />
									<c:param name="end" value="${ end }" />
									<c:param name="page" value="${ startPage - 10 }" />
								</c:url>
							</c:if>
							<a href="${ nsl }"><img
								src="${ pageContext.servletContext.contextPath }/resources/notice_img/arrow_l.gif"></a> &nbsp;
                           </c:if>
						<c:if
							test="${ !((currentPage - 10) < startPage and (currentPage - 10) > 1) }">
							<img
								src="${ pageContext.servletContext.contextPath }/resources/notice_img/arrow_l.gif"> &nbsp;
                           </c:if>
						<!-- 현재 페이지가 속한 페이지 그룹 페이지 숫자 출력 -->
						<span
							style="text-align: center; padding: 10px 0px 10px 0px; margin-top: 10px; vertical-align: top;">
							<c:forEach var="p" begin="${ startPage }" end="${ endPage }"
								step="1">
								<c:if test="${ p eq currentPage }">
									<font size="5" style="font-weight: bold"><b>[${ p }]&nbsp;&nbsp;</b></font>
								</c:if>
								<c:if test="${ p ne currentPage }">
									<c:if test="${ action eq 'title' }">
										<c:url var="nsl" value="nsearchTitle.do">
											<c:param name="keyword" value="${ keyword }" />
											<c:param name="page" value="${ p }" />
										</c:url>
									</c:if>

									<c:if test="${ action eq 'date' }">
										<c:url var="nsl" value="nsearchDate.do">
											<c:param name="begin" value="${ begin }" />
											<c:param name="end" value="${ end }" />
											<c:param name="page" value="${ p }" />
										</c:url>
									</c:if>
									<a href="${ nsl }"><b>${ p }&nbsp;&nbsp;</b></a>
								</c:if>
							</c:forEach>
						</span>
						<!-- 다음 페이지그룹으로 이동 처리 -->
						<c:if
							test="${ (currentPage + 10) > endPage and (currentPage + 10) < maxPage }">
							<c:if test="${ action eq 'title' }">
								<c:url var="nsl" value="nsearchTitle.do">
									<c:param name="keyword" value="${ keyword }" />
									<c:param name="page" value="${ endPage + 10 }" />
								</c:url>
							</c:if>

							<c:if test="${ action eq 'date' }">
								<c:url var="nsl" value="nsearchDate.do">
									<c:param name="begin" value="${ begin }" />
									<c:param name="end" value="${ end }" />
									<c:param name="page" value="${ endPage + 10 }" />
								</c:url>
							</c:if>
							<a href="${ nsl }"><img
								src="${ pageContext.servletContext.contextPath }/resources/notice_img/arrow_r.gif"></a>
						</c:if>
						<c:if
							test="${ !((currentPage + 10) > endPage and (currentPage + 10) < maxPage) }">
							<img
								src="${ pageContext.servletContext.contextPath }/resources/notice_img/arrow_r.gif">
						</c:if>
						<!-- 끝페이지로 이동 처리 -->
						<c:if test="${ currentPage eq maxPage }">
							<img
								src="${ pageContext.servletContext.contextPath }/resources/notice_img/arrow_r_end.gif"> &nbsp; 
                           </c:if>
						<c:if test="${ currentPage < maxPage }">
							<c:if test="${ action eq 'title' }">
								<c:url var="nsl" value="nsearchTitle.do">
									<c:param name="keyword" value="${ keyword }" />
									<c:param name="page" value="${ maxPage }" />
								</c:url>
							</c:if>

							<c:if test="${ action eq 'date' }">
								<c:url var="nsl" value="nsearchDate.do">
									<c:param name="begin" value="${ begin }" />
									<c:param name="end" value="${ end }" />
									<c:param name="page" value="${ maxPage }" />
								</c:url>
							</c:if>
							<a href="${ nsl }"><img
								src="${ pageContext.servletContext.contextPath }/resources/notice_img/arrow_r_end.gif"></a> &nbsp;
                           </c:if>
					</c:if>
				</div>
			</div>
		</div>
	</div>
</body>
</html>
