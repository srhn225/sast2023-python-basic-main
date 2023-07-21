import argparse
import json

def parser_data():
    """
    从命令行读取用户参数
    做出如下约定：
    1. -f 为必选参数，表示输入题库文件
    ...

    :return: 参数
    """
    parser = argparse.ArgumentParser(
        prog="Word filling game",
        description="A simple game",
        allow_abbrev=True
    )

    parser.add_argument("-f", "--file", help="题库文件", required=True)
    parser.add_argument("-v", "--view", help="查看题目和提示",action='store_true')
    parser.add_argument("-s", "--select", help="选择文章序号，默认为0",type=int, default=0)
    # TODO: 添加更多参数
    
    args = parser.parse_args()
    return args



def read_articles(filename):
    """
    读取题库文件

    :param filename: 题库文件名

    :return: 一个字典，题库内容
    """
    with open(filename, 'r', encoding="utf-8") as f:
        data = json.load(f)
    return data
        # TODO: 用 json 解析文件 f 里面的内容，存储到 data 中
    
    



def get_inputs(hints):
    """
    获取用户输入

    :param hints: 提示信息

    :return: 用户输入的单词
    """

    keys = []
    for hint in hints:
        print(f"请输入{hint}：")
        key = input()  # 读取一个用户输入
        keys.append(key)  # 存储到 keys 当中

    return keys


def replace(article, keys):
    """
    替换文章内容

    :param article: 文章内容
    :param keys: 用户输入的单词

    :return: 替换后的文章内容

    """
    for i in range(len(keys)):
        # TODO: 将 article 中的 {{i}} 替换为 keys[i]
        article = article.replace(f"{{{{{i+1}}}}}", keys[i])
        # hint: 你可以用 str.replace() 函数，也可以尝试学习 re 库，用正则表达式替换

    return article


if __name__ == "__main__":
    try:
        args = parser_data()
        data = read_articles(args.file)
        articles = data["articles"]
        article=articles[args.select]
        if args.view:
            print("文章名称：",article["title"])
            print("文章内容：",article["article"])
            print("提示：",article["hints"])
        keys=get_inputs(article["hints"])
        newarticle=replace(article["article"], keys)
        print("新文章内容：")
        print(newarticle)
    except FileNotFoundError:
        print("未找到指定文件")
    except IndexError:
        print("不存在这篇文章")
    
    


    # TODO: 根据参数或随机从 articles 中选择一篇文章
    # TODO: 给出合适的输出，提示用户输入
    # TODO: 获取用户输入并进行替换
    # TODO: 给出结果



