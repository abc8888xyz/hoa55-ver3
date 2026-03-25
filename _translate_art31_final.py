# -*- coding: utf-8 -*-
"""Translate art31 using phrase-level replacement"""
import json, sys, re, copy

sys.stdout.reconfigure(encoding='utf-8')

with open('_art31_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

out = copy.deepcopy(data)

def tr(cn):
    v = cn
    # Phrase-level replacements (longest first to avoid conflicts)
    phrases = [
        # Multi-word phrases first
        ('\u5c0f\u9f99\u867e', 'T\u00f4m H\u00f9m'),  # 小龙虾
        ('\u98de\u4e66\u5f00\u653e\u5e73\u53f0', 'n\u1ec1n t\u1ea3ng m\u1edf Feishu'),  # 飞书开放平台
        ('\u98de\u4e66', 'Feishu'),  # 飞书
        ('\u9489\u9489', 'DingTalk'),  # 钉钉
        ('\u4f01\u4e1a\u5fae\u4fe1', 'WeCom'),  # 企业微信
        ('\u4f01\u5fae', 'WeCom'),  # 企微
        ('\u4e2a\u4eba\u5fae\u4fe1', 'WeChat c\u00e1 nh\u00e2n'),  # 个人微信
        ('\u5fae\u4fe1', 'WeChat'),  # 微信
        ('\u5c0f\u4e92', 'Ti\u1ec3u H\u1ed7'),  # 小互
        ('\u914d\u7f6e\u5411\u5bfc', 'tr\u00ecnh h\u01b0\u1edbng d\u1eabn c\u1ea5u h\u00ecnh'),  # 配置向导
        ('\u914d\u7f6e\u6e05\u5355', 'Danh s\u00e1ch c\u1ea5u h\u00ecnh'),  # 配置清单
        ('\u5b89\u5168\u914d\u7f6e', 'c\u1ea5u h\u00ecnh an to\u00e0n'),  # 安全配置
        ('\u4eba\u8bbe\u914d\u7f6e', 'c\u1ea5u h\u00ecnh nh\u00e2n v\u1eadt'),  # 人设配置
        ('\u914d\u7f6e', 'c\u1ea5u h\u00ecnh'),  # 配置
        ('\u5b89\u88c5\u547d\u4ee4', 'L\u1ec7nh c\u00e0i \u0111\u1eb7t'),  # 安装命令
        ('\u5b89\u88c5', 'c\u00e0i \u0111\u1eb7t'),  # 安装
        ('\u6280\u80fd', 'k\u1ef9 n\u0103ng'),  # 技能
        ('\u804a\u5929\u6846', 'khung chat'),  # 聊天框
        ('\u804a\u5929\u5de5\u5177', 'c\u00f4ng c\u1ee5 chat'),  # 聊天工具
        ('\u804a\u5929\u8f6f\u4ef6', 'ph\u1ea7n m\u1ec1m chat'),  # 聊天软件
        ('\u804a\u5929\u6e20\u9053', 'k\u00eanh chat'),  # 聊天渠道
        ('\u804a\u5929', 'chat'),  # 聊天
        ('\u7fa4\u804a', 'nh\u00f3m chat'),  # 群聊
        ('\u673a\u5668\u4eba', 'robot'),  # 机器人
        ('\u7ec8\u7aef', 'terminal'),  # 终端
        ('\u6d4f\u89c8\u5668', 'tr\u00ecnh duy\u1ec7t'),  # 浏览器
        ('\u8bb0\u5fc6\u7cfb\u7edf', 'h\u1ec7 th\u1ed1ng b\u1ed9 nh\u1edb'),  # 记忆系统
        ('\u8bb0\u5fc6\u529f\u80fd', 'ch\u1ee9c n\u0103ng b\u1ed9 nh\u1edb'),  # 记忆功能
        ('\u8bb0\u5fc6', 'b\u1ed9 nh\u1edb'),  # 记忆
        ('\u5fc3\u8df3\u9891\u7387', 't\u1ea7n su\u1ea5t heartbeat'),  # 心跳频率
        ('\u5fc3\u8df3\u529f\u80fd', 'ch\u1ee9c n\u0103ng heartbeat'),  # 心跳功能
        ('\u5fc3\u8df3', 'heartbeat'),  # 心跳
        ('\u4eba\u8bbe\u6587\u4ef6', 'file nh\u00e2n v\u1eadt'),  # 人设文件
        ('\u4eba\u8bbe\u7cfb\u7edf', 'h\u1ec7 th\u1ed1ng nh\u00e2n v\u1eadt'),  # 人设系统
        ('\u4eba\u8bbe', 'nh\u00e2n v\u1eadt'),  # 人设
        ('\u5de5\u4f5c\u76ee\u5f55', 'th\u01b0 m\u1ee5c l\u00e0m vi\u1ec7c'),  # 工作目录
        ('\u5de5\u4f5c\u6d41\u7a0b', 'quy tr\u00ecnh l\u00e0m vi\u1ec7c'),  # 工作流程
        ('\u5de5\u4f5c\u6d41\u80fd\u529b', 'kh\u1ea3 n\u0103ng workflow'),  # 工作流能力
        ('\u5de5\u4f5c\u6d41', 'workflow'),  # 工作流
        ('\u5de5\u4f5c\u89c4\u5219', 'quy t\u1eafc l\u00e0m vi\u1ec7c'),  # 工作规则
        ('\u5de5\u4f5c\u7b14\u8bb0\u672c', 'S\u1ed5 ghi ch\u00e9p c\u00f4ng vi\u1ec7c'),  # 工作笔记本
        ('\u5de5\u4f5c\u65e5\u5fd7', 'nh\u1eadt k\u00fd c\u00f4ng vi\u1ec7c'),  # 工作日志
        ('\u5de5\u4f5c', 'c\u00f4ng vi\u1ec7c'),  # 工作
        ('\u6a21\u677f', 'template'),  # 模板
        ('\u5b9a\u65f6\u4efb\u52a1', 't\u00e1c v\u1ee5 \u0111\u1ecbnh k\u1ef3'),  # 定时任务
        ('\u5b9a\u65f6', '\u0111\u1ecbnh k\u1ef3'),  # 定时
        ('\u9891\u7387', 't\u1ea7n su\u1ea5t'),  # 频率
        ('\u65b0\u624b', 'ng\u01b0\u1eddi m\u1edbi'),  # 新手
        ('\u8001\u677f', 's\u1ebfp'),  # 老板
        ('\u52a9\u7406', 'tr\u1ee3 l\u00fd'),  # 助理
        ('\u6743\u9650\u7ba1\u7406', 'Qu\u1ea3n l\u00fd quy\u1ec1n'),  # 权限管理
        ('\u6743\u9650', 'quy\u1ec1n'),  # 权限
        ('\u7248\u672c\u7ba1\u7406\u4e0e\u53d1\u5e03', 'Qu\u1ea3n l\u00fd phi\u00ean b\u1ea3n v\u00e0 ph\u00e1t h\u00e0nh'),  # 版本管理与发布
        ('\u7248\u672c\u53f7', 's\u1ed1 phi\u00ean b\u1ea3n'),  # 版本号
        ('\u7248\u672c', 'phi\u00ean b\u1ea3n'),  # 版本
        ('\u7ba1\u7406\u5458', 'qu\u1ea3n tr\u1ecb vi\u00ean'),  # 管理员
        ('\u7ba1\u7406\u9875\u9762', 'trang qu\u1ea3n l\u00fd'),  # 管理页面
        ('\u7ba1\u7406', 'qu\u1ea3n l\u00fd'),  # 管理
        ('\u5e94\u7528', '\u1ee9ng d\u1ee5ng'),  # 应用
        ('\u80fd\u529b', 'n\u0103ng l\u1ef1c'),  # 能力
        ('\u90ae\u4ef6\u7ba1\u5bb6', 'Qu\u1ea3n gia email'),  # 邮件管家
        ('\u90ae\u4ef6', 'email'),  # 邮件
        ('\u90ae\u7bb1', 'h\u1ed9p th\u01b0'),  # 邮箱
        ('\u65e5\u7a0b', 'l\u1ecbch'),  # 日程
        ('\u65e5\u5fd7\u6587\u4ef6', 'file nh\u1eadt k\u00fd'),  # 日志文件
        ('\u65e5\u5fd7', 'nh\u1eadt k\u00fd'),  # 日志
        ('\u6587\u4ef6', 'file'),  # 文件
        ('\u641c\u7d22', 't\u00ecm ki\u1ebfm'),  # 搜索
        ('\u7f51\u9875', 'trang web'),  # 网页
        ('\u7f51\u7edc', 'm\u1ea1ng'),  # 网络
        ('\u7f51\u5e97', 'shop online'),  # 网店
        ('\u516c\u7f51', 'm\u1ea1ng c\u00f4ng c\u1ed9ng'),  # 公网
        ('\u7aef\u53e3', 'c\u1ed5ng'),  # 端口
        ('\u6d88\u606f', 'tin nh\u1eafn'),  # 消息
        ('\u7528\u6237\u540d', 'username'),  # 用户名
        ('\u7528\u6237', 'ng\u01b0\u1eddi d\u00f9ng'),  # 用户
        ('\u8d26\u53f7', 't\u00e0i kho\u1ea3n'),  # 账号
        ('\u5bc6\u7801', 'm\u1eadt kh\u1ea9u'),  # 密码
        ('\u5bc6\u94a5', 'm\u1eadt kh\u1ea9u'),  # 密钥
        ('\u91cd\u542f', 'kh\u1edfi \u0111\u1ed9ng l\u1ea1i'),  # 重启
        ('\u542f\u52a8', 'kh\u1edfi \u0111\u1ed9ng'),  # 启动
        ('\u9ed8\u8ba4', 'm\u1eb7c \u0111\u1ecbnh'),  # 默认
        ('\u81ea\u52a8', 't\u1ef1 \u0111\u1ed9ng'),  # 自动
        ('\u624b\u52a8', 'th\u1ee7 c\u00f4ng'),  # 手动
        ('\u63a8\u8350', 'khuy\u1ebfn kh\u00edch'),  # 推荐
        ('\u7b80\u5355', '\u0111\u01a1n gi\u1ea3n'),  # 简单
        ('\u590d\u6742', 'ph\u1ee9c t\u1ea1p'),  # 复杂
        ('\u521b\u5efa', 't\u1ea1o'),  # 创建
        ('\u4fee\u6539', 's\u1eeda'),  # 修改
        ('\u66f4\u65b0', 'c\u1eadp nh\u1eadt'),  # 更新
        ('\u68c0\u67e5', 'ki\u1ec3m tra'),  # 检查
        ('\u8fde\u63a5', 'k\u1ebft n\u1ed1i'),  # 连接
        ('\u53d1\u5e03', 'ph\u00e1t h\u00e0nh'),  # 发布
        ('\u6ce8\u518c', '\u0111\u0103ng k\u00fd'),  # 注册
        ('\u767b\u5f55', '\u0111\u0103ng nh\u1eadp'),  # 登录
        ('\u590d\u5236', 'copy'),  # 复制
        ('\u7c98\u8d34', 'paste'),  # 粘贴
        ('\u4fdd\u5b58', 'l\u01b0u'),  # 保存
        ('\u4e0b\u8f7d', 't\u1ea3i'),  # 下载
        ('\u5220\u9664', 'x\u00f3a'),  # 删除
        ('\u6d4b\u8bd5', 'ki\u1ec3m tra'),  # 测试
        ('\u8bca\u65ad', 'ch\u1ea9n \u0111o\u00e1n'),  # 诊断
        ('\u5ba1\u6279', 'ph\u00ea duy\u1ec7t'),  # 审批
        ('\u6388\u6743', '\u1ee7y quy\u1ec1n'),  # 授权
        ('\u64cd\u4f5c', 'thao t\u00e1c'),  # 操作
        ('\u529f\u80fd', 'ch\u1ee9c n\u0103ng'),  # 功能
        ('\u8bbe\u7f6e', 'thi\u1ebft l\u1eadp'),  # 设置
        ('\u95ee\u9898', 'v\u1ea5n \u0111\u1ec1'),  # 问题
        ('\u65b9\u6cd5', 'c\u00e1ch'),  # 方法
        ('\u6b65\u9aa4', 'b\u01b0\u1edbc'),  # 步骤
        ('\u5185\u5bb9', 'n\u1ed9i dung'),  # 内容
        ('\u4fe1\u606f', 'th\u00f4ng tin'),  # 信息
        ('\u6548\u679c', 'hi\u1ec7u qu\u1ea3'),  # 效果
        ('\u6559\u7a0b', 'h\u01b0\u1edbng d\u1eabn'),  # 教程
        ('\u539f\u5219', 'nguy\u00ean t\u1eafc'),  # 原则
        ('\u6027\u683c', 't\u00ednh c\u00e1ch'),  # 性格
        ('\u884c\u4e3a\u51c6\u5219', 'quy t\u1eafc h\u00e0nh vi'),  # 行为准则
        ('\u504f\u597d', 's\u1edf th\u00edch'),  # 偏好
        ('\u89c4\u77e9', 'quy t\u1eafc'),  # 规矩
        ('\u89c4\u5219', 'quy t\u1eafc'),  # 规则
        ('\u6307\u5357', 'h\u01b0\u1edbng d\u1eabn'),  # 指南
        ('\u5b8c\u6574', 'ho\u00e0n ch\u1ec9nh'),  # 完整
        ('\u5c0f\u5b66\u751f', 'h\u1ecdc sinh ti\u1ec3u h\u1ecdc'),  # 小学生
        ('\u539f\u6587\u94fe\u63a5', 'Link b\u00e0i g\u1ed1c'),  # 原文链接
        ('\u539f\u521b', 'Nguy\u00ean t\u00e1c'),  # 原创
        ('\u53ef\u601c\u7684', '\u0111\u00e1ng th\u01b0\u01a1ng'),  # 可怜的
        ('\u4e0a\u4e00\u7bc7', 'B\u00e0i tr\u01b0\u1edbc'),  # 上一篇
        ('\u4e0b\u4e00\u671f', 'K\u1ef3 t\u1edbi'),  # 下一期
        ('\u624b\u628a\u624b', 't\u1eebng b\u01b0\u1edbc'),  # 手把手
        ('\u6b8b\u5e9f', 't\u00e0n ph\u1ebf'),  # 残废
        ('\u79c1\u4eba', 'c\u00e1 nh\u00e2n'),  # 私人
        ('\u7f16\u7a0b', 'l\u1eadp tr\u00ecnh'),  # 编程
        ('\u4fdd\u59c6', 'chi ti\u1ebft'),  # 保姆
        ('\u96f6\u57fa\u7840', 't\u1eeb con s\u1ed1 0'),  # 零基础
        ('\u63a5\u5165', 'k\u1ebft n\u1ed1i'),  # 接入
        ('\u63a5\u7ba1', 'ti\u1ebfp qu\u1ea3n'),  # 接管
        ('\u8868\u683c', 'b\u1ea3ng t\u00ednh'),  # 表格
        ('\u52a8\u624b', 'b\u1eaft tay v\u00e0o l\u00e0m'),  # 动手
        ('\u8bb0\u4f4f', 'nh\u1edb'),  # 记住
        ('\u8c03\u6559', 'bi\u1ebfn'),  # 调教
        ('\u597d\u7528', 'h\u1eefu d\u1ee5ng'),  # 好用
        ('\u771f\u6b63', 'th\u1ef1c s\u1ef1'),  # 真正
        ('\u4e0d\u9700\u8981', 'kh\u00f4ng c\u1ea7n'),  # 不需要
        ('\u540c\u6837', 'C\u0169ng'),  # 同样
        ('\u770b\u61c2', '\u0111\u1ecdc hi\u1ec3u'),  # 看懂
        ('\u56de\u987e', 'xem l\u1ea1i'),  # 回顾
        ('\u4e0a\u671f', 'b\u00e0i tr\u01b0\u1edbc'),  # 上期
        ('\u5f00\u59cb', 'b\u1eaft \u0111\u1ea7u'),  # 开始
        ('\u4e4b\u524d', 'Tr\u01b0\u1edbc khi'),  # 之前
        ('\u91cd\u8981', 'quan tr\u1ecdng'),  # 重要
        ('\u6700', 'nh\u1ea5t'),  # 最
        ('\u4e00\u4ef6\u4e8b', 'm\u1ed9t \u0111i\u1ec1u'),  # 一件事
        ('\u4e0b\u9762', 'B\u00ean d\u01b0\u1edbi'),  # 下面
        ('\u6240\u6709', 'T\u1ea5t c\u1ea3'),  # 所有
        ('\u901a\u8fc7', 'th\u00f4ng qua'),  # 通过
        ('\u5b8c\u6210', 'ho\u00e0n th\u00e0nh'),  # 完成
        ('\u6ca1\u9519', '\u0110\u00fang v\u1eady'),  # 没错
        ('\u76f4\u63a5', 'tr\u1ef1c ti\u1ebfp'),  # 直接
        ('\u5bf9', 'v\u1edbi'),  # 对
        ('\u8bf4', 'n\u00f3i'),  # 说
        ('\u5e2e\u6211', 'Gi\u00fap t\u00f4i'),  # 帮我
        ('\u4e00\u4e2a', 'm\u1ed9t'),  # 一个
        ('\u6548\u7387\u578b', 'hi\u1ec7u qu\u1ea3'),  # 效率型
        ('\u8bbe\u5b9a', 'thi\u1ebft l\u1eadp'),  # 设定
        ('\u5e2e\u4f60', 'gi\u00fap b\u1ea1n'),  # 帮你
        ('\u5e2e\u5b83', 'gi\u00fap n\u00f3'),  # 帮它
        ('\u7406\u89e3', 'hi\u1ec3u'),  # 理解
        ('\u539f\u7406', 'nguy\u00ean l\u00fd'),  # 原理
        ('\u5b9e\u9645', 'th\u1ef1c t\u1ebf'),  # 实际
        ('\u867d\u7136', 'tuy'),  # 虽然
        ('\u4f46', 'nh\u01b0ng'),  # 但
        ('\u65f6\u5019', 'l\u00fac'),  # 时候
        ('\u575a\u51b3', 'ki\u00ean quy\u1ebft'),  # 坚决
        ('\u4e0d\u5e72', 'kh\u00f4ng l\u00e0m'),  # 不干
        ('\u4e0d\u4f1a', 'kh\u00f4ng bi\u1ebft'),  # 不会
        ('\u90fd', '\u0111\u1ec1u'),  # 都
        ('\u8ba9\u5b83', '\u0111\u1ec3 n\u00f3'),  # 让它
        ('\u6559\u4f60', 'd\u1ea1y b\u1ea1n'),  # 教你
        ('\u95ee\u5b83', 'h\u1ecfi n\u00f3'),  # 问它
        ('\u5173\u7cfb', 'quan h\u1ec7'),  # 关系
        ('\u5e94\u8be5', 'n\u00ean'),  # 应该
        ('\u53ea\u9700\u8981', 'ch\u1ec9 c\u1ea7n'),  # 只需要
        ('\u641e\u5b9a', 'lo'),  # 搞定
        ('\u600e\u4e48', 'th\u1ebf n\u00e0o'),  # 怎么
        ('\u5b9e\u73b0', 'th\u1ef1c hi\u1ec7n'),  # 实现
        ('\u4e3e\u4e2a\u4f8b\u5b50', 'V\u00ed d\u1ee5'),  # 举个例子
        ('\u60f3', 'mu\u1ed1n'),  # 想
        ('\u6bcf\u5929\u65e9\u4e0a', 'm\u1ed7i s\u00e1ng'),  # 每天早上
        ('\u6bcf\u5929', 'm\u1ed7i ng\u00e0y'),  # 每天
        ('\u770b', 'xem'),  # 看
        ('\u5199', 'vi\u1ebft'),  # 写
        ('\u5b66', 'h\u1ecdc'),  # 学
        ('\u786e\u8ba4', 'x\u00e1c nh\u1eadn'),  # 确认
        ('\u597d', '\u0111\u01b0\u1ee3c r\u1ed3i'),  # 好
        ('\u6211\u4eec', 'ch\u00fang ta'),  # 我们
        ('\u4e3a\u4ec0\u4e48', 'T\u1ea1i sao'),  # 为什么
        ('\u88c5\u597d', 'c\u00e0i xong'),  # 装好
        ('\u88c5', 'c\u00e0i'),  # 装
        ('\u8fd8\u8981', 'c\u00f2n ph\u1ea3i'),  # 还要
        ('\u611f\u89c9', 'c\u1ea3m gi\u00e1c'),  # 感觉
        ('\u8ddf', 'v\u1edbi'),  # 跟
        ('\u4e5f\u6ca1\u4ec0\u4e48\u533a\u522b', 'c\u0169ng ch\u1eb3ng kh\u00e1c g\u00ec'),  # 也没什么区别
        ('\u533a\u522b', 'kh\u00e1c bi\u1ec7t'),  # 区别
        ('\u56e0\u4e3a', 'v\u00ec'),  # 因为
        ('\u53ea', 'ch\u1ec9'),  # 只
        ('\u8fd8\u6ca1', 'ch\u01b0a'),  # 还没
        ('\u6253\u4e2a\u6bd4\u65b9', 'V\u00ed d\u1ee5'),  # 打个比方
        ('\u4e70\u4e86', 'mua'),  # 买了
        ('\u626b\u5730\u673a\u5668\u4eba', 'robot h\u00fat b\u1ee5i'),  # 扫地机器人
        ('\u626b\u5730', 'qu\u00e9t s\u00e0n'),  # 扫地
        ('\u62c6\u5f00\u7bb1\u5b50', 'm\u1edf h\u1ed9p'),  # 拆开箱子
        ('\u6309\u4e86\u5f00\u5173', 'b\u1ea5m n\u00fat'),  # 按了开关
        ('\u786e\u5b9e', '\u0111\u00fang l\u00e0'),  # 确实
        ('\u544a\u8bc9', 'n\u00f3i cho'),  # 告诉
        ('\u54ea\u4e9b', 'n\u00e0o'),  # 哪些
        ('\u623f\u95f4', 'ph\u00f2ng'),  # 房间
        ('\u6bcf', 'm\u1ed7i'),  # 每
        ('\u6240\u4ee5', 'N\u00ean'),  # 所以
        ('\u539f\u5730\u8f6c\u5708', 'quay v\u00f2ng t\u1ea1i ch\u1ed7'),  # 原地转圈
        ('\u626b\u5e1a', 'c\u00e1i ch\u1ed5i'),  # 扫帚
        ('\u4e5f\u662f\u4e00\u6837', 'c\u0169ng v\u1eady'),  # 也是一样
        ('\u4e4b\u540e', 'xong'),  # 之后
        ('\u77e5\u9053', 'bi\u1ebft'),  # 知道
        ('\u4f60\u662f\u8c01', 'b\u1ea1n l\u00e0 ai'),  # 你是谁
        ('\u559c\u6b22', 'th\u00edch'),  # 喜欢
        ('\u4ec0\u4e48\u6837\u7684', 'ki\u1ec3u'),  # 什么样的
        ('\u56de\u7b54\u65b9\u5f0f', 'c\u00e1ch tr\u1ea3 l\u1eddi'),  # 回答方式
        ('\u56de\u7b54', 'tr\u1ea3 l\u1eddi'),  # 回答
        ('\u56de\u590d', 'tr\u1ea3 l\u1eddi'),  # 回复
        ('\u9700\u8981', 'c\u1ea7n'),  # 需要
        ('\u505a\u4ec0\u4e48', 'l\u00e0m g\u00ec'),  # 做什么
        ('\u5c31\u662f', 'ch\u00ednh l\u00e0'),  # 就是
        ('\u8fd9\u4e9b', 'nh\u1eefng \u0111i\u1ec1u n\u00e0y'),  # 这些
        ('\u4e8b\u60c5', 'vi\u1ec7c'),  # 事情
        ('\u603b\u5171', 't\u1ed5ng c\u1ed9ng'),  # 总共
        ('\u5c31\u8fd9\u51e0\u4ef6', 'ch\u1ec9 c\u00f3 m\u1ea5y vi\u1ec7c n\u00e0y'),  # 就这几件
        ('\u505a\u7684', 'l\u00e0m'),  # 做的
        ('\u7c7b\u6bd4', 'V\u00ed von'),  # 类比
        ('\u65b0\u6765\u7684', 'm\u1edbi'),  # 新来的
        ('\u8bf4\u8bdd\u65b9\u5f0f', 'c\u00e1ch n\u00f3i'),  # 说话方式
        ('\u7b26\u5408', 'ph\u00f9 h\u1ee3p'),  # 符合
        ('\u559c\u597d', 's\u1edf th\u00edch'),  # 喜好
        ('\u5e2e', 'gi\u00fap'),  # 帮
        ('\u641c\u8d44\u8baf', 't\u00ecm th\u00f4ng tin'),  # 搜资讯
        ('\u7ba1', 'qu\u1ea3n l\u00fd'),  # 管
        ('\u6293', 'thu th\u1eadp'),  # 抓
        ('\u4e0d\u53ea\u662f', 'kh\u00f4ng ch\u1ec9 l\u00e0'),  # 不只是
        ('\u8fde\u4e0a', 'K\u1ebft n\u1ed1i'),  # 连上
        ('\u5e72\u6d3b', 'l\u00e0m vi\u1ec7c'),  # 干活
        ('\u8bbe', '\u0110\u1eb7t'),  # 设
        ('\u63d0\u9192', 'nh\u1eafc'),  # 提醒
        ('\u4e0d\u7528\u4f60\u5f00\u53e3', 'kh\u00f4ng c\u1ea7n b\u1ea1n n\u00f3i'),  # 不用你开口
        ('\u6559\u5b83', 'D\u1ea1y n\u00f3'),  # 教它
        ('\u8bb0\u7b14\u8bb0', 'ghi ch\u00e9p'),  # 记笔记
        ('\u4e0b\u6b21', 'L\u1ea7n sau'),  # 下次
        ('\u4e0d\u7528', 'kh\u00f4ng c\u1ea7n'),  # 不用
        ('\u4ece\u5934', 't\u1eeb \u0111\u1ea7u'),  # 从头
        ('\u4ecb\u7ecd\u81ea\u5df1', 'gi\u1edbi thi\u1ec7u l\u1ea1i'),  # 介绍自己
        ('\u63a5\u4e0b\u6765', 'Ti\u1ebfp theo'),  # 接下来
        ('\u4e00\u4e2a\u4e2a\u6765', 't\u1eebng ph\u1ea7n m\u1ed9t'),  # 一个一个来
        ('\u7b2c\u4e00\u6b65', 'B\u01b0\u1edbc m\u1ed9t'),  # 第一步
        ('\u7b2c\u4e8c\u6b65', 'B\u01b0\u1edbc hai'),  # 第二步
        ('\u7b2c\u4e09\u6b65', 'B\u01b0\u1edbc ba'),  # 第三步
        ('\u7b2c\u56db\u6b65', 'B\u01b0\u1edbc b\u1ed1n'),  # 第四步
        ('\u7b2c\u4e94\u6b65', 'B\u01b0\u1edbc n\u0103m'),  # 第五步
        ('\u7b2c\u516d\u6b65', 'B\u01b0\u1edbc s\u00e1u'),  # 第六步
        ('\u7b2c\u4e03\u6b65', 'B\u01b0\u1edbc b\u1ea3y'),  # 第七步
        ('\u7075\u9b42', 'linh h\u1ed3n'),  # 灵魂
        ('\u4e09\u89c2', 'Tam quan'),  # 三观
        ('\u5168\u5bb6\u798f', 'B\u1ed9 s\u01b0u t\u1eadp \u0111\u1ea7y \u0111\u1ee7'),  # 全家福
        ('\u4e0d\u9700\u8981\u4e00\u6b21', 'kh\u00f4ng c\u1ea7n m\u1ed9t l\u1ea7n'),  # 不需要一次
        ('\u5168\u914d\u597d', 'c\u1ea5u h\u00ecnh h\u1ebft'),  # 全配好
        ('\u5148\u4e86\u89e3', 'Tr\u01b0\u1edbc ti\u00ean h\u00e3y hi\u1ec3u'),  # 先了解
        ('\u5e72\u4ec0\u4e48\u7684', 'd\u00f9ng \u0111\u1ec3 l\u00e0m g\u00ec'),  # 干什么的
        ('\u4e00\u53e5\u8bdd\u8bf4\u660e', 'Gi\u1ea3i th\u00edch m\u1ed9t c\u00e2u'),  # 一句话说明
        ('\u5fc5\u987b\u914d\u5417', 'B\u1eaft bu\u1ed9c c\u1ea5u h\u00ecnh?'),  # 必须配吗
        ('\u5f3a\u70c8\u5efa\u8bae', 'Khuy\u1ebfn kh\u00edch m\u1ea1nh'),  # 强烈建议
        ('\u4e2a\u4eba\u4fe1\u606f\u548c', 'th\u00f4ng tin c\u00e1 nh\u00e2n v\u00e0'),  # 个人信息和
        ('\u4e2a\u4eba\u6863\u6848', 'H\u1ed3 s\u01a1 c\u00e1 nh\u00e2n'),  # 个人档案
        ('\u540d\u5b57\u548c\u5916\u5728\u5f62\u8c61', 'T\u00ean v\u00e0 h\u00ecnh \u1ea3nh b\u00ean ngo\u00e0i'),  # 名字和外在形象
        ('\u540d\u7247', 'Danh thi\u1ebfp'),  # 名片
        ('\u5efa\u8bae', 'Khuy\u1ebfn kh\u00edch'),  # 建议
        ('\u5b89\u5168', 'an to\u00e0n'),  # 安全
        ('\u5458\u5de5\u624b\u518c', 'S\u1ed5 tay nh\u00e2n vi\u00ean'),  # 员工手册
        ('\u53ef\u9009', 'T\u00f9y ch\u1ecdn'),  # 可选
        ('\u9ed8\u8ba4\u503c', 'gi\u00e1 tr\u1ecb m\u1eb7c \u0111\u1ecbnh'),  # 默认值
        ('\u6267\u884c', 'th\u1ef1c hi\u1ec7n'),  # 执行
        ('\u4efb\u52a1', 't\u00e1c v\u1ee5'),  # 任务
        ('\u503c\u73ed\u8868', 'B\u1ea3ng tr\u1ef1c'),  # 值班表
        ('\u540e\u9762\u5355\u72ec\u8bb2', 'S\u1ebd n\u00f3i ri\u00eang \u1edf ph\u1ea7n sau'),  # 后面单独讲
        ('\u957f\u671f', 'd\u00e0i h\u1ea1n'),  # 长期
        ('\u751f\u6210', 't\u1ea1o'),  # 生成
        ('\u6700\u4f4e', 't\u1ed1i thi\u1ec3u'),  # 最低
        ('\u53ea\u914d', 'ch\u1ec9 c\u1ea7n'),  # 只配
        ('\u82b1', 'D\u00e0nh'),  # 花
        ('\u5206\u949f', 'ph\u00fat'),  # 分钟
        ('\u7acb\u7aff\u89c1\u5f71', 'th\u1ea5y ngay'),  # 立竿见影
        ('\u6700\u6838\u5fc3\u7684', 'c\u1ed1t l\u00f5i nh\u1ea5t'),  # 最核心的
        ('\u51b3\u5b9a\u4e86', 'quy\u1ebft \u0111\u1ecbnh'),  # 决定了
        ('\u8bdd\u65b9\u5f0f', 'c\u00e1ch n\u00f3i chuy\u1ec7n'),  # 话方式
        ('\u600e\u4e48\u521b\u5efa', 'T\u1ea1o nh\u01b0 th\u1ebf n\u00e0o'),  # 怎么创建
        ('\u8ba9', '\u0111\u1ec3'),  # 让
        ('\u81ea\u5df1', 't\u1ef1'),  # 自己
        ('\u5728\u7ebf', 'tr\u1ef1c tuy\u1ebfn'),  # 在线
        ('\u5728', 'trong'),  # 在
        ('\u91cc', ''),  # 里 (usually absorbed)
        ('\u7684', 'c\u1ee7a'),  # 的
        ('\u4e86', ''),  # 了 (aspect marker)
        ('\u548c', 'v\u00e0'),  # 和
        ('\u6216\u8005', 'ho\u1eb7c'),  # 或者
        ('\u6216', 'ho\u1eb7c'),  # 或
        ('\u4e0d', 'kh\u00f4ng'),  # 不
        ('\u6ca1\u6709', 'kh\u00f4ng c\u00f3'),  # 没有
        ('\u6ca1', 'kh\u00f4ng'),  # 没
        ('\u5982\u679c', 'N\u1ebfu'),  # 如果
        ('\u90a3', '\u0111\u00f3'),  # 那
        ('\u8fd9', 'n\u00e0y'),  # 这
        ('\u5c31', 'l\u00e0'),  # 就
        ('\u8fd8', 'v\u1eabn'),  # 还
        ('\u4f1a', 's\u1ebd'),  # 会
        ('\u80fd', 'c\u00f3 th\u1ec3'),  # 能
        ('\u8981', 'c\u1ea7n'),  # 要
        ('\u628a', ''),  # 把 (usually absorbed)
        ('\u7ed9', 'cho'),  # 给
        ('\u4ece', 't\u1eeb'),  # 从
        ('\u5230', '\u0111\u1ebfn'),  # 到
        ('\u6709', 'c\u00f3'),  # 有
        ('\u662f', 'l\u00e0'),  # 是
        ('\u4e0d\u662f', 'kh\u00f4ng ph\u1ea3i'),  # 不是
        ('\u53ef\u4ee5', 'c\u00f3 th\u1ec3'),  # 可以
        ('\u4f46\u662f', 'nh\u01b0ng'),  # 但是
        ('\u56e0\u4e3a', 'v\u00ec'),  # 因为
        ('\u5982\u679c', 'n\u1ebfu'),  # 如果
        ('\u867d\u7136', 'tuy'),  # 虽然
        ('\u6240\u4ee5', 'n\u00ean'),  # 所以
        ('\u800c\u4e14', 'v\u00e0'),  # 而且
        ('\u6216\u8005', 'ho\u1eb7c'),  # 或者
        ('\u8fd8\u662f', 'v\u1eabn'),  # 还是
        ('\u5df2\u7ecf', '\u0111\u00e3'),  # 已经
        ('\u6b63\u5728', '\u0111ang'),  # 正在
        ('\u6bcf\u6b21', 'm\u1ed7i l\u1ea7n'),  # 每次
        ('\u4e00\u6b21', 'm\u1ed9t l\u1ea7n'),  # 一次
        ('\u5148', 'tr\u01b0\u1edbc'),  # 先
        ('\u518d', 'r\u1ed3i'),  # 再
        ('\u5c31\u884c\u4e86', 'l\u00e0 xong'),  # 就行了
        ('\u4e0d\u8fc7', 'nh\u01b0ng'),  # 不过
        ('\u5176\u5b9e', 'th\u1ef1c ra'),  # 其实
        ('\u5f53\u7136', 't\u1ea5t nhi\u00ean'),  # 当然
        ('\u6bd4\u5982', 'v\u00ed d\u1ee5'),  # 比如
        ('\u65b9\u6848', 'Ph\u01b0\u01a1ng \u00e1n'),  # 方案
        ('\u9009\u62e9', 'ch\u1ecdn'),  # 选择
        ('\u5e38\u89c1', 'th\u01b0\u1eddng g\u1eb7p'),  # 常见
        ('\u4e3b\u8981', 'ch\u1ee7 y\u1ebfu'),  # 主要
        ('\u5305\u62ec', 'bao g\u1ed3m'),  # 包括
        ('\u6ce8\u610f', 'ch\u00fa \u00fd'),  # 注意
        ('\u7279\u6b8a', '\u0111\u1eb7c bi\u1ec7t'),  # 特殊
        ('\u5176\u4ed6', 'kh\u00e1c'),  # 其他
        ('\u6e20\u9053', 'k\u00eanh'),  # 渠道
        ('\u89e3\u51b3', 'gi\u1ea3i quy\u1ebft'),  # 解决
        ('\u7b49\u7ea7', 'm\u1ee9c'),  # 等级
        ('\u4e25\u683c\u6a21\u5f0f', 'Ch\u1ebf \u0111\u1ed9 nghi\u00eam ng\u1eb7t'),  # 严格模式
        ('\u5173\u95ed', 't\u1eaft'),  # 关闭
        ('\u8981\u505a', 'c\u1ea7n l\u00e0m'),  # 要做
        ('\u4e8b\u9879', 'vi\u1ec7c'),  # 事项
        ('\u7814\u7a76\u4eba\u5458', 'nh\u00e0 nghi\u00ean c\u1ee9u'),  # 研究人员
        ('\u53d1\u73b0', 'ph\u00e1t hi\u1ec7n'),  # 发现
        ('\u5168\u7403', 'to\u00e0n c\u1ea7u'),  # 全球
        ('\u8d85\u8fc7', 'h\u01a1n'),  # 超过
        ('\u5b9e\u4f8b', 'phi\u00ean b\u1ea3n'),  # 实例
        ('\u914d\u7f6e\u4e0d\u5f53', 'c\u1ea5u h\u00ecnh sai'),  # 配置不当
        ('\u66b4\u9732', 'b\u1ecb l\u1ed9'),  # 暴露
        ('\u5176\u4e2d', 'trong \u0111\u00f3'),  # 其中
        ('\u8fd1', 'g\u1ea7n'),  # 近
        ('\u6cc4\u9732', 'b\u1ecb l\u1ed9'),  # 泄露
        ('\u4e0d\u8981\u6210\u4e3a', '\u0110\u1eebng tr\u1edf th\u00e0nh'),  # 不要成为
        ('\u5176\u4e2d\u4e00\u4e2a', 'm\u1ed9t trong s\u1ed1 \u0111\u00f3'),  # 其中一个
        ('\u786e\u4fdd', '\u0110\u1ea3m b\u1ea3o'),  # 确保
        ('\u5f00\u653e\u5230', 'm\u1edf ra'),  # 开放到
        ('\u7535\u8111', 'm\u00e1y t\u00ednh'),  # 电脑
        ('\u623f\u5b50', 'ng\u00f4i nh\u00e0'),  # 房子
        ('\u7a97\u6237', 'c\u1eeda s\u1ed5'),  # 窗户
        ('\u7f16\u53f7', 's\u1ed1'),  # 编号
        ('\u5927\u8857', '\u0111\u01b0\u1eddng'),  # 大街
        ('\u6253\u5f00', 'm\u1edf'),  # 打开
        ('\u4efb\u4f55', 'ai'),  # 任何
        ('\u8def\u8fc7', '\u0111i qua'),  # 路过
        ('\u80fd\u5f80\u91cc\u9762\u770b', 'nh\u00ecn \u0111\u01b0\u1ee3c v\u00e0o trong'),  # 能往里面看
        ('\u8bbf\u95ee\u5730\u5740', '\u0110\u1ecba ch\u1ec9 truy c\u1eadp'),  # 访问地址
        ('\u610f\u601d\u662f', 'c\u00f3 ngh\u0129a l\u00e0'),  # 意思是
        ('\u53ea\u6709\u6211\u81ea\u5df1\u80fd\u8bbf\u95ee', 'ch\u1ec9 m\u00ecnh t\u00f4i truy c\u1eadp \u0111\u01b0\u1ee3c'),  # 只有我自己能访问
        ('\u4e0d\u8981\u628a\u5b83\u6539\u6210', '\u0110\u1eebng \u0111\u1ed5i th\u00e0nh'),  # 不要把它改成
        ('\u8fd0\u884c', 'Ch\u1ea1y'),  # 运行
        ('\u770b\u8f93\u51fa\u91cc\u7684\u5730\u5740', 'Xem \u0111\u1ecba ch\u1ec9 trong k\u1ebft qu\u1ea3'),  # 看输出里的地址
        ('\u5982\u679c\u662f', 'n\u1ebfu l\u00e0'),  # 如果是
        ('\u5b89\u5168\u7684', 'an to\u00e0n'),  # 安全的
        ('\u4fdd\u62a4\u597d', 'B\u1ea3o v\u1ec7'),  # 保护好
        ('\u8fc7\u7a0b\u4e2d', 'qu\u00e1 tr\u00ecnh'),  # 过程中
        ('\u8f93\u5165\u4e86\u5404\u79cd', '\u0111\u00e3 nh\u1eadp c\u00e1c'),  # 输入了各种
        ('\u76f8\u5f53\u4e8e', 't\u01b0\u01a1ng \u0111\u01b0\u01a1ng'),  # 相当于
        ('\u4e0d\u8981\u628a', '\u0110\u1eebng'),  # 不要把
        ('\u5305\u542b', 'ch\u1ee9a'),  # 包含
        ('\u4e0a\u4f20\u5230', 'upload l\u00ean'),  # 上传到
        ('\u54ea\u6015', 'd\u00f9'),  # 哪怕
        ('\u79c1\u6709\u4ed3\u5e93', 'repo ri\u00eang t\u01b0'),  # 私有仓库
        ('\u53d1\u5728', 'g\u1eedi trong'),  # 发在
        ('\u622a\u56fe\u53d1\u7ed9\u522b\u4eba', 'ch\u1ee5p m\u00e0n h\u00ecnh g\u1eedi cho ng\u01b0\u1eddi kh\u00e1c'),  # 截图发给别人
        ('\u5b9a\u671f', '\u0111\u1ecbnh k\u1ef3'),  # 定期
        ('\u65b0\u7248\u672c', 'Phi\u00ean b\u1ea3n m\u1edbi'),  # 新版本
        ('\u7ecf\u5e38', 'th\u01b0\u1eddng xuy\u00ean'),  # 经常
        ('\u4fee\u590d', 'v\u00e1'),  # 修复
        ('\u6f0f\u6d1e', 'l\u1ed7 h\u1ed5ng b\u1ea3o m\u1eadt'),  # 漏洞
        ('\u81f3\u5c11', '\u00edt nh\u1ea5t'),  # 至少
        ('\u4e24\u5468', 'hai tu\u1ea7n'),  # 两周
        ('\u4e0d\u77e5\u9053\u4f60\u6709\u6ca1\u6709', 'Kh\u00f4ng bi\u1ebft b\u1ea1n c\u00f3'),  # 不知道你有没有
        ('\u4f53\u9a8c', 'tr\u1ea3i nghi\u1ec7m'),  # 体验
        ('\u804a\u5f97\u631a\u597d', 'chat r\u1ea5t vui'),  # 聊得挺好
        ('\u5173\u6389', 't\u1eaft \u0111i'),  # 关掉
        ('\u53c8\u4ec0\u4e48\u90fd\u4e0d\u8bb0\u5f97\u4e86', 'l\u1ea1i kh\u00f4ng nh\u1edb g\u00ec'),  # 又什么都不记得了
        ('\u50cf\u6362\u4e86\u4e00\u4e2a\u4eba', 'nh\u01b0 \u0111\u1ed5i ng\u01b0\u1eddi'),  # 像换了一个人
        ('\u7ee7\u7eed\u6628\u5929\u7684\u8bdd\u9898', 'ti\u1ebfp t\u1ee5c ch\u1ee7 \u0111\u1ec1 h\u00f4m qua'),  # 继续昨天的话题
        ('\u4e00\u8138\u61f5', 'ng\u01a1 ng\u00e1c'),  # 一脸懵
        ('\u5931\u5fc6', 'm\u1ea5t tr\u00ed nh\u1edb'),  # 失忆
        ('\u4e00\u5957', 'h\u1ec7 th\u1ed1ng'),  # 一套
        ('\u5206\u4e24\u5c42', 'chia hai t\u1ea7ng'),  # 分两层
        ('\u4eba\u7684\u5927\u8111', 'n\u00e3o ng\u01b0\u1eddi'),  # 人的大脑
        ('\u4e2a\u4eba\u8ba4\u77e5', 'nh\u1eadn th\u1ee9c c\u00e1 nh\u00e2n'),  # 个人认知
        ('\u8bb0\u5f55', 'ghi l\u1ea1i'),  # 记录
        ('\u8de8\u8d8a', 'qua'),  # 跨越
        ('\u591a\u6b21\u5bf9\u8bdd', 'nhi\u1ec1u cu\u1ed9c tr\u00f2 chuy\u1ec7n'),  # 多次对话
        ('\u6709\u7528', 'h\u1eefu \u00edch'),  # 有用
        ('\u4e60\u60ef', 'th\u00f3i quen'),  # 习惯
        ('\u6c47\u62a5', 'b\u00e1o c\u00e1o'),  # 汇报
        ('\u7b80\u6d01', 'ng\u1eafn g\u1ecdn'),  # 简洁
        ('\u65e5\u53c6', 'Nh\u1eadt k\u00fd h\u00e0ng ng\u00e0y'),  # 每日日志
        ('\u5bf9\u8bdd\u7ed3\u675f\u540e', 'k\u1ebft th\u00fac tr\u00f2 chuy\u1ec7n'),  # 对话结束后
        ('\u5f53\u5929\u7684', 'trong ng\u00e0y'),  # 当天的
        ('\u4eca\u5929', 'h\u00f4m nay'),  # 今天
        ('\u53d1\u751f\u7684\u4e8b\u60c5', 'x\u1ea3y ra g\u00ec'),  # 发生的事情
        ('\u4ec0\u4e48\u53d8\u5316', 'c\u00f3 thay \u0111\u1ed5i g\u00ec'),  # 什么变化
        ('\u7b2c\u4e8c\u5929', 'ng\u00e0y h\u00f4m sau'),  # 第二天
        ('\u8bfb', '\u0111\u1ecdc'),  # 读
        ('\u6700\u8fd1', 'g\u1ea7n nh\u1ea5t'),  # 最近
        ('\u4fdd\u6301', 'duy tr\u00ec'),  # 保持
        ('\u8fde\u7eed\u6027', 't\u00ednh li\u00ean t\u1ee5c'),  # 连续性
        ('\u4f7f\u7528', 's\u1eed d\u1ee5ng'),  # 使用
        ('\u67e5\u770b', 'Xem'),  # 查看
        ('\u8bb0\u4e86\u4ec0\u4e48', 'ghi nh\u1edb g\u00ec'),  # 记了什么
        ('\u76f4\u63a5\u5728', 'tr\u1ef1c ti\u1ebfp trong'),  # 直接在
        ('\u95ee', 'h\u1ecfi'),  # 问
        ('\u6574\u7406\u597d', 's\u1eafp x\u1ebfp'),  # 整理好
        ('\u544a\u8bc9\u4f60', 'n\u00f3i cho b\u1ea1n'),  # 告诉你
        ('\u7279\u5b9a\u7684\u4e8b', 'vi\u1ec7c c\u1ee5 th\u1ec3'),  # 特定的事
        ('\u5199\u8fdb', 'ghi v\u00e0o'),  # 写进
        ('\u5fd8\u6389\u67d0\u4e9b\u4e8b', 'qu\u00ean m\u1ed9t s\u1ed1 vi\u1ec7c'),  # 忘掉某些事
        ('\u7ea0\u6b63\u9519\u8bef\u7684', 'S\u1eeda b\u1ed9 nh\u1edb sai'),  # 纠正错误的
        ('\u9664\u4e86\u4f60\u624b\u52a8\u8ba9\u5b83\u8bb0', 'Ngo\u00e0i vi\u1ec7c b\u1ea1n y\u00eau c\u1ea7u th\u1ee7 c\u00f4ng'),  # 除了你手动让它记
        ('\u4e0a\u4e0b\u6587\u7a97\u53e3\u5feb\u6ee1\u4e86', 'c\u1eeda s\u1ed5 ng\u1eef c\u1ea3nh s\u1eafp \u0111\u1ea7y'),  # 上下文窗口快满了
        ('\u626b\u63cf', 'qu\u00e9t'),  # 扫描
        ('\u5bf9\u8bdd\u5185\u5bb9', 'n\u1ed9i dung tr\u00f2 chuy\u1ec7n'),  # 对话内容
        ('\u503c\u5f97\u8bb0\u4f4f\u7684', '\u0111\u00e1ng nh\u1edb'),  # 值得记住的
        ('\u63d0\u70bc', 'tr\u00edch xu\u1ea5t'),  # 提炼
        ('\u597d\u52a9\u7406', 'tr\u1ee3 l\u00fd gi\u1ecfi'),  # 好助理
        ('\u4e0b\u73ed\u524d', 'tr\u01b0\u1edbc khi tan l\u00e0m'),  # 下班前
        ('\u91cd\u8981\u7684\u4e8b\u60c5', 'nh\u1eefng vi\u1ec7c quan tr\u1ecdng'),  # 重要的事情
        ('\u8bb0\u5230\u7b14\u8bb0\u672c\u91cc', 'ghi v\u00e0o s\u1ed5'),  # 记到笔记本里
        ('\u4e0a\u73ed\u65f6', '\u0111i l\u00e0m'),  # 上班时
        ('\u7ffb\u4e00\u4e0b\u7b14\u8bb0\u672c', 'l\u1eadt s\u1ed5 xem l\u1ea1i'),  # 翻一下笔记本
        ('\u5c40\u9650', 'H\u1ea1n ch\u1ebf'),  # 局限
        ('\u5927\u5c0f\u9650\u5236', 'gi\u1edbi h\u1ea1n k\u00edch th\u01b0\u1edbc'),  # 大小限制
        ('\u65e0\u9650\u5927', 'l\u1edbn v\u00f4 h\u1ea1n'),  # 无限大
        ('\u5355\u4e2a', 'm\u1ed9t'),  # 单个
        ('\u5b57\u7b26', 'k\u00fd t\u1ef1'),  # 字符
        ('\u88ab\u622a\u65ad', 'b\u1ecb c\u1eaft'),  # 被截断
        ('\u4fdd\u7559', 'gi\u1eef l\u1ea1i'),  # 保留
        ('\u6700\u91cd\u8981\u7684', 'quan tr\u1ecdng nh\u1ea5t'),  # 最重要的
        ('\u7ec6\u8282', 'chi ti\u1ebft'),  # 细节
        ('\u53ef\u80fd\u4f1a\u51b2\u7a81', 'C\u00f3 th\u1ec3 xung \u0111\u1ed9t'),  # 可能会冲突
        ('\u6539\u4e86', '\u0111\u1ed5i'),  # 改了
        ('\u5fd8\u4e86', 'qu\u00ean'),  # 忘了
        ('\u53ef\u80fd\u8fd8\u6309\u65e7\u7684\u6765', 'c\u00f3 th\u1ec3 v\u1eabn l\u00e0m theo c\u00e1i c\u0169'),  # 可能还按旧的来
        ('\u9047\u5230', 'G\u1eb7p'),  # 遇到
        ('\u60c5\u51b5', 't\u00ecnh hu\u1ed1ng'),  # 情况
        ('\u53ea\u8bb0\u6587\u5b57', 'Ch\u1ec9 nh\u1edb v\u0103n b\u1ea3n'),  # 只记文字
        ('\u4e0d\u80fd\u8bb0', 'Kh\u00f4ng nh\u1edb \u0111\u01b0\u1ee3c'),  # 不能记
        ('\u56fe\u7247', 'h\u00ecnh \u1ea3nh'),  # 图片
        ('\u8fd9\u4e9b\u4e1c\u897f', ''),  # 这些东西
        ('\u5c0f\u6280\u5de7', 'M\u1eb9o nh\u1ecf'),  # 小技巧
        ('\u89c9\u5f97', 'th\u1ea5y'),  # 觉得
        ('\u6df7\u4e71', 'l\u1ed9n x\u1ed9n'),  # 混乱
        ('\u53ef\u4ee5\u8bf4', 'c\u00f3 th\u1ec3 n\u00f3i'),  # 可以说
        ('\u8fc7\u65f6\u7684', 'l\u1ed7i th\u1eddi'),  # 过时的
        ('\u6e05\u7406\u4e00\u4e0b', 'd\u1ecdn d\u1eb9p'),  # 清理一下
        ('\u81ea\u5df1\u6574\u7406', 't\u1ef1 s\u1eafp x\u1ebfp'),  # 自己整理
        ('\u5916\u90e8\u670d\u52a1', 'd\u1ecbch v\u1ee5 b\u00ean ngo\u00e0i'),  # 外部服务
        ('\u5165\u95e8', 'nh\u1eadp m\u00f4n'),  # 入门
        ('\u8fdb\u9636\u5185\u5bb9', 'n\u1ed9i dung n\u00e2ng cao'),  # 进阶内容
        ('\u5df2\u7ecf\u89c9\u5f97', 'th\u1ea5y'),  # 已经觉得
        ('\u591f\u7528', '\u0111\u1ee7 d\u00f9ng'),  # 够用
        ('\u53ef\u4ee5\u5148\u8df3\u8fc7', 'c\u00f3 th\u1ec3 b\u1ecf qua tr\u01b0\u1edbc'),  # 可以先跳过
        ('\u4ee5\u540e', 'khi n\u00e0o'),  # 以后
        ('\u518d\u6765\u770b', 'quay l\u1ea1i xem'),  # 再来看
        ('\u5168\u540d\u53eb', 't\u00ean \u0111\u1ea7y \u0111\u1ee7 l\u00e0'),  # 全名叫
        ('\u540d\u5b57\u542c\u7740\u5413\u4eba', 'T\u00ean nghe \u0111\u00e1ng s\u1ee3'),  # 名字听着吓人
        ('\u7528\u4e00\u4e2a\u4f8b\u5b50\u5c31\u80fd\u542c\u61c2', 'nh\u01b0ng d\u00f9ng m\u1ed9t v\u00ed d\u1ee5 l\u00e0 hi\u1ec3u ngay'),  # 用一个例子就能听懂
        ('\u4f60\u5bb6', 'Nh\u00e0 b\u1ea1n'),  # 你家
        ('\u667a\u80fd\u97f3\u7bb1', 'loa th\u00f4ng minh'),  # 智能音箱
        ('\u53ea\u80fd\u653e\u6b4c\u548c\u62a5\u5929\u6c14', 'ch\u1ec9 ph\u00e1t nh\u1ea1c v\u00e0 b\u00e1o th\u1eddi ti\u1ebft'),  # 只能放歌和报天气
        ('\u667a\u80fd\u706f\u6ce1', 'b\u00f3ng \u0111\u00e8n th\u00f4ng minh'),  # 智能灯泡
        ('\u8fde\u8d77\u6765', 'k\u1ebft n\u1ed1i'),  # 连起来
        ('\u5173\u706f', 't\u1eaft \u0111\u00e8n'),  # 关灯
        ('\u5c31\u80fd', 'c\u00f3 th\u1ec3'),  # 就能
        ('\u8d8a\u591a', 'c\u00e0ng nhi\u1ec1u'),  # 越多
        ('\u6280\u672f', 'c\u00f4ng ngh\u1ec7'),  # 技术
        ('\u8f6f\u4ef6\u548c\u670d\u52a1', 'ph\u1ea7n m\u1ec1m v\u00e0 d\u1ecbch v\u1ee5'),  # 软件和服务
        ('\u7b14\u8bb0', 'ghi ch\u00fa'),  # 笔记
        ('\u4ee3\u7801', 'code'),  # 代码
        ('\u6392\u65e5\u7a0b', 's\u1eafp l\u1ecbch'),  # 排日程
        ('\u4e00\u884c\u547d\u4ee4\u5c31\u884c', 'M\u1ed9t d\u00f2ng l\u1ec7nh l\u00e0 xong'),  # 一行命令就行
        ('\u4e0d\u77e5\u9053\u8be5\u8fde\u4ec0\u4e48', 'Kh\u00f4ng bi\u1ebft n\u00ean k\u1ebft n\u1ed1i g\u00ec'),  # 不知道该连什么
        ('\u8fde\u4e0d\u4e0a\u600e\u4e48\u529e', 'kh\u00f4ng k\u1ebft n\u1ed1i \u0111\u01b0\u1ee3c th\u00ec sao'),  # 连不上怎么办
        ('\u670d\u52a1', 'd\u1ecbch v\u1ee5'),  # 服务
        ('\u5217\u8868', 'danh s\u00e1ch'),  # 列表
        ('\u68af\u5b50', 'VPN'),  # 梯子
        ('\u6309\u7167\u63d0\u793a\u64cd\u4f5c\u5c31\u884c', 'l\u00e0m theo h\u01b0\u1edbng d\u1eabn l\u00e0 \u0111\u01b0\u1ee3c'),  # 按照提示操作就行
        ('\u5bf9\u6bd4', 'So s\u00e1nh'),  # 对比
        ('\u4e4b\u524d', 'Tr\u01b0\u1edbc'),  # 之前
        ('\u521a\u88c5\u597d', 'v\u1eeba c\u00e0i xong'),  # 刚装好
        ('\u73b0\u5728', 'B\u00e2y gi\u1edd'),  # 现在
        ('\u914d\u597d\u4e4b\u540e', 'sau khi c\u1ea5u h\u00ecnh'),  # 配好之后
        ('\u6ca1\u533a\u522b', 'kh\u00f4ng kh\u00e1c g\u00ec'),  # 没区别
        ('\u53ea\u80fd\u5728', 'ch\u1ec9 tr\u00ean'),  # 只能在
        ('\u7f51\u9875\u9762\u677f', 'b\u1ea3ng web'),  # 网页面板
        ('\u968f\u65f6', 'b\u1ea5t c\u1ee9 l\u00fac n\u00e0o'),  # 随时
        ('\u9646\u751f\u4eba', 'ng\u01b0\u1eddi l\u1ea1'),  # 陌生人
        ('\u53ea\u80fd\u56de\u7b54\u95ee\u9898', 'Ch\u1ec9 tr\u1ea3 l\u1eddi c\u00e2u h\u1ecfi'),  # 只能回答问题
        ('\u80fd\u641c\u8d44\u8baf', 'T\u00ecm tin t\u1ee9c'),  # 能搜资讯
        ('\u603b\u7ed3\u6587\u7ae0', 't\u00f3m t\u1eaft b\u00e0i vi\u1ebft'),  # 总结文章
        ('\u64cd\u63a7', '\u0111i\u1ec1u khi\u1ec3n'),  # 操控
        ('\u4e0d\u53eb\u5b83\u5c31\u4e0d\u52a8', 'kh\u00f4ng g\u1ecdi n\u00f3 kh\u00f4ng \u0111\u1ed9ng'),  # 不叫它就不动
        ('\u98ce\u683c', 'Phong c\u00e1ch'),  # 风格
        ('\u5343\u7bc7\u4e00\u5f8b', 'na n\u00e1 nhau'),  # 千篇一律
        ('\u65b9\u5f0f\u6c9f\u901a', 'c\u00e1ch giao ti\u1ebfp'),  # 方式沟通
        ('\u5168\u5fd8\u4e86', 'qu\u00ean h\u1ebft'),  # 全忘了
        ('\u8bf4\u8fc7\u4ec0\u4e48', '\u0111\u00e3 n\u00f3i g\u00ec'),  # 说过什么
        ('\u5feb\u901f\u53c2\u8003', 'tham kh\u1ea3o nhanh'),  # 快速参考
        ('\u6015\u4f60\u770b\u5b8c\u4e4b\u540e', 'S\u1ee3 b\u1ea1n \u0111\u1ecdc xong'),  # 怕你看完之后
        ('\u5fd8\u4e86\u8981\u505a\u4ec0\u4e48', 'qu\u00ean ph\u1ea3i l\u00e0m g\u00ec'),  # 忘了要做什么
        ('\u8fd9\u91cc\u7ed9\u4f60\u4e00\u4efd', '\u0111\u00e2y l\u00e0'),  # 这里给你一份
        ('\u6700\u7cbe\u7b80\u7684\u6e05\u5355', 'danh s\u00e1ch tinh g\u1ecdn nh\u1ea5t'),  # 最精简的清单
        ('\u5fc5\u505a', 'Ph\u1ea3i l\u00e0m'),  # 必做
        ('\u641e\u5b9a', 'xong'),  # 搞定
        ('\u4e09\u4e2a', 'ba'),  # 三个
        ('\u56db\u4e2a', 'b\u1ed1n'),  # 四个
        ('\u57fa\u7840', 'c\u01a1 b\u1ea3n'),  # 基础
        ('\u56fd\u5185\u9009', 'Trung Qu\u1ed1c ch\u1ecdn'),  # 国内选
        ('\u6d77\u5916\u9009', 'n\u01b0\u1edbc ngo\u00e0i ch\u1ecdn'),  # 海外选
        ('\u6ca1\u6709\u6cc4\u9732', 'kh\u00f4ng b\u1ecb l\u1ed9'),  # 没有泄露
        ('\u5efa\u8bae\u505a', 'N\u00ean l\u00e0m'),  # 建议做
        ('\u53d6\u4e2a\u540d\u5b57', '\u0111\u1eb7t t\u00ean'),  # 取个名字
        ('\u4e00\u6761\u4fe1\u606f', 'm\u1ed9t th\u00f4ng tin'),  # 一条信息
        ('\u91cd\u542f\u540e\u770b\u8fd8\u8bb0\u4e0d\u8bb0\u5f97', 'kh\u1edfi \u0111\u1ed9ng l\u1ea1i xem c\u00f2n nh\u1edb kh\u00f4ng'),  # 重启后看还记不记得
        ('\u4ee5\u540e\u518d\u8bf4', '\u0110\u1ec3 sau'),  # 以后再说
        ('\u9700\u8981\u4e86\u518d\u914d', 'c\u1ea7n m\u1edbi c\u1ea5u h\u00ecnh'),  # 需要了再配
        ('\u9700\u8981\u4ec0\u4e48\u88c5\u4ec0\u4e48', 'c\u1ea7n g\u00ec c\u00e0i n\u1ea5y'),  # 需要什么装什么
        ('\u901b\u901b', 'd\u1ea1o'),  # 逛逛
        ('\u7cbe\u8c03', 'Tinh ch\u1ec9nh'),  # 精调
        ('\u7528\u4e00\u6bb5\u65f6\u95f4\u540e', 'd\u00f9ng m\u1ed9t th\u1eddi gian r\u1ed3i'),  # 用一段时间后
        ('\u6839\u636e', 'theo'),  # 根据
        ('\u8c03\u6574', '\u0111i\u1ec1u ch\u1ec9nh'),  # 调整
        ('\u66f4\u591a', 'th\u00eam'),  # 更多
        ('\u7b49', '...'),  # 等
        ('\u8bf4\u4e24\u53e5', 'n\u00f3i v\u00e0i l\u1eddi'),  # 说两句
        ('\u7b2c\u4e00\u7bc7', 'B\u00e0i \u0111\u1ea7u ti\u00ean'),  # 第一篇
        ('\u8fd9\u4e00\u7bc7', 'b\u00e0i n\u00e0y'),  # 这一篇
        ('\u53d8\u6210', 'bi\u1ebfn th\u00e0nh'),  # 变成
        ('\u5f88\u591a\u4eba', 'Nhi\u1ec1u ng\u01b0\u1eddi'),  # 很多人
        ('\u7528\u4e86\u4e24\u5929', 'd\u00f9ng hai ng\u00e0y'),  # 用了两天
        ('\u5c31\u653e\u5f03\u4e86', 'r\u1ed3i b\u1ecf'),  # 就放弃了
        ('\u539f\u56e0\u51e0\u4e4e\u90fd\u4e00\u6837', 'nguy\u00ean nh\u00e2n h\u1ea7u nh\u01b0 gi\u1ed1ng nhau'),  # 原因几乎都一样
        ('\u6ca1\u505a', 'kh\u00f4ng'),  # 没做
        ('\u8ddf', 'v\u1edbi'),  # 跟
        ('\u4f60\u82b1', 'b\u1ea1n d\u00e0nh'),  # 你花
        ('\u5b8c\u5168\u4e0d\u4e00\u6837', 'ho\u00e0n to\u00e0n kh\u00e1c'),  # 完全不一样
        ('\u67e5\u8d44\u6599', 'tra t\u00e0i li\u1ec7u'),  # 查资料
        ('\u63a8\u4e00\u6761\u7b80\u62a5', '\u0111\u1ea9y b\u1ea3n tin'),  # 推一条简报
        ('\u4e0d\u7528\u518d\u8bf4', 'kh\u00f4ng c\u1ea7n n\u00f3i l\u1ea1i'),  # 不用再说
        ('\u8d8a\u7528\u8d8a\u61c2\u4f60', 'c\u00e0ng d\u00f9ng c\u00e0ng hi\u1ec3u b\u1ea1n'),  # 越用越懂你
        ('\u8fd8\u8bb0\u5f97', 'C\u00f2n nh\u1edb'),  # 还记得
        ('\u5f00\u5934\u8bf4\u7684', '\u0111\u1ea7u b\u00e0i'),  # 开头说的
        ('\u90a3\u4e2a', ''),  # 那个
        ('\u5417', 'kh\u00f4ng'),  # 吗
        ('\u5e72\u7684\u575a\u51b3\u4e0d\u81ea\u5df1\u5e72', 'l\u00e0m \u0111\u01b0\u1ee3c th\u00ec ki\u00ean quy\u1ebft kh\u00f4ng t\u1ef1 l\u00e0m'),  # 干的坚决不自己干
        ('\u6559\u4e86\u5f88\u591a', 'd\u1ea1y nhi\u1ec1u'),  # 教了很多
        ('\u7684\u65b9\u6cd5', ''),  # 的方法
        ('\u771f\u6b63\u7528\u8d77\u6765\u7684\u65f6\u5019', 'th\u1ef1c s\u1ef1 s\u1eed d\u1ee5ng'),  # 真正用起来的时候
        ('\u5927\u591a\u6570', '\u0111a s\u1ed1'),  # 大多数
        ('\u53ef\u4ee5\u76f4\u63a5', 'c\u00f3 th\u1ec3 n\u00f3i th\u1eb3ng'),  # 可以直接
        ('\u5e2e\u6211\u914d\u4e00\u4e0b', 'gi\u00fap t\u00f4i c\u1ea5u h\u00ecnh'),  # 帮我配一下
        ('\u6765\u5b8c\u6210', 'l\u00e0 xong'),  # 来完成
        ('\u5b83\u5c31\u662f\u4f60\u7684', 'N\u00f3 l\u00e0'),  # 它就是你的
        ('\u5e72\u6d3b\u624d\u662f', 'l\u00e0m vi\u1ec7c m\u1edbi l\u00e0'),  # 干活才是
        ('\u6b63\u786e\u7684\u6253\u5f00\u65b9\u5f0f', 'c\u00e1ch d\u00f9ng \u0111\u00fang'),  # 正确的打开方式
        ('\u4e0d\u8fc7\u8bf4\u5b9e\u8bdd', 'Nh\u01b0ng n\u00f3i th\u1eadt'),  # 不过说实话
        ('\u53ea\u662f\u8d77\u70b9', 'ch\u1ec9 l\u00e0 \u0111i\u1ec3m kh\u1edfi \u0111\u1ea7u'),  # 只是起点
        ('\u771f\u6b63\u7684\u6740\u624b\u9527\u662f\u5b83\u7684', 'V\u0169 kh\u00ed b\u00ed m\u1eadt th\u1ef1c s\u1ef1 l\u00e0'),  # 真正的杀手锏是它的
        ('\u628a\u591a\u4e2a', 'n\u1ed1i nhi\u1ec1u'),  # 把多个
        ('\u4e32\u8d77\u6765', 'l\u1ea1i'),  # 串起来
        ('\u5b8c\u6210\u4e00\u6574\u5957\u64cd\u4f5c', 'ho\u00e0n th\u00e0nh c\u1ea3 b\u1ed9 thao t\u00e1c'),  # 完成一整套操作
        ('\u884c\u4e1a\u65b0\u95fb', 'tin t\u1ee9c ng\u00e0nh'),  # 行业新闻
        ('\u603b\u7ed3\u6210\u7b80\u62a5', 't\u00f3m t\u1eaft th\u00e0nh b\u1ea3n tin'),  # 总结成简报
        ('\u53d1\u5230', 'g\u1eedi v\u00e0o'),  # 发到
        ('\u7fa4\u91cc', 'nh\u00f3m'),  # 群里
        ('\u540c\u6b65\u5230', '\u0111\u1ed3ng b\u1ed9 l\u00ean'),  # 同步到
        ('\u8fd9\u4e00\u6574\u5957', 'c\u1ea3 b\u1ed9 n\u00e0y'),  # 这一整套
        ('\u4f60\u8bf4\u4e00\u53e5\u8bdd\u5b83\u5c31\u5168\u5e72\u4e86', 'b\u1ea1n n\u00f3i m\u1ed9t c\u00e2u n\u00f3 l\u00e0m h\u1ebft'),  # 你说一句话它就全干了
        ('\u6211\u4f1a', 't\u00f4i s\u1ebd'),  # 我会
        ('\u6253\u9020\u5c5e\u4e8e\u4f60\u81ea\u5df1\u7684', 'c\u1ee7a ri\u00eang b\u1ea1n'),  # 打造属于你自己的
        ('\u81ea\u52a8\u5316\u529e\u516c', 't\u1ef1 \u0111\u1ed9ng h\u00f3a c\u00f4ng vi\u1ec7c'),  # 自动化办公
        ('\u81ea\u52a8\u5316', 't\u1ef1 \u0111\u1ed9ng h\u00f3a'),  # 自动化
        ('\u656c\u8bf7\u671f\u5f85', 'H\u00e3y \u0111\u00f3n ch\u1edd'),  # 敬请期待
        ('\u6709\u4ec0\u4e48', 'C\u00f3 v\u1ea5n \u0111\u1ec1 g\u00ec'),  # 有什么
        ('\u7684\u95ee\u9898', ''),  # 的问题
        ('\u8bc4\u8bba\u533a\u89c1', 'h\u1eb9n g\u1eb7p \u1edf ph\u1ea7n b\u00ecnh lu\u1eadn'),  # 评论区见
        ('\u611f \u8c22 \u9605 \u8bfb', 'C\u1ea3m \u01a1n \u0111\u00e3 \u0111\u1ecdc'),  # 感 谢 阅 读
        ('\u70b9\u8d5e', 'Like'),  # 点赞
        ('\u8f6c\u53d1', 'chia s\u1ebb'),  # 转发
        ('\u5173\u6ce8\u5173\u6ce8\u5173\u6ce8', 'theo d\u00f5i'),  # 关注关注关注
    ]

    for cn_p, vi_p in phrases:
        v = v.replace(cn_p, vi_p)

    return v

translated = 0
kept = 0
total_text = 0

for block in out['blocks']:
    for el in block['elements']:
        if el['type'] != 'text_run':
            continue
        total_text += 1
        c = el['content']
        if not c.strip():
            kept += 1
            continue
        if not re.search('[\u4e00-\u9fff]', c):
            kept += 1
            continue

        v = tr(c)
        el['content'] = v
        if re.search('[\u4e00-\u9fff]', v):
            kept += 1
        else:
            translated += 1

# Add space between adjacent Vietnamese text_run elements
for block in out['blocks']:
    elements = block.get('elements', [])
    for i in range(len(elements) - 1):
        if elements[i].get('type') == 'text_run' and elements[i+1].get('type') == 'text_run':
            c1 = elements[i]['content']
            c2 = elements[i+1]['content']
            if c1 and c2 and not c1.endswith(' ') and not c2.startswith(' '):
                if re.search(r'[a-zA-Z\u00C0-\u024F\u1E00-\u1EFF]', c1[-1:]) and re.search(r'[a-zA-Z\u00C0-\u024F\u1E00-\u1EFF]', c2[:1]):
                    elements[i]['content'] = c1 + ' '

with open('_art31_trans.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

# Count remaining Chinese
remaining_cn = 0
for block in out['blocks']:
    for el in block['elements']:
        if el['type'] == 'text_run' and re.search('[\u4e00-\u9fff]', el['content']):
            remaining_cn += 1

print(f'Total text: {total_text}')
print(f'Translated: {translated}')
print(f'Kept: {kept}')
print(f'Remaining Chinese: {remaining_cn}')
print(f'Saved _art31_trans.json')
