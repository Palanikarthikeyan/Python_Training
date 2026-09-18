
def connect(dsn):
    class DB:
        def __init__(self,dsn):
            self.dsn = dsn
        def display(self):
            return "Query-method"
    obj = DB(dsn)
    return obj



myconn = connect("oracle:1501/root")
print(myconn.display())