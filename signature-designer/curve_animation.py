import pygame
import json
import math
import time
from typing import List, Tuple

# 初始化Pygame
pygame.init()

# 设置窗口大小
WIDTH = 1400
HEIGHT = 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("曲线绘制动画")

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)

class Node:
    def __init__(self, pos, prev, next_pos, size):
        self.pos = pos
        self.prev = prev
        self.next = next_pos
        self.size = size

def load_curve_data(filename):
    """从JSON文件加载曲线数据"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"文件 {filename} 未找到")
        return None
    except json.JSONDecodeError:
        print(f"文件 {filename} 格式错误")
        return None

def curve(t, node1: Node, node2: Node) -> tuple[float, float]:
    """计算三次贝塞尔曲线上的点"""
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

def draw_bezier_curve_animated(screen, nodes, segment_index, segment_progress, color=WHITE):
    """绘制动画贝塞尔曲线（变宽度）"""
    if len(nodes) < 2:
        return
    
    total_segments = len(nodes) - 1
    
    # 绘制已完成的段
    for i in range(min(segment_index, total_segments)):
        node1 = nodes[i]
        node2 = nodes[i + 1]
        draw_variable_width_curve(screen, node1, node2, color)
    
    # 绘制当前正在进行的段（部分）
    if segment_index < total_segments and segment_progress > 0:
        node1 = nodes[segment_index]
        node2 = nodes[segment_index + 1]
        
        # 创建一个临时的部分段来绘制
        segments = 50
        max_t = segment_progress
        
        points = []
        widths = []
        
        # 计算部分曲线上的点和对应的宽度
        for i in range(int(segments * max_t) + 1):
            t = (i / segments) if segments > 0 else 0
            if t <= max_t:
                point = curve(t, node1, node2)
                # 线性插值计算宽度
                width = node1.size * (1 - t) + node2.size * t
                points.append(point)
                widths.append(width)
        
        # 绘制部分曲线
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

def main():
    clock = pygame.time.Clock()
    running = True
    
    # 加载曲线数据
    data = load_curve_data('signature-designer\signature_data.json')
    if not data:
        print("无法加载曲线数据")
        return
    
    # 转换数据为Node对象
    all_curves = []
    for curve_data in data.get('all_curves', []):
        curve_nodes = []
        for node_data in curve_data:
            node = Node(
                node_data['pos'],
                node_data['prev'],
                node_data['next'],
                node_data['size']
            )
            curve_nodes.append(node)
        all_curves.append(curve_nodes)
    
    # 当前曲线
    current_curve_nodes = []
    for node_data in data.get('current_curve', []):
        node = Node(
            node_data['pos'],
            node_data['prev'],
            node_data['next'],
            node_data['size']
        )
        current_curve_nodes.append(node)
    
    # 动画参数
    segment_duration = 0.05  # 每段曲线的固定时间（秒）
    start_time = time.time()
    current_curve_index = 0
    current_segment_index = 0
    
    # 显示控制
    show_nodes = True  # 是否显示节点
    show_control_points = True  # 是否显示控制点
    
    # 字体
    try:
        font = pygame.font.Font("signature-designer\MiSans-Regular.ttf", 36)
    except:
        font = pygame.font.Font("signature-designer\MiSans-Regular.ttf", 36)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    # 重新开始动画
                    start_time = time.time()
                    current_curve_index = 0
                    current_segment_index = 0
                elif event.key == pygame.K_UP:
                    # 加速（减少每段时间）
                    segment_duration = max(segment_duration - 0.1, 0.1)
                elif event.key == pygame.K_DOWN:
                    # 减速（增加每段时间）
                    segment_duration = min(segment_duration + 0.1, 3.0)
                elif event.key == pygame.K_n:
                    # 切换节点显示
                    show_nodes = not show_nodes
                elif event.key == pygame.K_c:
                    # 切换控制点显示
                    show_control_points = not show_control_points
        
        # 清屏
        screen.fill(BLACK)
        
        # 计算动画进度
        elapsed_time = time.time() - start_time
        
        # 绘制已完成的曲线
        for i in range(current_curve_index):
            if i < len(all_curves):
                # 绘制完整曲线
                for j in range(len(all_curves[i]) - 1):
                    draw_bezier_curve_animated(screen, all_curves[i], j, 1.0, RED)
                
                # 绘制节点和控制点（如果启用）
                if show_nodes or show_control_points:
                    for node in all_curves[i]:
                        if show_nodes:
                            # 绘制节点（小正方形）
                            rect_size = 8
                            rect_pos = (node.pos[0] - rect_size//2, node.pos[1] - rect_size//2)
                            pygame.draw.rect(screen, WHITE, (*rect_pos, rect_size, rect_size))
                        
                        if show_control_points:
                            # 绘制控制点（小圆形）
                            pygame.draw.circle(screen, WHITE, (int(node.prev[0]), int(node.prev[1])), 3)
                            pygame.draw.circle(screen, WHITE, (int(node.next[0]), int(node.next[1])), 3)
                            # 绘制控制线
                            pygame.draw.line(screen, GRAY, node.prev, node.pos, 1)
                            pygame.draw.line(screen, GRAY, node.next, node.pos, 1)
        
        # 绘制当前正在动画的曲线
        if current_curve_index < len(all_curves):
            current_curve = all_curves[current_curve_index]
            total_segments = len(current_curve) - 1
            
            if total_segments > 0:
                # 绘制已完成的段
                for j in range(current_segment_index):
                    draw_bezier_curve_animated(screen, current_curve, j, 1.0, RED)
                
                # 绘制当前段
                if current_segment_index < total_segments:
                    segment_progress = min(elapsed_time / segment_duration, 1.0)
                    draw_bezier_curve_animated(screen, current_curve, current_segment_index, segment_progress, RED)
                    
                    # 如果当前段完成，切换到下一段
                    if segment_progress >= 1.0:
                        current_segment_index += 1
                        start_time = time.time()
                        
                        # 如果所有段都完成，切换到下一条曲线
                        if current_segment_index >= total_segments:
                            current_curve_index += 1
                            current_segment_index = 0
                            start_time = time.time()
                
                # 绘制当前曲线的节点和控制点（如果启用）
                if show_nodes or show_control_points:
                    for i, node in enumerate(current_curve):
                        # 只绘制已经动画过的节点
                        if i <= current_segment_index:
                            if show_nodes:
                                # 绘制节点（小正方形）
                                rect_size = 8
                                rect_pos = (node.pos[0] - rect_size//2, node.pos[1] - rect_size//2)
                                pygame.draw.rect(screen, WHITE, (*rect_pos, rect_size, rect_size))
                            
                            if show_control_points:
                                # 绘制控制点（小圆形）
                                pygame.draw.circle(screen, WHITE, (int(node.prev[0]), int(node.prev[1])), 3)
                                pygame.draw.circle(screen, WHITE, (int(node.next[0]), int(node.next[1])), 3)
                                # 绘制控制线
                                pygame.draw.line(screen, GRAY, node.prev, node.pos, 1)
                                pygame.draw.line(screen, GRAY, node.next, node.pos, 1)
        elif len(current_curve_nodes) > 0:
            # 绘制当前曲线（如果存在）
            total_segments = len(current_curve_nodes) - 1
            if total_segments > 0:
                # 绘制已完成的段
                for j in range(current_segment_index):
                    draw_bezier_curve_animated(screen, current_curve_nodes, j, 1.0, (255, 165, 0))
                
                # 绘制当前段
                if current_segment_index < total_segments:
                    segment_progress = min(elapsed_time / segment_duration, 1.0)
                    draw_bezier_curve_animated(screen, current_curve_nodes, current_segment_index, segment_progress, (255, 165, 0))
                    
                    # 如果当前段完成，切换到下一段
                    if segment_progress >= 1.0:
                        current_segment_index += 1
                        start_time = time.time()
                
                # 绘制当前曲线的节点和控制点（如果启用）
                if show_nodes or show_control_points:
                    for i, node in enumerate(current_curve_nodes):
                        # 只绘制已经动画过的节点
                        if i <= current_segment_index:
                            if show_nodes:
                                # 绘制节点（小正方形）
                                rect_size = 8
                                rect_pos = (node.pos[0] - rect_size//2, node.pos[1] - rect_size//2)
                                pygame.draw.rect(screen, WHITE, (*rect_pos, rect_size, rect_size))
                            
                            if show_control_points:
                                # 绘制控制点（小圆形）
                                pygame.draw.circle(screen, WHITE, (int(node.prev[0]), int(node.prev[1])), 3)
                                pygame.draw.circle(screen, WHITE, (int(node.next[0]), int(node.next[1])), 3)
                                # 绘制控制线
                                pygame.draw.line(screen, GRAY, node.prev, node.pos, 1)
                                pygame.draw.line(screen, GRAY, node.next, node.pos, 1)
        
        # 显示控制信息
        info_texts = [
            "控制说明：",
            "空格键 - 重新开始动画",
            "↑键 - 加速动画",
            "↓键 - 减速动画",
            "N键 - 切换节点显示",
            "C键 - 切换控制点显示",
            "ESC键 - 退出",
            f"每段时间: {segment_duration:.1f}秒",
            f"当前曲线: {current_curve_index + 1}/{len(all_curves) + (1 if current_curve_nodes else 0)}",
            f"当前段: {current_segment_index + 1}",
            # f"节点显示: {'开' if show_nodes else '关'}",
            # f"控制点显示: {'开' if show_control_points else '关'}"
        ]
        
        for i, text in enumerate(info_texts):
            color = WHITE if i != 0 else GREEN
            text_surface = font.render(text, True, color)
            screen.blit(text_surface, (10, 10 + i * 30))
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()