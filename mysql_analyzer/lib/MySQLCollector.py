class MySQLCollector():
    mysql_data = {}
    mysql_args = ""

    def __init__(self,args):
        print("    Initializing MySQL Collector")
        self.mysql_args = args

    def collect(self):
        """
        self.info()
        self.users()
        self.schema()
        self.engine_status()
        self.variables()
        self.status()
        self.performance_schema()
        self.replication()
        self.indexes()
        self.foreign_keys()
        self.disk_usage()
        """
        return self.mysql_data

