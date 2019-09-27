import pandas as pd
arq_vcf_entrada = 'somatic.snvs.ann'
arq_vcf = arq_vcf_entrada + '.vcf'
arq_vcf_txt = arq_vcf_entrada + '.txt'
arq_vcf_xls = arq_vcf_entrada + '.xlsx'


cabecalho = ''
lista_cabecalho = []
linha_cromossomo = ''
lista_linha_cromossomo = []

arquivo = open(arq_vcf)
!touch somatic.snvs.ann.txt somatic.snvs.ann.xlsx
!chmod 777 somatic.snvs.ann.txt somatic.snvs.ann.xlsx

def escrever_arq_txt(linha):
    arquivo_txt = open(arq_vcf_txt, 'r')
    conteudo = arquivo_txt.readlines()
    
    
    arquivo_txt = open(arq_vcf_txt, 'w')
    conteudo.append(linha)
    arquivo_txt.writelines(conteudo)
    arquivo_txt.close()

def separa_conteudo(frase, lista):
    while(len(frase) > 0):
        x = frase.find('\t')
        if int(x) >= 0:            
            lista.append(frase[:int(x)])
            frase = frase[int(x+1):int(len(frase))]
            #print(cabecalho[:int(x)])
            #print(cabecalho[int(x+1):int(len(cabecalho))])
        else:
            lista.append(frase[:-1])
            #lista.append('\n')
            frase = ''
            break
            
i = 0
for linha in arquivo:
    if linha[:2] == str('##'):
        continue
    if linha[:2] == str('#C'):
        #cabecalho = linha
        #separa_conteudo(cabecalho, lista_cabecalho)
        escrever_arq_txt(linha)
    if linha[:3] == str('chr'):
        #linha_cromossomo = linha
        #linha_cromossomo = str(i) + '_' + linha_cromossomo
        #separa_conteudo(linha_cromossomo, lista_linha_cromossomo)
        escrever_arq_txt(linha)
        i+=1 #Contador de linhas do arquivo de entrada, uso não definido
        continue
    #print(linha[:2])
arquivo.close()

df = pd.read_csv(arq_vcf_txt, header= 0, sep= '\t')
#df.head(10)
df.info()
df.to_excel(arq_vcf_xls)

#Allele | Annotation | Annotation_Impact | Gene_Name | Gene_ID | Feature_Type | Feature_ID | Transcript_BioType | Rank | HGVS.c | HGVS.p | cDNA.pos / cDNA.length | CDS.pos / CDS.length | AA.pos / AA.length | Distance | ERRORS / WARNINGS / INFO
df = pd.DataFrame(df["INFO"].str.split(';', 1,).tolist(), columns=['Allele', 'Annotation'])
df.head()


#df.info()
#data["Team"]= data["Team"].str.split("t", n = 1, expand = True) 
#pd.DataFrame(df.row.str.split(' ',1).tolist(), columns = ['flips','row'])
#Allele | Annotation | Annotation_Impact | Gene_Name | Gene_ID | Feature_Type | Feature_ID | Transcript_BioType | Rank | HGVS.c | HGVS.p | cDNA.pos / cDNA.length | CDS.pos / CDS.length | AA.pos / AA.length | Distance | ERRORS / WARNINGS / INFO
df = pd.DataFrame(df["INFO"].str.split(';', 1,).tolist(), columns=['Allele', 'Annotation'])
df.head()

df = pd.DataFrame(df["Annotation"].str.split(';', 1,).tolist(), columns=['Allele', 'Annotation'])
df.head()


