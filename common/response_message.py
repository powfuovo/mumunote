class UserMessage():
    @staticmethod
    def success(data):
        return {"statue0":1000,"data":data}
    @staticmethod
    def other(data):
        return {"statue0":1001,"data":data}
    @staticmethod
    def error(data):
        return {"statue0":1002,"data":data}
