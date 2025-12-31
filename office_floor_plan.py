import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_office_plan():
    # 設定畫布尺寸與比例 (單位: cm)
    room_length = 723
    room_width = 450

    # 建立畫布
    fig, ax = plt.subplots(figsize=(10, 16)) # 調整為長型比例
    ax.set_xlim(-50, room_width + 50)
    ax.set_ylim(-50, room_length + 50)
    ax.set_aspect('equal')

    # 繪製房間外框
    room = patches.Rectangle((0, 0), room_width, room_length, linewidth=3, edgecolor='#333333', facecolor='#F9F9F9')
    ax.add_patch(room)

    # --- 定義繪圖輔助函數 ---
    def add_rect(x, y, w, h, label, color='#E0E0E0', label_color='black'):
        rect = patches.Rectangle((x, y), w, h, linewidth=1, edgecolor='#555555', facecolor=color)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h/2, label, ha='center', va='center', fontsize=9, color=label_color, fontname='WenQuanYi Zen Hei')

    def add_chair(x, y, direction):
        # 簡單的椅子示意圖
        chair_seat = patches.Circle((x, y), 15, facecolor='#FFFFFF', edgecolor='#555555')
        ax.add_patch(chair_seat)
        # 椅背
        if direction == 'right':
            arc = patches.Arc((x-5, y), 40, 40, theta1=-45, theta2=45, linewidth=2, color='#555555')
        elif direction == 'left':
            arc = patches.Arc((x+5, y), 40, 40, theta1=135, theta2=225, linewidth=2, color='#555555')
        ax.add_patch(arc)

    # --- 開始配置家具 (依據草圖位置與估算尺寸) ---

    # A. 左側 L 型座位區 (Seat 3 & 4)
    # 座位 4 (上方)
    add_rect(0, 420, 160, 70, "座位 4\n(Desk)", color='#D5E8D4')
    add_rect(0, 490, 60, 100, "側桌", color='#D5E8D4')
    add_chair(110, 455, 'right')
    # 隔間示意線
    ax.plot([165, 165], [410, 600], color='#808080', linewidth=2, linestyle='--')

    # 座位 3 (下方)
    add_rect(0, 150, 160, 70, "座位 3\n(Desk)", color='#D5E8D4')
    add_rect(0, 220, 60, 100, "側桌", color='#D5E8D4')
    add_chair(110, 185, 'right')
    # 隔間示意線
    ax.plot([165, 165], [140, 330], color='#808080', linewidth=2, linestyle='--')

    # 保險箱
    add_rect(0, 360, 50, 50, "保險箱", color='#A9C4EB')

    # B. 右側獨立座位區 (Seat 1 & 2)
    # 座位 2 (上方)
    add_rect(240, 420, 120, 70, "座位 2\n(Desk)", color='#FFE6CC')
    add_chair(310, 455, 'left') # 面向左側

    # 座位 1 (下方)
    add_rect(240, 150, 120, 70, "座位 1\n(Desk)", color='#FFE6CC')
    add_chair(310, 185, 'left') # 面向左側

    # C. 收納櫃體區
    # 上方牆面櫃 (深度40cm)
    add_rect(0, 683, 250, 40, "事務櫃(橫拉門) D40", color='#E1D5E7')
    add_rect(250, 683, 100, 40, "抽屜櫃", color='#E1D5E7')
    add_rect(350, 683, 100, 40, "雜物櫃", color='#E1D5E7')

    # 右側牆面櫃與設備
    add_rect(400, 500, 50, 150, "拉門明櫃", color='#E1D5E7')
    add_rect(410, 450, 40, 40, "碎紙機", color='#F8CECC')
    add_rect(400, 280, 50, 120, "矮櫃", color='#E1D5E7')
    # 白板 (牆上標示)
    ax.plot([448, 448], [280, 430], color='#0066CC', linewidth=4)
    ax.text(435, 355, "白板", rotation=90, ha='center', va='center', color='#0066CC', fontname='WenQuanYi Zen Hei')

    # D. 入口與茶水設備區 (下方牆面)
    # 門 (右下角)
    door_width = 90
    ax.plot([450, 450], [0, door_width], color='#B85450', linewidth=3) # 門框
    door_arc = patches.Arc((450, 0), door_width*2, door_width*2, theta1=90, theta2=180, color='#B85450', linestyle=':')
    ax.add_patch(door_arc)
    ax.text(400, 45, "入口", color='#B85450', fontname='WenQuanYi Zen Hei')

    # 設備
    add_rect(150, 0, 60, 60, "印表機", color='#F8CECC')
    add_rect(80, 0, 60, 60, "冰箱", color='#D4E1F5')
    add_rect(20, 0, 50, 40, "紙箱", color='#FFF2CC')

    # E. 標註與文字
    # 尺寸標註
    ax.arrow(-20, 0, 0, room_length, head_width=10, head_length=10, fc='k', ec='k')
    ax.arrow(-20, room_length, 0, -room_length, head_width=10, head_length=10, fc='k', ec='k')
    ax.text(-35, room_length/2, f'長 {room_length} cm', va='center', rotation=90, fontname='WenQuanYi Zen Hei')

    ax.arrow(0, -20, room_width, 0, head_width=10, head_length=10, fc='k', ec='k')
    ax.arrow(room_width, -20, -room_width, 0, head_width=10, head_length=10, fc='k', ec='k')
    ax.text(room_width/2, -35, f'寬 {room_width} cm', ha='center', fontname='WenQuanYi Zen Hei')

    # 走道文字
    ax.text(200, 330, "走 道 (Aisle)", ha='center', fontsize=12, color='#666666', fontname='WenQuanYi Zen Hei')

    # 北向指標
    ax.arrow(-30, 650, 0, 40, head_width=15, head_length=15, fc='k', ec='k')
    ax.text(-30, 630, "N", ha='center', fontname='WenQuanYi Zen Hei')

    # 標題
    ax.set_title("辦公室室內設計平面配置圖 (依照草圖繪製)", fontsize=16, pad=20, fontname='WenQuanYi Zen Hei')

    plt.axis('off') # 隱藏座標軸
    plt.tight_layout()

    # 保存圖像為文件
    plt.savefig('office_floor_plan.png', dpi=300, bbox_inches='tight')
    print("辦公室平面圖已保存為 office_floor_plan.png")

    # 也可以顯示圖像（如果有GUI環境）
    # plt.show()

if __name__ == '__main__':
    draw_office_plan()
