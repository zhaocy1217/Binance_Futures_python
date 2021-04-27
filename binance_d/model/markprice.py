

class MarkPrice:

    def __init__(self):
        self.symbol = ""
        self.pair = ""
        self.indexPrice = 0.0
        self.markPrice = 0.0
        self.estimatedSettlePrice = 0.0
        self.time = 0
        self.lastFundingRate = 0.0
        self.interestRate = 0.0
        self.nextFundingTime = 0
    
    @staticmethod
    def json_parse(json_data):
        result = MarkPrice()
        result.symbol = json_data.get_string("symbol")
        result.pair = json_data.get_string("pair")
        result.indexPrice = json_data.get_float("indexPrice")
        result.markPrice = json_data.get_float("markPrice")
        result.estimatedSettlePrice = json_data.get_float("estimatedSettlePrice")
        result.time = json_data.get_int("time")
        result.lastFundingRate = json_data.get_float("lastFundingRate")
        result.interestRate = json_data.get_float("interestRate")
        result.nextFundingTime = json_data.get_int("nextFundingTime")

        return result
