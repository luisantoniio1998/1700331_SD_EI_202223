f = open("/home/kali/Desktop/github_202223/1700331_SD_EI_202223/python/Deserialization/files/output1demo.txt", "w",encoding='utf8')
x="Mais de mil cidades e aldeias em toda a Ucrânia continuam " \
  "\nsem electricidade por causa dos ataques russos dos últimos dias, " \
  "\ndizem responsáveis ucranianos citados pela BBC. Os ataques tiveram como " \
  "\nalvo, muitas vezes, a infra-estrutura energética do país e, segundo o " \
  "\nPresidente Volodymyr Zelensky, destruíram 30% das centrais eléctricas da Ucrânia."
print(f.write(x))