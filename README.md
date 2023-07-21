# sast2023 word game

## 环境配置

目前没有第三方依赖项

## 使用设置

约定以下参数：

```

--file  -f  接文章的路径
--view  -v  在终端显示文章和提示信息
--select -s 选择文章序号

```

文章使用 JSON 存储，的格式如下：

{
    "language": "xxx",
    "articles": [
        {
            "title": "xx",
            "article": "xxx{{1}}xxx{{2}}...xxx",
            "hints": ["xx", "xx", ...]
        }
    ]
}

## 游戏功能

输入自己想要填写的词语，输出填写结果
