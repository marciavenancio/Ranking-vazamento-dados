print("ESSE É UM RANKING DE EMPRESAS QUE TIVERAM SEUS DADOS VAZADOS!\n")
#Legenda da lista empresas: Data de vazamento dos dados sendo: ano e mês; Nome da empresa e dados vazados.
empresas = ["2019.03, Hurb, senha, nome, email, telefone", "2021.03, Linkedin, nome, email",
            "2020.09, Nitro, senha, nome, email", "2013.10, Adobe, senha, dica de senha, email, nome",
            "2018.07, Apollo, nome, email, telefone", "2019.05, Canva, senha, nome, email",
            "2021.03, Descomplica, senha, nome, email", "2012.06, Dropbox, senha, email",
            "2021.09, Epik, nome, email, telefone", "2013.09, iMesh, senha, nome, email",
            "2020.06, James, senha, email", "2016.08, Leet, senha, email, nome",
            "2018.02, MyFitnessPal, senha, nome, email", "2008.07, Myspace, senha, email, nome",
            "2018.07, Netlog, senha, email","2015.10, Patreon, senha, email, endereço",
            "2015.07, PokeBip, senha, email, nome","2018.05, Poshmark, senha, email, nome, localização",
            "2019.08, Profarma, nome, email", "2018.06, Shein, senha, email",
            "2016.05, Shotbow, senha, nome, email", "2015.03, Snail, senha, nome, email",
            "2015.08, StoryBird, senha, nome, email", "2020.02, Straffic, email, nome, telefone, endereço",
            "2020.04, Tokopedia, senha, nome, email", "2018.10, Pluto TV, senha, email, nome",
            "2009.05, Money Bookers, email, nome, telefone, endereço","2021.08, IndiaMART, email, nome, telefone, endereço",
            "2020.02, Home Chef, senha, email, nome, telefone", "2020.10, Gravatar, email, nome"]

ranksenha = []
rank=[]
ranking = []
item=0
posicao=0

print("A lista abaixo, está classificada por grau de criticidade de vazamento."
      "\nSendo considerados como mais críticos os vazamentos MAIS RECENTES DE SENHA, "
      "\nseguidos pelos vazamentos MAIS RECENTES dos demais itens vazados:\n\n"
      "     DATA - EMPRESA  - DADOS VAZADOS")
for e in empresas:
    if "senha" in e:
        item = e
        ranksenha.append(item)
    if "senha" not in e:
        item = e
        rank.append(item)

ranksenha.sort()
ranksenha.reverse()
rank.sort()
rank.reverse()
ranking = ranksenha + rank
for r in ranking:
    posicao = posicao + 1
    print(f'{posicao}º', r)
