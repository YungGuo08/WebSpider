"""
转换设置说明：
翻译默认设置自动检测语言翻译，部分语言不支持自动检测翻译（会出现翻译结果为原文）
如果要选择对应语言翻译，请将ACTION改为lan-select；
再将FROM_LANGUAGE，TO_LANGUAGE修改成对应语言的字母就行

例如：
1、中文翻译成日语：ACTION设为'lan-select'，FROM_LANGUAGE设为'zh-CHS'，TO_LANGUAGE设为'ja'
2、日文翻译成中文：ACTION设为'lan-select'，FROM_LANGUAGE设为'ja'，TO_LANGUAGE设为'zh-CHS'
"""

# 中文：zh-CHS    日语：ja    英语：en        韩语：ko        法语：fr
# 德语：de        俄语：ru    西班牙语：es     葡萄牙语：pt     意大利语：it
# 越南语：vi       印尼语：id   阿拉伯语：ar    荷兰语：nl

# 翻译类型：自动检测（FY_BY_REALTlME）/手动选择（lan-select）
ACTION = 'FY_BY_REALTlME'

# AUTO代表自动检测
# 原文语言
FROM_LANGUAGE = 'AUTO'

# 翻译语言
TO_LANGUAGE = 'AUTO'
