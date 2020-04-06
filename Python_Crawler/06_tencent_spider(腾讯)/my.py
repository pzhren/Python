#encoding: utf-8

# 腾讯招聘网爬虫作业
# 现在已经不能用了

from lxml import etree
import requests

text= """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>职位搜索 | 社会招聘 | Tencent 腾讯招聘</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<!-- Js Css -->
     		<link media="screen" href="http://cdn.tencentgroup.qq.com/hr_static/css/all.css?max_age=86412" type="text/css" rel="stylesheet" />


	<script type="text/javascript" src="http://cdn.tencentgroup.qq.com/hr_static/js/jquery-1.3.2.min.js"></script>


    

    <script type="text/javascript" src="http://cdn.tencentgroup.qq.com/hr_static/js/jquery-ui-1.7.2.custom.min.js"></script>


    <script type="text/javascript" src="http://cdn.tencentgroup.qq.com/hr_static/js/thickbox.js"></script>


    <link media="screen" href="http://cdn.tencentgroup.qq.com/hr_static/css/thickbox.css" type="text/css" rel="stylesheet" />


    <script type="text/javascript" src="http://cdn.tencentgroup.qq.com/hr_static/js/functions.js"></script>


    <script type="text/javascript" src="http://cdn.tencentgroup.qq.com/hr_static/js/utils.js"></script>


    

    <script type="text/javascript" src="http://cdn.tencentgroup.qq.com/hr_static/js/all.js?max_age=86412"></script>	<!-- Js Css -->
	<script>
		var keywords_json = ["python"];
	</script>
</head>

<body>
    	<div id="header">
    	<div class="maxwidth">
    		<a href="index.php" class="left" id="logo"><img src="http://cdn.tencentgroup.qq.com/hr_static/img/logo.png"/></a>
    		<div class="right" id="headertr">
    			<div class="right pl9" id="topshares">
    				<div class="shares">
    					<span class="left">分享到：</span>
		    			<a href="javascript:;" onclick="shareto('qqt','top');" id="qqt" title="分享到腾讯微博">分享到腾讯微博</a>
		    			<a href="javascript:;" onclick="shareto('qzone','top');" id="qzone" title="分享到QQ空间">分享到QQ空间</a>
		    			<a href="javascript:;" onclick="shareto('pengyou','top');" id="pengyou" title="分享到腾讯朋友">分享到腾讯朋友</a>
		    			<a href="javascript:;"  onclick="shareto('sinat','top');"id="sinat" title="分享到新浪微博">分享到新浪微博</a>
		    			<a href="javascript:;"  onclick="shareto('renren','top');"id="renren" title="分享到人人网">分享到人人网</a>
		    			<a href="javascript:;"  onclick="shareto('kaixin001','top');"id="kaixin" title="分享到开心网">分享到开心网</a>
		    			<div class="clr"></div>
    				</div>
    				<a href="javascript:;">分享</a>
    			</div>
    			<div class="right pl9">
    				<a href="http://t.qq.com/QQjobs" id="tqq" target="_blank">收听腾讯招聘</a>
    			</div>
    			<div class="right pr9">
    				    				    					<a href="login.php" id="header_login_anchor">登录</a><span class="plr9">|</span><a href="reg.php">注册</a>
    				    				<span class="plr9">|</span><a href="question.php">反馈建议</a>
    				<span class="plr9">|</span><a href="http://careers.tencent.com/global" target="_blank">Tencent Global Talent</a>
    				<script>
    					var User_Account = "";
    				</script>
    				    			</div>
    			<div class="clr"></div>
    		</div>
    		<div class="clr"></div>
    	</div>
    	<div id="menus">
    		<div class="maxwidth">
	    		<ul id="menu" class="left">
	    			<li id="nav1" ><a href="index.php">&nbsp;</a></li>
	    			<li id="nav2" class="active" ><a href="social.php">&nbsp;</a></li>
	    			<li id="nav3"><a href="about.php">&nbsp;</a></li>
	    			<li id="nav4"><a href="workInTencent.php">&nbsp;</a></li>
	    		</ul>
	    		<a class="right texti9" target="_blank" id="navxy" href="http://join.qq.com">校园招聘</a>
	    		<div class="clr"></div>
	    	</div>
    	</div>
    </div>    <div id="sociaheader">
			</div>
    <div id="position" class="maxwidth">
    	<a name="a" id="a"></a>
    	<div class="left wcont_b box">
		    <div class="blueline"><div class="butzwss"></div></div>
		    <form id="searchform" class="buts1">
		    	<div id="searchrow1">
		    		<div id="search1"><input id="search2" name="keywords" t="请输入关键词" value="python" class="left"/><input class="left" id="search3" type="submit" value=""/><div class="clr"></div></div>
		    		<input type="hidden" name="lid" value="0"/>
		    		<input type="hidden" name="tid" value="0"/>
		    	</div>
		    	<div id="searchrow2">
		    		<div class="srow2l left"></div>
		    		<div class="left items pl9 itemnone" id="additems">
		    			<a href="position.php?keywords=python&tid=0" class="item active"><span><font>全部</font></span></a>
		    					    				<a class="item" href="position.php?keywords=python&tid=0&lid=2218"><span><font>深圳</font></span></a>
		    					    				<a class="item" href="position.php?keywords=python&tid=0&lid=2156"><span><font>北京</font></span></a>
		    					    				<a class="item" href="position.php?keywords=python&tid=0&lid=2175"><span><font>上海</font></span></a>
		    					    				<a class="item" href="position.php?keywords=python&tid=0&lid=2268"><span><font>成都</font></span></a>
		    					    				<a class="item" href="position.php?keywords=python&tid=0&lid=2196"><span><font>广州</font></span></a>
		    					    				<a class="item" href="position.php?keywords=python&tid=0&lid=33"><span><font>美国</font></span></a>
		    					    				<a class="item" href="position.php?keywords=python&tid=0&lid=2252"><span><font>杭州</font></span></a>
		    					    				<a class="item" href="position.php?keywords=python&tid=0&lid=2426"><span><font>昆明</font></span></a>
		    					    				<a class="item" href="position.php?keywords=python&tid=0&lid=2459"><span><font>香港</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=python&tid=0&lid=2226"><span><font>重庆</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=python&tid=0&lid=2407"><span><font>大连</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=python&tid=0&lid=2367"><span><font>长沙</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=python&tid=0&lid=2320"><span><font>合肥</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=python&tid=0&lid=2355"><span><font>武汉</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=python&tid=0&lid=2436"><span><font>贵阳</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=python&tid=0&lid=2228"><span><font>南京</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=python&tid=0&lid=2284"><span><font>厦门</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=python&tid=0&lid=32"><span><font>韩国</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=python&tid=0&lid=60"><span><font>马来西亚</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=python&tid=0&lid=2293"><span><font>济南</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=python&tid=0&lid=2406"><span><font>沈阳</font></span></a>
		    					    		</div>
		    		<div class="left"><a href="javascript:;" class="more2">更多</a></div>
		    		<div class="clr"></div>
		    	</div>
		    	<div id="searchrow3">
		    		<div class="srow2l left"></div>
		    		<div class="left items pl9">
		    			<a href="position.php?keywords=python&lid=0" class="item active"><span><font>全部</font></span></a>
		    					    				<a class="item" href="position.php?keywords=python&lid=0&tid=87"><span><font>技术类</font></span></a>
		    					    				<a class="item" href="position.php?keywords=python&lid=0&tid=82"><span><font>产品/项目类</font></span></a>
		    					    				<a class="item" href="position.php?keywords=python&lid=0&tid=83"><span><font>市场类</font></span></a>
		    					    				<a class="item" href="position.php?keywords=python&lid=0&tid=81"><span><font>设计类</font></span></a>
		    					    				<a class="item" href="position.php?keywords=python&lid=0&tid=84"><span><font>职能类</font></span></a>
		    					    				<a class="item" href="position.php?keywords=python&lid=0&tid=85"><span><font>内容编辑类</font></span></a>
		    					    				<a class="item" href="position.php?keywords=python&lid=0&tid=86"><span><font>客户服务类</font></span></a>
		    					    		</div>
		    		<div class="clr"></div>
		    	</div>
		    </form>
		    <table class="tablelist" cellpadding="0" cellspacing="0">
		    	<tr class="h">
		    		<td class="l" width="374">职位名称</td>
		    		<td>职位类别</td>
		    		<td>人数</td>
		    		<td>地点</td>
		    		<td>发布时间</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=29553&keywords=python&tid=0&lid=0">WXG02-133 微信运维工程师(广州）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>广州</td>
					<td>2017-11-26</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=28921&keywords=python&tid=0&lid=0">HY2-大数据高级工程师（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2017-11-26</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=31801&keywords=python&tid=0&lid=0">HY2-前端开发工程师（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2017-11-26</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=30868&keywords=python&tid=0&lid=0">HY2-高级数据分析工程师（深圳）</a><span class="hot">&nbsp;</span></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2017-11-26</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=24411&keywords=python&tid=0&lid=0">18428-财付通清算业务测试工程师（深圳）</a></td>
					<td>技术类</td>
					<td>7</td>
					<td>深圳</td>
					<td>2017-11-26</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=32549&keywords=python&tid=0&lid=0">22989-腾讯云售后技术支持（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2017-11-26</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=32878&keywords=python&tid=0&lid=0">MIG16-地图后台高级开发工程师（北京）</a><span class="hot">&nbsp;</span></td>
					<td>技术类</td>
					<td>1</td>
					<td>北京</td>
					<td>2017-11-26</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=31864&keywords=python&tid=0&lid=0">19823-动画绑定师</a></td>
					<td>设计类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2017-11-26</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=26381&keywords=python&tid=0&lid=0">TEG14-高级业务运维工程师（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2017-11-26</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=30128&keywords=python&tid=0&lid=0">TEG11-数据挖掘高级工程师（深圳）</a><span class="hot">&nbsp;</span></td>
					<td>技术类</td>
					<td>5</td>
					<td>深圳</td>
					<td>2017-11-26</td>
		    	</tr>
		    			    	<tr class="f">
		    		<td colspan="5">
		    			<div class="left">共<span class="lightblue total">423</span>个职位</div>
		    			<div class="right"><div class="pagenav"><a href="javascript:;" class="noactive" id="prev">上一页</a><a class="active" href="javascript:;">1</a><a href="position.php?lid=&tid=&keywords=python&start=10#a">2</a><a href="position.php?lid=&tid=&keywords=python&start=20#a">3</a><a href="position.php?lid=&tid=&keywords=python&start=30#a">4</a><a href="position.php?lid=&tid=&keywords=python&start=40#a">5</a><a href="position.php?lid=&tid=&keywords=python&start=50#a">6</a><a href="position.php?lid=&tid=&keywords=python&start=60#a">7</a><a href="position.php?lid=&tid=&keywords=python&start=70#a">...</a><a href="position.php?lid=&tid=&keywords=python&start=420#a">43</a><a href="position.php?lid=&tid=&keywords=python&start=10#a" id="next">下一页</a><div class="clr"></div></div></div>
		    			<div class="clr"></div>
		    		</td>
		    	</tr>
		    </table>
		</div>
		<div class="right wcont_s box">
		    <div class="blueline"><div class="butcjwt"></div></div>
		    <div class="module_faqs square"><a href="faq.php?id=5" title="如何应聘腾讯公司的职位？">如何应聘腾讯公司的职位？</a><a href="faq.php?id=3" title="应届生如何应聘？">应届生如何应聘？</a><a href="faq.php?id=19" title="腾讯应聘流程是什么？">腾讯应聘流程是什么？</a><a href="faq.php?id=20" title="我注册了简历，但为什么没有人联系我？">我注册了简历，但为什么没...</a><a href="faq.php?id=22" title="我忘记密码了，怎么办？">我忘记密码了，怎么办？</a><a href="faq.php?id=23" title="如何进行简历修改？">如何进行简历修改？</a></div>		</div>
		<div class="clr"></div>
	</div>
   	<div id="homeDep"><table id="homeads"><tr><td align="center"><a href="http://tencent.avature.net/career" target="blank">全球招聘</a></td><td align="center"><a href="http://game.qq.com/hr/" target="blank">互动娱乐事业群招聘</a></td><td align="center"><a href="http://hr.tencent.com/position.php?lid=&tid=&keywords=WXG" target="blank">微信事业群招聘</a></td><td align="center"><a href="http://hr.qq.com/" target="blank">技术工程事业群招聘</a></td><td align="center"><a href="http://snghr.tencent.com" target="blank">社交网络事业群招聘</a></td><td align="center"><a href="http://mighr.qq.com" target="blank">移动互联网事业群招聘</a></td><td align="center"><a href="http://hr.tencent.com/position.php?keywords=OMG" target="blank">网络媒体事业群招聘</a></td></tr></table></div>    	<div id="footer">
		<div>
			<a href="http://www.tencent.com/" target="_blank">关于腾讯</a><span>|</span><a href="http://www.qq.com/contract.shtml" target="_blank">服务条款</a><span>|</span><a href="http://adver.qq.com/" target="_blank">广告服务</a><span>|</span><a href="http://hr.tencent.com/" target="_blank">腾讯招聘</a><span>|</span><a href="http://careers.tencent.com/global" target="_blank">Tencent Global Talent</a><span>|</span><a href="http://gongyi.qq.com/" target="_blank">腾讯公益</a><span>|</span><a href="http://service.qq.com/" target="_blank">客服中心</a>
	    </div>
		<p>Copyright &copy; 1998 - 2017 Tencent. All Rights Reserved.</p>
	</div>
	<script type="text/javascript" src="http://pingjs.qq.com/tcss.ping.js"></script>
    <script type="text/javascript">
	    if(typeof(pgvMain)=='function')
	        pgvMain("",{virtualDomain:"hr.tencent.com"});
    </script></body>
</html>
"""
BASE_DOMAIN = "http://hr.tencent.com/"
html = etree.HTML(text)
links = html.xpath("//tr[@class='even' or @class='odd']//a/@href")
links = map(lambda url:BASE_DOMAIN+url,links)
for link in links:
    print(link)