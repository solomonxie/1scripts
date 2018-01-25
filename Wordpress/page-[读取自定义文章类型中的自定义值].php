<?php 
/********************************
single-[$自定义文章类型名称].php
自定义Post Type类型单页的模板。此模板被调用的前提：
- 注册自定义文章类型时，"单数名称"必须和这个single-[$]中的$一致。
********************************/
/*
===================================
	---获取页面所需所有信息---
1.获取"meta box"或"custom field"或"自定义值"时，可以按照正常的get_post_meta。
但是这里我们是在自定义文章类型的页面，且是又<type>插件帮忙创建的，所以
-> 它会在每个自定义字段的名称（slug）前加上"wpcf-"字样，获取时必须加上。
如：echo get_post_meta($pid, 'wpcf-outfit-size', True);
2.不过我们可以用<type>插件的api来更方便的（其实也不那么方便）的获取。
具体的API使用方法地址在这里；https://wp-types.com/documentation/functions/
其中对于不同种类的自定义值的调用方法是不同的。
罗列一下每种类型值的不同调用方法：
- 日期：types_render_field('outfit-date', array('style'=>'text', 'format'=>'Y/m/d'));
- 邮箱：
===================================
*/
if (have_posts()):
	while (have_posts()):
		the_post();
		$pid = get_the_id();
		$tags = the_tags('', ' ', '');
		$itemid = types_render_field('outfit-id', array());
		$number = types_render_field('outfit-item-number', array());
		$price0 = types_render_field('outfit-original-price',array());
		$price1 = types_render_field('outfit-current-price', array());
		$link = types_render_field("outfit-url", array('output'=>'raw'));
		$size = types_render_field('outfit-size', array( "separator" => " , " ));
		$colors = types_render_field('outfit-colors', array( "separator" => " , " ));
		$date = types_render_field('outfit-date', array('style'=>'text', 'format'=>'Y/m/d'));
		$thumbnail = wp_get_attachment_image_src( get_post_thumbnail_id($pid), array(600,360))[0];
	endwhile;
endif;
?>

<h1><?php echo $colors ?></h1>
