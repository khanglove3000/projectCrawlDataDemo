from pipelines import LoadSymbol
run = LoadSymbol.connectDB()
for i in range(len(run)):
    print(run[i][2])
