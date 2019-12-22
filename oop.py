
class birdaction:
    def tweet(self): return self.strings['tweet']
    def meow(self): return self.strings['meow']
    def quack(self): return self.strings['quack']
    def crow(self): return self.strings['crow']


class cocks(birdaction):
    strings = dict(
        crow= "crow!!.",
        tweet= "the cocks cannottweet!",
        meow= "The cock cannot meow.",
        quack= "The cock cannot quack.",
        
    )

class cat(birdaction):
    strings = dict(
        tweet= "the cat cannottweet!",
        meow= "meow.",
        quack= "The cat cannot quack.",
        crow= "the cat cannot crow!!."
    )
class Duck(birdaction):
    strings = dict(
        quack = "Quaaaaak!",
       tweet= "The duck  cannot tweet.",
        crow = "The duck cannot crow.",
        meow  = "The duck cannot meow."
    )
 



def in_house(cat):
    print(cat.meow())
    
def in_forest(cocks):
    print(cocks.crow())




def main():
    berry = Duck()
    
    mony= cat()
    petu = cocks()

    print("- In the forest:")
    for o in ( berry,mony , petu ):
        in_forest(o)

    print("- In the house:")
    for o in (berry, mony,petu ):
        in_house(o)
     

    
if __name__ == "__main__": main()
