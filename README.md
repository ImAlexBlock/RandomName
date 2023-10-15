# RandomName V2 Update
更新了挺多东西
重新画了ui
现在程序窗口默认在屏幕中心出现（方便咯）
加入了重复设置：当关闭重复选项的时候，将不会在第二次抽取的时候选到第一个人的名字（关闭程序后重置）
优化了一些逆天逻辑
你需要两个文本文档来运行程序：name.txt(用于保存学生名字，一行一个可以直接从excel复制)config.txt
其中config.txt的格式如下：
```//关闭重复抽取（抽过的就不会再抽了）
repeat_extraction=true
//抽取次数，过小会导致观赏性减弱
extractions_number=100```
