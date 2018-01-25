<?php 
/*
Plugin Name: Add Post Type Products
Plugin URI: http://localhost/wordpress/wp-content/plugins/add_custrom_post_type/
Description: 为系统添加自定义文章类型(Custom Post Type)和一些定制内容。
Version: 1.0
Author: Solomon Xie
Author URI: http://solomonxie.github.io
License: GPLv2
Notes: 	1. 其实以下的所有代码，直接复制到functions.php里，也是一模一样的运行。
		2. register_post_type('post_type', array())这个地方，"post_type"是极其重要的命名，因为会显示在其下所有文章的url中，且与模板文件名关联，并会用在其它的调用中。
		3. 在显示自定义文章类型的问题上，有两种显示模板：文章列表和文章详情页。
		默认的，文章列表会调用名叫archive-$post_type.php的文件。
		对应的，文章详情页调用名叫single-$post_type.php的文件。
		4. 在自定义菜单导航的问题上，只能在自定义菜单中，添加自定义链接。
		5. Meta Box插件生成的自定义栏目，调用方法很简单，
		一般为：echo rwmb_meta('name'); 复杂点类型的栏目则需要参考插件文档。
		https://metabox.io/docs/get-meta-value/
*/
?>
<?php 
/*
	========================================
	  为Admin后台添加“添加商品”的功能及菜单
	========================================
*/
function yeatone_custom_post_type() {
	// 注册装备商城类型
	register_post_type('outfits', array(
		'labels' => array( // 后台管理的各项显示名称。只管显示，不影响各处调用，随便改。
			'name' => '装备商城',
			'singular_name' => '装备',
			'add_new' => '添加装备',
			'all_items' => '所有装备',
			'add_new_item' => '添加装备',
			'edit_item' => '编辑装备',
			'new_item' => '新装备',
			'view_item' => '浏览装备',
			'search_item' =>	'搜索装备',
			'not_found' =>	'未找到装备',
			'not_found_in_trash' =>	'垃圾箱中未找到装备',
			'parent_item_colon' => '父级装备'
		),
		'public' => true,
		'has_archive' => true,
		'publicity_queryable' => true,
		'query_var' =>	true,
		'rewrite' => true,
		// 'show_ui' => true,
		'capability_type' => 'post', //是文章还是页面
		'hierarchical' => false, //是否有层级
		'supports' => array( // 必须是suports,少了"s"截然不同！
			// 为自定义文章类型添加各种内置功能
			'title',	//标题
			'author',	//作者
			'excerpt',	//摘要
			'editor', 	//编辑者
			'thumbnail',//缩略图（特色图片）
			'revisions',//编辑历史
			'custom-fields' //自定义栏目
		),
		'taxonomies' =>	array('category', 'post_tag'),
		// 'menu_position'	=> 5, //如果不写这个菜单位置 那就默认添加到最后
		'exclude_from_search' => false //是否可以被搜索到
	) ); //在Admin主菜单中注册这个新项目

	// 户外活动类型
	register_post_type('outdoors', array(
		'labels' => array(
			'name' => '户外活动',
			'singular_name' => 'outdoor',
			'add_new' => '添加活动',
			'all_items' => '所有活动',
			'add_new_item' => '添加活动',
			'edit_item' => '编辑活动',
			'new_item' => '新活动',
			'view_item' => '浏览活动',
			'search_item' =>	'搜索活动',
			'not_found' =>	'未找到活动',
			'not_found_in_trash' =>	'垃圾箱中未找到活动',
			'parent_item_colon' => '父级活动'
		),
		'public' => true,
		'has_archive' => true,
		'publicity_queryable' => true,
		'query_var' =>	true,
		'rewrite' => true,
		'capability_type' => 'post', //是文章还是页面
		'hierarchical' => false, //是否有层级
		'supports' => array( // 必须是suports,少了"s"截然不同！
			// 为自定义文章类型添加各种内置功能
			'title',	//标题
			'author',	//作者
			'excerpt',	//摘要
			'editor', 	//编辑者
			'thumbnail',//缩略图（特色图片）
			'revisions',//编辑历史
			'custom-fields' //自定义栏目
		),
		'taxonomies' =>	array('category', 'post_tag'),
		// 'menu_position'	=> 5, //如果不写这个菜单位置 那就默认添加到最后
		'exclude_from_search' => false //是否可以被搜索到
	) ); //在Admin主菜单中注册这个新项目
}
add_action('init', 'yeatone_custom_post_type'); //把这个动作(函数）挂到钩子上被自动运行


/*
    ===============================================================
      利用Meta Box插件，为指定文章类型添加自定义栏目(Custom Fields)
    ===============================================================  
*/
add_filter( 'rwmb_meta_boxes', 'your_prefix_meta_boxes' );
function your_prefix_meta_boxes( $meta_boxes ) {
    $meta_boxes[] = array(
        'title'      => __( 'Test Meta Box', 'textdomain' ),
        'post_types' => 'outfits',
        'fields'     => array(
            array(
                'id'   => 'name',
                'name' => __( 'Name', 'textdomain' ),
                'type' => 'text',
            ),
            array(
                'id'      => 'gender',
                'name'    => 'Gender',
                'type'    => 'radio',
                'options' => array(
                    'm' => __( 'Male', 'textdomain' ),
                    'f' => __( 'Female', 'textdomain' ),
                ),
            ),
            array(
                'id'   => 'email',
                'name' => __( 'Email', 'textdomain' ),
                'type' => 'email',
            ),
            array(
                'id'   => 'bio',
                'name' => __( 'Biography', 'textdomain' ),
                'type' => 'textarea',
            ),
            array(
                'id'   => 'bio2',
                'name' => __( 'Biography', 'textdomain' ),
                'type' => 'plupload_image',
            ),
        ),
    );
    return $meta_boxes;
}
?>