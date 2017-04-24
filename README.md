# android-layout-string-auto-localize
扫描layout中没有按照要求放在strings.xml中的文字，自动放到strings.xml中

开发环境： Windows 10, python 3.6

过程
扫描所有的layout xml ，
 如果 text=后面 不是 @string和 @android:string， 则要加入到 set 中
记录 哪些layout 需要修改 text=， 


后面计算 set 数量
然后 给 字符串 起名字， 做字典 ，名字， 和字符串内容  插入到 values/ strings.xml 里面去 

重新 扫描 之前记录需要改动的 layout.xml ， 替换字符串
