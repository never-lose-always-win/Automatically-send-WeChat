import time
import pyautogui as pg
import pyperclip as pc

# 操作间隔为1秒
pg.PAUSE = 1

name = '优优'
msg = 'good morning'
send_time = '09:56:00'  # 时间


def main():
    # 打开微信
    pg.hotkey('ctrl', 'alt', 'w')
    pg.hotkey('ctrl', 'f')

    # 找到对方
    pc.copy(name)
    pg.hotkey('ctrl', 'v')
    pg.press('enter')

    # 发送消息
    pc.copy(msg)
    while True:
        pg.hotkey('ctrl', 'v')
        pg.press('enter')

    # 隐藏微信
    # pg.hotkey('ctrl', 'alt', 'w')


if __name__ == '__main__':
    while True:
        hour = time.localtime()
        now_time = time.strftime("%H:%M:%S", hour)
        if now_time == send_time:
            print(f'时，开始发送消间已到：{send_time}息！')
            main()
            print("任务结束！")
            break
