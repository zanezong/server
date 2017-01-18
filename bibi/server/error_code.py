#coding: utf-8
__author__ = 'bozyao'

#==================
#错误信息及code列表

ERROR_MSG = "服务器链接失败，请稍候再试。"
ERROR_CODE = {
    #返回内容错误
    "CONTENT_ERROR":        10000,
    "SERVER_MAINTENANCE":   10001,

    #第三方或者其他服务错误
    "MYSQL_ERROR":          20001,
    "REDIS_ERROR":          20002,

    #参数错误
    "ARGUMENT_ERROR":       30001,
    "ALREADY_BUY":          30002,

    #未知错误
    "UNKNOW_ERROR":         11111,

    #非法词
    "ILLEGAL_WORD":         40001,
    #被禁言
    "USER_IS_MUTE":         40002,
    #重复的发言
    "REPEAT_SEND":          40003,
    #一天的发帖量超过5条
    "LARGEST_PUBLISH":      40004,
    #发送的帖子没有意义
    "MEANINGLESS_MESSAGE":  40005,
    #注册时间太短，1天内不能发评论，2天内不能发帖，5天内发帖不能发图
    "REGIST_LEVEL_LOW":     40006,
    #没有绑定手机号，不能发有图片的帖子
    "NOT_BIND_PHONE":       40007,

    #升级提示
    "UPDATE_ALTER":         50000,

    #User 相关
    "SESSION_IS_NULL":      60000,
    "SESSION_DATA_ERROR":   60001,
    "LIMITED_ACCESS":       60002,
    "PASSWD_IS_NULL":       60003,
    "NAME_CANT_USE":        60004,
    "NAME_IS_EXIST":        60005,
    #refer
    "USER_BIND_ERROR_IS_SELF":      61001,
    "USER_BIND_ERROR_NO_REFERER":   61002,
    "USER_BIND_BOUND":              61003,
    #exchange_code
    "EXCHANGED_PAY_ERROR":          62001,
    #RMB
    "RMB_LACK":             63000,
    #CAIBI
    "CAIBI_CHANGE_ERROR":   68000,

    #验证失败
    "VERIFY_FAILED":        70000,
    "PHONE_FORMAT_ERROR":   71001,
    "SEND_SMS_ERROR":       72001,
    "CHECK_SMS_ERROR":      72002,
    "T_VERIFY_ERROR":       73001,

    #交易支付相关
    "HAS_PAY":              80000,

    #prediction
    "NO_STAT_DATA":         90001,

    # 积分商城
    "NO_PRODUCT":           100001,
    "INFO_INSUFFICIENT":    100002,
    "CREATE_ORDER_ERROR":   100003,
    "BALANCE_SORTAGE":      100004,

    # 聊天室
    "NOT_RIGHT_TIME":       110000,
    "USER_NON_EXISTENT":    110001,

    # 用户签到
    "ALREADY_ATTEND":       120000,

    # 短信订阅---已经订阅
    "ALREADY_SUB":       130000,
    # 还未订阅
    "NOT_YET_SUB":       130001,
    # 没有绑定手机号
    "HAVE_NO_PHONE":     130002,
    # 不是VIP
    "NOT_VIP":           130003
}
