# sclm
bulid a admin management system with python django 
just for test to use django 


使用 python manage.py collectstatic 命令搜集我环境中的静态文件 ， 在settings.py 中增加了
STATICFILES_DIRS ='./Static'

___

模板Template 不属于静态资源 ， 静态资源就是 js  ,css 等网页资源。

使用filer上传的文件（图片或文档或视频）以及 文件的缩略图都不属于静态资源， 它们成为 MEDIA , 媒体资源。


--
使用virtulenv之后， 花了两个小时弄suit效果不存在的问题。 最后的结论是suit 安装的版本不对， 一不小心安装了V2版本的suit . 
