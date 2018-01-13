import TaliffDB.client as cli

cli.setUrl("http://127.0.0.1:5000/")
q = cli.querydb("Pass", "FileTest.sqlite", "SELECT * FROM test")
print(q)
#print(cli.decrypt(q))
