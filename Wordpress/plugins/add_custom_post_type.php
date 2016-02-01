<?php 
/*
Plugin Name: Add Post Type Products
Plugin URI: http://localhost/wordpress/wp-content/plugins/add_custrom_post_type/
Description: 为系统添加自定义文章类型(Custom Post Type)和一些定制内容。
Version: 1.0
Author: Solomon Xie
Author URI: http://solomonxie.github.io
License: GPLv2
Notes: 	其实以下的所有话，直接复制到functions.php里，也是一模一样的运行。
*/
?>
<?php 
/*
	========================================
	  为Admin添加“添加商品”的功能及菜单
	========================================
*/
function yeatone_custom_post_type() {
	$labels = array(
		'name'	=> '装备商城',
		'singular_name'	=> 'products',
		'add_new'	=> '添加装备',
		'all_items' => '所有装备',
		'add_new_item'	=> '添加装备',
		'edit_item'	=> '编辑装备',
		'new_item'	=> '新装备',
		'view_item'	=> '浏览装备',
		'search_item'	=>	'搜索装备',
		'not_found'	=>	'未找到装备',
		'not_found_in_trash'	=>	'垃圾箱中未找到装备',
		'parent_item_colon'	=> '父级装备'
	);
	$args = array(
		'labels'	=> $labels,
		'public'	=> true,
		'has_archive'	=> true,
		'publicity_queryable'	=> true,
		'query_var'	=>	true,
		'rewrite'	=> true,
		'capability_type'	=> 'post',
		'hierarchical'	=> false,
		'supports'	=> array( // 必须是suports,少了"s"截然不同！
			// 为自定义文章类型添加各种内置功能
			'title',	//标题
			'author',	//作者
			'excerpt',	//摘要
			'editor', 	//编辑者
			'thumbnail',//缩略图（特色图片）
			'revisions'	//编辑历史
		),
		'taxonomies'	=>	array('category', 'post_tag'),
		'menu_position'	=> 5,
		'exclude_from_search'	=> false
	);
	register_post_type('products', $args); //在Admin主菜单中注册这个新项目
}
add_action('init', 'yeatone_custom_post_type'); //把这个动作(函数）挂到钩子上被自动运行


	
?>