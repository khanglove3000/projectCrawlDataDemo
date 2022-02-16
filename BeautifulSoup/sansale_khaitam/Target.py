
class Target:
    def __init__(self, patternsStr='', categoryStr = ''):
        self.patternsString = patternsStr
        self.patterns = self.__splitPatter()
        self.cateforyUrl = categoryStr

    def info(self):
        return "Patterns: " + str(self.patterns) + "| category: " + self.cateforyUrl
    
    def __splitPatter(self):
        newList = self.patternsString.split(',')
        i = 0
        while i < len(newList):
            newList[i] = newList[i].strip()
            i = i + 1
        return newList
    
    def getKeyword(self):
        keyword = ""
        for key in self.patterns:
            keyword = keyword + " " + key
        return keyword

    def getSearchLink(self, pageNum):
        return self.categoryUrl+'SearchResults.aspx?q='+self.getKeyword()+'&p='+str(pageNum)
