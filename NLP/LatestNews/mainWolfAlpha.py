import wolfram
import keys
from wolfram import App
import wolframalpha


class WolfFramInfo():
    wolfram=None
    client=None
    def __init__(self) -> None:
        self.wolfram=App(keys.WOLF_KEY)
        self.client=wolframalpha.Client(keys.WOLF_KEY)
    
    def ask_qustion(self,qustion):
        res=self.client.query(qustion)
        answer=next(res.results).text
        print(answer)

    
    def test(self):
        pass
        # print(self.client.query())
        # print(wolfram.simple("Population of America", "america_population"))

qustion="who is the indian cricket team captain"
wf=WolfFramInfo()
wf.ask_qustion(qustion)
# wf.test()
