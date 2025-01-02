import pyautogui
import time

# 设置点击的位置 (x, y)
positions = [
    (1026, 1690),  # 第一步：第一个点击位置
    (575, 985),    # 第二步：第二个点击位置
    (768, 1087),   # 第三步：第三个点击位置
    (604, 1052)    # 第四步：第四个点击位置
]

# 设置常见姓氏的拼音列表（100 个）
surnames_pinyin = [
    "zhang", "wang", "li", "zhao", "chen", "qian", "sun", "zhou", "wu", "zheng",
    "feng", "chu", "wei", "jiang", "shen", "han", "yang", "zhu", "qin", "you",
    "xu", "he", "lv", "shi", "kong", "huang","bai", "mao", "qi", "yu", "hu",
    "gao", "lin", "guo", "lu", "luo", "gao", "xia", "cai", "deng", "tan",
    "song", "mao", "pang", "xiong", "jin", "lu", "jiang", "bai", "du", "ye",
    "qu", "yin", "yuan", "bu", "gu", "ping", "meng", "huang", "mu", "xiao",
    "yin", "shao", "zhan", "wang", "chang", "hua", "qiu", "miao", "fang", "yu",
    "qiu", "zhuo", "guan", "lu", "mu", "che", "hou", "long", "wan", "duan",
    "lei", "na", "liang", "tang", "fei", "lai", "yin", "zou", "xiong", "zuo",
    "gui", "yan", "rong", "jin", "pu", "xi", "zhu", "lai", "tu", "yan"
]

# 设置每次操作之间的延迟（秒）
delay = 0.5  # 加快速度

# 循环遍历姓氏列表，逐一输入
for surname in surnames_pinyin:
    # 第一步：在第一个位置点击
    pyautogui.click(positions[0][0], positions[0][1])
    time.sleep(delay)

    # 第二步：在第二个位置点击并输入姓氏
    pyautogui.click(positions[1][0], positions[1][1])  # 点击输入框
    time.sleep(delay)

    # 模拟人类输入拼音
    pyautogui.write(surname, interval=0.05)  # 加快输入速率，每个字符间隔 0.05 秒
    time.sleep(delay)

    # 按下空格键选择第一个候选词（通常是默认的中文字符）
    pyautogui.press('space')
    time.sleep(delay)

    # 第三步：在第三个位置点击
    pyautogui.click(positions[2][0], positions[2][1])
    time.sleep(delay)

    # 第四步：在第四个位置点击
    pyautogui.click(positions[3][0], positions[3][1])
    time.sleep(delay)

    print(f"姓氏 '{surname}' 输入完成！")

print("所有姓氏输入流程完成！")