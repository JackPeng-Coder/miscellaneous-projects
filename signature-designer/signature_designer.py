import pygame
import sys
import math
import json
import os
import ctypes
from ctypes import wintypes

class Node:
    def __init__(self, pos, prev, next, size=5) -> None:
        self.pos = pos
        self.prev = prev
        self.next = next
        self.size = size  # 节点大小，影响曲线宽度

def curve(t, node1: Node, node2: Node) -> tuple[float, float]:
    p0 = node1.pos
    p1 = node1.next
    p2 = node2.prev
    p3 = node2.pos
    return (
        (1 - t) ** 3 * p0[0] + 3 * (1 - t) ** 2 * t * p1[0] + 3 * (1 - t) * t ** 2 * p2[0] + t ** 3 * p3[0],
        (1 - t) ** 3 * p0[1] + 3 * (1 - t) ** 2 * t * p1[1] + 3 * (1 - t) * t ** 2 * p2[1] + t ** 3 * p3[1]
    )

def draw_variable_width_curve(screen, node1: Node, node2: Node, color, segments=50):
    """绘制变宽度的贝塞尔曲线"""
    points = []
    widths = []
    
    # 计算曲线上的点和对应的宽度
    for i in range(segments + 1):
        t = i / segments
        point = curve(t, node1, node2)
        # 线性插值计算宽度
        width = node1.size * (1 - t) + node2.size * t
        points.append(point)
        widths.append(width)
    
    # 绘制变宽度曲线（圆形+直线连接）
    for i in range(len(points)):
        if widths[i] > 0:
            # 绘制圆形
            pygame.draw.circle(screen, color, (int(points[i][0]), int(points[i][1])), max(1, int(widths[i] / 2)))
            
            # 在相邻点之间绘制直线连接
            if i > 0:
                # 计算两点间的直线，使用平均宽度
                avg_width = (widths[i-1] + widths[i]) / 2
                if avg_width > 1:
                    pygame.draw.line(screen, color, 
                                   (int(points[i-1][0]), int(points[i-1][1])), 
                                   (int(points[i][0]), int(points[i][1])), 
                                   max(1, int(avg_width)))

pygame.init()
screen = pygame.display.set_mode()
pygame.display.set_caption("贝塞尔曲线绘制工具")

# 加载背景图片
try:
    background_image = pygame.image.load("signature-designer/image.jpg")
    # 保持原始比例缩放背景图片
    screen_size = screen.get_size()
    image_size = background_image.get_size()
    
    # 计算缩放比例，保持宽高比
    scale_x = screen_size[0] / image_size[0]
    scale_y = screen_size[1] / image_size[1]
    scale = min(scale_x, scale_y)  # 使用较小的缩放比例以确保图片完全显示
    
    # 计算缩放后的尺寸
    new_width = int(image_size[0] * scale)
    new_height = int(image_size[1] * scale)
    
    background_image = pygame.transform.scale(background_image, (new_width, new_height))
    
    # 计算居中位置
    bg_x = (screen_size[0] - new_width) // 2
    bg_y = (screen_size[1] - new_height) // 2
    background_pos = (bg_x, bg_y)
except Exception as e:
    print(f"无法加载背景图片: {e}")
    background_image = None
    background_pos = (0, 0)

# 大写锁定控制函数
def set_caps_lock(state):
    """设置大写锁定状态"""
    try:
        # 获取当前大写锁定状态
        VK_CAPITAL = 0x14
        current_state = ctypes.windll.user32.GetKeyState(VK_CAPITAL) & 0x0001
        
        # 如果当前状态与目标状态不同，则切换
        if bool(current_state) != state:
            ctypes.windll.user32.keybd_event(VK_CAPITAL, 0, 0, 0)  # 按下
            ctypes.windll.user32.keybd_event(VK_CAPITAL, 0, 2, 0)  # 释放
    except Exception as e:
        print(f"设置大写锁定失败: {e}")

# 程序启动时开启大写锁定
set_caps_lock(True)
print("已开启大写锁定")

def screen_to_image_coords(screen_pos):
    """将屏幕坐标转换为图片坐标"""
    if not background_image:
        return screen_pos
    
    # 计算相对于背景图片的坐标
    img_x = screen_pos[0] - background_pos[0]
    img_y = screen_pos[1] - background_pos[1]
    
    # 确保坐标在图片范围内
    img_size = background_image.get_size()
    img_x = max(0, min(img_x, img_size[0]))
    img_y = max(0, min(img_y, img_size[1]))
    
    return (img_x, img_y)

def image_to_screen_coords(image_pos):
    """将图片坐标转换为屏幕坐标"""
    if not background_image:
        return image_pos
    
    screen_x = image_pos[0] + background_pos[0]
    screen_y = image_pos[1] + background_pos[1]
    
    return (screen_x, screen_y)

def save_data_to_json(filename="signature-designer/signature_data.json"):
    """将所有曲线数据保存到JSON文件"""
    data = {
        "all_curves": [],
        "current_curve": []
    }
    
    # 保存所有已完成的曲线
    for curve_nodes in all_curves:
        curve_data = []
        for node in curve_nodes:
            # 将屏幕坐标转换为图片坐标保存
            curve_data.append({
                "pos": screen_to_image_coords(node.pos),
                "prev": screen_to_image_coords(node.prev),
                "next": screen_to_image_coords(node.next),
                "size": node.size
            })
        data["all_curves"].append(curve_data)
    
    # 保存当前正在绘制的曲线
    for node in current_curve_nodes:
        data["current_curve"].append({
            "pos": screen_to_image_coords(node.pos),
            "prev": screen_to_image_coords(node.prev),
            "next": screen_to_image_coords(node.next),
            "size": node.size
        })
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"数据已保存到 {filename}")
    except Exception as e:
        print(f"保存失败: {e}")

def load_data_from_json(filename="signature-designer/signature_data.json"):
    """从JSON文件读取曲线数据"""
    global all_curves, current_curve_nodes
    
    if not os.path.exists(filename):
        print(f"文件 {filename} 不存在")
        return
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 清空现有数据
        all_curves.clear()
        current_curve_nodes.clear()
        
        # 加载所有已完成的曲线
        for curve_data in data.get("all_curves", []):
            curve_nodes = []
            for node_data in curve_data:
                # 将图片坐标转换为屏幕坐标
                node = Node(
                    image_to_screen_coords(tuple(node_data["pos"])),
                    image_to_screen_coords(tuple(node_data["prev"])),
                    image_to_screen_coords(tuple(node_data["next"])),
                    node_data.get("size", 5)  # 默认大小为5
                )
                curve_nodes.append(node)
            all_curves.append(curve_nodes)
        
        # 加载当前正在绘制的曲线
        for node_data in data.get("current_curve", []):
            # 将图片坐标转换为屏幕坐标
            node = Node(
                image_to_screen_coords(tuple(node_data["pos"])),
                image_to_screen_coords(tuple(node_data["prev"])),
                image_to_screen_coords(tuple(node_data["next"])),
                node_data.get("size", 5)  # 默认大小为5
            )
            current_curve_nodes.append(node)
        
        print(f"数据已从 {filename} 加载")
    except Exception as e:
        print(f"加载失败: {e}")

def find_nearby_node(pos, threshold=10):
    """查找鼠标位置附近的节点"""
    for curve_nodes in all_curves:
        for node in curve_nodes:
            distance = math.sqrt((pos[0] - node.pos[0])**2 + (pos[1] - node.pos[1])**2)
            if distance <= threshold:
                return node
    
    for node in current_curve_nodes:
        distance = math.sqrt((pos[0] - node.pos[0])**2 + (pos[1] - node.pos[1])**2)
        if distance <= threshold:
            return node
    
    return None

# 存储所有曲线的节点
all_curves = []  # 每个元素是一个节点列表
current_curve_nodes = []  # 当前正在绘制的曲线的节点
mouse_pressed = False
alt_pressed = False
current_pos = None
current_prev = None
current_next = None
current_size = 5  # 当前节点大小
mouse_pos = (0, 0)  # 鼠标位置
connecting_to_existing = False  # 是否正在连接到已存在的节点
target_node = None  # 目标连接节点

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 程序退出时关闭大写锁定
            set_caps_lock(False)
            print("已关闭大写锁定")
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LALT or event.key == pygame.K_RALT:
                alt_pressed = True
            elif event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                # 撤销上次操作
                if current_curve_nodes:
                    current_curve_nodes.pop()
                elif all_curves:
                    # 如果当前曲线为空，撤销上一条曲线的最后一个节点
                    if all_curves[-1]:
                        current_curve_nodes = all_curves.pop()
                        if current_curve_nodes:
                            current_curve_nodes.pop()
            elif event.key == pygame.K_SPACE:
                # 空格键：完成当前曲线并开始新曲线
                if current_curve_nodes:
                    all_curves.append(current_curve_nodes.copy())
                    current_curve_nodes = []
            elif event.key == pygame.K_s:
                # S键：保存数据到JSON文件
                save_data_to_json()
            elif event.key == pygame.K_r:
                # R键：从JSON文件读取数据
                load_data_from_json()
            elif event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS or event.key == pygame.K_UP:
                # +键或上箭头：增加节点大小
                current_size = min(current_size + 1, 20)  # 最大20
                # print(f"当前节点大小: {current_size}")
            elif event.key == pygame.K_MINUS or event.key == pygame.K_DOWN:
                # -键或下箭头：减少节点大小
                current_size = max(current_size - 1, 1)  # 最小1
                # print(f"当前节点大小: {current_size}")
            elif event.key == pygame.K_ESCAPE:
                # 程序退出时关闭大写锁定
                set_caps_lock(False)
                print("已关闭大写锁定")
                sys.exit()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LALT or event.key == pygame.K_RALT:
                alt_pressed = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 只处理鼠标左键
            if event.button == 1:  # 1 表示鼠标左键
                # 检查是否点击到已存在的节点
                nearby_node = find_nearby_node(event.pos)
                if nearby_node:
                    # 如果点击到已存在的节点，直接连接
                    connecting_to_existing = True
                    target_node = nearby_node
                    current_pos = nearby_node.pos
                    current_prev = nearby_node.pos
                    current_next = nearby_node.pos
                else:
                    # 正常创建新节点
                    connecting_to_existing = False
                    target_node = None
                    current_pos = event.pos
                    current_prev = current_pos
                    current_next = current_pos
                mouse_pressed = True

        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos
            if mouse_pressed:
                # 检查鼠标位置是否接近按下点，如果是则吸附
                distance_to_press = math.sqrt((event.pos[0] - current_pos[0])**2 + (event.pos[1] - current_pos[1])**2)
                if distance_to_press <= 10:  # 吸附范围10像素
                    # 吸附到按下点
                    current_next = current_pos
                    if not alt_pressed:
                        current_prev = current_pos
                else:
                    current_next = event.pos
                    if not alt_pressed:
                        current_prev = (2 * current_pos[0] - current_next[0], 2 * current_pos[1] - current_next[1])

        elif event.type == pygame.MOUSEBUTTONUP:
            # 只处理鼠标左键
            if event.button == 1 and mouse_pressed:  # 1 表示鼠标左键
                if connecting_to_existing and target_node:
                    # 连接到已存在的节点，继承目标节点的所有属性
                    current_curve_nodes.append(Node(target_node.pos, target_node.prev, target_node.next, target_node.size))
                else:
                    # 创建新节点，使用当前设置的大小
                    current_curve_nodes.append(Node(current_pos, current_prev, current_next, current_size))
                
                mouse_pressed = False
                current_pos = None
                current_prev = None
                current_next = None
                connecting_to_existing = False
                target_node = None
        
        elif event.type == pygame.MOUSEWHEEL:
            # 鼠标滚轮调整节点大小
            if event.y > 0:  # 向上滚动，增加大小
                current_size = min(current_size + 1, 20)  # 最大20
            elif event.y < 0:  # 向下滚动，减少大小
                current_size = max(current_size - 1, 1)  # 最小1
            # print(f"当前节点大小: {current_size}")

    # 绘制背景图片（如果加载成功）
    if background_image:
        screen.fill("BLACK")  # 先填充黑色背景
        screen.blit(background_image, background_pos)  # 在计算的位置绘制图片
    else:
        screen.fill("BLACK")
    
    # 显示当前节点大小信息
    font = pygame.font.Font("signature-designer/MiSans-Regular.ttf", 36)
    size_text = font.render(f"节点大小: {current_size}", True, "WHITE")
    screen.blit(size_text, (10, 10))

    # 绘制所有已完成的曲线
    for curve_nodes in all_curves:
        # 绘制节点
        for node in curve_nodes:
            rect_size = 10
            rect_pos = (node.pos[0] - rect_size/2, node.pos[1] - rect_size/2)
            pygame.draw.rect(screen, "WHITE", (*rect_pos, rect_size, rect_size))
            pygame.draw.circle(screen, "WHITE", node.prev, 5)
            pygame.draw.circle(screen, "WHITE", node.next, 5)
            pygame.draw.line(screen, "WHITE", node.prev, node.pos)
            pygame.draw.line(screen, "WHITE", node.next, node.pos)
        
        # 绘制曲线
        for index in range(1, len(curve_nodes)):
            node1 = curve_nodes[index - 1]
            node2 = curve_nodes[index]
            draw_variable_width_curve(screen, node1, node2, "RED")

    # 绘制当前曲线的已完成节点
    for node in current_curve_nodes:
        rect_size = 10
        rect_pos = (node.pos[0] - rect_size/2, node.pos[1] - rect_size/2)
        pygame.draw.rect(screen, "CYAN", (*rect_pos, rect_size, rect_size))
        pygame.draw.circle(screen, "CYAN", node.prev, 5)
        pygame.draw.circle(screen, "CYAN", node.next, 5)
        pygame.draw.line(screen, "CYAN", node.prev, node.pos)
        pygame.draw.line(screen, "CYAN", node.next, node.pos)

    # 绘制当前曲线的已完成部分
    for index in range(1, len(current_curve_nodes)):
        node1 = current_curve_nodes[index - 1]
        node2 = current_curve_nodes[index]
        draw_variable_width_curve(screen, node1, node2, "ORANGE")

    # 绘制当前正在拖动的节点（实时预览）
    if mouse_pressed and current_pos:
        rect_size = 10
        rect_pos = (current_pos[0] - rect_size/2, current_pos[1] - rect_size/2)
        pygame.draw.rect(screen, "YELLOW", (*rect_pos, rect_size, rect_size))
        pygame.draw.circle(screen, "YELLOW", current_prev, 5)
        pygame.draw.circle(screen, "YELLOW", current_next, 5)
        pygame.draw.line(screen, "YELLOW", current_prev, current_pos)
        pygame.draw.line(screen, "YELLOW", current_next, current_pos)
        
        # 如果有前一个节点，绘制实时贝塞尔曲线预览
        if current_curve_nodes:
            last_node = current_curve_nodes[-1]
            if connecting_to_existing and target_node:
                # 连接到已存在节点时，使用目标节点的属性
                temp_node = Node(target_node.pos, target_node.prev, target_node.next, target_node.size)
            else:
                # 正常创建新节点时，使用当前拖动的控制点和当前设置的大小
                temp_node = Node(current_pos, current_prev, current_next, current_size)
            
            draw_variable_width_curve(screen, last_node, temp_node, "GREEN")
    
    # 鼠标悬停预览（未按下鼠标时）
    elif not mouse_pressed and current_curve_nodes:
        # 检查鼠标是否悬停在已存在的节点上
        nearby_node = find_nearby_node(mouse_pos)
        
        if nearby_node:
            # 如果悬停在已存在节点上，显示连接预览
            last_node = current_curve_nodes[-1]
            temp_node = Node(nearby_node.pos, nearby_node.prev, nearby_node.next, nearby_node.size)
            
            draw_variable_width_curve(screen, last_node, temp_node, "LIGHTBLUE")
            
            # 高亮显示目标节点
            rect_size = 12
            rect_pos = (nearby_node.pos[0] - rect_size/2, nearby_node.pos[1] - rect_size/2)
            pygame.draw.rect(screen, "LIGHTBLUE", (*rect_pos, rect_size, rect_size))
        else:
            # 正常的鼠标悬停预览
            last_node = current_curve_nodes[-1]
            # 创建一个临时节点，控制点与鼠标位置相同（直线效果），使用当前设置的大小
            temp_node = Node(mouse_pos, mouse_pos, mouse_pos, current_size)
            
            draw_variable_width_curve(screen, last_node, temp_node, "GRAY")
            
            # 绘制鼠标位置的预览节点
            rect_size = 8
            rect_pos = (mouse_pos[0] - rect_size/2, mouse_pos[1] - rect_size/2)
            pygame.draw.rect(screen, "GRAY", (*rect_pos, rect_size, rect_size))
            
    pygame.display.flip()