
PASMS = 'pasms-mysql'

MODELDB = 'dev78-mysql'
HIVE = 'hive'
SPARK = 'spark'
IDW = 'idw-oracle'
DEV78 = 'dev78-mysql'

# 浮点数想等比较的误差
EPSINON = 0.000001

# 全局错误代码和注释
# 错误码均用字符串类型标识， 通常为6位，但用0（即“00000”）表示结果正常返回
# 前两位QU表示金工模型
# 第三位表示错误类型， 用字母表示， 例如A表示错误来源于用户，B表示错误来源于系统，
#          C表示错误来源于数据端  Z表示其他尚未归类错误
# 第4~6位用数字表示具体错误

SUCCESS = "00000"
SUCCESS_MSG = "success"
CALCING = "QUA000"
CALCING_MSG = "模型计算中"
ARGUMENTS_ERR = "QUA001"
ARGUMENTS_ERR_MSG = "参数错误，需要的参数为满足"
CACHE_EXP = "QU002"
CACHE_EXP_MSG = "缓存已过期"
ARGUMENTS_TIME_ERR = "QUA003"
ARGUMENTS_TIME_ERR_MSG = "请重亲选择有效日期"
MISMATCH_TYPE_ERR = "QUA100"
MISMATCH_TYPE_ERR_MSG = "调用的参数不匹配"
NETWORK_ERR = "QUB001"
NETWORK_ERR_MSG = "网络连接异常"
TIMEOUT_ERR = "QUB001"
TIMEOUT_ERR_MSG = "时间超时错误"
FILE_NOFOUND_ERR = "QUB100"
FILE_NOFOUND_ERR_MSG = "文件未找到"
NO_DATA_EXP = "QUC001"
NO_DATA_EXP_MSG = "未获取到数据"
OTHER_EXP = 'QUZ001'
OTHER_EXP_MSG = '其他未定义错误'


# 运行环境相关
DEV = 'dev',
STG = 'stg',
STG1 = 'stg1',
STG2 = 'stg2',
STG5 = 'stg5',
STGNEW = 'stgnew',
STGPERF = 'stgperf',
PRD = 'prd',

SUPPORTED_PROFILES = set([DEV, STG, STG1, STG2, STG5, STGNEW, STGPERF, PRD])
MODE = 'service'