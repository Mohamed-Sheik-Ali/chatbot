class BaseCfg(object):
    SECRET_KEY = 'ILpnyT{7#bw)aW6wgGC/bP?CQXkk1F|%ye*Kj8hX.gpXm;l9Z-9&1#)8!7>V)gv'
    DEBUG = False
    TESTING = False


class DevelopmentCfg(BaseCfg):
    DEBUG = True
    TESTING = True


class TestingCfg(BaseCfg):
    DEBUG = False
    TESTING = True


class ProductionCfg(BaseCfg):

    SECRET_KEY = "{'LP%VO!A > }9AXRV?8T[ |`rdDPO3[Gb2S @\"{g9Gi | ekQjY ^ >mmYDU. % @x*&k'W %"
    DEBUG = False
    TESTING = False
