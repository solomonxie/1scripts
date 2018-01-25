<?php 
/**********************************
Functions全面掌控wp的各项功能（包括注册插件、改dashboard等也在这里）
***********************************/

/*
	========================================
	  缩短url引用的函数
	========================================
*/
function myUrl($type='') {
	if ($type == '' or $type == 'dir')
		echo get_stylesheet_directory_uri();
	else if ($type == 'home')
		echo get_home_url();
}

/*
	========================================
	  在Admin中向文章、页面开启主题的支持性功能（缩略图、自定义背景、自定义导航等）
	  主题支持性功能是内置的无需我们单独开发，只要我们声明，wp就会自动添加上去。
	========================================
*/
// -----添加文章特色图像功能-----
	// 为所有类型的文章、页面、自定义文章开启缩略图（特色图像）功能
add_theme_support('post-thumbnails'); 
	// 添加自定义菜单功能（位置在：外观->菜单）
add_theme_support('menus'); 
	// 添加自定义背景功能（位置在：外观->背景）
add_theme_support('custom-background');
	// 添加自定义Logo功能（位置在：外观->顶部）
add_theme_support('custom-header');
